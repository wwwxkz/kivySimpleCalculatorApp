from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Window(BoxLayout):
	pass 

class Calculator(App):
	def build(self):
		return Window()

Calculator().run()
