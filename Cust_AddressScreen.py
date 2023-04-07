from kivy.uix.screenmanager import Screen,ScreenManager

class Cust_AddressScreen(Screen):
    def customer_address(self):
        global Address1, Address2, Address3, Address4, Address5, Address6, email, Tel
        Address1 = self.ids.house_num_textf.text
        Address2 = self.ids.street_textf.text
        Address3 = self.ids.city_town_textf.text
        Address4 = self.ids.county_textf.text
        Address5 = self.ids.country_textf.text
        Address6 = self.ids.postcode_textf.text
        email = self.ids.email_textf.text
        Tel = self.ids.tel_textf.text

        self.manager.current ="deposit_or_sale"