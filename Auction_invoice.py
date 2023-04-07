from kivy.uix.screenmanager import Screen
from kivymd.uix.picker import MDDatePicker
from kivy.properties import ListProperty



class Auction_invoice(Screen):
    custom_list = ListProperty()

    l = [(1,"Tesla","Model S","Elvy"),
     (2,"BMW","3 Series","RG1 5XP"),
     (3,"Toyota","Yaris","TG3 9PP"),
     (4,"Alfa Romeo","Guilia","SX1 5AA")]

    custom_list = l
    Auct_vehicle_list = ["{0}, {1}, {2},{3}".format(x[0], x[1],x[2],x[3]) for x in custom_list]

    def Auct_selected_vehicle(self,value):
        x=value.split(',')
        global V5C_id, Vehicle_reg
        V5C_id = x[0]
        Vehicle_reg =x[3]

    # creating a list of auction houses, retrieve this from the database
    Auction_house_list = ListProperty()

    list_auct_house = [(1,"Aston Barclays"),
     (2,"The Nottingham Auction"),
     (3,"BCA"),
     (4,"Manheim Auction")]

    Auction_house_list = list_auct_house
    Auct_Houses_list = ["{0}, {1}".format(x[0], x[1]) for x in Auction_house_list]

    def Auct_house_select(self,value):
        x=value.split(',')
        global Auction_id, Auction_name
        Auction_id = x[0]
        Auction_name =x[1]

    # creating a list of Vendors, retrieve this from the database
    Vend_list = ListProperty()

    vend_l = [(1,"Aston A1"),
     (2,"Nottingham A3113"),
     (3,"BCA i3"),
     (4,"Manheim Cds")]

    Vend_list = vend_l
    Vendor_list = ["{0}, {1}".format(x[0], x[1]) for x in Vend_list]

    def Vendor_select(self,value):
        x=value.split(',')
        global Vendor_id, Vendor_name
        Vendor_id = x[0]
        Vendor_name =x[1]

    # Invoice_Date
    def Invoice_Date_on_save(self,instance,value,date_range):
        global Invoice_Date
        Invoice_Date = value
        self.ids.Invoice_Date_id.text = "Invoice date:\n[color=#76FF03][b]{0}[/b][/color]".format(Invoice_Date)
        

    # click cancel
    def Invoice_Date_on_cancel(self,instance,value):
        pass
    
    # try also passing a value for variable to the on_save below
    def Invoice_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Invoice_Date_on_save, on_cancel=self.Invoice_Date_on_cancel)
        date_dialog.open()

    # Date first reg
    def Date_first_Reg_on_save(self,instance,value,date_range):
        global Date_first_Reg
        Date_first_Reg = value
        self.ids.Date_first_Reg_id.text = "Date first reg:\n[color=#76FF03][b]{0}[/b][/color]".format(Date_first_Reg)
        

    # click cancel
    def Date_first_Reg_on_cancel(self,instance,value):
        pass
    
    def Date_first_Reg_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Date_first_Reg_on_save, on_cancel=self.Date_first_Reg_on_cancel)
        date_dialog.open()

    # MOT indicator, has vehicle got an MOT?
    MOT_YN = ListProperty()

    yn = [(0,"No"),
     (1,"Yes")]

    MOT_YN = yn
    MOT_YesNo = ["{0}, {1}".format(x[0], x[1]) for x in MOT_YN]

    def MOT_YesNo_select(self,value):
        x=value.split(',')
        global MOT_Flag, MOT_Y_N
        MOT_Flag = x[0]
        MOT_Y_N =x[1]

    # MOT expiry date
    def MOT_Expiry_date_on_save(self,instance,value,date_range):
        global MOT_Expiry_date
        MOT_Expiry_date = value
        self.ids.MOT_Expiry_date_id.text = "MOT expiry date:\n[color=#76FF03][b]{0}[/b][/color]".format(MOT_Expiry_date)

    # click cancel
    def MOT_Expiry_date_on_cancel(self,instance,value):
        pass
    
    def MOT_Expiry_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.MOT_Expiry_date_on_save, on_cancel=self.MOT_Expiry_date_on_cancel)
        date_dialog.open()

    # MOT indicator, has vehicle got an MOT?
    Cash_YN = ListProperty()

    cash_yn = [(0,"No"),
     (1,"Yes")]

    Cash_YN = cash_yn
    Cash_YesNo = ["{0}, {1}".format(x[0], x[1]) for x in Cash_YN]

    def Cash_YesNo_select(self,value):
        x=value.split(',')
        global Cash_Flag, Cash_Y_N
        Cash_Flag = x[0]
        Cash_Y_N =x[1]
    
    def Submit_Auction_invoice(self):
        print("\n\n\nAuction invoice upload")
        print("\nV5C_id:\t{0}".format(V5C_id))
        print("Vehicle registration:\t{0}".format(Vehicle_reg))
        print("Auction_id:\t{0}".format(Auction_id))
        print("Auction name:\t{0}".format(Auction_name))
        print("Vendor_id:\t{0}".format(Vendor_id))
        print("Vendor name:\t{0}".format(Vendor_name))
        print("Invoice number:\t{0}".format(self.ids.Invoice_nbr_textf.text))
        print("Invoice date:\t{0}".format(Invoice_Date))
        print("Make:\t{0}".format(self.ids.Make_textf.text))
        print("Model:\t{0}".format(self.ids.Model_textf.text))
        print("Date first registration:\t{0}".format(Date_first_Reg))
        print("MOT flag:\t{0} {1}".format(MOT_Flag, MOT_Y_N))
        print("MOT expiry date:\t{0}".format(MOT_Expiry_date))
        print("Mileage:\t{0}".format(self.ids.Mileage_textf.text))
        print("Cash payment flag:\t{0} {1}".format(Cash_Flag,Cash_Y_N))
        print("Price:\t{0}".format(self.ids.Price_textf.text))
        print("Buyers fee:\t{0}".format(self.ids.Buyers_Fee_textf.text))
        print("Assurance fee:\t{0}".format(self.ids.Assurance_Fee_textf.text))
        print("Other fee:\t{0}".format(self.ids.Other_Fee_textf.text))
        print("Storage fee:\t{0}".format(self.ids.Storage_Fee_textf.text))
        print("Cash handling fee:\t{0}".format(self.ids.Cash_Handling_fee_textf.text))
        print("VAT rate:\t{0}".format(self.ids.VAT_rate_textf.text))
        print("Auction VAT:\t{0}".format(self.ids.Auction_VAT_textf.text))
        print("Total price:\t{0}".format(self.ids.Total_textf.text))

        self.manager.current = "auction_menu_screen"