from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color,Ellipse,Line
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
# frontend
class MyPaintWidget(Widget):
    # constructor for calling multiple keyword args which are built-in methods and attributes
    def __init__(self,**kwargs):
        super(MyPaintWidget,self).__init__(**kwargs)
        # setting up default drawing width
        self.line_width=5
        self.line_style='bold'
        self.eraser_mode=False  # Initialize eraser_mode attribute
    # touch on screen action, defining it's initial touch shape
    def on_touch_down(self,touch): 
        # canvas attribute is called with respect to touch attribute (built-in)
        with self.canvas: 
            # diameter
            d=3 
            # rgb
            Color(1,1,1) 
            # width(d),height(d) on touch x and y axis
            Ellipse(pos=(touch.x,touch.y),size=(d,d)) 
            # defining the width by calling line_style(user-def)
            if self.eraser_mode:
                Color(0,0,0)
                touch.ud['line']=Line(points=(touch.x,touch.y),width=10)
            else:
                if self.line_style=='bold':
                    touch.ud['line']=Line(points=(touch.x,touch.y),width=5)
                elif self.line_style=='thin':
                    touch.ud['line']=Line(points=(touch.x,touch.y),width=2)
                elif self.line_style=='light':
                    touch.ud['line']=Line(points=(touch.x,touch.y),width=0.5)
    # touch will increment with respect to y and x axis 
    def on_touch_move(self,touch):
        if 'line' in touch.ud:
            touch.ud['line'].points+=[touch.x,touch.y]
    # flag is reset to false when the user releases the touch
    def on_touch_up(self,touch):
        if self.eraser_mode:
            # reset eraser mode flag
            self.eraser_mode=False 
    def change_line_style(self, style):
        if style=='bold':
            self.line_style='bold'
        elif style=='thin':
            self.line_style='thin'
        elif style=='light':
            self.line_style='light'
        elif style=='eraser':
            self.line_style='eraser'
            self.eraser_mode=True
        else:
            print("Unknown line style: ",style)
# backend  
class OreoPaint(App): 
    def build(self): 
        parent=BoxLayout(orientation="vertical") 
        # calling the mypaintwidget class for canvas attribute
        self.userdef1=MyPaintWidget() 
        # func called to clear screen
        clrbtn=Button(text="Clear",size_hint=(.1,.1)) 
        clrbtn.bind(on_release=self.clear_canvas) 
        # defining lambda function concept for efficiency no need to create func for each event
        boldbtn=Button(text="Bold",size_hint=(.1,.1))
        boldbtn.bind(on_release=lambda x:self.userdef1.change_line_style('bold'))
        thinbtn=Button(text="Thin",size_hint=(.1,.1))
        thinbtn.bind(on_release=lambda x:self.userdef1.change_line_style('thin'))
        lightbtn=Button(text="Light",size_hint=(.1,.1))
        lightbtn.bind(on_release=lambda x:self.userdef1.change_line_style('light'))
        eraserbtn=Button(text="Eraser",size_hint=(.1,.1))
        eraserbtn.bind(on_release=lambda x:self.userdef1.change_line_style('eraser'))
        parent.add_widget(self.userdef1) 
        parent.add_widget(clrbtn)
        parent.add_widget(boldbtn)
        parent.add_widget(thinbtn)
        parent.add_widget(lightbtn)
        parent.add_widget(eraserbtn)
        return parent
    def clear_canvas(self,btn):
        self.userdef1.canvas.clear() 
# final execution 
if __name__ == '__main__':
    OreoPaint().run()