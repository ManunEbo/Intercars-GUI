from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDTimePicker
from kivy.properties import ListProperty
import CustomerScreen
import Cust_AddressScreen
import Deposit_or_SaleScreen

class Sale_in_three_Screen(Screen):
    def S3_dep_sal_option_choice1(self,value):
        print("Payment method 1: {0}".format(value))
    
    def S3_Debit_type1(self,value):
        print("Sale debit type 1: {0}".format(value))
    
        # S3 Card Expiry Date 1
    # click ok
    def S3_card_Exp_1_on_save(self,instance,value,date_range):
        global S3_Expiry_Date_1
        S3_Expiry_Date_1 = value
        self.ids.S3_Card_Expiry_1_id.text = "Card Expiry date:\n[color=#76FF03][b]{0}[/b][/color]".format(S3_Expiry_Date_1)

    # click cancel
    def S3_card_Exp_1_on_cancel(self,instance,value):
        print("You cancelled card expiry date")
    
    # Sale card expiry date
    def S3_card_Exp_date_picker1(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.S3_card_Exp_1_on_save, on_cancel=self.S3_card_Exp_1_on_cancel)
        date_dialog.open()

    # Card Start Date
    # click ok
    def S3_card_start_1_on_save(self,instance,value,date_range):
        global S3_Start_Date1
        S3_Start_Date1 = value
        self.ids.S3_Card_Start_1_id.text = "Card Start Date:\n[color=#76FF03][b]{0}[/b][/color]".format(S3_Start_Date1)
        

    # click cancel
    def S3_card_start_1_on_cancel(self,instance,value):
        print("You cancelled card start date")
    
    # try also passing a value for variable to the on_save below
    def S3_card_start_date_1_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.S3_card_start_1_on_save, on_cancel=self.S3_card_start_1_on_cancel)
        date_dialog.open()

    # Sale/transaction  Date
    # click ok
    def S3_transaction_1_on_save(self,instance,value,date_range):
        global S3_Trans_Date_1
        S3_Trans_Date_1 = value
        self.ids.S3_transaction_Date_1_id.text = "Sale Date:\n[color=#76FF03][b]{0}[/b][/color]".format(S3_Trans_Date_1)

    # click cancel
    def S3_transaction_1_on_cancel(self,instance,value):
        print("You cancelled card expiry date")
    
    # try also passing a value for variable to the on_save below
    def S3_transaction_date_1_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.S3_transaction_1_on_save, on_cancel=self.S3_transaction_1_on_cancel)
        date_dialog.open()

    # Get time
    def S3_get_time_1(self,instance,time):
        global S3_Trans_time1
        S3_Trans_time1 = time
        self.ids.S3_transaction_time_1_id.text = "Transaction Time:\n[color=#76FF03][b]{0}[/b][/color]".format(S3_Trans_time1)
    # Cancel
    def S3_on_time_1_cancel(self,instance,time):
        print("You canceled the time picker")

    def S3_show_time_picker1(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.S3_on_time_1_cancel,time = self.S3_get_time_1)
        time_dialog.open()

    # Second Payment
    def S3_dep_sal_option_choice2(self,value):
        print("Payment method 2: {0}".format(value))
    
    def S3_Debit_type2(self,value):
        print("Sale debit type 2: {0}".format(value))
    
        # D2 Card Expiry Date 1
    # click ok
    def S3_card_Exp_2_on_save(self,instance,value,date_range):
        global S3_Expiry_Date_2
        S3_Expiry_Date_2 = value
        self.ids.S3_Card_Expiry_2_id.text = "Card Expiry Date:\n[color=#76FF03][b]{0}[/b][/color]".format(S3_Expiry_Date_2)
        

    # click cancel
    def S3_card_Exp_2_on_cancel(self,instance,value):
        print("You cancelled card expiry date")
    
    # Sale card expiry date
    def S3_card_Exp_date_picker2(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.S3_card_Exp_2_on_save, on_cancel=self.S3_card_Exp_2_on_cancel)
        date_dialog.open()

    # Card Start Date
    # click ok
    def S3_card_start_2_on_save(self,instance,value,date_range):
        global S3_Start_Date2
        S3_Start_Date2 = value
        self.ids.S3_Card_Start_2_id.text = "Card Start Date:\n[color=#76FF03][b]{0}[/b][/color]".format(S3_Start_Date2)
        

    # click cancel
    def S3_card_start_2_on_cancel(self,instance,value):
        print("You cancelled card start date")
    

    def S3_card_start_date_2_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.S3_card_start_2_on_save, on_cancel=self.S3_card_start_2_on_cancel)
        date_dialog.open()

    # Sale/transaction  Date
    # click ok
    def S3_transaction_2_on_save(self,instance,value,date_range):
        global S3_Trans_Date_2
        S3_Trans_Date_2 = value
        self.ids.S3_transaction_Date_2_id.text = "Transaction Date:\n[color=#76FF03][b]{0}[/b][/color]".format(S3_Trans_Date_2)

    # click cancel
    def S3_transaction_2_on_cancel(self,instance,value):
        print("You cancelled card expiry date")
    
    # try also passing a value for variable to the on_save below
    def S3_transaction_date_2_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.S3_transaction_2_on_save, on_cancel=self.S3_transaction_2_on_cancel)
        date_dialog.open()

    # Get time
    def S3_get_time_2(self,instance,time):
        global S3_Trans_time2
        S3_Trans_time2 = time
        self.ids.S3_transaction_time_2_id.text = "Transaction Time:\n[color=#76FF03][b]{0}[/b][/color]".format(S3_Trans_time2)
    # Cancel
    def S3_on_time_2_cancel(self,instance,time):
        print("You canceled the time picker")

    def S3_show_time_picker2(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.S3_on_time_2_cancel,time = self.S3_get_time_2)
        time_dialog.open()

    # Third Payment
    def S3_dep_sal_option_choice3(self,value):
        print("Payment method 3: {0}".format(value))
    
    def S3_Debit_type3(self,value):
        print("Sale debit type 3: {0}".format(value))
    
        # S3 Card Expiry Date 3
    # click ok
    def S3_card_Exp_3_on_save(self,instance,value,date_range):
        global S3_Expiry_Date_3
        S3_Expiry_Date_3 = value
        self.ids.S3_Card_Expiry_3_id.text = "Card Expiry Date:\n[color=#76FF03][b]{0}[/b][/color]".format(S3_Expiry_Date_3)
        

    # click cancel
    def S3_card_Exp_3_on_cancel(self,instance,value):
        print("You cancelled card expiry date 3")
    
    # Sale card expiry date
    def S3_card_Exp_date_picker3(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.S3_card_Exp_3_on_save, on_cancel=self.S3_card_Exp_3_on_cancel)
        date_dialog.open()

    # Card Start Date
    # click ok
    def S3_card_start_3_on_save(self,instance,value,date_range):
        global S3_Start_Date3
        S3_Start_Date3 = value
        self.ids.S3_Card_Start_3_id.text = "Card Start Date:\n[color=#76FF03][b]{0}[/b][/color]".format(S3_Start_Date3)
        

    # click cancel
    def S3_card_start_3_on_cancel(self,instance,value):
        print("You cancelled card start date")
    

    def S3_card_start_date_3_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.S3_card_start_3_on_save, on_cancel=self.S3_card_start_3_on_cancel)
        date_dialog.open()

    # Sale/transaction  Date
    # click ok
    def S3_transaction_3_on_save(self,instance,value,date_range):
        global S3_Trans_Date_3
        S3_Trans_Date_3 = value
        self.ids.S3_transaction_Date_3_id.text = "Transaction Date:\n[color=#76FF03][b]{0}[/b][/color]".format(S3_Trans_Date_3)

    # click cancel
    def S3_transaction_3_on_cancel(self,instance,value):
        print("You cancelled card expiry date 3")
    
    # try also passing a value for variable to the on_save below
    def S3_transaction_date_3_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.S3_transaction_3_on_save, on_cancel=self.S3_transaction_3_on_cancel)
        date_dialog.open()

    # Get time
    def S3_get_time_3(self,instance,time):
        global S3_Trans_time3
        S3_Trans_time3 = time
        self.ids.S3_transaction_time_3_id.text = "Transaction Time:\n[color=#76FF03][b]{0}[/b][/color]".format(S3_Trans_time3)
    # Cancel
    def S3_on_time_3_cancel(self,instance,time):
        print("You canceled the time picker 3")

    def S3_show_time_picker3(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.S3_on_time_3_cancel,time = self.S3_get_time_3)
        time_dialog.open()

    # submit to database
    def S3_submit(self):
        # pass the input values into variables
        S3_Payment_method1 = self.ids.S3_payment_method_1_spin_id.text
        S3_Transfer_Reference1 = self.ids.S3_transfer_ref_1_textf.text
        S3_Card_nbr1 = self.ids.S3_card_nbr_1_textf.text
        S3_Debit_Type1 = self.ids.S3_Debit_type_1_spin_id.text
        S3_Auth_code1 = self.ids.S3_auth_1_textf.text
        S3_Amount1 = self.ids.S3_Amount_1_textf.text
        S3_Receipt_Nbr1 = self.ids.S3_Receipt_nbr_1_textf.text

        # Second payment
        S3_Payment_method2 = self.ids.S3_payment_method_2_spin_id.text
        S3_Transfer_Reference2 = self.ids.S3_transfer_ref_2_textf.text
        S3_Card_nbr2 = self.ids.S3_card_nbr_2_textf.text
        S3_Debit_Type2 = self.ids.S3_Debit_type_2_spin_id.text
        S3_Auth_code2 = self.ids.S3_auth_2_textf.text
        S3_Amount2 = self.ids.S3_Amount_2_textf.text
        S3_Receipt_Nbr2 = self.ids.S3_Receipt_nbr_2_textf.text

        # Second payment
        S3_Payment_method3 = self.ids.S3_payment_method_3_spin_id.text
        S3_Transfer_Reference3 = self.ids.S3_transfer_ref_3_textf.text
        S3_Card_nbr3 = self.ids.S3_card_nbr_3_textf.text
        S3_Debit_Type3 = self.ids.S3_Debit_type_3_spin_id.text
        S3_Auth_code3 = self.ids.S3_auth_3_textf.text
        S3_Amount3 = self.ids.S3_Amount_3_textf.text
        S3_Receipt_Nbr3 = self.ids.S3_Receipt_nbr_3_textf.text

        # Printing variables
        print("\nSale in three submision:\n")
        print("Firstname:\t{0}".format(CustomerScreen.FirstName))
        print("Middlename:\t{0}".format(CustomerScreen.MiddleName))
        print("Lastname:\t{0}".format(CustomerScreen.LastName))
        print("DOB:\t{0}".format(CustomerScreen.Customer_DOB))
        print("Age group:\t{0}".format(CustomerScreen.AgeGroup))

        print("House number:\t{0}".format(Cust_AddressScreen.Address1))
        print("Street:\t{0}".format(Cust_AddressScreen.Address2))
        print("City or Town:\t{0}".format(Cust_AddressScreen.Address3))
        print("County or Shire:\t{0}".format(Cust_AddressScreen.Address4))
        print("Country:\t{0}".format(Cust_AddressScreen.Address5))
        print("Postcode:\t{0}".format(Cust_AddressScreen.Address6))
        print("Email:\t{0}".format(Cust_AddressScreen.email))
        print("Tel:\t{0}".format(Cust_AddressScreen.Tel))
        print("\nVehicle registration:\t{0}".format(Deposit_or_SaleScreen.Vehicle_reg))

        # First Payment
        print("\nFirst Payment")
        print("Payment method 1:\t{0}".format(S3_Payment_method1))
        print("Transfer reference 1:\t{0}".format(S3_Transfer_Reference1))
        print("Card number 1:\t{0}".format(S3_Card_nbr1))
        print("Debit type 1:\t{0}".format(S3_Debit_Type1))
        print("Card expiry date 1:\t{0}".format(S3_Expiry_Date_1))
        print("Card start date 1:\t{0}".format(S3_Start_Date1))
        print("Transaction date 1:\t{0}".format(S3_Trans_Date_1))
        print("Tansaction time 1:\t{0}".format(S3_Trans_time1))
        print("Auth code 1:\t{0}".format(S3_Auth_code1))
        print("Sale Amount 1:\t{0}".format(S3_Amount1))
        print("Receipt number 1:\t{0}".format(S3_Receipt_Nbr1))

        # Payment 2
        print("\nSecond Payment")
        print("Payment method 2:\t{0}".format(S3_Payment_method2))
        print("Transfer reference 2:\t{0}".format(S3_Transfer_Reference2))
        print("Card number 2:\t{0}".format(S3_Card_nbr2))
        print("Debit type 2:\t{0}".format(S3_Debit_Type2))
        print("Card expiry date 2:\t{0}".format(S3_Expiry_Date_2))
        print("Card start date 2:\t{0}".format(S3_Start_Date2))
        print("Transaction date 2:\t{0}".format(S3_Trans_Date_2))
        print("Tansaction time 2:\t{0}".format(S3_Trans_time2))
        print("Auth code 2:\t{0}".format(S3_Auth_code2))
        print("Sale Amount 2:\t{0}".format(S3_Amount2))
        print("Receipt number 2:\t{0}".format(S3_Receipt_Nbr2))

        # Payment 3
        print("\nThird Payment")
        print("Payment method 3:\t{0}".format(S3_Payment_method3))
        print("Transfer reference 3:\t{0}".format(S3_Transfer_Reference3))
        print("Card number 3:\t{0}".format(S3_Card_nbr3))
        print("Debit type 3:\t{0}".format(S3_Debit_Type3))
        print("Card expiry date 3:\t{0}".format(S3_Expiry_Date_3))
        print("Card start date 3:\t{0}".format(S3_Start_Date3))
        print("Transaction date 3:\t{0}".format(S3_Trans_Date_3))
        print("Tansaction time 3:\t{0}".format(S3_Trans_time3))
        print("Auth code 3:\t{0}".format(S3_Auth_code3))
        print("Sale Amount 3:\t{0}".format(S3_Amount3))
        print("Receipt number 3:\t{0}".format(S3_Receipt_Nbr3))