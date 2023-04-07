from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDTimePicker
from kivy.properties import ListProperty
import CustomerScreen
import Cust_AddressScreen
import Deposit_or_SaleScreen

class Sale_with_Deposit_in_one_Screen(Screen):

    # Retrieving deposit info
    SD1 = [("Ngosa","Ndonge","2021/02/19"),
     ("Helena","Masitch","2021/03/01"),
     ("Hakimi","Ngi","2021/03/03"),
     ("Alfonso","Bertoli","2021/03/09")]

    
    Live_Deposit_list = ["{0}, {1}, {2}".format(x[0], x[1],x[2]) for x in SD1]

    def SD1_selected_Live_Deposit(self,value):
        x=value.split(',')
        global SD1_Deposit_Date
        SD1_Deposit_Date = x[2]

        # Checks on the values being passed
    # Payment method
    def SD1_dep_sal_option_choice(self,value):
        print("\nPayment method: {0}".format(value))
    
    # Debit type
    def SD1_Debit_type(self,value):
        print("\nDeposit type: {0}".format(value))

    # Card Expiry Date
    # click ok
    def SD1_card_Exp_on_save(self,instance,value,date_range):
        global SD1_Expiry_Date
        SD1_Expiry_Date = value
        self.ids.SD1_Card_Expiry_id.text = "Card Expiry Date:\n[color=#76FF03][b]{0}[/b][/color]".format(SD1_Expiry_Date)
        
    # click cancel
    def SD1_card_Exp_on_cancel(self,instance,value):
        print("You cancelled card expiry date")
    
    # try also passing a value for variable to the on_save below
    def SD1_card_Exp_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.SD1_card_Exp_on_save, on_cancel=self.SD1_card_Exp_on_cancel)
        date_dialog.open()

    # Card Start Date
    # click ok
    def SD1_card_start_on_save(self,instance,value,date_range):
        global SD1_Card_Start_Date
        SD1_Card_Start_Date = value
        self.ids.SD1_Card_Start_id.text = "Card Start Date:\n[color=#76FF03][b]{0}[/b][/color]".format(SD1_Card_Start_Date)
        

    # click cancel
    def SD1_card_start_on_cancel(self,instance,value):
        print("You cancelled card start date")
    
    # try also passing a value for variable to the on_save below
    def SD1_card_start_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.SD1_card_start_on_save, on_cancel=self.SD1_card_start_on_cancel)
        date_dialog.open()

    # Deposit/transaction  Date
    # click ok
    def SD1_transaction_on_save(self,instance,value,date_range):
        global SD1_Trans_Date
        SD1_Trans_Date = value
        self.ids.SD1_transaction_Date_id.text = "Deposit Date:\n[color=#76FF03][b]{0}[/b][/color]".format(SD1_Trans_Date)

    # click cancel
    def SD1_transaction_on_cancel(self,instance,value):
        print("You cancelled card expiry date")
    
    # try also passing a value for variable to the on_save below
    def SD1_transaction_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.SD1_transaction_on_save, on_cancel=self.SD1_transaction_on_cancel)
        date_dialog.open()


    # Get time
    def SD1_get_time(self,instance,time):
        global SD1_Trans_time
        SD1_Trans_time = time
        self.ids.SD1_transaction_time_id.text = "Deposit Time:\n[color=#76FF03][b]{0}[/b][/color]".format(SD1_Trans_time)
    # Cancel
    def SD1_on_time_cancel(self,instance,time):
        print("You canceled the time picker")

    def show_SD1_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.SD1_on_time_cancel,time = self.SD1_get_time)
        time_dialog.open()

    # submit to database
    def SD1_submit(self):
        # pass the input values into variables
        SD1_Payment_method = self.ids.SD1_payment_method_spin_id.text
        SD1_Transfer_Reference = self.ids.SD1_transfer_ref_textf.text
        SD1_Card_nbr = self.ids.SD1_card_nbr_textf.text
        SD1_Debit_Type = self.ids.SD1_Debit_type_spin_id.text
        SD1_Auth_code = self.ids.SD1_auth_textf.text
        SD1_Amount = self.ids.SD1_Amount_textf.text
        SD1_Receipt_Nbr = self.ids.SD1_Receipt_nbr_textf.text

        print("\nSale in one after Deposit submision:\n")
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
        print("\nDeposit Date:\t{0}".format(SD1_Deposit_Date))

        print("Payment method:\t{0}".format(SD1_Payment_method))
        print("Transfer reference:\t{0}".format(SD1_Transfer_Reference))
        print("Card number:\t{0}".format(SD1_Card_nbr))
        print("Debit type:\t{0}".format(SD1_Debit_Type))
        print("Card expiry date:\t{0}".format(SD1_Expiry_Date))
        print("Card start date:\t{0}".format(SD1_Card_Start_Date))
        print("Transaction date:\t{0}".format(SD1_Trans_Date))
        print("Tansaction time:\t{0}".format(SD1_Trans_time))
        print("Auth code:\t{0}".format(SD1_Auth_code))
        print("Deposit Amount:\t{0}".format(SD1_Amount))
        print("Receipt number:\t{0}".format(SD1_Receipt_Nbr))