import os
from kivy.uix.screenmanager import Screen
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDTimePicker
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

class CallLogScreen(Screen):

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
    Vehicle_log_list = ["{0}, {1}, {2}".format(x[0], x[1],x[2]) for x in custom_list]

    def selected_vehicle(self,value):
        x=value.split(',')
        global V5C_id,Vehicle_of_interest
        V5C_id =x[0]
        Vehicle_of_interest ="{0} {1}".format(x[1],x[2])
    
    def Customer_sex_log(self,value):
        global Customer_sex
        Customer_sex = value

    # Date of call    
    def Date_of_call_on_save(self,instance,value,date_range):
        global Date_of_call
        Date_of_call = value
        self.ids.Date_of_call_lbl.text = "Date of call:\n[color=#76FF03][b]{0}[/b][/color]".format(Date_of_call)

    # click cancel
    def Date_of_call_on_cancel(self,instance,value):
        pass
    
    def Date_of_call_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Date_of_call_on_save, on_cancel=self.Date_of_call_on_cancel)
        date_dialog.open()

    # Time of call
    def get_time_of_call(self,instance,time):
        global Time_of_Call
        Time_of_Call = time
        self.ids.Time_of_call_id.text = "Time of call:\n[color=#76FF03][b]{0}[/b][/color]".format(Time_of_Call)
    # Cancel
    def time_of_call_cancel(self,instance,time):
        print("You canceled the time picker")

    def show_time_of_call_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.time_of_call_cancel,time = self.get_time_of_call)
        time_dialog.open()
    
    def Submit_Call_log(self):

        sql_string1 = "set @Name ='{0}';".format(self.ids.Name_textf.text)
        sql_string2 = "set @Customer_sex ='{0}';".format(Customer_sex)
        sql_string3 = "set @Tel ={0};".format(self.ids.Tel_textf.text)
        sql_string4 = "set @City_or_village ='{0}';".format(self.ids.City_or_village_textf.text)
        sql_string5 = "set @Vehicle_of_interest ='{0}';".format(Vehicle_of_interest)
        sql_string6 = "set @V5C_id ='{0}';".format(V5C_id)
        sql_string7 = "set @Date_of_call ='{0}';".format(Date_of_call)
        sql_string8 = "set @Time_of_Call ='{0}';".format(Time_of_Call)
        sql_string9 = "call Op_call_Log_call();"

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

        mydb.commit()        

        self.manager.current = "vehiclescreen"