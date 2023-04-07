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

class ServiceHistoryScreen(Screen):
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
    v5c_list_SHist = ["{0}, {1}, {2}".format(x[0], x[1],x[2]) for x in custom_list]


    def selected_id_SHist(self,value):
        x=value.split(',')
        global V5c_id
        V5c_id =x[0]
    
    # Test date    
    def Serv_Date_on_save(self,instance,value,date_range):
        global Serv_Date
        Serv_Date = value
        self.ids.Serv_Date_lbl.text = "Service date:\n[color=#76FF03][b]{0}[/b][/color]".format(Serv_Date)

    # click cancel
    def Serv_Date_on_cancel(self,instance,value):
        pass
    
    def Serv_Date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Serv_Date_on_save, on_cancel=self.Serv_Date_on_cancel)
        date_dialog.open()
    
    def Submit_Service(self):
        sql_string1 = "set @V5C_id ={0};".format(V5c_id)
        sql_string2 = "set @Vehicle_Reg_serv_Date ='{0}';".format(self.ids.Reg_Serv_Date_textf.text)
        sql_string3 = "set @Serv_comp ='{0}';".format(self.ids.Serv_comp_textf.text)
        sql_string4 = "set @Serv_Addr ='{0}';".format(self.ids.Serv_Addr_textf.text)
        sql_string5 = "set @Serv_Date ='{0}';".format(Serv_Date)
        sql_string6 = "set @Serv_Parts_desc = '{0}';".format(self.ids.Serv_Parts_desc_textf.text)
        sql_string7 = "set @Quantity = {0};".format(self.ids.Quantity_textf.text)
        sql_string8 = "set @Unit_price ={0};".format(self.ids.Unit_price_textf.text)
        sql_string9 = "set @Sum_per_Parts ={0};".format(self.ids.Sum_per_Parts_textf.text)
        sql_string10 = "set @Total_Labour ={0};".format(self.ids.Total_Labour_textf.text)
        sql_string11 = "set @Total_Parts ={0};".format(self.ids.Total_Parts_textf.text)
        sql_string12 = "set @MOT_Fee = {0};".format(self.ids.Serv_MOT_Fee_textf.text)
        sql_string13 = "set @VAT ={0};".format(self.ids.VAT_textf.text)
        sql_string14 = "set @Grand_Total ={0};".format(self.ids.Grand_Total_textf.text)
        sql_string15 = "call icp_service_history_call();"

        mycursor = mydb.cursor()
        mycursor.execute(sql_string1)
        mycursor.execute(sql_string2)
        mycursor.execute(sql_string3)
        mycursor.execute(sql_string4)
        mycursor.execute(sql_string5)
        mycursor.execute(sql_string6)
        mycursor.execute(sql_string7)
        mycursor.execute(sql_string8)
        mycursor.execute(sql_string9)
        mycursor.execute(sql_string10)
        mycursor.execute(sql_string11)
        mycursor.execute(sql_string12)
        mycursor.execute(sql_string13)
        mycursor.execute(sql_string14)
        mycursor.execute(sql_string15)

        mydb.commit()        

        self.manager.current = "vehiclescreen"