from ast import Or
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

entries = []

outputs = []

def OR_(type, inputs, idd):
    if type == "OR":
        result = inputs[0]
        for bitt in inputs[2:]:
            if result == 1 or bitt == 1:
                result = 1
            else:
                result = 0
        return result
    return NOR_(type, inputs)

def AND_(type, inputs):
    if type == "AND":
        result = inputs[0]
        for bitt in inputs[2:]:
            if result == 1 and bitt == 1:
                result = 1
            else:
                result = 0
        return result
    return NOR_(type, inputs)

def NOR_(type, inputs):
    if type == "NOR":
        result = inputs[0]
        for bitt in inputs:
            if result == 1 or bitt == 1:
                result = 1
            else:
                result = 0
        if result == 1:
            return 0
        return 1
    return NOR_(type, inputs)

def NAND_(type, inputs):
    if type == "NOR":
        result = inputs[0]
        for bitt in inputs:
            if result == 1 and bitt == 1:
                result = 1
            else:
                result = 0
        if result == 1:
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
        mainexit_ = Button(mainframe_, text="X",command=self.master.quit, bg="red")
        mainexit_.pack(side=RIGHT, padx=5, pady=5)
        mainlink_ = Button(mainframe_, text="Link",command=self.link_,bg="orange")
        mainlink_.pack(side=RIGHT, padx = 1, pady = 5)
        creategate_ = Button(mainframe_, text="Create",command=self.create_gate_window_,bg="orange")
        creategate_.pack(side=LEFT, padx=5,pady=5)

    def create_gate_window_(self):
        createwindow = Toplevel(app)
        mainframe_ = Frame(createwindow, bg = "gray")
        mainexit_ = Button(mainframe_, text="Cancel", command = createwindow.destroy, bg = "orange")
        maincreate_ = Button(mainframe_, text="Create",command= lambda:[self.create_gate(), createwindow.destroy()] , bg="orange")
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

    def error_wrapper_(self, window_title, error_message):
        error_window = Toplevel(app)
        error_window.title(window_title)
        error_window.geometry("400x100")
        message = Label(error_window, text=error_message).pack(padx=10, pady=10)

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
            self.error_wrapper_("Error", "The NOT gate can only accept one input.")
            return

        if type_of_gate_var.get() != "NOT" and number_of_inputs_var.get()==1:
            self.error_wrapper_("Error", "The {} gate accepts at least 2 inputs.".format(type_of_gate_var.get()))
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
            two_[row-1][0] = chr(self.name_count)
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

    def link_(self):
        linkwindow_ = Toplevel(app)
        linkwindow_.title("Link")
        mainframe_ = Frame(linkwindow_, bg="gray")
        link_button_ = Button(mainframe_, text="Link", bg="orange", command=self.process).pack(side=LEFT, padx= 5, pady=5)
        mainframe_.pack(side=TOP, fill="both")
        for gate in one_:
            if len(gate[0]) == 0:
                continue
            entry_frame_ = Frame(linkwindow_)
            entry_info_ = Button(entry_frame_, text="{}-gate id=[{}]\n[Inputs={}]".format(gate[1], gate[0], gate[2]), bg="orange").pack()
            entry_entry_ = Entry(entry_frame_)
            entry_entry_.pack()
            current_entry_and_info_ = []
            current_entry_and_info_.append(entry_entry_)
            current_entry_and_info_.append(gate)
            entries.append(current_entry_and_info_)
            entry_frame_.place(x=250, y=gate[3]*200)

        for gate in two_:
            if len(gate[0]) == 0:
                continue
            entry_frame_ = Frame(linkwindow_)
            entry_info_ = Button(entry_frame_, text="{}-gate id=[{}]\n[Inputs={}]".format(gate[1], gate[0], gate[2]), bg="orange").pack()
            entry_entry_ = Entry(entry_frame_)
            entry_entry_.pack()
            current_entry_and_info_ = []
            current_entry_and_info_.append(entry_entry_)
            current_entry_and_info_.append(gate)
            entries.append(current_entry_and_info_)
            entry_frame_.place(x=700, y=gate[3]*200)

        for gate in three_:
            if len(gate[0]) == 0:
                continue
            entry_frame_ = Frame(linkwindow_)
            entry_info_ = Button(entry_frame_, text="{}-gate id=[{}]\n[Inputs={}]".format(gate[1], gate[0], gate[2]), bg="orange").pack()
            entry_entry_ = Entry(entry_frame_)
            entry_entry_.pack()
            current_entry_and_info_ = []
            current_entry_and_info_.append(entry_entry_)
            current_entry_and_info_.append(gate)
            entries.append(current_entry_and_info_)
            entry_frame_.place(x=1150, y=gate[3]*200)

        for gate in four_:
            if len(gate[0]) == 0:
                continue
            entry_frame_ = Frame(linkwindow_)
            entry_info_ = Button(entry_frame_, text="{}-gate id=[{}]\n[Inputs={}]".format(gate[1], gate[0], gate[2]), bg="orange").pack()
            entry_entry_ = Entry(entry_frame_)
            entry_entry_.pack()
            current_entry_and_info_ = []
            current_entry_and_info_.append(entry_entry_)
            current_entry_and_info_.append(gate)
            entries.append(current_entry_and_info_)
            entry_frame_.place(x=1600, y=gate[3]*200)
    
    def process(self):
        for entryy in entries:
            self.gate_result_(entryy[1][1], str(entryy[0].get()), entryy[1][0], entryy[1][3], entryy[1][4])

    def valid(self, bitts):
        for bitt in bitts:
            if int(bitt) != 48 and int(bitt) != 49 and int(bitt) < self.name_count and int(bitt) >= 65:
                return False
        return True

    def same_row_(self, idd1, idd2):
        col1 = 0
        col2 = 0
        for gate in entries:
            if gate[1][0] == idd1:
                col1 = gate[4]
            if gate[1][0] == idd2:
                col2 = gate[4]
        if col1 == col2:
            return True
        return False

    def transform(self, bitts, idd, row, col):
        for i in range(len(bitts)):
            if ord(bitts[i])!=48 and ord(bitts[i])!=49:
                found = False
                for output in outputs:
                    if output[0] == bitts[i]:
                        if self.same_row_(bitts[i], idd):
                            self.error_wrapper_("Error", "You may be trying to use a gate of the same column or less as input to a gate of the same column or higher.")
                            return
                        found = True
                        bitts[i] = output[1]
                if found == False:
                    self.error_wrapper_("Error", "You may be trying to use a gate of the same column or less as input to a gate of the same column or higher.")
                    return
            else:
                bitts[i] = int(bitts[i])
        return bitts


    def gate_result_(self, type, inputs, idd, row, col):
        inputs = inputs.replace(" ","")
        inputs = list(str(inputs))
        if self.valid(inputs):
            inputs = self.transform(inputs, idd, row, col)
        else:
            self.error_wrapper_("Error", "Input in one of the gates is invalid.")
            return
        gate_result = []
        gate_result.append(idd)
        gate_result.append(OR_(type, inputs, idd))
        outputs.append(gate_result)

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