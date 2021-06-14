import kivy
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.graphics import Color
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader

class Mywid(GridLayout):
	def __init__(self,**kwargs):
		super(Mywid,self).__init__(**kwargs)
		self.name='untitled'
	def increase(self):
		s=SoundLoader.load('click.mp3')
		s.play()
		self.txt.font_size=self.txt.font_size+5
	def decrease(self):
		s=SoundLoader.load('click.mp3')
		s.play()
		self.txt.font_size=self.txt.font_size-5
		if int(self.txt.font_size)<=30:
			self.txt.font_size=30
			self.pop = Popup(title='Font size ',content=Label(text="Sorry can't go lower than this\nIts not good for your eyes"),size_hint=(0.5,0.5))
			self.pop.open()
	def clear(self):
		s=SoundLoader.load('click.mp3')
		s.play()
		self.pop = Popup(title='New file',content=Label(text='Editor was cleared'),size_hint=(0.5,0.5))
		self.pop.open()
		self.txt.text = ''
	def open(self):
		s=SoundLoader.load('click.mp3')
		s.play()
		try:
			f=open(self.name+'.html','r')
			text=f.read()
			self.txt.text=text
			f.close()
		except:
			self.pop = Popup(title='Open file',content=Label(text="No such file"),size_hint=(0.5,0.5))
			self.pop.open()
	def save(self):
	    s=SoundLoader.load('click.mp3')
	    s.play()
	    if self.txt.text !='':
	        try:
	            f=open(self.name+".html",'w')
	            f.write(self.txt.text)
	            f.close()
	            m=Label(text='File was saved')
	            self.pop = Popup(title='Save file',content=m,size_hint=(0.5,0.5))
	            self.pop.open()
	        except:
	            f= open(self.name+".html",'w+')
	            f.write(self.txt.text)
	            f.close()
	            m=Label(text='File was saved')
	            self.pop = Popup(title='Save file',content=m,size_hint=(0.5,0.5))
	            self.pop.open()
	    else:
	        m=Label(text="Can't save empty file")
	        self.pop = Popup(title='Save file',content=m,size_hint=(0.5,0.5))
	        self.pop.open()
class MyApp(App):
	def build(self):
		return Mywid()

if __name__ == "__main__":
	MyApp().run()