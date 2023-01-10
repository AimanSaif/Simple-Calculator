import tkinter as tk
from tkinter import * 
field_text=""

def display(user_input):
    global field_text
    field_text=field_text+str(user_input)
    field.delete("1.0", "end")
    field.insert("1.0", field_text)

def calculate():
    global field_text
    result=str(eval(field_text))
    field.delete("1.0", "end")
    field.insert("1.0", result)

def clear():
    global field_text
    field_text=""
    field.delete("1.0", "end")
    field.insert("1.0", field_text)

window=tk.Tk()
window.geometry("300x300")
field=tk.Text(window,height=2,width=21,font=("Times New Roman",20))
firld.grid(row=1,column=1,columnspan=4)
window.mainloop() #we want to show window at all times

# Number Buttons

btn_1=tk.Button(window,text="1",command=lamda: add_to_field(1),width=5,font=("Times New Roman",14))
btn_1.grid(row=5,column=1)

btn_2=tk.Button(window,text="2",command=lamda: add_to_field(2),width=5,font=("Times New Roman",14))
btn_2.grid(row=5,column=2)

btn_3=tk.Button(window,text="3",command=lamda: add_to_field(3),width=5,font=("Times New Roman",14))
btn_3.grid(row=5,column=3)

btn_4=tk.Button(window,text="4",command=lamda: add_to_field(4),width=5,font=("Times New Roman",14))
btn_4.grid(row=4,column=1)

btn_5=tk.Button(window,text="5",command=lamda: add_to_field(5),width=5,font=("Times New Roman",14))
btn_5.grid(row=4,column=2)

btn_6=tk.Button(window,text="6",command=lamda: add_to_field(6),width=5,font=("Times New Roman",14))
btn_6.grid(row=4,column=3)

btn_7=tk.Button(window,text="7",command=lamda: add_to_field(7),width=5,font=("Times New Roman",14))
btn_7.grid(row=3,column=1)

btn_8=tk.Button(window,text="8",command=lamda: add_to_field(8),width=5,font=("Times New Roman",14))
btn_8.grid(row=3,column=2)

btn_9=tk.Button(window,text="9",command=lamda: add_to_field(9),width=5,font=("Times New Roman",14))
btn_9.grid(row=3,column=3)

btn_0=tk.Button(window,text="0",command=lamda: add_to_field(0),width=5,font=("Times New Roman",14))
btn_0.grid(row=6,column=1)

# Operation Buttons

btn_add=tk.Button(window,text="+",command=lamda: add_to_field("+"),width=5,font=("Times New Roman",14))
btn_add.grid(row=5,column=4)

btn_sub=tk.Button(window,text="-",command=lamda: add_to_field("-"),width=5,font=("Times New Roman",14))
btn_sub.grid(row=4,column=4)

btn_mult=tk.Button(window,text="*",command=lamda: add_to_field("*"),width=5,font=("Times New Roman",14))
btn_mult.grid(row=3,column=4)

btn_div=tk.Button(window,text="/",command=lamda: add_to_field("/"),width=5,font=("Times New Roman",14))
btn_div.grid(row=2,column=4)

btn_dec=tk.Button(window,text=".",command=lamda: add_to_field("."),width=5,font=("Times New Roman",14))
btn_dec.grid(row=6,column=2)

btn_equal=tk.Button(window,text="=",command=lamda: calculate(),width=13,font=("Times New Roman",14))
btn_equal.grid(row=6,column=3,columnspan=2)

btn_clear=tk.Button(window,text="clear",command=lamda: clear(),width=5,font=("Times New Roman",14))
btn_clear.grid(row=2,column=1)

btn_openbraket=tk.Button(window,text="(",command=lamda: add_to_field("("),width=5,font=("Times New Roman",14))
btn_div.grid(row=2,column=2)

btn_closedbracket=tk.Button(window,text=")",command=lamda: add_to_field(")"),width=5,font=("Times New Roman",14))
btn_div.grid(row=2,column=3)
