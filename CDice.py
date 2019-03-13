from tkinter import *
import turtle
from random import randint
CDtrayOpen = False


class Application(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.homeframe = Frame(master, width=350, height=320)
        self.grid_propagate(0)
        self.homeframe.grid()
        
        self.inputframe = Frame(master,width=350, height=320)
        self.inputframe.grid_propagate(0)
        
        
        
        self.TurtleScreen = turtle.Screen()
        self.vcmd = (master.register(self.validate_float),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.create_widgets()

    def create_widgets(self):
        self.SpiroBot = turtle.Turtle()

        self.quit = Button(self.homeframe, text="QUIT", fg="red", command=lambda: [
                           root.destroy(), self.TurtleScreen.bye()])
        self.quit.grid(row=0, column=7)

        self.addnewSpiro = Button(
            self.homeframe, text="Add new spirolateral", fg="blue", command = self.inputGrid)
        self.addnewSpiro.grid(row=0, column=5, sticky=W)

        self.Distancentry = Entry(
            self.homeframe, width=10, validate='key', validatecommand=self.vcmd,)
        self.Distancentry.insert(0, '1')
        self.Distancentry.grid(row=1, column=5, sticky=W)

        self.movefd = Button(self.homeframe, text='Move Forward ', font=(
            "Comic Sans MS", 11), command=self.TurtleMove)
        self.movefd.grid(row=0, column=1)

        self.goHome = Button(self.inputframe,text = "Go Back(without saving)",command = self.homeGrid)
        self.goHome.grid(row = 0, column = 2)
    def TurtleMove(self):
        self.SpiroBot.fd(int(self.Distancentry.get()))

    def validate_float(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if(action == '1'):
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

    def inputGrid(self):
        
        """ Switches from collecting frame to displaying frame.  """
        self.homeframe.grid_forget()
        self.inputframe.grid(row = 0, column = 0)
    def homeGrid(self):
        self.inputframe.grid_forget()
        self.homeframe.grid(row = 0, column = 0)
    



root = Tk()
app = Application(root)
app.mainloop()
