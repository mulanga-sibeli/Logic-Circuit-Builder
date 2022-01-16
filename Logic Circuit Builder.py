from cgitb import text
from textwrap import fill
import tkinter as tk
from tkinter import *
from unicodedata import name

one_ = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
two_ = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
three_ = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
four_ = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]

one_x = 100
two_x = 100
three_x = 100
four_x = 100

taken = []

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
    name_count = 65
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        mainframe_ = Frame(self.master, bg="gray")
        mainframe_.pack(side=TOP, fill="both")
        mainexit_ = Button(mainframe_, text="X", command= self.master.quit, bg="red")
        mainexit_.pack(side=RIGHT, padx=5, pady=5)
        creategate_ = Button(mainframe_, text="Create", command=self.create_gate_window_, bg="orange")
        creategate_.pack(side=LEFT, padx=5,pady=5)

    def create_gate_window_(self):
        createwindow = Toplevel(app)
        mainframe_ = Frame(createwindow, bg = "gray")
        mainexit_ = Button(mainframe_, text="Cancel", command = createwindow.destroy, bg = "orange")
        maincreate_ = Button(mainframe_, text="Create",command=self.create_gate , bg="orange")
        maincreate_.pack(side=LEFT, padx=20, pady=20)
        mainexit_.pack(side=RIGHT, padx=20, pady=20)
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
        row = rows_var.get()
        col = cols_var.get()
        if row + col in taken:
            create_gate_error = Toplevel(app)
            create_gate_error.geometry("400x100")
            error_text = Label(create_gate_error, text="The position you have specified for this\ngate is already taken by another gate.")    
            error_text.pack(padx=20, pady=20)
            return

        if type_of_gate_var.get() == "NOT" and number_of_inputs_var.get()!=1:
            create_gate_error = Toplevel(app)
            create_gate_error.title("Error")
            create_gate_error.geometry("400x100")
            error_text = Label(create_gate_error, text="The NOT gate can only accept one input.")    
            error_text.pack(padx=20, pady=20)
            return

        if type_of_gate_var.get() != "NOT" and number_of_inputs_var.get()==1:
            create_gate_error = Toplevel(app)
            create_gate_error.title("Error")
            create_gate_error.geometry("400x100")
            error_text = Label(create_gate_error, text="The {} gate accepts at least 2 inputs.".format(type_of_gate_var.get()))    
            error_text.pack(padx=20, pady=20)
            return

        if col == 1:
            one_[row-1][4] = col
            one_[row-1][3] = row
            one_[row-1][2] = number_of_inputs_var.get()
            one_[row-1][1] = type_of_gate_var.get()
            one_[row-1][0] = chr(self.name_count)
            taken.append(col+row)
            current_gate = Button(self.master, text=type_of_gate_var.get()+"\n"+"[id={}]".format(chr(self.name_count)), width=4, height=6, bg="orange").place(x=250, y=row*200)
            self.name_count+=1
            return
            
        if col == 2:
            two_[row-1][4] = col
            two_[row-1][3] = row
            two_[row-1][2] = number_of_inputs_var.get()
            two_[row-1][1] = type_of_gate_var.get()
            one_[row-1][0] = chr(self.name_count)
            taken.append(col+row)
            current_gate = Button(self.master, text=type_of_gate_var.get()+"\n"+"[id={}]".format(chr(self.name_count)), bg="orange", width=4, height=6).place(x=700, y=row*200)
            self.name_count+=1
            return

        if col == 3:
            three_[row-1][4] = col
            three_[row-1][3] = row
            three_[row-1][2] = number_of_inputs_var.get()
            three_[row-1][1] = type_of_gate_var.get()
            three_[row-1][0] = chr(self.name_count)
            taken.append(col+row)
            current_gate = Button(self.master, text= type_of_gate_var.get()+"\n"+"[id={}]".format(chr(self.name_count)), bg="orange", width=4, height=6).place(x=1150, y=row*200)
            self.name_count+=1
            return
    
        if col == 4:
            four_[row-1][4] = col
            four_[row-1][3] = row
            four_[row-1][2] = number_of_inputs_var.get()
            four_[row-1][1] = type_of_gate_var.get()
            four_[row-1][0] = chr(self.name_count)
            taken.append(col+row)
            current_gate = Button(self.master, text= type_of_gate_var.get() + "\n" + "[id={}]".format(chr(self.name_count)), bg="orange", width=4, height=6).place(x=1600, y=row*200)
            self.name_count+=1
            return

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