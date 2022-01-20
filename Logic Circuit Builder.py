from ast import Or
from cgitb import text
from os import link
from textwrap import fill
import tkinter as tk
from tkinter import *
from turtle import pos
from unicodedata import name

universal_icon = "D:\comsIII\orange.png"

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
    return NAND_(type, inputs)

def NAND_(type, inputs):
    if type == "NAND":
        result = inputs[0]
        for i in range(1, len(inputs)):
            if result == 1 and inputs[i] == 1:
                result = 1
            else:
                result = 0
        if result == 1:
            return 0
        return 1
    return XOR_(type, inputs)

def XOR_(type, inputs):
    if type == "XOR":
        result = inputs[0]
        for i in range(1, len(inputs)):
            if result != inputs[i]:
                result = 1
            else:
                result = 0
        return result
    return XNOR_(type, inputs)

def XNOR_(type, inputs):
    if type == "XNOR":
        result = inputs[0]
        for i in range(1, len(inputs)):
            if result == inputs[i]:
                result = 1
            else:
                result = 0
        return result
    return NOT_(type, inputs)
    
def NOT_(type, inputs):
    if type == "NOT":
        if inputs[0] == 1:
            return 0
        else:
            return 1

name_count = 65
outputs = []
entries = []
taken = []
packed_widgets = []
one_ = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
two_ = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
three_ = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
four_ = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
inputs = []
drawn_widgets = []
link_window_list = []
input_and_output_buttons = []
lines = []

def main_reset():
    for line in lines:
        canvas.delete(line)
        lines.pop()
    global name_count
    global outputs
    global entries 
    global taken
    global input_and_output_buttons
    global one_
    global two_
    global three_
    global four_
    global inputs
    name_count = 65
    outputs = []
    entries = []
    taken = []
    global packed_widgets
    for packed_widget in packed_widgets:
        packed_widget.destroy()
    packed_widgets = []
    input_and_output_buttons = []
    one_ = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
    two_ = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
    three_ = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
    four_ = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
    inputs = []

def sub_reset():
        global entries
        global outputs
        global inputs
        global link_window_list
        entries = []
        outputs = []
        inputs = []
        link_window_list = []

def undo():
        packed_widgets[-1].destroy()

def create_gate_window_():
        createwindow = Toplevel(app)
        createwindow.iconbitmap("D:\comsIII\orange.ico")
        mainframe_ = Frame(createwindow, bg = "gray")
        mainexit_ = Button(mainframe_, text="Cancel", command = createwindow.destroy, bg = "orange")
        maincreate_ = Button(mainframe_, text="Create",command= lambda:[create_gate(), createwindow.destroy()] , bg="orange")
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
        gate_options_ = ["OR", "AND", "NOT", "NAND", "NOR", "XOR", "XNOR"]
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

def error_wrapper_(window_title, error_message, width, height):
        global universal_icon
        error_window = Toplevel(app)
        error_window.title(window_title)
        error_window.geometry("{}x{}".format(width, height))
        message = Label(error_window, text=error_message).pack(padx=10, pady=10)
        error_window.iconphoto(True, PhotoImage(file=universal_icon))

def create_gate():
        row = rows_var.get()
        col = cols_var.get()
        global taken
        global name_count
        global one_ 
        global two_ 
        global three_ 
        global four_  
        for position in taken:
            if row == position[0] and col == position[1]:
                error_wrapper_("Error", "The position you have specified for this\ngate is already taken by another gate.", 300, 75)
                return

        if type_of_gate_var.get() == "NOT" and number_of_inputs_var.get()!=1:
            error_wrapper_("Error", "The NOT gate can only accept one input.", 250, 50)
            return

        if type_of_gate_var.get() != "NOT" and number_of_inputs_var.get()==1:
            error_wrapper_("Error", "The {} gate accepts at least 2 inputs.".format(type_of_gate_var.get()), 250, 50)
            return

        if col == 1:
            one_[row-1][4] = col
            one_[row-1][3] = row
            one_[row-1][2] = number_of_inputs_var.get()
            one_[row-1][1] = type_of_gate_var.get()
            one_[row-1][0] = chr(name_count)
            current_taken = [row ,col]
            taken.append(current_taken)
            current_gate = Button(app, text=type_of_gate_var.get()+"\n"+"[id={}]".format(chr(name_count)), width=4, height=10, bg="orange", pady=10)
            packed_widgets.append(current_gate)
            current_gate.place(x=250, y =(row-1)*200+150)
            name_count+=1
            return
            
        if col == 2:
            two_[row-1][4] = col
            two_[row-1][3] = row
            two_[row-1][2] = number_of_inputs_var.get()
            two_[row-1][1] = type_of_gate_var.get()
            two_[row-1][0] = chr(name_count)
            current_taken = [row ,col]
            taken.append(current_taken)
            current_gate = Button(app, text=type_of_gate_var.get()+"\n"+"[id={}]".format(chr(name_count)), bg="orange", width=4, height=10, pady=10)
            packed_widgets.append(current_gate)
            current_gate.place(x=700, y =(row-1)*200+150)
            name_count+=1
            return

        if col == 3:
            three_[row-1][4] = col
            three_[row-1][3] = row
            three_[row-1][2] = number_of_inputs_var.get()
            three_[row-1][1] = type_of_gate_var.get()
            three_[row-1][0] = chr(name_count)
            current_taken = [row ,col]
            taken.append(current_taken)
            current_gate = Button(app, text= type_of_gate_var.get()+"\n"+"[id={}]".format(chr(name_count)), bg="orange", width=4, height=10, pady=10)
            packed_widgets.append(current_gate)
            current_gate.place(x=1150, y =(row-1)*200+150)
            name_count+=1
            return
    
        if col == 4:
            four_[row-1][4] = col
            four_[row-1][3] = row
            four_[row-1][2] = number_of_inputs_var.get()
            four_[row-1][1] = type_of_gate_var.get()
            four_[row-1][0] = chr(name_count)
            current_taken = [row ,col]
            taken.append(current_taken)
            current_gate = Button(app, text= type_of_gate_var.get() + "\n" + "[id={}]".format(chr(name_count)), bg="orange", width=4, height=10, pady=10)
            packed_widgets.append(current_gate)
            current_gate.place(x=1600, y =(row-1)*200+150)
            name_count+=1
            return

