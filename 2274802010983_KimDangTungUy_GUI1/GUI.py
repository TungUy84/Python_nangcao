import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import *

win = tk.Tk()
win.title("Máy Tính")
win.iconbitmap("D:/NAM3_HK1/Python Nâng Cao/Ly_Thuyet/Do_An_1_GUI/calculator.ico")
##win.geometry("400x300")
win.resizable(False,False)

menu_bar = Menu(win)
win.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)   
file_menu.add_command(label="New")                
menu_bar.add_cascade(label="File", menu=file_menu)  
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)

def _msgBox():
    answer = msg.askyesnocancel("Python Message Multi Choice Box", "Are you sure you really wish to do this?")
    print (answer)

help_menu = Menu(menu_bar, tearoff=0)                             
menu_bar.add_cascade(label="Help", menu=help_menu)             
help_menu.add_command(label="About", command= _msgBox)

tabControl = ttk.Notebook(win)
#May tinh bassic
tab1 = tk.Frame(tabControl,)
tabControl.add(tab1, text="   Bassic   ")
tabControl.pack(expand=1, fill= "both")

frame_tt = tk.LabelFrame(tab1, text="Tính Toán")
frame_tt.grid(column=0, row=0, padx=16, pady= 10,)

a_lable = ttk.Label(frame_tt, text="a = ")
a_lable.grid(column=0, row=0, padx= 10)
a = tk.IntVar()
textbox_a = ttk.Entry(frame_tt, width=15, textvariable= a)
textbox_a.grid(column= 1, row= 0, )
textbox_a.delete(0, tk.END)

b_lable = ttk.Label(frame_tt, text="b = ")
b_lable.grid(column=0, row=1, padx= 10, pady= 5)
b = tk.IntVar()
textbox_b = ttk.Entry(frame_tt, width=15, textvariable= b)
textbox_b.grid(column= 1, row= 1, padx=3)
textbox_b.delete(0, tk.END)

cl2= tk.Label(frame_tt, width=10, )
cl2.grid(column=2, row=0)

def button_tong():
    try:
        tong = a.get() + b.get()
        expression = f"{a.get()} + {b.get()} = {tong}"
        kq_number.configure(state='normal')
        kq_number.delete(0, tk.END)
        kq_number.insert(0, str(tong))
        kq_number.config(state='readonly')
        add_to_history(expression)
    except:
        kq_number.configure(state='normal')
        kq_number.delete(0, tk.END)
        kq_number.insert(0, str("Sai số"))
        kq_number.config(state='readonly')
cong_button = ttk.Button(frame_tt, text=' + ', command= button_tong, width=8)
cong_button.grid(column=3, row=0, padx=5, pady=3)

def button_tru():
    try:
        tru = a.get() - b.get()
        kq_number.configure(state='normal')
        kq_number.delete(0, tk.END)
        kq_number.insert(0, str(tru))
        kq_number.config(state='readonly')
        expression = f"{a.get()} - {b.get()} = {tru}"
        add_to_history(expression)

    except:
        kq_number.configure(state='normal')
        kq_number.delete(0, tk.END)
        kq_number.insert(0, str("Sai số"))
        kq_number.config(state='readonly')
tru_button = ttk.Button(frame_tt, text=' - ', command= button_tru, width=8)
tru_button.grid(column=4, row=0, padx=5, pady=3)

def button_nhan():
    try:
        nhan = a.get() * b.get()
        kq_number.configure(state='normal')
        kq_number.delete(0, tk.END)
        kq_number.insert(0, str(nhan))
        kq_number.config(state='readonly')
        expression = f"{a.get()} x {b.get()} = {nhan}"
        add_to_history(expression)

    except:
        kq_number.configure(state='normal')
        kq_number.delete(0, tk.END)
        kq_number.insert(0, str("Sai số"))
        kq_number.config(state='readonly')
nhan_button = ttk.Button(frame_tt, text=' x ', command= button_nhan, width=8)
nhan_button.grid(column=3, row=1, padx=5, pady=3)

