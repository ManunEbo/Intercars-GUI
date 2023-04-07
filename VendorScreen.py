from kivy.uix.screenmanager import Screen

class VendorScreen(Screen):

    def Submit_Vendor(self):
        print("\n\n\nVendor upload")
        print("Entity name:\t{0}".format(self.ids.Entity_Name_textf.text))
        print("Vendor reference:\t{0}".format(self.ids.Vendor_reference_textf.text))
        print("VAT registration:\t{0}".format(self.ids.VAT_Reg_Number_textf.text))
        print("House number:\t{0}".format(self.ids.Addr1_textf.text))
        print("Street:\t{0}".format(self.ids.Addr2_textf.text))
        print("City or village:\t{0}".format(self.ids.Addr3_textf.text))
        print("County or shire:\t{0}".format(self.ids.Addr4_textf.text))
        print("Country:\t{0}".format(self.ids.Addr5_textf.text))
        print("Post code:\t{0}".format(self.ids.Addr6_textf.text))
        print("email:\t{0}".format(self.ids.email_textf.text))
        print("Telephone number:\t{0}".format(self.ids.Tel_textf.text))

        self.manager.current = "auction_menu_screen"