def link_():
        global link_window_list
        global packed_widgets
        global taken
        global name_count
        global one_ 
        global two_ 
        global three_ 
        global four_ 
        global entries

        if len(packed_widgets) == 0:
            error_wrapper_("Error", "No gates to link.", 250, 50)
            return
        if len(link_window_list)!=0:
            return
        linkwindow_ = Toplevel(app)
        link_window_list.append(linkwindow_)
        linkwindow_.title("Link")
        linkwindow_.iconbitmap("D:\comsIII\orange.ico")
        linkwindow_.attributes("-fullscreen", True)
        mainframe_ = Frame(linkwindow_, bg="gray")
        link_button_ = Button(mainframe_, text="Link", bg="orange", command=lambda:[process(), display_results_()]).pack(side=LEFT, padx= 5, pady=5)
        mainexit_ = Button(mainframe_, text="X",command=linkwindow_.destroy , bg="red").pack(side=RIGHT, padx=5, pady=5)
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
    
def process():
        global outputs
        outputs = []
        stop_trigger = False
        for entryy in entries:
            inputs.append([entryy[1][0],str(entryy[0].get())])
            stop_trigger = gate_result_(entryy[1][1], str(entryy[0].get()), entryy[1][0], entryy[1][3], entryy[1][4])
            if stop_trigger == True:
                break
        return
        
def display_results_():
        global entries
        global outputs
        global packed_widgets
        global link_window_list
        if len(outputs) != len(entries):
            return
        for processed in outputs:
            current_frame = Frame(app)
            current_col = -1
            current_row = -1
            input_values = []
            for i in range(len(entries)):
                if processed[0] == entries[i][1][0]:
                    current_col = entries[i][1][4]
                    current_row = entries[i][1][3]
                    input_values = inputs[i][1]
                    
            for i in range(len(input_values)):
                current_button = Button(current_frame, text="{}".format(input_values[i]), bg="orange", height=1, width=6)
                current_button.pack(padx=1, pady=8)
            
            x_val = -1
            y_val = -1
            if current_col == 1:
                x_val = 150
            if current_col == 2:
                x_val = 600
            if current_col == 3:
                x_val = 1050
            if current_col == 4:
                x_val = 1500
            packed_widgets.append(current_frame)
            current_frame.place(x = x_val, y = (current_row-1)*200 + 150)
            current_button = Button(app, height = 1, width=6 ,bg="orange",text="{}".format(processed[1]))
            packed_widgets.append(current_button)
            current_button.place(x=x_val+200, y=(current_row-1)*200 + 225)
            link_window_list[0].destroy()

def valid_1(bitts):
        for bitt in bitts:
            if ord(bitt) != 48 and ord(bitt) != 49 and (ord(bitt) >= name_count or ord(bitt) < 65):
                return False
        return True

def valid_2(idd):
        global entries
        for entryy in entries:
            if entryy[1][0] == idd:
                if len(str(entryy[0].get())) == entryy[1][2]:
                    return True
        return False

def same_row_(idd1, idd2):
        col1 = 0
        col2 = 0
        global entries
        for gate in entries:
            if gate[1][0] == idd1:
                col1 = gate[1][4]
            if gate[1][0] == idd2:
                col2 = gate[1][4]
        if col1 == col2:
            return True
        return False