def button_chia():
    try:
        chia = a.get() / b.get()
        kq_number.configure(state='normal')
        kq_number.delete(0, tk.END)
        kq_number.insert(0, str(chia))
        kq_number.config(state='readonly')
        expression = f"{a.get()} / {b.get()} = {chia}"
        add_to_history(expression)

    except:
        kq_number.configure(state='normal')
        kq_number.delete(0, tk.END)
        kq_number.insert(0, str("Sai số"))
        kq_number.config(state='readonly')
chia_button = ttk.Button(frame_tt, text=' / ', command= button_chia, width=8)
chia_button.grid(column=4, row=1, padx=5, pady=3)

kq_label = ttk.Label(frame_tt, text='Kết quả: ')
kq_label.grid(column=0, row=4, pady=20 , columnspan=2)
kq_number = ttk.Entry(frame_tt, width=30, state='readonly')
kq_number.grid(column=1, row=4, columnspan=4)

def clearnumber():
    textbox_a.delete(0, tk.END)
    textbox_b.delete(0, tk.END) 
    kq_number.configure(state='normal') 
    kq_number.delete(0, tk.END)
    kq_number.configure(state='readonly') 

clear_button = ttk.Button(frame_tt, text='Clear', command=clearnumber)
clear_button.grid(column=3, row=4,columnspan=2 )

LS = ttk.Label(tab1, text="Lịch sử")
LS.grid(column=0, row=5, pady=3)

def add_to_history(expression):
    scr.insert(tk.END, expression + "\n")
    scr.yview(tk.END)

scrol_w  = 30
scrol_h  =  6
scr = scrolledtext.ScrolledText(tab1, width=scrol_w, height=scrol_h, wrap=tk.WORD, state = 'normal')
scr.grid(column=0, row=6, )             


#Chuyển đổi cơ số BIN & HEX
tab2 = tk.Frame(tabControl)
tabControl.add(tab2, text="   BIN   ")
tabControl.pack(expand=2, fill= "both")

frame_cd = tk.LabelFrame(tab2, text="  HEX > BIN  ")
frame_cd.grid(column=0, row=0, padx=36, pady= 15,)

input_HEX_lable = ttk.Label(frame_cd, text='HEX = ')
input_HEX_lable.grid(column=0, row=0, padx=10, pady=10)

PIN = tk.IntVar()
input_HEX_enter = ttk.Entry(frame_cd, width=40,textvariable=PIN)
input_HEX_enter.grid(column=1, row=0, padx= 5)
input_HEX_enter.delete(0, tk.END)
input_HEX_enter.focus()

def hex_pin():
    try:
        binary = ""  # Khởi tạo chuỗi binary
        value = PIN.get()  # Lấy giá trị từ IntVar 'a'

        while value > 0:
            binary = str(value % 2) + binary
            value //=2 

        output_PIN_enter.configure(state='normal')
        output_PIN_enter.delete(0, tk.END)
        output_PIN_enter.insert(0,binary)
        output_PIN_enter.configure(state='readonly')
    except:
        output_PIN_enter.configure(state='normal')
        output_PIN_enter.delete(0, tk.END)
        output_PIN_enter.insert(0, str("Vui lòng nhập đúng yêu cầu"))
        output_PIN_enter.configure(state='readonly')

HEX_button = ttk.Button(frame_cd, width=20, text= "Tính", command= hex_pin)
HEX_button.grid(column=0, row=1, columnspan= 2)

def clear_HEX():
    input_HEX_enter.delete(0, tk.END)
    output_PIN_enter.configure(state='normal') 
    output_PIN_enter.delete(0, tk.END)
    output_PIN_enter.configure(state='readonly') 

HEX_clear = ttk.Button(frame_cd, width=12, text="Clear", command= clear_HEX)
HEX_clear.grid(column=1, row=1, sticky='E')

