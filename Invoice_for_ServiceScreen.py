from kivy.uix.screenmanager import Screen
from kivymd.uix.picker import MDDatePicker

class Invoice_for_ServiceScreen(Screen):

    # Pull the current inhouse vehicles for service
    custom_list = [("1","Tesla","Model S","Elvy"),
     ("2","BMW","3 Series","RG1 5XP"),
     ("3","Toyota","Yaris","TG3 9PP"),
     ("4","Alfa Romeo","Guilia","SX1 5AA")]

    Vehicle_invoice_list = ["{0}, {1}, {2},{3}".format(x[0], x[1],x[2],x[3]) for x in custom_list]

    # Extract the V5C_id this will be used to narrow down the service you sent the vehicle on
    def selected_vehicle_invoice(self,value):
        x=value.split(',')
        global V5C_id,Vehicle_of_interest,Reg_numb
        V5C_id =x[0]
        Vehicle_of_interest ="{0} {1}".format(x[1],x[2])
        Reg_numb = x[3]


    def Service_type_invoice(self,value):
        global Serv_type
        Serv_type = value

        if Serv_type == "":
            serv_type_list = [("Select Service","Service date")]
            Serv_type_send_list = ["{0}, {1}".format(x[0], x[1]) for x in serv_type_list]
            self.ids.Entity_serv_date_select_spin_id.values = Serv_type_send_list

        # Conditionaly narrow down the service, see example code below:
        # select b.Entity_name, a.Serv_date from icp.Op_serv a
        # left join
        # icp.Entity b
        # on a.Carwash_id = b.Carwash_id
        # where V5C_id=@V5C_id and Serv_type= @Serv_type
        elif Serv_type == "Carwash":
            serv_type_list = [("The Carwash place","2021/09/10")]
            Serv_type_return_list = ["{0}, {1}".format(x[0], x[1]) for x in serv_type_list]
            self.ids.Entity_serv_date_select_spin_id.values =  Serv_type_return_list

        elif Serv_type == "Electrical":

            serv_type_list = [("Super Mario Electrical","2021/08/09")]
            Serv_type_return_list = ["{0}, {1}".format(x[0], x[1]) for x in serv_type_list]
            self.ids.Entity_serv_date_select_spin_id.values =  Serv_type_return_list

        elif Serv_type == "Mechanic":
            serv_type_list = [("Belugia motors","2021/08/17")]
            Serv_type_return_list = ["{0}, {1}".format(x[0], x[1]) for x in serv_type_list]
            self.ids.Entity_serv_date_select_spin_id.values =  Serv_type_return_list

        elif Serv_type == "MOT":
            serv_type_list = [("Ndoki MOT","2021/07/29")]
            Serv_type_return_list = ["{0}, {1}".format(x[0], x[1]) for x in serv_type_list]
            self.ids.Entity_serv_date_select_spin_id.values =  Serv_type_return_list

        else:
            print("WTF1?")

    def selected_serv_type_invoice(self,value):
        x=value.split(',')
        global Entity_Name, Serv_date

        if Serv_type == "Carwash":
            Serv_date =x[1]
            Entity_Name ="{0}".format(x[0])
        
        elif Serv_type == "Electrical":
            Serv_date =x[1]
            Entity_Name ="{0}".format(x[0])
        
        elif Serv_type == "Mechanic":
            Serv_date =x[1]
            Entity_Name ="{0}".format(x[0])
        
        elif Serv_type == "MOT":
            Serv_date =x[1]
            Entity_Name ="{0}".format(x[0])
        
        else:
            print("Say what???")

    # Invoice date 
    def Invoice_date_on_save(self,instance,value,date_range):
        global Invoice_date
        Invoice_date = value
        self.ids.Invoice_date_lbl.text = "Return date:\n[color=#76FF03][b]{0}[/b][/color]".format(Invoice_date)

    # click cancel
    def Invoice_date_on_cancel(self,instance,value):
        pass
    
    def Invoice_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Invoice_date_on_save, on_cancel=self.Invoice_date_on_cancel)
        date_dialog.open()
   
    # Update icp.Op_Service
    def Submit_invoice_for_service(self):
        print("\n\n\nInvoice for Service upload")
        print("V5C_id:\t{0}".format(V5C_id))
        print("Vehicle of interest:\t{0}".format(Vehicle_of_interest))
        print("Registration number:\t{0}".format(Reg_numb))
        print("Service type:\t{0}".format(Serv_type))
        print("Service date:\t{0}".format(Serv_date))
        print("Entity name:\t{0}".format(Entity_Name))
        print("Invoice date:\t{0}".format(Invoice_date))
        print("Invoice number:\t{0}".format(self.ids.Invoice_nbr_textf.text))
        print("Price:\t{0}".format(self.ids.Price_textf.text))

        self.manager.current = "op_service_screen"