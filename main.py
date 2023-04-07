# Disabling the red dots when I click on a screen
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')

from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
#from kivymd.uix.picker import MDDatePicker
#from kivymd.uix.picker import MDTimePicker
from kivy.properties import ListProperty
from kivy.lang import builder
from kivymd.uix.picker import MDDatePicker, MDTimePicker

# Importing the the modules storing classes

import CustomerScreen
import Cust_AddressScreen

import Deposit_in_two_Screen
import Deposit_in_one_Screen
import Deposit_in_three_Screen
import Sale_in_one_Screen
import Sale_in_two_Screen
import Sale_in_three_Screen

import Sale_with_Deposit_in_one_Screen
import Sale_with_Deposit_in_two_Screen
import Sale_with_Deposit_in_three_Screen
import VehicleScreen

import V5CScreen
import MOTHistoryScreen
import MOTRefusalScreen
import ServiceHistoryScreen
import MileageHistoryScreen

import CallLogScreen
import VehicleViewingScreen
import StaffScreen

import AuctionScreen
import VendorScreen
import FundScreen
import Auction_invoice
import ElectricalScreen
import MechanicScreen
import MOT_GarageScreen
import CarwashScreen

import Send_to_ServiceScreen
import Return_from_ServiceScreen
import Invoice_for_ServiceScreen
import Op_Service_ReceiptScreen
import Op_Bank_TransferScreen
import Op_Miscellaneous_ReceiptScreen

class WelcomeScreen(Screen):
    def logger(self):
        if self.ids.user.text == "elvy" and self.ids.password.text == "hello":
            self.manager.current = 'menuscreen'
            return
        else:
            self.ids.welcome_label.text = "Invalid username or password"
    
    def clear(self):
        self.ids.welcome_label.text = "Welcome"
        self.ids.user.text = ""
        self.ids.password.text = ""

class MenuScreen(Screen):
    pass

class AuctionMenuScreen(Screen):
    pass

class GarageScreen(Screen):
    pass

class OperationScreen(Screen):
    pass

class Op_serviceScreen(Screen):
    pass

class Op_serviceScreen(Screen):
    pass

class MainApp(MDApp):

    def on_start(self):        
        self.theme_cls.primary_palette = 'LightGreen'
        self.theme_cls.primary_hue = "700"
        self.theme_cls.theme_style = "Dark"
        self.title = "Intercars DB"
        screen_manager = self.root.ids.screen_manager
        screen_manager.current = 'welcomescreen'

    def change_screen(self, screen_name):
        # Get the screen manager from the kv file.
        screen_manager = self.root.ids.screen_manager
        screen_manager.current = screen_name

       
  
MainApp().run() 