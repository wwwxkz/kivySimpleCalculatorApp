#ARQUIVO PARA INTERFACE SEPARADO NOMEDACLASSPRINCIPAL.KV ########################################
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Janela(BoxLayout):
	pass 

class Djaime(App):
	def build(self):
		return Janela()

Djaime().run()
