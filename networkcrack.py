import subprocess
import threading
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from utils import *


class NetworkListButton(ListItemButton):
    pass

class NetworkCrack(BoxLayout):
    network_list = ObjectProperty()
    network_bssid = []
    word_list_strength = ObjectProperty()
    cracked_password = StringProperty()
    value = NumericProperty()

    def __init__(self, **kwa):
        super(NetworkCrack, self).__init__(**kwa)
        value = 0

    def get_networks(self):
        #Fixed
        getNetworks()

    def get_handshake(self):
        num = parse_num_ssid(self.network_list.adapter.selection[0].text) + 1
        bssid = self.network_bssid[num - 1]
        ranIndex = random.randint(1, len(network_bssid))
        while ranIndex == num:
            ranIndex = random.randint(1, len(network_bssid))
        getHandshake(bssid, network_bssid[ranIndex])

    def refresh_networks(self):
        self.network_list.adapter.data.clear()
        ls = []
        bssid = []
        networks = read_bssid()
        for network in networks:
            ls.append(network[0]) ##Grabbing name
            bssid.append(network[1]) ##Grabbing BSSID
        self.network_list.adapter.data.extend(ls)
        self.network_bssid = bssid
        #self.network_list.adapter.data.remove('')
        self.network_list._trigger_reset_populate()

    def next(self, dt):
        if self.value>=100:
            self.value = 0
            return False
        self.value += 1

    def next_nmap(self, dt):
        if self.value>=100:
            self.value = 0
            return False
        self.value += 1

    def puopen(self):
        Clock.schedule_interval(self.next, 1/5)

    def nmap_timer(self):
        Clock.schedule_interval(self.next_nmap, 1/2)

    def set_strength_low(self):
        if self.word_list_strength == 1:
            self.word_list_strength = 0
        else:
            self.word_list_strength = 1

    def set_strength_medium(self):
        if self.word_list_strength == 2:
            self.word_list_strength = 0
        else:
            self.word_list_strength = 2

    def set_strength_high(self):
        if self.word_list_strength == 3:
            self.word_list_strength = 0
        else:
            self.word_list_strength = 3

    def crack_network(self):
        if self.word_list_strength == 0 or not self.network_list.adapter.selection:
            popup = Popup(title='Error', content=Label(text='Please select a network and word list strength.'), size_hint=(None, None), size=(400, 400))
            popup.open()
        if self.network_list.adapter.selection:
            num = parse_num_ssid(self.network_list.adapter.selection[0].text) + 1
            #self.cracked_password = "praetorian"
            #Add different wordlists here
            bssid = self.network_bssid[num - 1]
            self.cracked_password = runPasswordCracker(bssid)
            selection = self.network_list.adapter.selection[0].text
        pass

    def connect_to_network(self):
        if self.cracked_password == "":
            popup = Popup(title='Error', content=Label(text='No password has been cracked.'), size_hint=(None, None), size=(400, 400))
            popup.open()

    def scan_network(self):
        if self.cracked_password == "":
            popup = Popup(title='Error', content=Label(text='No password has been cracked.'), size_hint=(None, None), size=(400, 400))
            popup.open()
        threading.Thread(target = self.nmap_timer).start()
        #threading.Thread(target = runNMAP).start()
        threading.Thread(target = runNMAP).start()

class NetworkCrackApp(App):
    def build(self):
        return NetworkCrack()

crackApp = NetworkCrackApp()
crackApp.run()
