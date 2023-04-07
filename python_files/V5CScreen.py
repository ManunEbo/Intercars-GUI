import os
from kivy.uix.screenmanager import Screen
from kivymd.uix.picker import MDDatePicker
import mysql.connector

from dotenv import load_dotenv
load_dotenv()


mydb = mysql.connector.connect(
host=os.getenv('host'),
user=os.getenv('username'),
password=os.getenv('password'),
database=os.getenv('database',
auth_plugin=os.getenv('auth_plugin'
)


class V5CScreen(Screen):
    
    # First registration date
    # click ok
    def First_Reg_on_save(self,instance,value,date_range):
        global First_Reg
        First_Reg = value
        self.ids.First_reg_lbl.text = "First registration:\n[color=#76FF03][b]{0}[/b][/color]".format(First_Reg)
        
    # click cancel
    def First_Reg_on_cancel(self,instance,value):
        pass
    
    # try also passing a value for variable to the on_save below
    def First_Reg_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.First_Reg_on_save, on_cancel=self.First_Reg_on_cancel)
        date_dialog.open()
    
    # First registration UK date
    # click ok
    def First_Reg_uk_on_save(self,instance,value,date_range):
        global First_Reg_uk
        First_Reg_uk = value
        self.ids.First_reg_uk_lbl.text = "First registration UK:\n[color=#76FF03][b]{0}[/b][/color]".format(First_Reg_uk)

    # click cancel
    def First_Reg_uk_on_cancel(self,instance,value):
        pass
    
    def First_Reg_uk_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.First_Reg_uk_on_save, on_cancel=self.First_Reg_uk_on_cancel)
        date_dialog.open()

    # Logbook issue date

    def Logbook_issued_date_on_save(self,instance,value,date_range):
        global Logbook_issued_date
        Logbook_issued_date = value
        self.ids.Logbook_Issued_date_lbl.text = "Logbook issued date:\n[color=#76FF03][b]{0}[/b][/color]".format(Logbook_issued_date)

    # click cancel
    def Logbook_issued_date_on_cancel(self,instance,value):
        pass
    
    def Logbook_issued_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Logbook_issued_date_on_save, on_cancel=self.Logbook_issued_date_on_cancel)
        date_dialog.open()

    # Owner 1 Acquisition date
    
    def Owner1_Acq_date_on_save(self,instance,value,date_range):
        global Owner1_Acq_date
        Owner1_Acq_date = value
        self.ids.Owner1_Acq_date_lbl.text = "Owner1 Acq date:\n[color=#76FF03][b]{0}[/b][/color]".format(Owner1_Acq_date)

    # click cancel
    def Owner1_Acq_date_on_cancel(self,instance,value):
        pass
    
    def Owner1_Acq_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Owner1_Acq_date_on_save, on_cancel=self.Owner1_Acq_date_on_cancel)
        date_dialog.open()

    # Owner 2 Acquisition date
    global Owner2_Acq_date
    Owner2_Acq_date = None
    def Owner2_Acq_date_on_save(self,instance,value,date_range):        
        Owner2_Acq_date = value            
        self.ids.Owner2_Acq_date_lbl.text = "Owner2 Acq date:\n[color=#76FF03][b]{0}[/b][/color]".format(Owner2_Acq_date)

    # click cancel
    def Owner2_Acq_date_on_cancel(self,instance,value):
        pass
    
    def Owner2_Acq_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Owner2_Acq_date_on_save, on_cancel=self.Owner2_Acq_date_on_cancel)
        date_dialog.open()

    # Owner 3 Acquisition date
    global Owner3_Acq_date
    Owner3_Acq_date = None
    def Owner3_Acq_date_on_save(self,instance,value,date_range):
        Owner3_Acq_date = value
        self.ids.Owner3_Acq_date_lbl.text = "Owner3 Acq date:\n[color=#76FF03][b]{0}[/b][/color]".format(Owner3_Acq_date)

    # click cancel
    def Owner3_Acq_date_on_cancel(self,instance,value):
        pass
    
    def Owner3_Acq_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Owner3_Acq_date_on_save, on_cancel=self.Owner3_Acq_date_on_cancel)
        date_dialog.open()

    # Owner 4 Acquisition date
    global Owner4_Acq_date
    Owner4_Acq_date = None
    def Owner4_Acq_date_on_save(self,instance,value,date_range):
        Owner4_Acq_date = value
        self.ids.Owner4_Acq_date_lbl.text = "Owner4 Acq date:\n[color=#76FF03][b]{0}[/b][/color]".format(Owner4_Acq_date)

    # click cancel
    def Owner4_Acq_date_on_cancel(self,instance,value):
        pass
    
    def Owner4_Acq_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Owner4_Acq_date_on_save, on_cancel=self.Owner4_Acq_date_on_cancel)
        date_dialog.open()

    # Print the V5C
    def Submit_V5C(self):

        Regnum = self.ids.Regnum_textf.text
        
        if self.ids.Prev_regnum_textf.text is None:
            Prev_regnum = ""
        else:
            Prev_regnum = self.ids.Prev_regnum_textf.text

        Document_Reference = self.ids.Document_Reference_textf.text
        First_registration_date = First_Reg
        First_registration_date_uk = First_Reg_uk
        Make = self.ids.Make_textf.text
        Model = self.ids.Model_textf.text
        Bodytype = self.ids.Bodytype_textf.text
        TaxClass = self.ids.TaxClass_textf.text
        FuelType = self.ids.FuelType_textf.text
        number_Seats = self.ids.number_Seats_textf.text
        Vehicle_Category = self.ids.Vehicle_Category_textf.text
        Colour = self.ids.Colour_textf.text
        Logbook_Issued_date1 = Logbook_issued_date
        Cylinder_capacity = self.ids.Cylinder_capacity_textf.text

        nbr_Prev_Owners = self.ids.nbr_Prev_Owners_textf.text

        Prev_owner1_Name = self.ids.Owner1_Name_textf.text
        Prev_Owner1_Address = self.ids.Owner1_Address_textf.text
        prev_Owner1_Acq_date1 = Owner1_Acq_date

        if self.ids.Owner2_Name_textf.text is None:
            Prev_owner2_Name = ""
        else:
            Prev_owner2_Name = self.ids.Owner2_Name_textf.text

        if self.ids.Owner2_Address_textf.text is None:
            Prev_Owner2_Address = ""
        else:
            Prev_Owner2_Address = self.ids.Owner2_Address_textf.text

        if Owner2_Acq_date is None:
            prev_Owner2_Acq_date = "null"
        else:
            prev_Owner2_Acq_date = Owner2_Acq_date

        if self.ids.Owner3_Name_textf.text is None:
            Prev_owner3_Name = ""
        else:
            Prev_owner3_Name = self.ids.Owner3_Name_textf.text
        
        if self.ids.Owner3_Address_textf.text is None:
            Prev_Owner3_Address = ""
        else:
            Prev_Owner3_Address = self.ids.Owner3_Address_textf.text
        
        if Owner3_Acq_date is None:
            prev_Owner3_Acq_date = "null"
        else:
            prev_Owner3_Acq_date = Owner3_Acq_date

        if self.ids.Owner4_Name_textf.text is None:
            Prev_owner4_Name =""
        else:
            Prev_owner4_Name = self.ids.Owner4_Name_textf.text
        
        if self.ids.Owner4_Address_textf.text is None:
            Prev_Owner4_Address = ""
        else:
            Prev_Owner4_Address = self.ids.Owner4_Address_textf.text
        
        if Owner4_Acq_date is None:
            prev_Owner4_Acq_date = "null"
        else:
            prev_Owner4_Acq_date = Owner4_Acq_date        


        sql_string1 = "set @Regnum = '{0}';".format(Regnum)
        sql_string2 = "set @Prev_regnum = '{0}';".format(Prev_regnum)
        sql_string3 = "set @Document_Reference = {0};".format(Document_Reference)
        sql_string4 = "set @First_reg = '{0}';".format(First_registration_date)
        sql_string5 = "set @first_reg_uk = '{0}';".format(First_registration_date_uk)
        sql_string6 = "set @Make = '{0}';".format(Make)
        sql_string7 = "set @Model = '{0}';".format(Model)
        sql_string8 = "set @Bodytype ='{0}';".format(Bodytype)
        sql_string9 = "set @TaxClass = '{0}';".format(TaxClass)
        sql_string10 = "set @FuelType = '{0}';".format(FuelType)
        sql_string11 = "set @number_Seats = {0};".format(number_Seats)
        sql_string12 = "set @Vehicle_Category = '{0}';".format(Vehicle_Category)
        sql_string13 = "set @Colour = '{0}';".format(Colour)
        sql_string14 = "set @Logbook_Issued_date = '{0}';".format(Logbook_Issued_date1)
        sql_string15 = "set @Cylinder_capacity = '{0}';".format(Cylinder_capacity)
        sql_string16 = "set @nbr_Prev_Owners = {0};".format(nbr_Prev_Owners)
        sql_string17 = "set @Prev_owner1_Name = '{0}';".format(Prev_owner1_Name)
        sql_string18 = "set @Prev_Owner1_Address = '{0}';".format(Prev_Owner1_Address)
        sql_string19 = "set @prev_Owner1_Acq_date = '{0}';".format(prev_Owner1_Acq_date1)
        sql_string20 = "set @Prev_owner2_Name = '{0}';".format(Prev_owner2_Name)
        sql_string21 = "set @Prev_Owner2_Address = '{0}';".format(Prev_Owner2_Address)
        sql_string22 = "set @prev_Owner2_Acq_date = '{0}';".format(prev_Owner2_Acq_date)
        sql_string23 = "set @Prev_owner3_Name = '{0}';".format(Prev_owner3_Name)
        sql_string24 = "set @Prev_Owner3_Address = '{0}';".format(Prev_Owner3_Address)
        sql_string25 = "set @prev_Owner3_Acq_date = '{0}';".format(prev_Owner3_Acq_date)
        sql_string26 = "set @Prev_owner4_Name = '{0}';".format(Prev_owner4_Name)
        sql_string27 = "set @Prev_Owner4_Address = '{0}';".format(Prev_Owner4_Address)
        sql_string28 = "set @prev_Owner4_Acq_date = '{0}';".format(prev_Owner4_Acq_date)
        sql_string29 = "call icp_V5C_Call();"

        mycursor = mydb.cursor()
        mycursor.execute(sql_string1)
        mycursor.execute(sql_string2)
        mycursor.execute(sql_string3)
        mycursor.execute(sql_string4)
        mycursor.execute(sql_string5)
        mycursor.execute(sql_string6)
        mycursor.execute(sql_string7)
        mycursor.execute(sql_string8)
        mycursor.execute(sql_string9)
        mycursor.execute(sql_string10)
        mycursor.execute(sql_string11)
        mycursor.execute(sql_string12)
        mycursor.execute(sql_string13)
        mycursor.execute(sql_string14)
        mycursor.execute(sql_string15)
        mycursor.execute(sql_string16)
        mycursor.execute(sql_string17)
        mycursor.execute(sql_string18)
        mycursor.execute(sql_string19)
        mycursor.execute(sql_string20)
        mycursor.execute(sql_string21)
        mycursor.execute(sql_string22)
        mycursor.execute(sql_string23)
        mycursor.execute(sql_string24)
        mycursor.execute(sql_string25)
        mycursor.execute(sql_string26)
        mycursor.execute(sql_string27)
        mycursor.execute(sql_string28)
        mycursor.execute(sql_string29)

        mydb.commit()


        self.manager.current = "vehiclescreen"