output_PIN_lable = ttk.Label(frame_cd, text='PIN = ')
output_PIN_lable.grid(column=0, row=2, padx=10, pady=10)

output_PIN_enter = ttk.Entry(frame_cd, width=40, state="readonly")
output_PIN_enter.grid(column=1, row=2, padx= 5,)
frame_cd = tk.LabelFrame(tab2, text="  HEX > BIN  ")
frame_cd.grid(column=0, row=0, padx=36, pady= 15,)

input_HEX_lable = ttk.Label(frame_cd, text='HEX = ')
input_HEX_lable.grid(column=0, row=0, padx=10, pady=10)

PIN = tk.IntVar()
input_HEX_enter = ttk.Entry(frame_cd, width=40,textvariable=PIN)
input_HEX_enter.grid(column=1, row=0, padx= 5)
input_HEX_enter.delete(0, tk.END)
input_HEX_enter.focus()

def hex_pin():
    try:
        binary = ""  # Khởi tạo chuỗi binary
        value = PIN.get()  # Lấy giá trị từ IntVar 'a'

        while value > 0:
            binary = str(value % 2) + binary
            value //=2 

        output_PIN_enter.configure(state='normal')
        output_PIN_enter.delete(0, tk.END)
        output_PIN_enter.insert(0,binary)
        output_PIN_enter.configure(state='readonly')
    except:
        output_PIN_enter.configure(state='normal')
        output_PIN_enter.delete(0, tk.END)
        output_PIN_enter.insert(0, str("Vui lòng nhập đúng yêu cầu"))
        output_PIN_enter.configure(state='readonly')

HEX_button = ttk.Button(frame_cd, width=20, text= "Tính", command= hex_pin)
HEX_button.grid(column=0, row=1, columnspan= 2)

def clear_HEX():
    input_HEX_enter.delete(0, tk.END)
    output_PIN_enter.configure(state='normal') 
    output_PIN_enter.delete(0, tk.END)
    output_PIN_enter.configure(state='readonly') 

HEX_clear = ttk.Button(frame_cd, width=12, text="Clear", command= clear_HEX)
HEX_clear.grid(column=1, row=1, sticky='E')

output_PIN_lable = ttk.Label(frame_cd, text='PIN = ')
output_PIN_lable.grid(column=0, row=2, padx=10, pady=10)

output_PIN_enter = ttk.Entry(frame_cd, width=40, state="readonly")
output_PIN_enter.grid(column=1, row=2, padx= 5,)

######
frame_cd_H_P = tk.LabelFrame(tab2, text="  PIN > HEX  ")
frame_cd_H_P.grid(column=0, row=1, padx=36, pady= 15,)

input_PIN_lable = ttk.Label(frame_cd_H_P, text='PIN = ')
input_PIN_lable.grid(column=0, row=0, padx=10, pady=10)

HEX = tk.StringVar()
input_PIN_enter = ttk.Entry(frame_cd_H_P, width=40,textvariable=HEX)
input_PIN_enter.grid(column=1, row=0, padx= 5)
input_PIN_enter.delete(0, tk.END)
input_PIN_enter.focus()

def pin_hex():
    binary_str = HEX.get()
    try:
        demical = int(binary_str, 2)
        output_HEX_enter.configure(state='normal')
        output_HEX_enter.delete(0, tk.END)
        output_HEX_enter.insert(0, str(demical))  # Hiển thị kết quả
        output_HEX_enter.configure(state='readonly')
    except:
        output_HEX_enter.configure(state='normal')
        output_HEX_enter.delete(0, tk.END)
        output_HEX_enter.insert(0, str("Vui lòng nhập đúng yêu cầu"))
        output_HEX_enter.configure(state='readonly')

PIN_button = ttk.Button(frame_cd_H_P, width=20, text= "Tính", command= pin_hex)
PIN_button.grid(column=0, row=1, columnspan= 2)

