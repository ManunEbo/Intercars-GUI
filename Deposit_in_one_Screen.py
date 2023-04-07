import os
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDTimePicker
import CustomerScreen
import Cust_AddressScreen
import Deposit_or_SaleScreen
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

class Deposit_in_one_Screen(Screen):
    # Checks on the values being passed
    # Payment method
    global Split_pay
    Split_pay = "No"
    def dep_sal_option_choice(self,value):
        global Payment_method
        Payment_method = value
    
    # Debit type
    def Deposit_Debit_type(self,value):
        global Debit_Type
        Debit_Type = value

    # Card Expiry Date
    global Deposit_in_1_Expiry_Date
    Deposit_in_1_Expiry_Date = None
    def Deposit_card_Exp_on_save(self,instance,value,date_range):        
        Deposit_in_1_Expiry_Date = value
        self.ids.Card_Expiry_id.text = "Card Expiry date:\n[color=#76FF03][b]{0}[/b][/color]".format(Deposit_in_1_Expiry_Date)

    if Deposit_in_1_Expiry_Date is None:
        Deposit_in_1_Expiry_Date = "null"
    # click cancel
    def Deposit_card_Exp_on_cancel(self,instance,value):
        pass
    
    # try also passing a value for variable to the on_save below
    def Deposit_card_Exp_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Deposit_card_Exp_on_save, on_cancel=self.Deposit_card_Exp_on_cancel)
        date_dialog.open()

    # Card Start Date
    global Deposit_in_1_Start_Date
    Deposit_in_1_Start_Date = None
    def Deposit_card_start_on_save(self,instance,value,date_range):        
        Deposit_in_1_Start_Date = value
        self.ids.Card_Start_id.text = "Card start date:\n[color=#76FF03][b]{0}[/b][/color]".format(Deposit_in_1_Start_Date)

    if Deposit_in_1_Start_Date is None:
        Deposit_in_1_Start_Date = "null"

    # click cancel
    def Deposit_card_start_on_cancel(self,instance,value):
        pass
    
    # try also passing a value for variable to the on_save below
    def Deposit_card_start_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Deposit_card_start_on_save, on_cancel=self.Deposit_card_start_on_cancel)
        date_dialog.open()

    # Deposit/transaction  Date
    global Deposit_in_1_Trans_Date
    Deposit_in_1_Trans_Date = None
    def Deposit_transaction_on_save(self,instance,value,date_range):        
        Deposit_in_1_Trans_Date = value
        self.ids.Deposit_transaction_Date_id.text = "Deposit date:\n[color=#76FF03][b]{0}[/b][/color]".format(Deposit_in_1_Trans_Date)

    if Deposit_in_1_Trans_Date is None:
        Deposit_in_1_Trans_Date = "null"

    # click cancel
    def Deposit_transaction_on_cancel(self,instance,value):
        pass
    
    # try also passing a value for variable to the on_save below
    def Deposit_transaction_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Deposit_transaction_on_save, on_cancel=self.Deposit_transaction_on_cancel)
        date_dialog.open()


    # Get time
    global Deposit_in_1_Trans_time
    Deposit_in_1_Trans_time = None
    def Deposit_get_time(self,instance,time):        
        Deposit_in_1_Trans_time = time
        self.ids.Deposit_transaction_time_id.text = "Deposit Time:\n[color=#76FF03][b]{0}[/b][/color]".format(Deposit_in_1_Trans_time)
    if Deposit_in_1_Trans_time is None:
        Deposit_in_1_Trans_time = "null"
    # Cancel
    def Deposit_on_time_cancel(self,instance,time):
        pass

    def show_Deposit_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.Deposit_on_time_cancel,time = self.Deposit_get_time)
        time_dialog.open()
    
    global Deposit_in_1_Transfer_Reference, Deposit_in_1_Card_nbr, Deposit_in_1_Auth_code,Deposit_in_1_Receipt_Nbr,Sale_date,Staff_id
    Deposit_in_1_Transfer_Reference = None
    Deposit_in_1_Card_nbr = None
    Deposit_in_1_Auth_code = None
    Deposit_in_1_Receipt_Nbr = None
    Staff_id = 1


    # submit to database
    def Deposit_in_1_submit(self):

        if self.ids.deposit_in_one_transfer_ref_textf.text is None:
            Deposit_in_1_Transfer_Reference = None
        else:
            Deposit_in_1_Transfer_Reference = self.ids.deposit_in_one_transfer_ref_textf.text

        if self.ids.deposit_in_1_card_nbr_textf.text is None:
            Deposit_in_1_Card_nbr = None
        else:
            Deposit_in_1_Card_nbr = self.ids.deposit_in_1_card_nbr_textf.text
        
        # if self.ids.Deposit_in_1_Debit_type_spin_id.text is None:
        #     Deposit_in_1_Debit_Type = None
        # else:
        #     Deposit_in_1_Debit_Type = self.ids.Deposit_in_1_Debit_type_spin_id.text
        
        if self.ids.Deposit_in_1_auth_textf.text is None:
            Deposit_in_1_Auth_code = None
        else:
            Deposit_in_1_Auth_code = self.ids.Deposit_in_1_auth_textf.text
        
        if self.ids.Deposit_in_1_Amount_textf.text is None:
            Deposit_in_1_Deposit_Amount = None
        else:
            Deposit_in_1_Deposit_Amount = self.ids.Deposit_in_1_Amount_textf.text
        
        if self.ids.Deposit_in_1_Receipt_nbr_textf.text is None:
            Deposit_in_1_Receipt_Nbr = None
        else:
            Deposit_in_1_Receipt_Nbr = self.ids.Deposit_in_1_Receipt_nbr_textf.text

        sql_string1 = "set @Split_pay ='{0}';".format(Split_pay)
        sql_string2 = "set @V5C_ID = {0};".format(Deposit_or_SaleScreen.V5c_id)
        sql_string3 = "set @Payment_method ='{0}';".format(Payment_method)
        sql_string4 = "set @Transfer_Reference = '{0}';".format(Deposit_in_1_Transfer_Reference)
        sql_string5 = "set @Card_nbr = {0};".format(Deposit_in_1_Card_nbr)
        sql_string6 = "set @Debit_Type ='{0}';".format(Debit_Type)
        sql_string7 = "set @Exp_Date = '{0}';".format(Deposit_in_1_Expiry_Date)
        sql_string8 = "set @Start_Date ='{0}';".format(Deposit_in_1_Start_Date)
        sql_string9 = "set @Trans_Date = '{0}';".format(Deposit_in_1_Trans_Date)
        sql_string10 = "set @Trans_time = '{0}';".format(Deposit_in_1_Trans_time)
        sql_string11 = "set @Auth_code = {0};".format(Deposit_in_1_Auth_code)
        sql_string12 = "set @Amount = {0};".format(Deposit_in_1_Deposit_Amount)
        sql_string13 = "set @Receipt_Nbr = {0};".format(Deposit_in_1_Receipt_Nbr)
        sql_string14 = "Set @Fname= '{0}';".format(CustomerScreen.FirstName)
        sql_string15 = "Set @Mname= '{0}';".format(CustomerScreen.MiddleName)
        sql_string16 = "Set @Lname= '{0}';".format(CustomerScreen.LastName)
        sql_string17 = "Set @DOB= '{0}';".format(CustomerScreen.Customer_DOB)
        sql_string18 = "set @Age_Group= '{0}';".format(CustomerScreen.AgeGroup)
        sql_string19 = "Set @Address1= '{0}';".format(Cust_AddressScreen.Address1)
        sql_string20 = "Set @Address2= '{0}';".format(Cust_AddressScreen.Address2)
        sql_string21 = "Set @Address3= '{0}';".format(Cust_AddressScreen.Address3)
        sql_string22 = "Set @Address4= '{0}';".format(Cust_AddressScreen.Address4)
        sql_string23 = "Set @Address5= '{0}';".format(Cust_AddressScreen.Address5)
        sql_string24 = "Set @Address6 = '{0}';".format(Cust_AddressScreen.Address6)
        sql_string25 = "Set @email = '{0}';".format(Cust_AddressScreen.email)
        sql_string26 = "Set @Tel = '{0}';".format(Cust_AddressScreen.Tel)
        sql_string27 = "set @Sale_date= '';"
        sql_string28 = "set @Deposit_Date = @Trans_Date;"
        sql_string29 = "set @Staff_id = {0};".format(Staff_id)
        sql_string30 = "call Customer_Insert_call();"


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
        mycursor.execute(sql_string16)
        mycursor.execute(sql_string17)
        mycursor.execute(sql_string18)
        mycursor.execute(sql_string19)
        mycursor.execute(sql_string20)
        mycursor.execute(sql_string21)
        mycursor.execute(sql_string22)
        mycursor.execute(sql_string23)
        mycursor.execute(sql_string24)
        mycursor.execute(sql_string25)
        mycursor.execute(sql_string26)
        mycursor.execute(sql_string27)
        mycursor.execute(sql_string28)
        mycursor.execute(sql_string29)
        mycursor.execute(sql_string30)      
        mydb.commit()