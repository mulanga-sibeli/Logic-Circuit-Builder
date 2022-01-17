from ast import Or
from cgitb import text
from os import link
from textwrap import fill
import tkinter as tk
from tkinter import *
from unicodedata import name

def OR_(type, inputs):
    if type == "OR":
        result = inputs[0]
        for i in range(1, len(inputs)):
            if result == 1 or inputs[i] == 1:
                result = 1
            else:
                result = 0
        return result
    else:
        return AND_(type, inputs)

def AND_(type, inputs):
    if type == "AND":
        result = inputs[0]
        for i in range(1, len(inputs)):
            if result == 1 and inputs[i] == 1:
                result = 1
            else:
                result = 0
        return result
    return NOR_(type, inputs)

def NOR_(type, inputs):
    if type == "NOR":
        result = inputs[0]
        for i in range(1, len(inputs)):
            if result == 1 or inputs[i] == 1:
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
        for i in range(1, len(inputs)):
            if result == 1 and inputs[i] == 1:
                result = 1
            else:
                result = 0
        if result == 1:
            return 0
        return 1

class Window(Frame):
    name_count = 65
    outputs = []
    entries = []
    taken = []
    buttons = []
    one_ = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
    two_ = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
    three_ = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
    four_ = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
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

    def error_wrapper_(self, window_title, error_message, width, height):
        error_window = Toplevel(app)
        error_window.title(window_title)
        error_window.geometry("{}x{}".format(width, height))
        message = Label(error_window, text=error_message).pack(padx=10, pady=10)

    def create_gate(self):
        row = rows_var.get()
        col = cols_var.get()
        if row + col in self.taken:
            self.error_wrapper_("Error", "The position you have specified for this\ngate is already taken by another gate.", 300, 75)
            return

        if type_of_gate_var.get() == "NOT" and number_of_inputs_var.get()!=1:
            self.error_wrapper_("Error", "The NOT gate can only accept one input.", 250, 50)
            return

        if type_of_gate_var.get() != "NOT" and number_of_inputs_var.get()==1:
            self.error_wrapper_("Error", "The {} gate accepts at least 2 inputs.".format(type_of_gate_var.get()), 250, 50)
            return

        if col == 1:
            self.one_[row-1][4] = col
            self.one_[row-1][3] = row
            self.one_[row-1][2] = number_of_inputs_var.get()
            self.one_[row-1][1] = type_of_gate_var.get()
            self.one_[row-1][0] = chr(self.name_count)
            self.taken.append(col+row)
            current_gate = Button(self.master, text=type_of_gate_var.get()+"\n"+"[id={}]".format(chr(self.name_count)), width=4, height=10, bg="orange").place(x=250, y=row*150)
            self.name_count+=1
            return
            
        if col == 2:
            self.two_[row-1][4] = col
            self.two_[row-1][3] = row
            self.two_[row-1][2] = number_of_inputs_var.get()
            self.two_[row-1][1] = type_of_gate_var.get()
            self.two_[row-1][0] = chr(self.name_count)
            self.taken.append(col+row)
            current_gate = Button(self.master, text=type_of_gate_var.get()+"\n"+"[id={}]".format(chr(self.name_count)), bg="orange", width=4, height=10).place(x=700, y=row*150 + 75)
            self.name_count+=1
            return

        if col == 3:
            self.three_[row-1][4] = col
            self.three_[row-1][3] = row
            self.three_[row-1][2] = number_of_inputs_var.get()
            self.three_[row-1][1] = type_of_gate_var.get()
            self.three_[row-1][0] = chr(self.name_count)
            self.taken.append(col+row)
            current_gate = Button(self.master, text= type_of_gate_var.get()+"\n"+"[id={}]".format(chr(self.name_count)), bg="orange", width=4, height=10).place(x=1150, y=row*150 + 75)
            self.name_count+=1
            return
    
        if col == 4:
            self.four_[row-1][4] = col
            self.four_[row-1][3] = row
            self.four_[row-1][2] = number_of_inputs_var.get()
            self.four_[row-1][1] = type_of_gate_var.get()
            self.four_[row-1][0] = chr(self.name_count)
            self.taken.append(col+row)
            current_gate = Button(self.master, text= type_of_gate_var.get() + "\n" + "[id={}]".format(chr(self.name_count)), bg="orange", width=4, height=10).place(x=1600, y=row*150 + 75)
            self.name_count+=1
            return

    def link_(self):
        self.entries = []
        self.outputs = []
        self.link_window_list = []
        link_window_list = []
        linkwindow_ = Toplevel(app)
        self.link_window_list.append(linkwindow_)
        linkwindow_.title("Link")
        linkwindow_.attributes("-fullscreen", True)
        mainframe_ = Frame(linkwindow_, bg="gray")
        link_button_ = Button(mainframe_, text="Link", bg="orange", command=lambda:[self.process(), self.display_results_()]).pack(side=LEFT, padx= 5, pady=5)
        mainexit_ = Button(mainframe_, text="X",command=linkwindow_.destroy , bg="red").pack(side=RIGHT, padx=5, pady=5)
        mainframe_.pack(side=TOP, fill="both")
        for gate in self.one_:
            if len(gate[0]) == 0:
                continue
            entry_frame_ = Frame(linkwindow_)
            entry_info_ = Button(entry_frame_, text="{}-gate id=[{}]\n[Inputs={}]".format(gate[1], gate[0], gate[2]), bg="orange").pack()
            entry_entry_ = Entry(entry_frame_)
            entry_entry_.pack()
            current_entry_and_info_ = []
            current_entry_and_info_.append(entry_entry_)
            current_entry_and_info_.append(gate)
            self.entries.append(current_entry_and_info_)
            entry_frame_.place(x=250, y=gate[3]*200)

        for gate in self.two_:
            if len(gate[0]) == 0:
                continue
            entry_frame_ = Frame(linkwindow_)
            entry_info_ = Button(entry_frame_, text="{}-gate id=[{}]\n[Inputs={}]".format(gate[1], gate[0], gate[2]), bg="orange").pack()
            entry_entry_ = Entry(entry_frame_)
            entry_entry_.pack()
            current_entry_and_info_ = []
            current_entry_and_info_.append(entry_entry_)
            current_entry_and_info_.append(gate)
            self.entries.append(current_entry_and_info_)
            entry_frame_.place(x=700, y=gate[3]*200)

        for gate in self.three_:
            if len(gate[0]) == 0:
                continue
            entry_frame_ = Frame(linkwindow_)
            entry_info_ = Button(entry_frame_, text="{}-gate id=[{}]\n[Inputs={}]".format(gate[1], gate[0], gate[2]), bg="orange").pack()
            entry_entry_ = Entry(entry_frame_)
            entry_entry_.pack()
            current_entry_and_info_ = []
            current_entry_and_info_.append(entry_entry_)
            current_entry_and_info_.append(gate)
            self.entries.append(current_entry_and_info_)
            entry_frame_.place(x=1150, y=gate[3]*200)

        for gate in self.four_:
            if len(gate[0]) == 0:
                continue
            entry_frame_ = Frame(linkwindow_)
            entry_info_ = Button(entry_frame_, text="{}-gate id=[{}]\n[Inputs={}]".format(gate[1], gate[0], gate[2]), bg="orange").pack()
            entry_entry_ = Entry(entry_frame_)
            entry_entry_.pack()
            current_entry_and_info_ = []
            current_entry_and_info_.append(entry_entry_)
            current_entry_and_info_.append(gate)
            self.entries.append(current_entry_and_info_)
            entry_frame_.place(x=1600, y=gate[3]*200)
    
    def process(self):
        self.outputs = []
        print(len(self.entries))
        for entryy in self.entries:
            self.gate_result_(entryy[1][1], str(entryy[0].get()), entryy[1][0], entryy[1][3], entryy[1][4])
        return
        
    def display_results_(self):
        if len(self.outputs) != len(self.entries):
            return
        for processed in self.outputs:
            current_processed = processed
            current_frame = Frame(self.master)
            current_col = -1
            current_row = -1
            number_of_inputs = -1
            input_values = []
            for gatee in self.entries:
                if current_processed[0] == gatee[1][0]:
                    current_col = gatee[1][4]
                    current_row = gatee[1][3]
                    number_of_inputs = len(str(gatee[0].get()))
                    input_values = list(str(gatee[0].get()))
            
            for i in range(len(input_values)):
                current_button = Button(current_frame, text="{}".format(input_values[i]), bg="orange", height=1, width=6)
                self.buttons.append(current_button)
                current_button.pack(padx=1, pady=8)
            
            x_val = -1
            if current_col == 1:
                x_val = 150
            if current_col == 2:
                x_val = 600
            if current_col == 3:
                x_val = 1050
            if current_col == 4:
                x_val = 1500
            if current_row == 1:
                y_val = 145 * current_row
            if current_row != 1:
                y_val = 145 * current_row + 75
            current_frame.place(x = x_val, y = y_val)
            current_button = Button(self.master, height = 1, width=6 ,bg="orange",text="{}".format(current_processed[1])).place(x=x_val+175, y = y_val+60)
            self.link_window_list[0].destroy()

    def valid_1(self, bitts):
        for bitt in bitts:
            if int(bitt) != 48 and int(bitt) != 49 and int(bitt) < self.name_count and int(bitt) >= 65:
                return False
        return True

    def valid_2(self, idd):
        for entryy in self.entries:
            if entryy[1][0] == idd:
                if len(str(entryy[0].get())) == entryy[1][2]:
                    return True
        return False

    def same_row_(self, idd1, idd2):
        col1 = 0
        col2 = 0
        for gate in self.entries:
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
                for output in self.outputs:
                    if output[0] == bitts[i]:
                        if self.same_row_(bitts[i], idd):
                            self.error_wrapper_("Error", "You may be trying to use a gate of the same column or less as input to a gate of the same column or higher.", 300, 75)
                            self.outputs = []
                            return
                        found = True
                        bitts[i] = output[1]
                if found == False:
                    self.error_wrapper_("Error", "You may be trying to use a gate of the same column or less as input to a gate of the same column or higher.", 300, 50)
                    self.outputs = []
                    return
            else:
                bitts[i] = int(bitts[i])
        return bitts

    def gate_result_(self, type, inputs, idd, row, col):
        inputs = inputs.replace(" ","")
        inputs = list(str(inputs))
        if not self.valid_2(idd):
            self.error_wrapper_("Error", "One of the gates has an incomplete number of inputs.", 250, 50)
            self.outputs = []
            return

        if self.valid_1(inputs):
            inputs = self.transform(inputs, idd, row, col)
        else:
            self.error_wrapper_("Error", "Input in one of the gates is invalid.", 250, 50)
            self.outputs = []
            return
        gate_result = []
        gate_result.append(idd)
        gate_result.append(OR_(type, inputs))
        self.outputs.append(gate_result)

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