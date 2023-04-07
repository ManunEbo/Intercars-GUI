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

class MOTHistoryScreen(Screen):

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
    v5c_list = ["{0}, {1}, {2}".format(x[0], x[1],x[2]) for x in custom_list]

    def selected_id(self,value):
        x=value.split(',')
        global V5c_id
        V5c_id =x[0]
    
    # Test date    
    def Test_Date_on_save(self,instance,value,date_range):
        global Test_Date
        Test_Date = value
        self.ids.Test_Date_lbl.text = "Test date:\n[color=#76FF03][b]{0}[/b][/color]".format(Test_Date)

    # click cancel
    def Test_Date_on_cancel(self,instance,value):
        pass
    
    def Test_Date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Test_Date_on_save, on_cancel=self.Test_Date_on_cancel)
        date_dialog.open()

    # Test expiry date    
    def Test_expiry_Date_on_save(self,instance,value,date_range):
        global Test_expiry_Date
        Test_expiry_Date = value
        self.ids.Expiry_date_lbl.text = "Test expiry date:\n[color=#76FF03][b]{0}[/b][/color]".format(Test_expiry_Date)

    # click cancel
    def Test_expiry_Date_on_cancel(self,instance,value):
        pass
    
    def Test_expiry_Date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Test_expiry_Date_on_save, on_cancel=self.Test_expiry_Date_on_cancel)
        date_dialog.open()
    
    global Advisory1,Advisory2,Advisory3,Advisory4,Advisory5,MOT_tst_Cert_Nbr,Price
    
    # Initializing the advisory variables to None so that if they are not set
    # they exist, this stops a variable not defined error from occurring
    Advisory1 = None
    Advisory2 = None
    Advisory3 = None
    Advisory4 = None
    Advisory5 = None

    def Submit_MOThistory(self):
        sql_string1 = "set @V5C_ID ={0}".format(V5c_id)
        sql_string2 = "set @Vehicle_Reg_MOT_Date ='{0}'".format(self.ids.Reg_MOT_Date_textf.text)
        sql_string3 = "set @Test_Org = '{0}'".format(self.ids.Test_Org_textf.text)
        sql_string4 = "set @Test_Addr = '{0}'".format(self.ids.Test_Addr_textf.text)
        sql_string5 = "set @Test_Date = '{0}'".format(Test_Date)
        sql_string6 = "set @Expiry_date = '{0}'".format(Test_expiry_Date)

        if self.ids.Advisory1_textf.text is None:
            Advisory1 = ""            
        else:
            Advisory1 = self.ids.Advisory1_textf.text
        sql_string7 = "set @Advisory1 = '{0}'".format(Advisory1)

        if self.ids.Advisory2_textf.text is None:
            Advisory2 = ""
        else:
            Advisory2 = self.ids.Advisory2_textf.text
        sql_string8 = "set @Advisory2 = '{0}'".format(Advisory2)

        if self.ids.Advisory3_textf.text is None:
            Advisory3 = ""
        else:
            Advisory3 = self.ids.Advisory3_textf.text
        sql_string9 = "set @Advisory3 = '{0}'".format(Advisory3)

        if self.ids.Advisory4_textf.text is None:
            Advisory4 = ""
        else:
            Advisory4 = self.ids.Advisory4_textf.text
        sql_string10 = "set @Advisory4 = '{0}'".format(Advisory4)

        if self.ids.Advisory5_textf.text is None:
            Advisory5 = ""
        else:
            Advisory5 = self.ids.Advisory5_textf.text
        sql_string11 = "set @Advisory5 = '{0}'".format(Advisory5)

        MOT_tst_Cert_Nbr =self.ids.MOT_tst_Cert_Nbr_textf.text
        sql_string12 = "set @MOT_tst_Cert_Nbr ='{0}'".format(MOT_tst_Cert_Nbr)

        Price = self.ids.Price_textf.text
        sql_string13 = "set @Price ={0}".format(Price)

        sql_string14 = "call icp_MOT_History_call();"

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

        mydb.commit()


        self.manager.current="vehiclescreen"