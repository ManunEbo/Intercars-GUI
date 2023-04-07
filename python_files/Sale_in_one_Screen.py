from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDTimePicker
from kivy.properties import ListProperty
import CustomerScreen
import Cust_AddressScreen
import Deposit_or_SaleScreen

class Sale_in_one_Screen(Screen):
        # Checks on the values being passed
    # Payment method
    def S1_dep_sal_option_choice(self,value):
        print("\nPayment method: {0}".format(value))
    
    # Debit type
    def S1_Debit_type(self,value):
        print("\nDeposit type: {0}".format(value))

    # Card Expiry Date
    # click ok
    def S1_card_Exp_on_save(self,instance,value,date_range):
        global S1_Expiry_Date
        S1_Expiry_Date = value
        self.ids.S1_Card_Expiry_id.text = "Card Expiry Date:\n[color=#76FF03][b]{0}[/b][/color]".format(S1_Expiry_Date)
        
    # click cancel
    def S1_card_Exp_on_cancel(self,instance,value):
        print("You cancelled card expiry date")
    
    # try also passing a value for variable to the on_save below
    def S1_card_Exp_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.S1_card_Exp_on_save, on_cancel=self.S1_card_Exp_on_cancel)
        date_dialog.open()

    # Card Start Date
    # click ok
    def S1_card_start_on_save(self,instance,value,date_range):
        global S1_Card_Start_Date
        S1_Card_Start_Date = value
        self.ids.S1_Card_Start_id.text = "Card Start Date:\n[color=#76FF03][b]{0}[/b][/color]".format(S1_Card_Start_Date)
        

    # click cancel
    def S1_card_start_on_cancel(self,instance,value):
        print("You cancelled card start date")
    
    # try also passing a value for variable to the on_save below
    def S1_card_start_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.S1_card_start_on_save, on_cancel=self.S1_card_start_on_cancel)
        date_dialog.open()

    # Deposit/transaction  Date
    # click ok
    def S1_transaction_on_save(self,instance,value,date_range):
        global S1_Trans_Date
        S1_Trans_Date = value
        self.ids.S1_transaction_Date_id.text = "Deposit Date:\n[color=#76FF03][b]{0}[/b][/color]".format(S1_Trans_Date)

    # click cancel
    def S1_transaction_on_cancel(self,instance,value):
        print("You cancelled card expiry date")
    
    # try also passing a value for variable to the on_save below
    def S1_transaction_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.S1_transaction_on_save, on_cancel=self.S1_transaction_on_cancel)
        date_dialog.open()


    # Get time
    def S1_get_time(self,instance,time):
        global S1_Trans_time
        S1_Trans_time = time
        self.ids.S1_transaction_time_id.text = "Deposit Time:\n[color=#76FF03][b]{0}[/b][/color]".format(S1_Trans_time)
    # Cancel
    def S1_on_time_cancel(self,instance,time):
        print("You canceled the time picker")

    def show_S1_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.S1_on_time_cancel,time = self.S1_get_time)
        time_dialog.open()

    # submit to database
    def S1_submit(self):
        # pass the input values into variables
        S1_Payment_method = self.ids.S1_payment_method_spin_id.text
        S1_Transfer_Reference = self.ids.S1_transfer_ref_textf.text
        S1_Card_nbr = self.ids.S1_card_nbr_textf.text
        S1_Debit_Type = self.ids.S1_Debit_type_spin_id.text
        S1_Auth_code = self.ids.S1_auth_textf.text
        S1_Amount = self.ids.S1_Amount_textf.text
        S1_Receipt_Nbr = self.ids.S1_Receipt_nbr_textf.text

        print("\nSale in one submision:\n")
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

        print("Payment method:\t{0}".format(S1_Payment_method))
        print("Transfer reference:\t{0}".format(S1_Transfer_Reference))
        print("Card number:\t{0}".format(S1_Card_nbr))
        print("Debit type:\t{0}".format(S1_Debit_Type))
        print("Card expiry date:\t{0}".format(S1_Expiry_Date))
        print("Card start date:\t{0}".format(S1_Card_Start_Date))
        print("Transaction date:\t{0}".format(S1_Trans_Date))
        print("Tansaction time:\t{0}".format(S1_Trans_time))
        print("Auth code:\t{0}".format(S1_Auth_code))
        print("Deposit Amount:\t{0}".format(S1_Amount))
        print("Receipt number:\t{0}".format(S1_Receipt_Nbr))