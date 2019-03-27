#!/usr/bin/env python3
# ensures we run in py3
from tkinter import *
import turtle


class Spirolateral:
    '''
    Spirolateral Class that stores the necessary data for a spirolateral
    '''

    def __init__(self, name: str, segment: int, angle: int):
        self.name = name
        self.segment = segment
        self.angle = angle
        self.digitalList = []

    def digit_root(self, n):
        return (n - 1) % 9 + 1

    def digitCalc(self,):
        for i in range(20):
            test = (i+1)
            print(test)
            n = test * 8
            if digit_root(n) in digitalList:
                break
            else:
                digitalList.append(digit_root(n))
        print(digitalList)


class Application(Frame):
    '''
    GUI Application
    '''

    def __init__(self, master):
        super().__init__(master)  # to ensure parent is called correctly.

        # Constants for formatting
        self.BG_COL = "#4286f4"
        self.PX = 20
        self.PY = 10
        self.WDTH = 800
        self.HGHT = 400

        # setting up a main container
        self.__maincontainer = Frame(master, width=self.WDTH, height=self.HGHT)
        self.__maincontainer.grid(row=0, column=0, sticky="nsew")

        # Setting up the initial frame for the home window.
        self.__homeframe = Frame(self.__maincontainer,
                                 width=self.WDTH/2, height=self.HGHT)

        self.__homeframe.grid(row=0, column=0, sticky="nsew")

        # header in the homeframe
        self.displaying_header = Frame(self.__homeframe,  bg=self.BG_COL,
                                       width=self.WDTH/2, height=60)
        self.displaying_header.grid_propagate(0)
        self.displaying_header.grid(row=0, columnspan=2)

        # Setting up the frame for the canvas
        self.__canvasframe = Frame(
            self.__maincontainer, width=self.WDTH/2, height=self.HGHT)
        self.__canvasframe.grid_propagate(0)  # to reserve space.
        self.__canvasframe.grid(row=0, column=1, sticky='E')

        self.canvas = Canvas(self.__canvasframe,
                             height=self.HGHT, width=self.WDTH/2)
        self.canvas.grid(row=0, column=3)

        # Setting up the frame for the data input
        self.__inputframe = Frame(self.__maincontainer, width=self.WDTH/2,
                                  height=self.HGHT)
        self.__inputframe.grid_propagate(0)

        self.collecting_header = Frame(self.__inputframe,  bg=self.BG_COL,
                                       width=self.WDTH/2, height=60)
        self.collecting_header.grid_propagate(0)  # preserves the space we want
        self.collecting_header.grid(row=0, columnspan=2)

        collecting_label = Label(self.collecting_header, bg=self.BG_COL,
                                 text="Collecting Spiro Data")
        collecting_label.grid(row=0, column=0,  padx=self.PX, pady=self.PY)

        # data validation for our Entry boxes.
        self.vcmd = (master.register(self.validate_int),
                     '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        # the list that will store our spiros
        self.spirolateralist = []

        self.create_home_widgets()
        self.create_input_widgets()
        # setup turtle elements
        self.spiroTurt = turtle.RawTurtle(self.canvas)
        self.spiroTurt.speed(-1)

    def create_home_widgets(self):
        '''
        Method for creating widgets on the home frame.
        '''
        displaying_label = Label(
            self.displaying_header, bg=self.BG_COL,
            text="Displaying Spiro Data")
        displaying_label.grid(row=0, column=0, padx=self.PX, pady=self.PY)

        self.go_to_collect_btn = Button(
            self.displaying_header, width=10, text="Add Spiro",
            command=self.inputGrid)
        self.go_to_collect_btn.grid(row=0, column=1, padx=self.PX,
                                    pady=self.PY)

        fname_label_d = Label(self.__homeframe, anchor=NW,
                              text="Spiro Name:")
        fname_label_d.grid(row=1, column=0, sticky=NW, padx=self.PX,
                           pady=self.PY)

        self.first_name = Label(self.__homeframe, anchor=NW)
        self.first_name.grid(row=1, column=1, sticky=NW, pady=self.PY)

        age_label_d = Label(self.__homeframe, anchor=NW, text="Segment: ")
        age_label_d.grid(row=2, column=0, sticky=NW,
                         padx=self.PX, pady=self.PY)

        self.age = Label(self.__homeframe, anchor=NW)
        self.age.grid(row=2, column=1, sticky=NW, pady=self.PY)

        angel_label_d = Label(self.__homeframe, anchor=NW, text="Angle:")
        angel_label_d.grid(row=3, column=0, sticky=NW,
                           padx=self.PX, pady=self.PY)

        self.angel = Label(self.__homeframe, anchor=NW)
        self.angel.grid(row=3, column=1, sticky=NW, pady=self.PY)

        self.mobile_info = Label(self.__homeframe)
        self.mobile_info.grid(row=4, columnspan=2)

        self.prev_btn = Button(self.__homeframe, text="Previous",
                               state=DISABLED, command=self.previous)
        self.prev_btn.grid(row=5, column=0,
                           padx=self.PX/2, pady=self.PY, sticky='W')

        self.next_btn = Button(self.__homeframe, text="Next",
                               state=DISABLED, command=self.next_person)
        self.next_btn.grid(row=5, column=1,
                           padx=self.PX/2, pady=self.PY, sticky='E')
        self.__index = 0  # to maintain our position in the list.

        self.turtleDrawButt = Button(
            self.__homeframe, text="Draw this Spiro.",
            command=self.turtleSpiroDraw)
        self.turtleDrawButt.grid(row=5, columnspan=2, pady=15)

    def create_input_widgets(self):
        '''
        Method for creating widgets on the input frame
        '''
        self.go_to_display_btn = Button(
            self.collecting_header, width=10,  text="Show All",
            command=self.homeGrid)
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

        self.seg_ent = Entry(
            self.__inputframe, validate='key', validatecommand=self.vcmd)
        self.seg_ent.grid(row=2, column=1, sticky=NW)

        angel_label = Label(self.__inputframe, anchor=NW, text="Angle:")
        angel_label.grid(row=3, column=0, sticky=NW,
                         padx=self.PX, pady=self.PY)

        self.ang_ent = Entry(
            self.__inputframe, validate='key', validatecommand=self.vcmd)
        self.ang_ent .grid(row=3, column=1, sticky=NW)

        self.create_person_btn = Button(self.__inputframe, width=10,
                                        text="Enter Data",
                                        command=self.make_spiro)
        self.create_person_btn.grid(row=5, columnspan=2, pady=15)
        self.errorLabel = Label(self.__inputframe, text="")
        self.errorLabel.grid(row=6, columnspan=2)

    def validate_int(self, action, index, value_if_allowed,
                     prior_value, text, validation_type, trigger_type,
                     widget_name):
        '''
        Integer validation for entry boxes.
        '''
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
        self.__inputframe.grid(row=0, column=0, sticky="nsew")

    def homeGrid(self):
        self.__inputframe.grid_forget()
        self.__homeframe.grid_propagate(0)
        self.__homeframe.grid(row=0, column=0, sticky="nsew")

        if len(self.spirolateralist) > 0:
            self.__index = 0
            self.show_data()
            self.mobile_info.configure(
                text="")
        else:
            self.mobile_info.configure(
                text="There is not currently any data to show")

    def make_spiro(self):
        '''Creates a spirolateral object'''
        if "" in {self.spiro_name_entry.get(),
                  self.seg_ent.get(), self.ang_ent.get()}:

            self.errorLabel.configure(text="There is no data entered.")
        else:
            self.errorLabel.configure(text="")
            spiroClass = Spirolateral(self.spiro_name_entry.get(
            ), self.seg_ent.get(), self.ang_ent.get())
            self.spirolateralist.append(spiroClass)
            self.clear()
        if len(self.spirolateralist) > 1:
            self.next_btn.configure(state=NORMAL)

    def clear(self):
        """ Clears entries and selections in input frame. """
        self.spiro_name_entry.delete(0, END)
        self.seg_ent.delete(0, END)
        self.ang_ent.delete(0, END)

    def next_person(self):
        """ Increments self.__index and calls show_data method. Disables next
        button if at the end of the list. Ensures prev button is normal."""
        self.__index += 1

        if self.__index == len(self.spirolateralist)-1:
            self.next_btn.configure(state=DISABLED)

        self.prev_btn.configure(state=NORMAL)
        self.show_data()

    def previous(self):
        """ Decrements self.__index and calls show_data method. Disables prev
        button if at the start of the list. Ensures next button is normal."""

        self.__index -= 1
        if self.__index == 0:
            self.prev_btn.configure(state=DISABLED)

        self.next_btn.configure(state=NORMAL)
        self.show_data()

    def show_data(self):
        """ Configures the displaying frame to show data associated with person
        object stored at self.__index"""
        self.first_name.configure(text=self.spirolateralist[self.__index].name)
        self.age.configure(text=self.spirolateralist[self.__index].segment)
        self.angel.configure(text="{}°".format(
            self.spirolateralist[self.__index].angle))

    def turtleSpiroDraw(self):
        angle = int(self.spirolateralist[self.__index].angle)
        segments = int(self.spirolateralist[self.__index].segment)
        complete = False
        self.spiroTurt.reset()  # clears any previous drawings

        startPosx, startPosy = self.spiroTurt.pos()
        startPos = (startPosx, startPosy)
        self.spiroTurt.speed(-1)  # for maximum speed
        cycles = 0
        SCALE = 20
        while not complete:
            for distance in range(1, segments + 1):
                # range increases for more segments
                print(distance)
                self.spiroTurt.right(180 - angle)
                # turns at the correct angle
                self.spiroTurt.forward(distance * SCALE)
                # increases the size of the spiro by a factor.

            cycles += 1

            currentPosx, currentPosy = self.spiroTurt.pos()
            # grabs current pos
            currentPos = (round(currentPosx, 3), round(currentPosy, 3))
            print("Current cycle", cycles)

            if currentPos == startPos:
                print("We're done here")
                complete = True


if __name__ == "__main__":
    # Executes when the file itself is run, not when imported.
    root = Tk()
    app = Application(root)
    app.mainloop()
