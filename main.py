from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.size=(400,600)
Window.clearcolor=(0,1,1,1)

Builder.load_file("calc.kv")

class Design(Widget):
    
    def input(self):
        
        if self.ids.tex.text=="0":
            self.ids.tex.text=""
        elif self.ids.tex.text=="Error":
            self.ids.tex.text=""
        else:
            pass
    def clear(self):
        self.ids.tex.text="0"

    def pressed(self):
        try:
            self.ids.tex.text=str(eval(self.ids.tex.text))
        except Exception as e:
            self.ids.tex.text="Error"


class CalculatorHero(App):
    def build(self):
        return Design()
    
ap=CalculatorHero()
ap.run()