def transform(bitts, idd, row, col):
        global outputs 
        global inputs
        for i in range(len(bitts)):
            if ord(bitts[i])!=48 and ord(bitts[i])!=49:
                found = False
                for output in outputs:
                    if output[0] == bitts[i]:
                        if same_row_(bitts[i], idd):
                            error_wrapper_("Error", "You may be trying to use a gate of the same column or\nless as input to a gate of the same column or higher.", 300, 75)
                            inputs = []
                            outputs = []
                            return
                        found = True
                        bitts[i] = output[1]
                if found == False:
                    error_wrapper_("Error", "You may be trying to use a gate of the same column or\nless as input to a gate of the same column or higher.", 300, 75)
                    inputs = []
                    outputs = []
                    return
            else:
                bitts[i] = int(bitts[i])
        return bitts

def gate_result_(type, input_string, idd, row, col):
        global outputs
        global inputs
        input_string = input_string.replace(" ","")
        input_string = list(str(input_string))
        if not valid_2(idd):
            error_wrapper_("Error", "One of the gates has an incomplete number of inputs.", 320, 50)
            outputs = []
            inputs = []
            return True

        if valid_1(input_string):
            input_string = transform(input_string, idd, row, col)
        else:
            error_wrapper_("Error", "Input in one of the gates is invalid.", 250, 50)
            outputs = []
            inputs = []
            return True
        gate_result = []
        gate_result.append(idd)
        gate_result.append(OR_(type, input_string))
        outputs.append(gate_result)

def show():
        type_of_gate_var.set(type_of_gate_var.get())

coords = {"x":0,"y":0,"x2":0,"y2":0}

def click(e):
    # define start point for line
    coords["x"] = e.x
    coords["y"] = e.y


    lines.append(canvas.create_line(coords["x"],coords["y"],coords["x"],coords["y"]))

def drag(e):

    coords["x2"] = e.x
    coords["y2"] = e.y

    canvas.coords(lines[-1], coords["x"],coords["y"],coords["x2"],coords["y2"])

def undo_drawing():
    try:
        canvas.delete(lines[-1])
        lines.pop()
    except:
        return None
    

app = tk.Tk()

canvas = Canvas(app)
canvas.pack(fill="both", expand=True)

canvas.bind('<ButtonPress-1>', click)
canvas.bind('<B1-Motion>', drag)

mainframe_ = Frame(canvas, bg="gray")
mainframe_.pack(side=TOP, fill="both")
mainexit_ = Button(mainframe_, text="X",command=quit, bg="red")
mainexit_.pack(side=RIGHT, padx=5, pady=5)
mainlink_ = Button(mainframe_, text="Link",command=lambda:[sub_reset(), link_()],bg="orange")
mainlink_.pack(side=RIGHT, padx = 1, pady = 5)
mainreset_ = Button(mainframe_, text="Reset",command=main_reset,bg="orange")
mainreset_.pack(side=RIGHT, padx = 1, pady = 5)
creategate_ = Button(mainframe_, text="Create",command=create_gate_window_,bg="orange")
creategate_.pack(side=LEFT, padx=5,pady=5)
guide_button = Button(mainframe_, text="Guide", command=lambda:[error_wrapper_("Guide", "Author: Mulanga Sibeli.\n\nLogic-Circuit-Builder Guide:\n\nThe Create Gate button allows you to create a new gate.\n\nYou can specificy details about the gate you would like to create:\n\nRow: The Row your gate should be in. Range: (1-4).\nCol: The Column your gate should be in. Range: (1-4).\n\nType: The type of gate you would like to create.\n\nInputs: The number of inputs your gate should take.\n\nEach gate will be allocated a unique ID. These IDs will be uppercase letters.\n\nAfter creating your gates, you can now use the Link button which will open\na new window allowing you to specify inputs for each gate.\nEach gate will have a corresponding text box allowing you to type out your inputs.\n\nExamples of inputs:\n\nA11 (This means that the gate given this input will take 1 and 1 and gate A's output as input).\n\n01C (This means that the gate given this input will take 0 and 1 and gate C's output as input).\n\nAfter specifying the inputs, use the Done button which will\nnow take you back to the first window to display the resulting logic circuit.\n\nNote that you can remove everything on the screen\nand create a new circuit by using the Reset button.\n\nNote that if you wish to draw lines on your circuit,\nyou can click your mouse anywhere on the screen, drag\nit and click it again to end the line drawing.\nDrawing mistakes can be fixed by the Undo Drawing button.\n\nHAVE FUN!", 600, 750, 'D:\comsIII\orange.ico')] ,bg = "orange")
guide_button.pack(side=LEFT, padx=5, pady=5)
undo_drawing_button = Button(mainframe_, text="Undo Drawing", command=undo_drawing, bg="orange")
undo_drawing_button.pack(side=LEFT, padx=5, pady=5)
        
app.title("Gates")
app.iconbitmap("D:\comsIII\orange.ico")
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