def clear_pin():
    input_PIN_enter.delete(0, tk.END)
    output_HEX_enter.configure(state='normal') 
    output_HEX_enter.delete(0, tk.END)
    output_HEX_enter.configure(state='readonly') 

HEX_clear = ttk.Button(frame_cd_H_P, width=12, text="Clear", command= clear_pin)
HEX_clear.grid(column=1, row=1, sticky='E')

output_HEX_lable = ttk.Label(frame_cd_H_P, text='HEX = ')
output_HEX_lable.grid(column=0, row=2, padx=10, pady=10)

output_HEX_enter = ttk.Entry(frame_cd_H_P, width=40, state="readonly")
output_HEX_enter.grid(column=1, row=2, padx= 5,)

tabsetting = tk.Frame(tabControl)
tabControl.add(tabsetting, text="   Setting   ")
tabControl.pack(expand=3, fill= "both")

frame_setting_cl = tk.LabelFrame(tabsetting, text="  Color  ")
frame_setting_cl.grid(column=0, row=0,padx=55, pady=10)

colors = ["#f0f0f0", "#9b9b9b", "#6fffbe"]   
names = ["Light", "Dark", "Green"]

def radCall():
    radSel = radVar.get()
    if   radSel == 0: tabsetting.configure(bg=colors[0]), tab1.configure(bg=colors[0]), tab2.configure(bg=colors[0]), 
    elif radSel == 1:
        tabsetting.configure(bg=colors[1]), 
        tab1.configure(bg=colors[1]), 
        tab2.configure(bg=colors[1]),
        frame_setting_cl.configure(bg='#dadada'), 
        frame_tt.configure(bg='#dadada'), 
        frame_cd_H_P.configure(bg='#dadada'), 
        frame_cd.configure(bg='#dadada'), 
        cl2.configure(bg="#dadada")
    elif radSel == 2: 
        tabsetting.configure(bg=colors[2]), 
        tab1.configure(bg=colors[2]), 
        tab2.configure(bg=colors[2]),
        frame_setting_cl.configure(bg='#caffe7'), 
        frame_tt.configure(bg='#caffe7'), 
        frame_cd_H_P.configure(bg='#caffe7'), 
        frame_cd.configure(bg='#caffe7'), 
        cl2.configure(bg="#caffe7")

radVar = tk.IntVar()
radVar.set(0)                                 
 
for col in range(3):                             
    curRad = tk.Radiobutton(frame_setting_cl, text=names[col], variable=radVar, 
                            value=col, command=radCall)          
    curRad.grid(column=col, row=2, padx=20, pady=10)

frame_setting_check = tk.LabelFrame(tabsetting, text="  Check  ")
frame_setting_check.grid(column=0, row=3, pady=5)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(frame_setting_check, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)                   

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(frame_setting_check, text="No Input", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)                   

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(frame_setting_check, text="No Copy Answer", variable=chVarEn)
check3.deselect()
check3.grid(column=2, row=4, sticky=tk.W)       

def checkCallback(*ignoredArgs):
    # only enable one checkbutton
    if chVarUn.get(): 
        input_HEX_enter.configure(state='readonly')
        input_PIN_enter.configure(state='readonly')
        textbox_a.configure(state='readonly')
        textbox_b.configure(state='readonly')
    else:             
        input_HEX_enter.configure(state='normal')
        input_PIN_enter.configure(state='normal')
        textbox_a.configure(state='normal')
        textbox_b.configure(state='normal')

    if chVarEn.get(): 
        output_HEX_enter.configure(state='disabled')
        output_PIN_enter.configure(state='disabled')
        kq_number.configure(state='disabled')
    else:             
        output_HEX_enter.configure(state='readonly')
        output_PIN_enter.configure(state='readonly')
        kq_number.configure(state='readonly') 

# trace the state of the two checkbuttons
chVarUn.trace('w', lambda unused0, unused1, unused2 : checkCallback())    
chVarEn.trace('w', lambda unused0, unused1, unused2 : checkCallback())   

textbox_a.focus()
win.mainloop()