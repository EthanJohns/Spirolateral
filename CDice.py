#!/usr/bin/env python3
from tkinter import *
import turtle


class Spirolateral:
    def __init__(self, name: str, segment: int, angle):
        self.name = name
        self.segment = segment
        self.angle = angle


class Application(Frame):

    def __init__(self, master):
        super().__init__(master)
<<<<<<< HEAD

        # Constants for formatting
        self.BG_COL = "#4286f4"
        self.PX = 20
        self.PY = 10

        self.__homeframe = Frame(master, width=400, height=320)
        self.__homeframe.grid_propagate(0)
        self.__homeframe.grid()

        self.displaying_header = Frame(self.__homeframe,  bg=self.BG_COL,
                                       width=400, height=60)
        self.displaying_header.grid_propagate(0)
        self.displaying_header.grid(row=0, columnspan=2)

        self.__inputframe = Frame(master, width=400, height=320)
        self.__inputframe.grid_propagate(0)
        self.collecting_header = Frame(self.__inputframe,  bg=self.BG_COL,
                                       width=400, height=60)
        self.collecting_header.grid_propagate(0)  # preserves the space we want
        self.collecting_header.grid(row=0, columnspan=2)

        collecting_label = Label(self.collecting_header, bg=self.BG_COL,
                                 text="Collecting Spiro Data")
        collecting_label.grid(row=0, column=0,  padx=self.PX, pady=self.PY)

        self.vcmd = (master.register(self.validate_float),
                     '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.spirolateralist = []

        self.create_home_widgets()
        self.create_input_widgets()
        '''
        self.canvas = Canvas(self.__homeframe, width = 400, height = 400)
        self.canvas.grid(row = 8, column = 0)
        self.SpiroBot = turtle.RawTurtle(self.canvas)
        '''

    def create_home_widgets(self):
        '''
        self.quit = Button(self.displaying_header, text="QUIT",
                           fg="red", command=root.destroy)
        self.quit.grid(row=0, column=2)
        '''
        displaying_label = Label(
            self.displaying_header, bg=self.BG_COL, anchor=NW, text="Displaying Spiro Data")
        displaying_label.grid(row=0, column=0, sticky=NW,  padx=20, pady=10)

        self.go_to_collect_btn = Button(
            self.displaying_header, width = 10, text="Add Spiro", command=self.inputGrid)
        self.go_to_collect_btn.grid(row=0, column=1, padx=self.PX,
                                    pady=self.PY)

        fname_label_d = Label(self.__homeframe, anchor=NW,
                              text="Spiro name:")
        fname_label_d.grid(row=1, column=0, sticky=NW, padx=self.PX,
                           pady=self.PY)

        self.first_name = Label(self.__homeframe, anchor=NW)
        self.first_name.grid(row=1, column=1, sticky=NW, pady=self.PY)

        age_label_d = Label(self.__homeframe, anchor=NW, text="Segment: ")
        age_label_d.grid(row=2, column=0, sticky=NW,
                         padx=self.PX, pady=self.PY)

        self.age = Label(self.__homeframe, anchor=NW)
        self.age.grid(row=2, column=1, sticky=NW, pady=self.PY)

        angel_label_d = Label(self.__homeframe, anchor=NW, text="Angel:")
        angel_label_d.grid(row=3, column=0, sticky=NW,
                           padx=self.PX, pady=self.PY)

        self.angel = Label(self.__homeframe, anchor=NW)
        self.angel.grid(row=3, column=1, sticky=NW, pady=self.PY)

        self.mobile_info = Label(self.__homeframe)
        self.mobile_info.grid(row=4, columnspan=2, sticky=W+E)

        self.prev_btn = Button(self.__homeframe, text="Previous",
                               state=DISABLED, command=self.previous)
        self.prev_btn.grid(row=5, column=0, sticky=W,
                           padx=self.PX/2, pady=self.PY)

        self.next_btn = Button(self.__homeframe, text="Next",
                               state=DISABLED, command=self.next_person)
        self.next_btn.grid(row=5, column=1, sticky=E,
                           padx=self.PX/2, pady=self.PY)
        self.__index = 0

    def create_input_widgets(self):
        '''
        self.quit = Button(self.collecting_header, text="QUIT",
                           fg="red", command=lambda: root.destroy())
        self.quit.grid(row=0, column=2)
        '''
        self.go_to_display_btn = Button(
            self.collecting_header, width=10,  text="Show All", command=self.homeGrid)
        self.go_to_display_btn.grid(
            row=0, column=1, padx=self.PX, pady=self.PY)

        fname_label = Label(self.__inputframe, anchor=NW,
                            text="Spiro Name:")
        fname_label.grid(row=1, column=0, sticky=NW,
                         padx=self.PX, pady=self.PY)

        self.spiro_name_entry = Entry(self.__inputframe)
        self.spiro_name_entry.grid(row=1, column=1, sticky=NW, pady=self.PY)

        segment_label = Label(self.__inputframe, anchor=NW, text="Segment:")
        segment_label.grid(row=2, column=0, sticky=NW,
                           padx=self.PX, pady=self.PY)

        self.age_entry = Entry(
            self.__inputframe, validate='key', validatecommand=self.vcmd)
        self.age_entry .grid(row=2, column=1, sticky=NW)

        angel_label = Label(self.__inputframe, anchor=NW, text="Angle:")
        angel_label.grid(row=3, column=0, sticky=NW,
                         padx=self.PX, pady=self.PY)

        self.angel_entry = Entry(
            self.__inputframe, validate='key', validatecommand=self.vcmd)
        self.angel_entry .grid(row=3, column=1, sticky=NW)

        self.create_person_btn = Button(self.__inputframe, width=10,
                                        text="Enter Data",
                                        command=self.make_spiro)
        self.create_person_btn.grid(row=5, columnspan=2, pady=15)
        self.errorLabel = Label(self.__inputframe, text="")
        self.errorLabel.grid(row=6,columnspan = 2)

=======
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
>>>>>>> 3bf82b03c518c08ab302475209150f5bccd3d2cc
    def TurtleMove(self):
        self.spirolateralist[self.__index].segment

    def validate_float(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if(action == '1'):
            if text in '0123456789-+':
                try:
                    int(value_if_allowed)
                    return True
                except ValueError:
                    return False
            else:
                return False
        else:
            return True

    def inputGrid(self):
        """ Switches from collecting frame to displaying frame.  """
        self.__homeframe.grid_forget()
        self.__inputframe.grid_propagate(0)
        self.__inputframe.grid(row=0, column=0)

    def homeGrid(self):
        self.__inputframe.grid_forget()
        self.__homeframe.grid_propagate(0)
        self.__homeframe.grid(row=0, column=0)

        if len(self.spirolateralist) > 0:
            self.__index = 0
            self.show_data()
        else:
            self.mobile_info.configure(
                text="There is not currently any data to show")

    def make_spiro(self):
        if self.spiro_name_entry.get() or self.age_entry.get() or self.angel_entry.get() == "":
            self.errorLabel.configure(text="There is no data entered.")
            print(1)
        else:
            spiroClass = Spirolateral(self.spiro_name_entry.get(), self.age_entry.get(), self.angel_entry.get())
            self.spirolateralist.append(spiroClass)

        if len(self.spirolateralist) > 1:
            self.next_btn.configure(state=NORMAL)
        self.clear()

    def clear(self):
        """ Clears entries and selections in collecting frame. """
        self.spiro_name_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.angel_entry.delete(0, END)

    def next_person(self):
        """ Increments self.__index and calls show_data method. Disables next
            button if at the end of the list. Ensures prev button is normal.
        """
        self.__index += 1

        if self.__index == len(self.spirolateralist)-1:
            self.next_btn.configure(state=DISABLED)

        self.prev_btn.configure(state=NORMAL)
        self.show_data()

    def previous(self):
        """ Decrements self.__index and calls show_data method. Disables prev
            button if at the start of the list. Ensures next button is normal.
        """
        self.__index -= 1
        if self.__index == 0:
            self.prev_btn.configure(state=DISABLED)

        self.next_btn.configure(state=NORMAL)
        self.show_data()

    def show_data(self):
        """ Configures the displaying frame to show data associated with person
            object stored at self.__index
        """
        self.first_name.configure(text=self.spirolateralist[self.__index].name)
        self.age.configure(text=self.spirolateralist[self.__index].segment)
        self.angel.configure(text="{}°".format(
            self.spirolateralist[self.__index].angle))


root = Tk()
app = Application(root)
app.mainloop()
