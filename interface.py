from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.config import ConfigParser
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.metrics import dp
from curs import *
from kivy.app import App
from kivy.lang import Builder
import os

Builder.load_string("""
#:kivy 1.10.0
#:import FallOutTransition kivy.uix.screenmanager.FallOutTransition

<ScreenManagement>:
    transition: FallOutTransition()
    MainScreen:
        id: main
        name: 'main'
    FileChoser:
        id: choser
        name: 'choser'
    FileChoser2:
        id: choser2
        name: 'choser2'                
                                   
<MainScreen>:
    BoxLayout:
        id:box                               
        orientation: 'vertical'                         
        TextInput: 
            id: txt1
            hint_text:'Enter text'
            pos:0,0 
            size_hint: 1., 0.3
        BoxLayout:  
            orientation: 'horizontal'
                                   
            TextInput: 
                id: txt2
                hint_text:'Enter text'
                pos_hint: {'center_x': 0.5, 'center_y': 0.605} 
                size_hint: 0.75, 0.3                                              
    
            Button: 
                id:btn2     
                text:"..."
                size_hint: 0.25, 0.3
                pos_hint: {'center_x': 0.5, 'center_y': 0.605} 
                on_press: root.manager.current = 'choser'
                     
        BoxLayout:  
            orientation: 'horizontal'
            pos: self.pos 
            size: root.size                             
            TextInput: 
                id: txt3
                hint_text:'Enter text'
                pos_hint: {'center_x': 0.5, 'center_y': 1.} 
                size_hint: 0.75, 0.3                                              
    
            Button: 
                id:btn3     
                text:"..."
                size_hint: 0.25, 0.3
                pos_hint: {'center_x': 0.5, 'center_y': 1} 
                on_press:  root.manager.current = 'choser2'
                                       
        Button: 
            id:btn1     
            text:"Анализировать"
            size_hint: 1., 0.3
            pos: 10,10 
            on_press: root.buttonClicked(txt1,txt2,txt3,box)
         
<FileChoser>:
    id:choser
    BoxLayout:
        orientation: 'vertical' 
        BoxLayout:
            orientation: 'horizontal'                     
            FileChooserIconView:
                id:filechooser
                on_selection:choser.selected(filechooser.selection)

            Image:
                id:image
                source:""            
        
        Button: 
 
            id:image_button     
            text:"Выбрать"
            size_hint: 1., 0.1
            pos: 10, 10
            on_press: root.manager.current = 'main'

<FileChoser2>:
    id:choser2
    BoxLayout:
        orientation: 'vertical' 
        BoxLayout:
            orientation: 'horizontal'                     
            FileChooserIconView:
                id:filechooser
                on_selection:choser2.selected(filechooser.selection)

            Image:
                id:image
                source:""            
        
        Button: 
 
            id:image_button     
            text:"Выбрать"
            size_hint: 1., 0.1
            pos: 10, 10
            on_press: root.manager.current = 'main'                     
        
                                                                            
""")

class MainScreen(Screen):

    def buttonClicked(self, txt1,txt2,txt3,box):
        if (txt1.text != '' and txt2.text != ''    
        and txt3.text != '' ) and (txt1.text != 'Ошибка заполнения!' and txt2.text != 'Ошибка заполнения!'    
        and txt3.text != 'Ошибка заполнения!' ):
            self.app = App.get_running_app()
            result = Image(source=str(recognition(str(txt3.text),str(txt1.text),str(txt2.text))))
            box.add_widget(result)
            txt1.text = ''
            txt2.text = ''    
            txt3.text = ''
        else:
            txt1.text = 'Ошибка заполнения!'     
            txt2.text = 'Ошибка заполнения!'   
            txt3.text = 'Ошибка заполнения!'
                             
class FileChoser(Screen):
    def __init__(self, **kw):
        super(FileChoser,self).__init__(**kw)
            
    def selected(self, filename):
        try:
            self.ids.image.source = filename[0]
            pri=(self.ids.image.source.split(os.path.sep))
            save_path=''
            for i in range(len(pri)-1):
                save_path+=pri[i]+(os.path.sep)
            self.manager.ids.main.ids.txt2.text = save_path
        except:
            pass

class FileChoser2(Screen):
    def __init__(self, **kw):
        super(FileChoser2,self).__init__(**kw)
            
    def selected(self, filename):
        try:
            self.ids.image.source = filename[0]
            self.manager.ids.main.ids.txt3.text = self.ids.image.source
        except:
            pass

class ScreenManagement(ScreenManager):
    pass

class FotoOptionsApp(App):

    def __init__(self, **kvargs):
        super(FotoOptionsApp, self).__init__(**kvargs)

    def build(self):
        return ScreenManagement()

if __name__ == '__main__':
    FotoOptionsApp().run()