from logging import root
from kivy.uix.screenmanager import Screen
from kivymd.uix.picker import MDDatePicker,MDTimePicker

class Op_Miscellaneous_ReceiptScreen(Screen):

    # Transaction date 
    def Misc_Receipt_date_on_save(self,instance,value,date_range):
        global Receipt_date
        Receipt_date = value
        self.ids.Misc_Receipt_date_lbl.text = "Receipt date:\n[color=#76FF03][b]{0}[/b][/color]".format(Receipt_date)

    # click cancel
    def Misc_Receipt_date_on_cancel(self,instance,value):
        pass
    
    def Misc_Receipt_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Misc_Receipt_date_on_save, on_cancel=self.Misc_Receipt_date_on_cancel)
        date_dialog.open()

    # Get time
    def Receipt_get_time(self,instance,time):
        global Receipt_time
        Receipt_time = time
        self.ids.Misc_receipt_time_id.text = "Receipt time:\n[color=#76FF03][b]{0}[/b][/color]".format(Receipt_time)
    # Cancel
    def Receipt_on_time_cancel(self,instance,time):
        pass

    def show_Misc_receipt_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.Receipt_on_time_cancel,time = self.Receipt_get_time)
        time_dialog.open()

    # Creating the VAT flag
    def VAT_Receip(self,value):
        global VAT_Flag
        VAT_Flag = value

    # Update icp.Op_Service
    def Submit_Miscellaneous_Receipt(self):
        print("\n\n\nMiscellaneous Receipt Upload")
        print("Venue:\t{0}".format(self.ids.Venue_textf.text))
        print("VAT registration nbr:\t{0}".format(self.ids.Vat_registration_textf.text))
        print("Item:\t{0}".format(self.ids.Item_textf.text))
        print("Price:\t{0}".format(self.ids.Price_textf.text))
        print("Quantity:\t{0}".format(self.ids.Quantity_textf.text))
        print("Total:\t{0}".format(self.ids.Total_textf.text))
        print("Authorization code:\t{0}".format(self.ids.Auth_code_textf.text))
        print("Receipt number:\t{0}".format(self.ids.Receipt_nbr_textf.text))
        print("Receipt date:\t{0}".format(Receipt_date))
        print("Transaction time:\t{0}".format(Receipt_time))
        print("\nVAT flag:\t{0}".format(VAT_Flag))
        if VAT_Flag == "Y":
            Gross_price = float(self.ids.Price_textf.text)*float(self.ids.Quantity_textf.text)
            Net = Gross_price/1.2
            VAT = Gross_price - Net
            print("\nGross price:\t{0}".format(Gross_price))
            print("Net:\t{0}".format(Net))
            print("VAT rate:\t0.2")
            print("VAT:\t{0}".format(VAT))

        self.manager.current = "operation_screen"