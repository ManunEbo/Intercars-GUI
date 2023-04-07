from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDTimePicker
from kivy.properties import ListProperty
import CustomerScreen
import Cust_AddressScreen
import Deposit_or_SaleScreen

class Deposit_in_two_Screen(Screen):
    def D2_1_dep_sal_option_choice(self,value):
        print("Payment method 1: {0}".format(value))
    
    def D2_Deposit_Debit_type1(self,value):
        print("Deposit debit type 1: {0}".format(value))
    
        # D2 Card Expiry Date 1
    # click ok
    def D2_Deposit_card_Exp_1_on_save(self,instance,value,date_range):
        global D2_Deposit_Expiry_Date_1
        D2_Deposit_Expiry_Date_1 = value
        self.ids.D2_Card_Expiry_1_id.text = "Card Expiry date:\n[color=#76FF03][b]{0}[/b][/color]".format(D2_Deposit_Expiry_Date_1)

    # click cancel
    def D2_Deposit_card_Exp_1_on_cancel(self,instance,value):
        print("You cancelled card expiry date")
    
    # Deposit card expiry date
    def D2_Deposit_card_Exp_date_picker1(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.D2_Deposit_card_Exp_1_on_save, on_cancel=self.D2_Deposit_card_Exp_1_on_cancel)
        date_dialog.open()

    # Card Start Date
    # click ok
    def D2_Deposit_card_start_1_on_save(self,instance,value,date_range):
        global D2_Deposit_Start_Date1
        D2_Deposit_Start_Date1 = value
        self.ids.D2_Card_Start_1_id.text = "Card start date:\n[color=#76FF03][b]{0}[/b][/color]".format(D2_Deposit_Start_Date1)
        

    # click cancel
    def D2_Deposit_card_start_1_on_cancel(self,instance,value):
        print("You cancelled card start date")
    
    # try also passing a value for variable to the on_save below
    def D2_Deposit_card_start_date_1_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.D2_Deposit_card_start_1_on_save, on_cancel=self.D2_Deposit_card_start_1_on_cancel)
        date_dialog.open()

    # Deposit/transaction  Date
    # click ok
    def D2_Deposit_transaction_1_on_save(self,instance,value,date_range):
        global D2_Deposit_Trans_Date_1
        D2_Deposit_Trans_Date_1 = value
        self.ids.D2_Deposit_transaction_Date_1_id.text = "Deposit date:\n[color=#76FF03][b]{0}[/b][/color]".format(D2_Deposit_Trans_Date_1)

    # click cancel
    def D2_Deposit_transaction_1_on_cancel(self,instance,value):
        print("You cancelled card expiry date")
    
    # try also passing a value for variable to the on_save below
    def D2_Deposit_transaction_date_1_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.D2_Deposit_transaction_1_on_save, on_cancel=self.D2_Deposit_transaction_1_on_cancel)
        date_dialog.open()

    # Get time
    def D2_Deposit_get_time_1(self,instance,time):
        global Deposit_in_1_Trans_time
        Deposit_in_1_Trans_time = time
        self.ids.D2_Deposit_transaction_time_1_id.text = "Deposit Time:\n[color=#76FF03][b]{0}[/b][/color]".format(Deposit_in_1_Trans_time)
    # Cancel
    def D2_Deposit_on_time_1_cancel(self,instance,time):
        print("You canceled the time picker")

    def D2_show_Deposit_time_picker1(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.D2_Deposit_on_time_1_cancel,time = self.D2_Deposit_get_time_1)
        time_dialog.open()

    # Second Payment
    def D2_dep_sal_option_choice2(self,value):
        print("Payment method 2: {0}".format(value))
    
    def D2_Deposit_Debit_type2(self,value):
        print("Deposit debit type 2: {0}".format(value))
    
        # D2 Card Expiry Date 1
    # click ok
    def D2_Deposit_card_Exp_2_on_save(self,instance,value,date_range):
        global D2_Deposit_Expiry_Date_2
        D2_Deposit_Expiry_Date_2 = value
        self.ids.D2_Card_Expiry_2_id.text = "Card Expiry date:\n[color=#76FF03][b]{0}[/b][/color]".format(D2_Deposit_Expiry_Date_2)
        

    # click cancel
    def D2_Deposit_card_Exp_2_on_cancel(self,instance,value):
        print("You cancelled card expiry date")
    
    # Deposit card expiry date
    def D2_Deposit_card_Exp_date_picker2(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.D2_Deposit_card_Exp_2_on_save, on_cancel=self.D2_Deposit_card_Exp_2_on_cancel)
        date_dialog.open()

    # Card Start Date
    # click ok
    def D2_Deposit_card_start_2_on_save(self,instance,value,date_range):
        global D2_Deposit_Start_Date2
        D2_Deposit_Start_Date2 = value
        self.ids.D2_Card_Start_2_id.text = "Card start date:\n[color=#76FF03][b]{0}[/b][/color]".format(D2_Deposit_Start_Date2)
        

    # click cancel
    def D2_Deposit_card_start_2_on_cancel(self,instance,value):
        print("You cancelled card start date")
    

    def D2_Deposit_card_start_date_2_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.D2_Deposit_card_start_2_on_save, on_cancel=self.D2_Deposit_card_start_2_on_cancel)
        date_dialog.open()

    # Deposit/transaction  Date
    # click ok
    def D2_Deposit_transaction_2_on_save(self,instance,value,date_range):
        global D2_Deposit_Trans_Date_2
        D2_Deposit_Trans_Date_2 = value
        self.ids.D2_Deposit_transaction_Date_2_id.text = "Deposit date:\n[color=#76FF03][b]{0}[/b][/color]".format(D2_Deposit_Trans_Date_2)

    # click cancel
    def D2_Deposit_transaction_2_on_cancel(self,instance,value):
        print("You cancelled card expiry date")
    
    # try also passing a value for variable to the on_save below
    def D2_Deposit_transaction_date_2_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.D2_Deposit_transaction_2_on_save, on_cancel=self.D2_Deposit_transaction_2_on_cancel)
        date_dialog.open()

    # Get time
    def D2_Deposit_get_time_2(self,instance,time):
        global D2_Deposit_Trans_time2
        D2_Deposit_Trans_time2 = time
        self.ids.D2_Deposit_transaction_time_2_id.text = "Deposit Time:\n[color=#76FF03][b]{0}[/b][/color]".format(D2_Deposit_Trans_time2)
    # Cancel
    def D2_Deposit_on_time_2_cancel(self,instance,time):
        print("You canceled the time picker")

    def D2_show_Deposit_time_picker2(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.D2_Deposit_on_time_2_cancel,time = self.D2_Deposit_get_time_2)
        time_dialog.open()


    # submit to database
    def D2_Deposit_submit(self):
        # pass the input values into variables
        D2_Deposit_Payment_method1 = self.ids.D2_payment_method_1_spin_id.text
        D2_Deposit_Transfer_Reference1 = self.ids.D2_transfer_ref_1_textf.text
        D2_Deposit_Card_nbr1 = self.ids.D2_card_nbr_1_textf.text
        D2_Deposit_Debit_Type1 = self.ids.D2_Debit_type_1_spin_id.text
        D2_Deposit_Auth_code1 = self.ids.D2_Deposit_auth_1_textf.text
        D2_Deposit_Amount1 = self.ids.D2_Deposit_Amount_1_textf.text
        D2_Deposit_Receipt_Nbr1 = self.ids.D2_Deposit_Receipt_nbr_1_textf.text

        # Second payment
        D2_Deposit_Payment_method2 = self.ids.D2_payment_method_2_spin_id.text
        D2_Deposit_Transfer_Reference2 = self.ids.D2_transfer_ref_2_textf.text
        D2_Deposit_Card_nbr2 = self.ids.D2_card_nbr_2_textf.text
        D2_Deposit_Debit_Type2 = self.ids.D2_Debit_type_2_spin_id.text
        D2_Deposit_Auth_code2 = self.ids.D2_Deposit_auth_2_textf.text
        D2_Deposit_Amount2 = self.ids.D2_Deposit_Amount_2_textf.text
        D2_Deposit_Receipt_Nbr2 = self.ids.D2_Deposit_Receipt_nbr_2_textf.text

        # Printing variables
        print("\nDeposit in one submision:\n")
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
        print("Payment method 1:\t{0}".format(D2_Deposit_Payment_method1))
        print("Transfer reference 1:\t{0}".format(D2_Deposit_Transfer_Reference1))
        print("Card number 1:\t{0}".format(D2_Deposit_Card_nbr1))
        print("Debit type 1:\t{0}".format(D2_Deposit_Debit_Type1))
        print("Card expiry date 1:\t{0}".format(D2_Deposit_Expiry_Date_1))
        print("Card start date 1:\t{0}".format(D2_Deposit_Start_Date1))
        print("Transaction date 1:\t{0}".format(D2_Deposit_Trans_Date_1))
        print("Tansaction time 1:\t{0}".format(Deposit_in_1_Trans_time))
        print("Auth code 1:\t{0}".format(D2_Deposit_Auth_code1))
        print("Deposit Amount 1:\t{0}".format(D2_Deposit_Amount1))
        print("Receipt number 1:\t{0}".format(D2_Deposit_Receipt_Nbr1))

        # Payment 2
        print("\nSecond Payment")
        print("Payment method 2:\t{0}".format(D2_Deposit_Payment_method2))
        print("Transfer reference 2:\t{0}".format(D2_Deposit_Transfer_Reference2))
        print("Card number 2:\t{0}".format(D2_Deposit_Card_nbr2))
        print("Debit type 2:\t{0}".format(D2_Deposit_Debit_Type2))
        print("Card expiry date 2:\t{0}".format(D2_Deposit_Expiry_Date_2))
        print("Card start date 2:\t{0}".format(D2_Deposit_Start_Date2))
        print("Transaction date 2:\t{0}".format(D2_Deposit_Trans_Date_2))
        print("Tansaction time 2:\t{0}".format(D2_Deposit_Trans_time2))
        print("Auth code 2:\t{0}".format(D2_Deposit_Auth_code2))
        print("Deposit Amount 2:\t{0}".format(D2_Deposit_Amount2))
        print("Receipt number 2:\t{0}".format(D2_Deposit_Receipt_Nbr2))