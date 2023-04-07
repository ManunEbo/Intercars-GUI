import os
from kivy.uix.screenmanager import Screen
from kivymd.uix.picker import MDDatePicker
import pandas as pd
import numpy as np
import mysql.connector

from dotenv import load_dotenv
load_dotenv()


mydb = mysql.connector.connect(
host=os.getenv('host'),
user=os.getenv('username'),
password=os.getenv('password'),
database=os.getenv('database',
auth_plugin=os.getenv('auth_plugin'
)

class MileageHistoryScreen(Screen):
    
    sql_str = """ select a.V5C_id,
    a.Model,
    a.Reg_numb
    from icp.V5C a 
    left join icp.Sale b
    on a.V5C_id = b.V5C_id
    where b.V5C_id is null; """

    mydata = pd.read_sql_query(sql_str,mydb)


    # converting the pandas dataframe into a numpy array
    num_data = mydata.to_numpy()

    # Reshaping the data
    Ar_shape = num_data.reshape(num_data.shape)
    #Converting to a list 
    Array_tup = list(map(tuple,Ar_shape))

    custom_list = Array_tup
    v5c_list_MHist = ["{0}, {1}, {2}".format(x[0], x[1],x[2]) for x in custom_list]

    def selected_id_MHist(self,value):
        x=value.split(',')
        global V5c_id
        V5c_id =x[0]
    
    # Mileage date    
    def Mileage_Date_on_save(self,instance,value,date_range):
        global Mileage_Date
        Mileage_Date = value
        self.ids.Mileage_Date_lbl.text = "Mileage date:\n[color=#76FF03][b]{0}[/b][/color]".format(Mileage_Date)

    # click cancel
    def Mileage_Date_on_cancel(self,instance,value):
        pass
    
    def Mileage_Date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Mileage_Date_on_save, on_cancel=self.Mileage_Date_on_cancel)
        date_dialog.open()
    
    def Submit_Mileage(self):

        sql_string1 = "set @V5C_id ={0};".format(V5c_id)
        sql_string2 = "set @Vehicle_Reg_MOT_Date ='{0}';".format(self.ids.Reg_MOT_Date_textf.text)
        sql_string3 = "set @Source  ='{0}';".format(self.ids.Source_textf.text)
        sql_string4 = "set @Mileage ={0};".format(self.ids.Mileage_textf.text)
        sql_string5 = "set @Date = '{0}';".format(Mileage_Date)
        sql_string6 = "call icp_Mileage_History_call();"

        mycursor = mydb.cursor()
        mycursor.execute(sql_string1)
        mycursor.execute(sql_string2)
        mycursor.execute(sql_string3)
        mycursor.execute(sql_string4)
        mycursor.execute(sql_string5)
        mycursor.execute(sql_string6)

        mydb.commit()        

        self.manager.current = "vehiclescreen"