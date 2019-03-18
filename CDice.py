from tkinter import *
import turtle
from random import randint
CDtrayOpen = False


class Application(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.grid()
        
        self.TurtleScreen = turtle.Screen()
        vcmd = (master.register(self.validate_float),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.create_widgets(vcmd)

    def create_widgets(self,vcmd):
        self.SpiroBot = turtle.Turtle()
        
        self.quit = Button(self, text="QUIT", fg="red", command= lambda:[root.destroy(), self.TurtleScreen.bye()])
        self.quit.grid(row=0, column=7)

        #self.hi_there = Button(
           #self, text="Do you want a cup holder", fg="blue", command=self.cupholder)
        #self.hi_there.grid(row=0, column=5)

        
        self.Distancentry = Entry(self, width = 10, validate = 'key', validatecommand = vcmd,)
        self.Distancentry.insert(0,'1')
        self.Distancentry.grid(row = 1, column = 5, sticky = W)        
        
        
        
        
        self.d4 = Button(self, text='Move Forward ', font=("Comic Sans MS", 11),command=self.TurtleMove)
        self.d4.grid(row=0, column=1)


        self.output = Label(root, text="")
        self.output.grid()
    def TurtleMove(self):
        self.SpiroBot.fd(int(self.Distancentry.get()))

    def validate_float(self, action, index, value_if_allowed,
    prior_value, text, validation_type, trigger_type, widget_name):
        # action=1 -> insert
        if(action=='1'):
            if text in '0123456789.-+':
                try:
                    float(value_if_allowed)
                    return True
                except ValueError:
                    return False
            else:
                return False
        else:
            return True
    

root = Tk()
app = Application(root)
app.mainloop()
