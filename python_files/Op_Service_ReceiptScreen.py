from logging import root
from kivy.uix.screenmanager import Screen
from kivymd.uix.picker import MDDatePicker,MDTimePicker

class Op_Service_ReceiptScreen(Screen):

    def Service_type_Receip(self,value):
        global Serv_type
        Serv_type = value

        if Serv_type == "":
            serv_type_list = [("Select Service","Service date")]
            Serv_type_Receipt_list = ["{0}, {1}".format(x[0], x[1]) for x in serv_type_list]
            self.ids.Service_invoice_select_spin_id.values = Serv_type_Receipt_list

        # Conditionaly narrow down the service, see example code below:
        # select b.Entity_name, a.Serv_date from icp.Op_serv a
        # left join
        # icp.Entity b
        # on a.Carwash_id = b.Carwash_id
        # where V5C_id=@V5C_id and Serv_type= @Serv_type
        elif Serv_type == "Carwash":
            serv_Invoice_list = [(1,"2021/08/15","A378463",10),
            (10,"2021/08/29","Z7686139",10),
            (45,"2021/09/10","B4633167",10),]
            Serv_type_Receipt_list = ["{0}, {1}, {2}, £{3}".format(x[0], x[1],x[2],x[3]) for x in serv_Invoice_list]
            self.ids.Service_invoice_select_spin_id.values =  Serv_type_Receipt_list

        elif Serv_type == "Electrical":

            serv_Invoice_list = [(7,"2021/08/03","K3331",75),
            (11,"2021/08/30","HZ9999111",100),
            (44,"2021/09/13","C44463444",60),]
            Serv_type_Receipt_list = ["{0}, {1}, {2}, £{3}".format(x[0], x[1],x[2],x[3]) for x in serv_Invoice_list]
            self.ids.Service_invoice_select_spin_id.values =  Serv_type_Receipt_list

        elif Serv_type == "Mechanic":

            serv_Invoice_list = [(37,"2021/08/5","AAA378463",150),
            (41,"2021/08/19","CZX686686",99),
            (53,"2021/09/17","BJK331334",130),]
            Serv_type_Receipt_list = ["{0}, {1}, {2}, £{3}".format(x[0], x[1],x[2],x[3]) for x in serv_Invoice_list]
            self.ids.Service_invoice_select_spin_id.values =  Serv_type_Receipt_list

        elif Serv_type == "MOT":

            serv_Invoice_list = [(6,"2021/08/09","CX3763888",32),
            (28,"2021/08/14","PRT38711999",32),
            (40,"2021/09/21","BKU6665333",32),]
            Serv_type_Receipt_list = ["{0}, {1}, {2}, £{3}".format(x[0], x[1],x[2],x[3]) for x in serv_Invoice_list]
            self.ids.Service_invoice_select_spin_id.values =  Serv_type_Receipt_list

        else:
            print("WTF1?")

    def Serv_Receipt_invoice(self,value):
        x=value.split(',')
        global Op_service_id, Serv_Invoice_Date, Serv_Invoice_nbr,Price
        Op_service_id = x[0]
        Serv_Invoice_Date = x[1]
        Serv_Invoice_nbr = x[2]
        Price = x[3]
    
        # Setting the values for splitpayment
        Split_payment1 = [(0,"N"),(1,"Y")]
        Split_payment_list = ["{0}, {1}".format(x[0], x[1]) for x in Split_payment1]
        self.ids.Split_payment_select_spin_id.values =  Split_payment_list

    # creating the splitpayment flag
    def Split_payment(self,value):
        x = value.split(',')
        global Split_payment
        Split_payment = x[1]

    # Transaction date 
    def Transaction_date_on_save(self,instance,value,date_range):
        global Trans_Date
        Trans_Date = value
        self.ids.Transaction_date_lbl.text = "Transaction date:\n[color=#76FF03][b]{0}[/b][/color]".format(Trans_Date)

    # click cancel
    def Transaction_date_on_cancel(self,instance,value):
        pass
    
    def Transaction_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.Transaction_date_on_save, on_cancel=self.Transaction_date_on_cancel)
        date_dialog.open()

    # Get time
    def trans_get_time(self,instance,time):
        global Trans_time
        Trans_time = time
        self.ids.Transaction_time_id.text = "Transaction time:\n[color=#76FF03][b]{0}[/b][/color]".format(Trans_time)
    # Cancel
    def trans_on_time_cancel(self,instance,time):
        print("You canceled the time picker")

    def show_Transaction_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.trans_on_time_cancel,time = self.trans_get_time)
        time_dialog.open()

    # Creating the VAT flag
    def VAT_Receip(self,value):
        global VAT_Flag
        VAT_Flag = value

    # Update icp.Op_Service
    def Submit_service_Receipt(self):
        print("\n\n\nService Receipt upload")
        print("Service type:\t{0}".format(Serv_type))
        print("Op_service_id:\t{0}".format(Op_service_id))
        print("Service invoice date:\t{0}".format(Serv_Invoice_Date))
        print("Service invoice number:\t{0}".format(Serv_Invoice_nbr))
        print("Service price:\t{0}".format(Price))
        print("Split payment:\t{0}".format(Split_payment))
        print("Transaction date:\t{0}".format(Trans_Date))
        print("Transaction time:\t{0}".format(Trans_time))
        print("Authorization code:\t{0}".format(self.ids.Auth_code_textf.text))
        print("Receipt number:\t{0}".format(self.ids.Receipt_nbr_textf.text))
        print("Amount:\t{0}".format(self.ids.Amount_textf.text))
        print("\nVAT flag:\t{0}".format(VAT_Flag))
        if VAT_Flag == "Y":
            print("\nGross price:\t{0}".format(self.ids.Amount_textf.text))
            print("Net:\t{0}".format(float(self.ids.Amount_textf.text)/1.2))
            print("VAT rate:\t0.2")
            print("VAT:\t{0}".format(float(float(self.ids.Amount_textf.text)-(float(self.ids.Amount_textf.text)/1.2))))

        self.manager.current = "operation_screen"