from kivy.uix.screenmanager import Screen,ScreenManager
# from kivymd.uix.picker import MDDatePicker
# from kivymd.uix.picker import MDTimePicker
from kivymd.uix.picker import MDDatePicker, MDTimePicker


class CustomerScreen(Screen):
    def agegroup_clicked(self, value):
        global FirstName, MiddleName, LastName, AgeGroup   
        FirstName = self.ids.firstname_textf.text
        MiddleName = None
        if self.ids.middlename_textf.text is None:
            MiddleName = None
        else:
            MiddleName = self.ids.middlename_textf.text

        LastName = self.ids.lastname_textf.text
        AgeGroup = value
    
    # DOB
    global Customer_DOB
    Customer_DOB = "1980/01/01"
    def Customer_DOB_on_save(self,instance,value,date_range):        
        Customer_DOB = value
        self.ids.DOB_label.text = "DOB:\n[color=#76FF03][b]{0}[/b][/color]".format(Customer_DOB)
    

        
    # click cancel
    def Customer_DOB_on_cancel(self,instance,value):
        print("You cancelled Customer DOB")
    
    # try also passing a value for variable to the on_save below
    def Customer_DOB_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Customer_DOB_on_save, on_cancel=self.Customer_DOB_on_cancel)
        date_dialog.open()