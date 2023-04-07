from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDTimePicker
from kivy.properties import ListProperty
import CustomerScreen
import Cust_AddressScreen
import Deposit_or_SaleScreen

class Sale_with_Deposit_in_three_Screen(Screen):
    # Retrieving deposit info
    SD3 = [("Ngosa","Ndonge","2021/02/19"),
     ("Helena","Masitch","2021/03/01"),
     ("Hakimi","Ngi","2021/03/03"),
     ("Alfonso","Bertoli","2021/03/09")]

    SD3_Live_Deposit_list = ["{0}, {1}, {2}".format(x[0], x[1],x[2]) for x in SD3]

    def SD3_selected_Live_Deposit(self,value):
        x=value.split(',')
        global SD3_Deposit_Date
        SD3_Deposit_Date = x[2]

    def SD3_dep_sal_option_choice1(self,value):
        print("Payment method 1: {0}".format(value))
    
    def SD3_Debit_type1(self,value):
        print("Sale debit type 1: {0}".format(value))
    
        # SD3 Card Expiry Date 1
    # click ok
    def SD3_card_Exp_1_on_save(self,instance,value,date_range):
        global SD3_Expiry_Date_1
        SD3_Expiry_Date_1 = value
        self.ids.SD3_Card_Expiry_1_id.text = "Card Expiry date:\n[color=#76FF03][b]{0}[/b][/color]".format(SD3_Expiry_Date_1)

    # click cancel
    def SD3_card_Exp_1_on_cancel(self,instance,value):
        print("You cancelled card expiry date")
    
    # Sale card expiry date
    def SD3_card_Exp_date_picker1(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.SD3_card_Exp_1_on_save, on_cancel=self.SD3_card_Exp_1_on_cancel)
        date_dialog.open()

    # Card Start Date
    # click ok
    def SD3_card_start_1_on_save(self,instance,value,date_range):
        global SD3_Start_Date1
        SD3_Start_Date1 = value
        self.ids.SD3_Card_Start_1_id.text = "Card Start Date:\n[color=#76FF03][b]{0}[/b][/color]".format(SD3_Start_Date1)
        

    # click cancel
    def SD3_card_start_1_on_cancel(self,instance,value):
        print("You cancelled card start date")
    
    # try also passing a value for variable to the on_save below
    def SD3_card_start_date_1_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.SD3_card_start_1_on_save, on_cancel=self.SD3_card_start_1_on_cancel)
        date_dialog.open()

    # Sale/transaction  Date
    # click ok
    def SD3_transaction_1_on_save(self,instance,value,date_range):
        global SD3_Trans_Date_1
        SD3_Trans_Date_1 = value
        self.ids.SD3_transaction_Date_1_id.text = "Sale Date:\n[color=#76FF03][b]{0}[/b][/color]".format(SD3_Trans_Date_1)

    # click cancel
    def SD3_transaction_1_on_cancel(self,instance,value):
        print("You cancelled card expiry date")
    
    # try also passing a value for variable to the on_save below
    def SD3_transaction_date_1_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.SD3_transaction_1_on_save, on_cancel=self.SD3_transaction_1_on_cancel)
        date_dialog.open()

    # Get time
    def SD3_get_time_1(self,instance,time):
        global SD3_Trans_time1
        SD3_Trans_time1 = time
        self.ids.SD3_transaction_time_1_id.text = "Transaction Time:\n[color=#76FF03][b]{0}[/b][/color]".format(SD3_Trans_time1)
    # Cancel
    def SD3_on_time_1_cancel(self,instance,time):
        print("You canceled the time picker")

    def SD3_show_time_picker1(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.SD3_on_time_1_cancel,time = self.SD3_get_time_1)
        time_dialog.open()

    # Second Payment
    def SD3_dep_sal_option_choice2(self,value):
        print("Payment method 2: {0}".format(value))
    
    def SD3_Debit_type2(self,value):
        print("Sale debit type 2: {0}".format(value))
    
        # D2 Card Expiry Date 1
    # click ok
    def SD3_card_Exp_2_on_save(self,instance,value,date_range):
        global SD3_Expiry_Date_2
        SD3_Expiry_Date_2 = value
        self.ids.SD3_Card_Expiry_2_id.text = "Card Expiry Date:\n[color=#76FF03][b]{0}[/b][/color]".format(SD3_Expiry_Date_2)
        

    # click cancel
    def SD3_card_Exp_2_on_cancel(self,instance,value):
        print("You cancelled card expiry date")
    
    # Sale card expiry date
    def SD3_card_Exp_date_picker2(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.SD3_card_Exp_2_on_save, on_cancel=self.SD3_card_Exp_2_on_cancel)
        date_dialog.open()

    # Card Start Date
    # click ok
    def SD3_card_start_2_on_save(self,instance,value,date_range):
        global SD3_Start_Date2
        SD3_Start_Date2 = value
        self.ids.SD3_Card_Start_2_id.text = "Card Start Date:\n[color=#76FF03][b]{0}[/b][/color]".format(SD3_Start_Date2)
        

    # click cancel
    def SD3_card_start_2_on_cancel(self,instance,value):
        print("You cancelled card start date")
    

    def SD3_card_start_date_2_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.SD3_card_start_2_on_save, on_cancel=self.SD3_card_start_2_on_cancel)
        date_dialog.open()

    # Sale/transaction  Date
    # click ok
    def SD3_transaction_2_on_save(self,instance,value,date_range):
        global SD3_Trans_Date_2
        SD3_Trans_Date_2 = value
        self.ids.SD3_transaction_Date_2_id.text = "Transaction Date:\n[color=#76FF03][b]{0}[/b][/color]".format(SD3_Trans_Date_2)

    # click cancel
    def SD3_transaction_2_on_cancel(self,instance,value):
        print("You cancelled card expiry date")
    
    # try also passing a value for variable to the on_save below
    def SD3_transaction_date_2_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.SD3_transaction_2_on_save, on_cancel=self.SD3_transaction_2_on_cancel)
        date_dialog.open()

    # Get time
    def SD3_get_time_2(self,instance,time):
        global SD3_Trans_time2
        SD3_Trans_time2 = time
        self.ids.SD3_transaction_time_2_id.text = "Transaction Time:\n[color=#76FF03][b]{0}[/b][/color]".format(SD3_Trans_time2)
    # Cancel
    def SD3_on_time_2_cancel(self,instance,time):
        print("You canceled the time picker")

    def SD3_show_time_picker2(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.SD3_on_time_2_cancel,time = self.SD3_get_time_2)
        time_dialog.open()

    # Third Payment
    def SD3_dep_sal_option_choice3(self,value):
        print("Payment method 3: {0}".format(value))
    
    def SD3_Debit_type3(self,value):
        print("Sale debit type 3: {0}".format(value))
    
        # SD3 Card Expiry Date 3
    # click ok
    def SD3_card_Exp_3_on_save(self,instance,value,date_range):
        global SD3_Expiry_Date_3
        SD3_Expiry_Date_3 = value
        self.ids.SD3_Card_Expiry_3_id.text = "Card Expiry Date:\n[color=#76FF03][b]{0}[/b][/color]".format(SD3_Expiry_Date_3)
        

    # click cancel
    def SD3_card_Exp_3_on_cancel(self,instance,value):
        print("You cancelled card expiry date 3")
    
    # Sale card expiry date
    def SD3_card_Exp_date_picker3(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.SD3_card_Exp_3_on_save, on_cancel=self.SD3_card_Exp_3_on_cancel)
        date_dialog.open()

    # Card Start Date
    # click ok
    def SD3_card_start_3_on_save(self,instance,value,date_range):
        global SD3_Start_Date3
        SD3_Start_Date3 = value
        self.ids.SD3_Card_Start_3_id.text = "Card Start Date:\n[color=#76FF03][b]{0}[/b][/color]".format(SD3_Start_Date3)
        

    # click cancel
    def SD3_card_start_3_on_cancel(self,instance,value):
        print("You cancelled card start date")
    

    def SD3_card_start_date_3_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.SD3_card_start_3_on_save, on_cancel=self.SD3_card_start_3_on_cancel)
        date_dialog.open()

    # Sale/transaction  Date
    # click ok
    def SD3_transaction_3_on_save(self,instance,value,date_range):
        global SD3_Trans_Date_3
        SD3_Trans_Date_3 = value
        self.ids.SD3_transaction_Date_3_id.text = "Transaction Date:\n[color=#76FF03][b]{0}[/b][/color]".format(SD3_Trans_Date_3)

    # click cancel
    def SD3_transaction_3_on_cancel(self,instance,value):
        print("You cancelled card expiry date 3")
    
    # try also passing a value for variable to the on_save below
    def SD3_transaction_date_3_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.SD3_transaction_3_on_save, on_cancel=self.SD3_transaction_3_on_cancel)
        date_dialog.open()

    # Get time
    def SD3_get_time_3(self,instance,time):
        global SD3_Trans_time3
        SD3_Trans_time3 = time
        self.ids.SD3_transaction_time_3_id.text = "Transaction Time:\n[color=#76FF03][b]{0}[/b][/color]".format(SD3_Trans_time3)
    # Cancel
    def SD3_on_time_3_cancel(self,instance,time):
        print("You canceled the time picker 3")

    def SD3_show_time_picker3(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.SD3_on_time_3_cancel,time = self.SD3_get_time_3)
        time_dialog.open()

    # submit to database
    def SD3_submit(self):
        # pass the input values into variables
        SD3_Payment_method1 = self.ids.SD3_payment_method_1_spin_id.text
        SD3_Transfer_Reference1 = self.ids.SD3_transfer_ref_1_textf.text
        SD3_Card_nbr1 = self.ids.SD3_card_nbr_1_textf.text
        SD3_Debit_Type1 = self.ids.SD3_Debit_type_1_spin_id.text
        SD3_Auth_code1 = self.ids.SD3_auth_1_textf.text
        SD3_Amount1 = self.ids.SD3_Amount_1_textf.text
        SD3_Receipt_Nbr1 = self.ids.SD3_Receipt_nbr_1_textf.text

        # Second payment
        SD3_Payment_method2 = self.ids.SD3_payment_method_2_spin_id.text
        SD3_Transfer_Reference2 = self.ids.SD3_transfer_ref_2_textf.text
        SD3_Card_nbr2 = self.ids.SD3_card_nbr_2_textf.text
        SD3_Debit_Type2 = self.ids.SD3_Debit_type_2_spin_id.text
        SD3_Auth_code2 = self.ids.SD3_auth_2_textf.text
        SD3_Amount2 = self.ids.SD3_Amount_2_textf.text
        SD3_Receipt_Nbr2 = self.ids.SD3_Receipt_nbr_2_textf.text

        # Second payment
        SD3_Payment_method3 = self.ids.SD3_payment_method_3_spin_id.text
        SD3_Transfer_Reference3 = self.ids.SD3_transfer_ref_3_textf.text
        SD3_Card_nbr3 = self.ids.SD3_card_nbr_3_textf.text
        SD3_Debit_Type3 = self.ids.SD3_Debit_type_3_spin_id.text
        SD3_Auth_code3 = self.ids.SD3_auth_3_textf.text
        SD3_Amount3 = self.ids.SD3_Amount_3_textf.text
        SD3_Receipt_Nbr3 = self.ids.SD3_Receipt_nbr_3_textf.text

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
        print("\nDeposit Date:\t{0}".format(SD3_Deposit_Date))

        # First Payment
        print("\nFirst Payment")
        print("Payment method 1:\t{0}".format(SD3_Payment_method1))
        print("Transfer reference 1:\t{0}".format(SD3_Transfer_Reference1))
        print("Card number 1:\t{0}".format(SD3_Card_nbr1))
        print("Debit type 1:\t{0}".format(SD3_Debit_Type1))
        print("Card expiry date 1:\t{0}".format(SD3_Expiry_Date_1))
        print("Card start date 1:\t{0}".format(SD3_Start_Date1))
        print("Transaction date 1:\t{0}".format(SD3_Trans_Date_1))
        print("Tansaction time 1:\t{0}".format(SD3_Trans_time1))
        print("Auth code 1:\t{0}".format(SD3_Auth_code1))
        print("Sale Amount 1:\t{0}".format(SD3_Amount1))
        print("Receipt number 1:\t{0}".format(SD3_Receipt_Nbr1))

        # Payment 2
        print("\nSecond Payment")
        print("Payment method 2:\t{0}".format(SD3_Payment_method2))
        print("Transfer reference 2:\t{0}".format(SD3_Transfer_Reference2))
        print("Card number 2:\t{0}".format(SD3_Card_nbr2))
        print("Debit type 2:\t{0}".format(SD3_Debit_Type2))
        print("Card expiry date 2:\t{0}".format(SD3_Expiry_Date_2))
        print("Card start date 2:\t{0}".format(SD3_Start_Date2))
        print("Transaction date 2:\t{0}".format(SD3_Trans_Date_2))
        print("Tansaction time 2:\t{0}".format(SD3_Trans_time2))
        print("Auth code 2:\t{0}".format(SD3_Auth_code2))
        print("Sale Amount 2:\t{0}".format(SD3_Amount2))
        print("Receipt number 2:\t{0}".format(SD3_Receipt_Nbr2))

        # Payment 3
        print("\nThird Payment")
        print("Payment method 3:\t{0}".format(SD3_Payment_method3))
        print("Transfer reference 3:\t{0}".format(SD3_Transfer_Reference3))
        print("Card number 3:\t{0}".format(SD3_Card_nbr3))
        print("Debit type 3:\t{0}".format(SD3_Debit_Type3))
        print("Card expiry date 3:\t{0}".format(SD3_Expiry_Date_3))
        print("Card start date 3:\t{0}".format(SD3_Start_Date3))
        print("Transaction date 3:\t{0}".format(SD3_Trans_Date_3))
        print("Tansaction time 3:\t{0}".format(SD3_Trans_time3))
        print("Auth code 3:\t{0}".format(SD3_Auth_code3))
        print("Sale Amount 3:\t{0}".format(SD3_Amount3))
        print("Receipt number 3:\t{0}".format(SD3_Receipt_Nbr3))