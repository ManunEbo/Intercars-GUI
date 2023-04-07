from kivy.uix.screenmanager import Screen
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDTimePicker
#from kivy.properties import ListProperty

class Send_to_ServiceScreen(Screen):
    
    #custom_list = ListProperty()

    l = [("1","Tesla","Model S","Elvy"),
     ("2","BMW","3 Series","RG1 5XP"),
     ("3","Toyota","Yaris","TG3 9PP"),
     ("4","Alfa Romeo","Guilia","SX1 5AA")]

    custom_list = l
    Vehicle_send_list = ["{0}, {1}, {2},{3}".format(x[0], x[1],x[2],x[3]) for x in custom_list]

    def selected_vehicle_send(self,value):
        x=value.split(',')
        global V5C_id,Vehicle_of_interest,Reg_numb
        V5C_id =x[0]
        Vehicle_of_interest ="{0} {1}".format(x[1],x[2])
        Reg_numb = x[3]

    # Service date   
    def serv_date_on_save(self,instance,value,date_range):
        global Serv_date
        Serv_date = value
        self.ids.serv_date_lbl.text = "Service date:\n[color=#76FF03][b]{0}[/b][/color]".format(Serv_date)

    # click cancel
    def serv_date_on_cancel(self,instance,value):
        pass
    
    def serv_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.serv_date_on_save, on_cancel=self.serv_date_on_cancel)
        date_dialog.open()


    def Service_type_send(self,value):
        global Serv_type
        Serv_type = value

        if Serv_type == "":
            l = [("0","Select Service")]
            serv_type_list = l
            Serv_type_send_list = ["{0}, {1}".format(x[0], x[1]) for x in serv_type_list]
            self.ids.Entity_list_select_spin_id.values = Serv_type_send_list

        elif Serv_type == "Carwash":
            l = [("1","The Carwash place"),
            ("2","Jet Carwash"),
            ("3","Total Carwash"),
            ("4","Slick Carwash")]

            serv_type_list = l
            Serv_type_send_list = ["{0}, {1}".format(x[0], x[1]) for x in serv_type_list]
            self.ids.Entity_list_select_spin_id.values =  Serv_type_send_list

        elif Serv_type == "Electrical":

            l = [("1","Super Mario Electrical"),
            ("2","Jetrical motors"),
            ("3","Electricians LEC"),
            ("4","Nzashi")]

            serv_type_list = l
            Serv_type_send_list = ["{0}, {1}".format(x[0], x[1]) for x in serv_type_list]
            self.ids.Entity_list_select_spin_id.values =  Serv_type_send_list

        elif Serv_type == "Mechanic":
            l = [("1","Coils motors"),
            ("2","Simon Says motors"),
            ("3","Belugia motors"),
            ("4","Ndoki mituka")]

            serv_type_list = l
            Serv_type_send_list = ["{0}, {1}".format(x[0], x[1]) for x in serv_type_list]
            self.ids.Entity_list_select_spin_id.values =  Serv_type_send_list

        elif Serv_type == "MOT":
            l = [("1","Coils MOT"),
            ("2","Simon Says MOT"),
            ("3","Belugia MOT"),
            ("4","Ndoki MOT")]

            serv_type_list = l
            Serv_type_send_list = ["{0}, {1}".format(x[0], x[1]) for x in serv_type_list]
            self.ids.Entity_list_select_spin_id.values =  Serv_type_send_list

        else:
            print("WTF1?")

    def selected_serv_type_send(self,value):
        x=value.split(',')
        global Entity_Name

        if Serv_type == "Carwash":
            global Carwash_id
            Carwash_id =x[0]
            Entity_Name ="{0}".format(x[1])
        
        elif Serv_type == "Electrical":
            global Elect_mech_id
            Elect_mech_id =x[0]
            Entity_Name ="{0}".format(x[1])
        
        elif Serv_type == "Mechanic":
            global Mech_Grg_id
            Mech_Grg_id =x[0]
            Entity_Name ="{0}".format(x[1]) 
        
        elif Serv_type == "MOT":
            global MOT_Grg_id
            MOT_Grg_id =x[0]
            Entity_Name ="{0}".format(x[1])
        
        else:
            print("Say what???")


    
    def Submit_send_to_service(self):
        print("\n\n\nSend to Service upload")
        print("Vehicle info:\t{0} {1} {2}".format(V5C_id,Vehicle_of_interest,Reg_numb))
        print("Service date:\t{0}".format(Serv_date))
        print("Service type:\t{0}".format(Serv_type))
        if Serv_type == "Carwash":
            print("Carwash_id:\t{0}".format(Carwash_id))
            print("Entity name:\t{0}".format(Entity_Name))
            

        elif Serv_type == "Electrical":
            print("Elect_mech_id:\t{0}".format(Elect_mech_id))
            print("Entity name:\t{0}".format(Entity_Name))

        elif Serv_type == "Mechanic":
            print("Mech_Grg_id:\t{0}".format(Mech_Grg_id))
            print("Entity name:\t{0}".format(Entity_Name))

        elif Serv_type == "MOT":
            print("MOT_Grg_id:\t{0}".format(MOT_Grg_id))
            print("Entity name:\t{0}".format(Entity_Name))
        else:
            print("WTF")
        
        print("Service description:\t{0}".format(self.ids.Serv_Description_textf.text))

        self.manager.current = "op_service_screen"