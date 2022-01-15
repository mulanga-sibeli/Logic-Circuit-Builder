from cgitb import text
from textwrap import fill
import tkinter as tk
from tkinter import *

one_ = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
two_ = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
three_ = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
four_ = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
name_count = 65
one_x = 100
two_x = 100
three_x = 100
four_x = 100

def NOR_(inputs):
    for val in inputs:
        if val == 1:
            return 0
    return 1

def OR_(inputs):
    for val in inputs:
        if val == 1:
            return 1
    return 0

def NAND_(inputs):
    for val in inputs:
        if val == 0:
            return 1
    return 0

def AND_(inputs):
    for val in inputs:
        if val == 0:
            return 0
    return 1

def NOT_(input):
    if input == 1:
        return 0
    return 1



class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        mainframe_ = Frame(self.master, bg="gray")
        mainframe_.pack(side=TOP, fill="both")
        mainexit_ = Button(mainframe_, text="Exit", command= self.master.quit, bg="orange")
        mainexit_.pack(side=RIGHT, padx=5, pady=5)
        creategate_ = Button(mainframe_, text="Create", command=self.create_gate_window_, bg="orange")
        creategate_.pack(side=LEFT, padx=5,pady=5)

    def create_gate_window_(self):
        createwindow = Toplevel(app)
        mainframe_ = Frame(createwindow, bg = "gray")
        mainexit_ = Button(mainframe_, text="Cancel", command = createwindow.destroy, bg = "orange")
        mainexit_.pack(side=RIGHT, padx=20, pady=20)
        maincreate_ = Button(mainframe_, text="Create", bg="orange")
        maincreate_.pack(side=LEFT, padx=20, pady=20)
        createwindow.title("Create Gate")
        createwindow.geometry("300x200")
        mainframe_.pack(side=BOTTOM, fill="both")
        secframe_ = Frame(createwindow)
        secframe_.pack(fill="both")
        terframe_ = Frame(createwindow)
        terframe_.pack(fill="both")
        terframe_1 = Frame(createwindow)
        terframe_1.pack(fill="both")
        terframe_2 = Frame(createwindow)
        terframe_2.pack(fill="both")
        type_of_gate = Label(secframe_, text = "Type").pack(side=LEFT, padx=5, pady=5)
        gate_options_ = ["OR", "AND", "NOT", "NAND", "NOR"]
        number_options = [1, 2, 3, 4]
        gate_options_drop = OptionMenu(secframe_, type_of_gate_var, *gate_options_)
        gate_options_drop.pack(side=RIGHT)
        number_of_rows = Label(terframe_1, text = "Row").pack(side=LEFT, padx=5, pady=5)
        row_options_drop = OptionMenu(terframe_1, rows_var, *number_options)
        row_options_drop.pack(side=RIGHT)
        number_of_cols = Label(terframe_2, text = "Col").pack(side=LEFT, padx=5, pady=5)
        col_options_drop = OptionMenu(terframe_2, cols_var, *number_options)
        col_options_drop.pack(side=RIGHT)
        number_of_inputs = Label(terframe_, text = "Inputs").pack(side=LEFT, padx = 5, pady = 5)
        input_options = ["1", "2", "3", "4"]
        input_options_drop = OptionMenu(terframe_, number_of_inputs_var, *number_options).pack(side=RIGHT)

    def create_gate(self):
        if cols_var.get() == 1:
            one_[rows_var.get()-1][4] = cols_var.get()
            one_[rows_var.get()-1][3] = rows_var.get()
            one_[rows_var.get()-1][2] = number_of_inputs_var.get()
            one_[rows_var.get()-1][1] = type_of_gate_var.get()
            one_[rows_var.get()-1][0] = chr(name_count)
            current_gate = Button(self.master, text=chr(name_count) + "\n"+ type_of_gate_var.get()).place(x=100, y=one_x)
            one_x+=250
        
        if cols_var.get() == 2:
            two_[rows_var.get()-1][4] = cols_var.get()
            two_[rows_var.get()-1][3] = rows_var.get()
            two_[rows_var.get()-1][2] = number_of_inputs_var.get()
            two_[rows_var.get()-1][1] = type_of_gate_var.get()
            one_[rows_var.get()-1][0] = chr(name_count)

        if cols_var.get() == 3:
            three_[rows_var.get()-1][4] = cols_var.get()
            three_[rows_var.get()-1][3] = rows_var.get()
            three_[rows_var.get()-1][2] = number_of_inputs_var.get()
            three_[rows_var.get()-1][1] = type_of_gate_var.get()
            one_[rows_var.get()-1][0] = chr(name_count)
    
        if cols_var.get() == 4:
            four_[rows_var.get()-1][4] = cols_var.get()
            four_[rows_var.get()-1][3] = rows_var.get()
            four_[rows_var.get()-1][2] = number_of_inputs_var.get()
            four_[rows_var.get()-1][1] = type_of_gate_var.get()
            one_[rows_var.get()-1][0] = chr(name_count)

    def show():
        type_of_gate_var.set(type_of_gate_var.get())

        
app = tk.Tk()
main = Window(app)
app.title("Gates")
app.attributes("-fullscreen", True)
type_of_gate_var = StringVar()
type_of_gate_var.set("OR")
number_of_inputs_var = IntVar()
number_of_inputs_var.set(1)
rows_var = IntVar()
rows_var.set(1)
cols_var = IntVar()
cols_var.set(1)
app.mainloop()