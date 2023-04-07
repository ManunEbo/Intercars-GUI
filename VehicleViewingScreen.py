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

class VehicleViewingScreen(Screen):

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
    Vehicle_v_list = ["{0}, {1}, {2}".format(x[0], x[1],x[2]) for x in custom_list]

    def selected_vehicle_v(self,value):
        x=value.split(',')
        global V5C_id,Vehicle_of_interest
        V5C_id =x[0]
        Vehicle_of_interest ="{0} {1}".format(x[1],x[2]) 
    
    def Viewing_agegroup(self,value):
        global Customer_Age_Bracket
        Customer_Age_Bracket = value
    
    def Customer_sex_v(self,value):
        global Customer_sex
        Customer_sex = value
    
    # Viewing date   
    def Viewing_date_on_save(self,instance,value,date_range):
        global Viewing_date
        Viewing_date = value
        self.ids.Viewing_date_lbl.text = "Viewing date:\n[color=#76FF03][b]{0}[/b][/color]".format(Viewing_date)

    # click cancel
    def Viewing_date_on_cancel(self,instance,value):
        pass
    
    def Viewing_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Viewing_date_on_save, on_cancel=self.Viewing_date_on_cancel)
        date_dialog.open()

    # Time of call
    def get_viewing_time(self,instance,time):
        global Viewing_time
        Viewing_time = time
        self.ids.Viewing_time_id.text = "Viewing time:\n[color=#76FF03][b]{0}[/b][/color]".format(Viewing_time)
    # Cancel
    def viewing_time_cancel(self,instance,time):
        pass

    def show_viewing_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.viewing_time_cancel,time = self.get_viewing_time)
        time_dialog.open()
    
    def Deposit_Flag_v(self,value):
        global Deposit_Flag
        Deposit_Flag = value
    
    def Sale_Flag_v(self,value):
        global Sale_Flag
        Sale_Flag = value
    
    def Submit_Viewing(self):
        sql_string1 = "set @Vehicle_of_interest ='{0}';".format(Vehicle_of_interest)
        sql_string2 = "set @V5C_id ={0};".format(V5C_id)
        sql_string3 = "set @Nbr_Vehicles_viewed = {0};".format(self.ids.Nbr_Vehicles_viewed_textf.text)
        sql_string4 = "set @Customer_Age_Bracket ='{0}';".format(Customer_Age_Bracket)
        sql_string5 = "set @Customer_sex ='{0}';".format(Customer_sex)
        sql_string6 = "set @City_or_village = '{0}';".format(self.ids.City_or_village_textf.text)
        sql_string7 = "set @Viewing_date ='{0}';".format(Viewing_date)
        sql_string8 = "set @Viewing_time = '{0}';".format(Viewing_time)
        sql_string9 = "set @Deposit_Flag = '{0}';".format(Deposit_Flag)
        sql_string10 = "set @Sale_Flag ='{0}';".format(Sale_Flag)
        sql_string11 = "call Op_vehicle_viewing_call();"

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

        mydb.commit()

        self.manager.current = "vehiclescreen"