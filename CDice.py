from tkinter import *
import turtle

class Spirolateral:
    def __init__(self, name, segment, angle):
        self.name = name
        self.segment = segment
        self.angle = angle


class Application(Frame):

    def __init__(self, master):
        super().__init__(master)

        # Constants for formatting
        self.BG_COL = "#4286f4"
        self.PX = 20
        self.PY = 10

        self.homeframe = Frame(master, width=400, height=640)
        self.homeframe.grid_propagate(0)
        self.homeframe.grid()

        self.displaying_header = Frame(self.homeframe,  bg=self.BG_COL,
                                       width=400, height=60)
        self.displaying_header.grid_propagate(0)
        self.displaying_header.grid(row=0, columnspan=2)

        self.inputframe = Frame(master, width=400, height=640)
        self.inputframe.grid_propagate(0)
        self.collecting_header = Frame(self.inputframe,  bg=self.BG_COL,
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
        self.canvas = Canvas(self.homeframe, width = 400, height = 320)
        self.canvas.grid(row = 6, column = 0)
        self.SpiroBot = turtle.RawTurtle(self.canvas)

    def create_home_widgets(self):
        self.quit = Button(self.displaying_header, text="QUIT", fg="red", command=root.destroy)
        self.quit.grid(row=0, column=2)

        self.movefd = Button(self.homeframe, text='Move Forward ', font=(
            "Comic Sans MS", 11), command=self.TurtleMove)
        self.movefd.grid(row=10, column=1)

        displaying_label = Label(
            self.displaying_header, bg=self.BG_COL, anchor=NW, text="Displaying Spiro Data")
        displaying_label.grid(row=0, column=0, sticky=NW,  padx=20, pady=10)

        self.go_to_collect_btn = Button(
            self.displaying_header, width=15, anchor=NW, text="Add New Spiro", command=self.inputGrid)
        self.go_to_collect_btn.grid(row=0, column=1, sticky=NW,  padx=self.PX,
                                    pady=self.PY)

        fname_label_d = Label(self.homeframe, anchor=NW,
                              text="Spiro name:")
        fname_label_d.grid(row=1, column=0, sticky=NW, padx=self.PX,
                           pady=self.PY/2)

        self.first_name = Label(self.homeframe, anchor=NW)
        self.first_name.grid(row=1, column=1, sticky=NW, pady=self.PY/2)

        age_label_d = Label(self.homeframe, anchor=NW, text="Segment: ")
        age_label_d.grid(row=2, column=0, sticky=NW,
                         padx=self.PX, pady=self.PY/2)

        self.age = Label(self.homeframe, anchor=NW)
        self.age.grid(row=2, column=1, sticky=NW, pady=5)

        angel_label_d = Label(self.homeframe,anchor=NW, text="Angel:")
        angel_label_d.grid(row=3,column=0,sticky=NW,padx =self.PX,pady=self.PY/2)

        self.angel = Label(self.homeframe, anchor=NW)
        self.angel.grid(row=3,column=1,sticky=NW, pady=5)

        self.mobile_info = Label(self.homeframe)
        self.mobile_info.grid(row=4, columnspan=2, sticky=W+E)

        self.prev_btn = Button(self.homeframe, text="Previous",
                               state=DISABLED, command=self.previous)
        self.prev_btn.grid(row=5, column=0, sticky=W,
                           padx=self.PX/2, pady=self.PY)

        self.next_btn = Button(self.homeframe, text="Next",
                               state=DISABLED, command=self.next_person)
        self.next_btn.grid(row=5, column=1, sticky=E, padx=self.PX/2,
                           pady=self.PY)
        self.index = 0
    def create_input_widgets(self):
        self.quit = Button(self.collecting_header, text="QUIT", fg="red", command=lambda: [
                           root.destroy(), self.TurtleScreen.bye()])
        self.quit.grid(row=0, column=2)

        self.go_to_display_btn = Button(
            self.collecting_header, width=10,  text="Show All", command=self.homeGrid)
        self.go_to_display_btn.grid(
            row=0, column=1, padx=self.PX, pady=self.PY)

        fname_label = Label(self.inputframe, anchor=NW,
                            text="Spiro Name:")
        fname_label.grid(row=1, column=0, sticky=NW,
                         padx=self.PX, pady=self.PY)

        self.spiro_name_entry = Entry(self.inputframe)
        self.spiro_name_entry .grid(row=1, column=1, sticky=NW, pady=self.PY/2)

        segment_label = Label(self.inputframe, anchor=NW, text="Segment:")
        segment_label.grid(row=2, column=0, sticky=NW,
                           padx=self.PX, pady=self.PY/2)

        self.age_entry = Entry(self.inputframe)
        self.age_entry .grid(row=2, column=1, sticky=NW)

        angel_label = Label(self.inputframe, anchor=NW, text="Angle:")
        angel_label.grid(row=3, column=0, sticky=NW,
                         padx=self.PX, pady=self.PY/2)

        self.angel_entry = Entry(self.inputframe)
        self.angel_entry .grid(row=3, column=1, sticky=NW)

        self.create_person_btn = Button(self.inputframe, width=10,
                                        text="Enter Data",
                                        command=self.make_spiro)
        self.create_person_btn.grid(row=5, columnspan=2, pady=15)

    def TurtleMove(self):
        self.spirolateralist[self.index].segment

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
        
        
        self.homeframe.grid_forget()
        self.inputframe.grid_propagate(0)
        self.inputframe.grid(row=0, column=0)

    def homeGrid(self):
        self.inputframe.grid_forget()
        self.homeframe.grid_propagate(0)
        self.homeframe.grid(row=0, column=0)

        if len(self.spirolateralist) > 0:
            self.index = 0
            self.show_data()
        else:
           self.mobile_info.configure(text = "There is not currently any data to show")

    def make_spiro(self):
        self.spirolateralist.append(Spirolateral(self.spiro_name_entry.get(),
                                                 self.age_entry.get(), self.angel_entry.get()))
        if len(self.spirolateralist) > 1:
            self.next_btn.configure(state=NORMAL)
        self.clear()

    def clear(self):
        """ Clears entries and selections in collecting frame. """
        self.spiro_name_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.angel_entry.delete(0, END)

    def next_person(self):
        """ Increments self.index and calls show_data method. Disables next
            button if at the end of the list. Ensures prev button is normal.
        """
        self.index += 1
        
        if self.index == len(self.spirolateralist)-1:
            self.next_btn.configure(state=DISABLED)

        self.prev_btn.configure(state=NORMAL)
        self.show_data()

    def previous(self):
        """ Decrements self.index and calls show_data method. Disables prev
            button if at the start of the list. Ensures next button is normal.
        """
        self.index -= 1
        if self.index == 0:
            self.prev_btn.configure(state=DISABLED)

        self.next_btn.configure(state=NORMAL)
        self.show_data()

    def show_data(self):
        """ Configures the displaying frame to show data associated with person
            object stored at self.index
        """
        self.first_name.configure(text=self.spirolateralist[self.index].name)
        self.age.configure(text=self.spirolateralist[self.index].segment)
        self.angel.configure(text="{}°".format(self.spirolateralist[self.index].angle))


root = Tk()
app = Application(root)
app.mainloop()
