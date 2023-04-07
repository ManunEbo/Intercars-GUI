from kivy.uix.screenmanager import Screen


class ElectricalScreen(Screen):
    
    def Submit_Electrical(self):
        print("\n\n\nElectrical garage upload")
        print("Garage name:\t{0}".format(self.ids.Entity_Name_textf.text))
        print("VAT registration:\t{0}".format(self.ids.VAT_Reg_Number_textf.text))
        print("Firstname:\t{0}".format(self.ids.Fname_textf.text))
        print("Middlename:\t{0}".format(self.ids.Mname_textf.text))
        print("Lastname:\t{0}".format(self.ids.Lname_textf.text))
        print("House number:\t{0}".format(self.ids.Addr1_textf.text))
        print("Street:\t{0}".format(self.ids.Addr2_textf.text))
        print("City or village:\t{0}".format(self.ids.Addr3_textf.text))
        print("County or shire:\t{0}".format(self.ids.Addr4_textf.text))
        print("Country:\t{0}".format(self.ids.Addr5_textf.text))
        print("Postcode:\t{0}".format(self.ids.Addr6_textf.text))
        print("email:\t{0}".format(self.ids.email_textf.text))
        print("Tel:\t{0}".format(self.ids.Tel_textf.text))

        self.manager.current = "garage_screen"