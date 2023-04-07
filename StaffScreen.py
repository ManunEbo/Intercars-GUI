from kivy.uix.screenmanager import Screen
from kivymd.uix.picker import MDDatePicker

class StaffScreen(Screen):

    # Viewing date   
    def Staff_DOB_on_save(self,instance,value,date_range):
        global DOB
        DOB = value
        self.ids.Staff_DOB_lbl.text = "DOB:\n[color=#76FF03][b]{0}[/b][/color]".format(DOB)

    # click cancel
    def Staff_DOB_on_cancel(self,instance,value):
        pass
    
    def Staff_DOB_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Staff_DOB_on_save, on_cancel=self.Staff_DOB_on_cancel)
        date_dialog.open()
    
    def Submit_Staff(self):
        print("\n\n\nStaff upload")
        print("First name:\t{0}".format(self.ids.Fname_textf.text))
        print("Middle name:\t{0}".format(self.ids.Mname_textf.text))
        print("Last name:\t{0}".format(self.ids.Lname_textf.text))
        print("House number:\t{0}".format(self.ids.Addr1_textf.text))
        print("Street:\t{0}".format(self.ids.Addr2_textf.text))
        print("City or village:\t{0}".format(self.ids.Addr3_textf.text))
        print("County or shire:\t{0}".format(self.ids.Addr4_textf.text))
        print("Country:\t{0}".format(self.ids.Addr5_textf.text))
        print("Post code:\t{0}".format(self.ids.Addr6_textf.text))
        print("email:\t{0}".format(self.ids.email_textf.text))
        print("Telephone number:\t{0}".format(self.ids.Tel_textf.text))
        print("DOB:\t{0}".format(DOB))

        self.manager.current = "menuscreen"