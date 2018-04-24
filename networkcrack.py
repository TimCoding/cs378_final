import subprocess

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
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

	def refresh_networks(self):
		#self.cracked_password = "Password:"
		#self.network_list.adapter.data.clear()
		# subprocesses = subprocess.check_output(["netsh", "wlan", "show", "network"])
		# subprocesses = subprocesses.decode("ascii")
		# subprocesses = subprocesses.replace("\r", "")
		# ls = subprocesses.split("\n")
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

class NetworkCrackApp(App):
	def build(self):
		return NetworkCrack()

crackApp = NetworkCrackApp()
crackApp.run()
