from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDTimePicker
from kivy.properties import ListProperty
import CustomerScreen
import Cust_AddressScreen
import Deposit_or_SaleScreen

class Sale_with_Deposit_in_two_Screen(Screen):

        # Retrieving deposit info
    SD2 = [("Ngosa","Ndonge","2021/02/19"),
     ("Helena","Masitch","2021/03/01"),
     ("Hakimi","Ngi","2021/03/03"),
     ("Alfonso","Bertoli","2021/03/09")]

    
    SD2_Live_Deposit_list = ["{0}, {1}, {2}".format(x[0], x[1],x[2]) for x in SD2]

    def SD2_selected_Live_Deposit(self,value):
        x=value.split(',')
        global SD2_Deposit_Date
        SD2_Deposit_Date = x[2]

    def SD2_1_dep_sal_option_choice(self,value):
        print("Payment method 1: {0}".format(value))
    
    def SD2_Debit_type1(self,value):
        print("Sale debit type 1: {0}".format(value))
    
        # D2 Card Expiry Date 1
    # click ok
    def SD2_card_Exp_1_on_save(self,instance,value,date_range):
        global SD2_Card_Expiry_Date_1
        SD2_Card_Expiry_Date_1 = value
        self.ids.SD2_Card_Expiry_1_id.text = "Card Expiry Date:\n[color=#76FF03][b]{0}[/b][/color]".format(SD2_Card_Expiry_Date_1)

    # click cancel
    def SD2_card_Exp_1_on_cancel(self,instance,value):
        print("You cancelled card expiry date 1")
    
    # Sale card expiry date
    def SD2_card_Exp_date_picker1(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.SD2_card_Exp_1_on_save, on_cancel=self.SD2_card_Exp_1_on_cancel)
        date_dialog.open()

    # Card Start Date
    # click ok
    def SD2_card_start_1_on_save(self,instance,value,date_range):
        global SD2_Card_Start_Date1
        SD2_Card_Start_Date1 = value
        self.ids.SD2_Card_Start_1_id.text = "Card Start Date:\n[color=#76FF03][b]{0}[/b][/color]".format(SD2_Card_Start_Date1)
        

    # click cancel
    def SD2_card_start_1_on_cancel(self,instance,value):
        print("You cancelled card start date")
    

    def SD2_card_start_date_1_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.SD2_card_start_1_on_save, on_cancel=self.SD2_card_start_1_on_cancel)
        date_dialog.open()

    # Deposit/transaction  Date
    # click ok
    def SD2_transaction_1_on_save(self,instance,value,date_range):
        global SD2_Trans_Date_1
        SD2_Trans_Date_1 = value
        self.ids.SD2_transaction_Date_1_id.text = "Transaction Date:\n[color=#76FF03][b]{0}[/b][/color]".format(SD2_Trans_Date_1)

    # click cancel
    def SD2_transaction_1_on_cancel(self,instance,value):
        print("You cancelled card expiry date")
    
    # try also passing a value for variable to the on_save below
    def SD2_transaction_date_1_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.SD2_transaction_1_on_save, on_cancel=self.SD2_transaction_1_on_cancel)
        date_dialog.open()

    # Get time
    def SD2_get_time_1(self,instance,time):
        global SD2_Trans_time1
        SD2_Trans_time1 = time
        self.ids.SD2_transaction_time_1_id.text = "Transaction Time 1:\n[color=#76FF03][b]{0}[/b][/color]".format(SD2_Trans_time1)
    # Cancel
    def SD2_on_time_1_cancel(self,instance,time):
        print("You canceled the time picker")

    def SD2_show_Trans_1_time_picker1(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.SD2_on_time_1_cancel,time = self.SD2_get_time_1)
        time_dialog.open()

    # Second Payment
    def SD2_dep_sal_option_choice2(self,value):
        print("Payment method 2: {0}".format(value))
    
    def SD2_Debit_type2(self,value):
        print("Sale debit type 2: {0}".format(value))
    
        # D2 Card Expiry Date 1
    # click ok
    def SD2_card_Exp_2_on_save(self,instance,value,date_range):
        global SD2_Card_Expiry_Date2
        SD2_Card_Expiry_Date2 = value
        self.ids.SD2_Card_Expiry_2_id.text = "Card Expiry Date:\n[color=#76FF03][b]{0}[/b][/color]".format(SD2_Card_Expiry_Date2)
        

    # click cancel
    def SD2_card_Exp_2_on_cancel(self,instance,value):
        print("You cancelled card expiry date")
    
    # Deposit card expiry date
    def SD2_card_Exp_date_picker2(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.SD2_card_Exp_2_on_save, on_cancel=self.SD2_card_Exp_2_on_cancel)
        date_dialog.open()

    # Card Start Date
    # click ok
    def SD2_card_start_2_on_save(self,instance,value,date_range):
        global SD2_Card_Start_Date2
        SD2_Card_Start_Date2 = value
        self.ids.SD2_Card_Start_2_id.text = "Card Start Date:\n[color=#76FF03][b]{0}[/b][/color]".format(SD2_Card_Start_Date2)
        

    # click cancel
    def SD2_card_start_2_on_cancel(self,instance,value):
        print("You cancelled card start date")
    

    def SD2_Card_start_date_2_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.SD2_card_start_2_on_save, on_cancel=self.SD2_card_start_2_on_cancel)
        date_dialog.open()

    # Deposit/transaction  Date
    # click ok
    def SD2_transaction_2_on_save(self,instance,value,date_range):
        global SD2_Trans_Date_2
        SD2_Trans_Date_2 = value
        self.ids.SD2_transaction_Date_2_id.text = "Transaction Date:\n[color=#76FF03][b]{0}[/b][/color]".format(SD2_Trans_Date_2)

    # click cancel
    def SD2_transaction_2_on_cancel(self,instance,value):
        print("You cancelled card expiry date")
    
    # try also passing a value for variable to the on_save below
    def SD2_transaction_date_2_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.SD2_transaction_2_on_save, on_cancel=self.SD2_transaction_2_on_cancel)
        date_dialog.open()

    # Get time
    def SD2_get_time_2(self,instance,time):
        global SD2_Trans_time2
        SD2_Trans_time2 = time
        self.ids.SD2_transaction_time_2_id.text = "Transaction Time:\n[color=#76FF03][b]{0}[/b][/color]".format(SD2_Trans_time2)
    # Cancel
    def SD2_on_time_2_cancel(self,instance,time):
        print("You canceled the time picker")

    def SD2_show_time_picker2(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.SD2_on_time_2_cancel,time = self.SD2_get_time_2)
        time_dialog.open()


    # submit to database
    def SD2_submit(self):
        # pass the input values into variables
        SD2_Payment_method1 = self.ids.SD2_payment_method_1_spin_id.text
        SD2_Transfer_Reference1 = self.ids.SD2_transfer_ref_1_textf.text
        SD2_Card_nbr1 = self.ids.SD2_card_nbr_1_textf.text
        SD2_Debit_Type1 = self.ids.SD2_Debit_type_1_spin_id.text
        SD2_Auth_code1 = self.ids.SD2_auth_1_textf.text
        SD2_Amount1 = self.ids.SD2_Amount_1_textf.text
        SD2_Receipt_Nbr1 = self.ids.SD2_Receipt_nbr_1_textf.text

        # Second payment
        SD2_Payment_method2 = self.ids.SD2_payment_method_2_spin_id.text
        SD2_Transfer_Reference2 = self.ids.SD2_transfer_ref_2_textf.text
        SD2_Card_nbr2 = self.ids.SD2_card_nbr_2_textf.text
        SD2_Debit_Type2 = self.ids.SD2_Debit_type_2_spin_id.text
        SD2_Auth_code2 = self.ids.SD2_auth_2_textf.text
        SD2_Amount2 = self.ids.SD2_Amount_2_textf.text
        SD2_Receipt_Nbr2 = self.ids.SD2_Receipt_nbr_2_textf.text

        # Printing variables
        print("\nSale after Deposit two payments submision:\n")
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
        print("\nDeposit Date:\t{0}".format(SD2_Deposit_Date))

        # First Payment
        print("\nFirst Payment")
        print("Payment method 1:\t{0}".format(SD2_Payment_method1))
        print("Transfer reference 1:\t{0}".format(SD2_Transfer_Reference1))
        print("Card number 1:\t{0}".format(SD2_Card_nbr1))
        print("Debit type 1:\t{0}".format(SD2_Debit_Type1))
        print("Card expiry date 1:\t{0}".format(SD2_Card_Expiry_Date_1))
        print("Card start date 1:\t{0}".format(SD2_Card_Start_Date1))
        print("Transaction date 1:\t{0}".format(SD2_Trans_Date_1))
        print("Tansaction time 1:\t{0}".format(SD2_Trans_time1))
        print("Auth code 1:\t{0}".format(SD2_Auth_code1))
        print("Transaction Amount 1:\t{0}".format(SD2_Amount1))
        print("Receipt number 1:\t{0}".format(SD2_Receipt_Nbr1))

        # Payment 2
        print("\nSecond Payment")
        print("Payment method 2:\t{0}".format(SD2_Payment_method2))
        print("Transfer reference 2:\t{0}".format(SD2_Transfer_Reference2))
        print("Card number 2:\t{0}".format(SD2_Card_nbr2))
        print("Debit type 2:\t{0}".format(SD2_Debit_Type2))
        print("Card expiry date 2:\t{0}".format(SD2_Card_Expiry_Date2))
        print("Card start date 2:\t{0}".format(SD2_Card_Start_Date2))
        print("Transaction date 2:\t{0}".format(SD2_Trans_Date_2))
        print("Tansaction time 2:\t{0}".format(SD2_Trans_time2))
        print("Auth code 2:\t{0}".format(SD2_Auth_code2))
        print("Transaction Amount 2:\t{0}".format(SD2_Amount2))
        print("Receipt number 2:\t{0}".format(SD2_Receipt_Nbr2))