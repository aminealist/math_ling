import tkinter
from tkinter import font
okn = tkinter.Tk()

def c_b0():
    otv["text"] = ""
    try:
        otv["text"] = str(int(ch1.get()) + int(ch2.get()))
        otv["bg"] = "mediumspringgreen"
    except:
        otv["bg"]="red"
        otv["text"]=("ошибка")
def c_b1():
    otv["text"] = ""
    try:
        otv["text"] = str(int(ch1.get()) - int(ch2.get()))
        otv["bg"] = "mediumspringgreen"
    except:
        otv["bg"]="red"
        otv["text"]=("ошибка")
def c_b2():
    otv["text"] = ""
    try:
        otv["text"] = str(int(ch1.get()) * int(ch2.get()))
        otv["bg"] = "mediumspringgreen"
    except:
        otv["bg"]="red"
        otv["text"]=("ошибка")
def c_b3():
    otv["text"] = ""
    try:
        otv["text"] = str(int(ch1.get()) / int(ch2.get()))
        otv["bg"] = "mediumspringgreen"
    except:
        otv["bg"]="red"
        otv["text"]=("ошибка")







sh = font.Font(size=20)
okn.geometry('300x444+111+111')
okn.title("what the dog doing")
okn ["bg"]=("light goldenrod")
ch1 = tkinter.Entry(okn, width=15, bd=0, bg="lightblue", justify='center')
ch1.place(x=30, y=50)
ch2 = tkinter.Entry(okn, width=15, bd=0, bg="lightblue", justify='center')
ch2.place(x=180, y=50)
b1 = tkinter.Button(okn, width=3, height=1, text="+", bg="pink2", command=c_b0)
b2 = tkinter.Button(okn, width=3, height=1, text="-", bg="pink2", command=c_b1)
b3 = tkinter.Button(okn, width=3, height=1, text="*", bg="pink2", command=c_b2)
b4 = tkinter.Button(okn, width=3, height=1, text="/", bg="pink2", command=c_b3)
otvp = tkinter.Label(okn, width=15, height=1, bd=0, justify="center", text="what the calc doing", bg="mediumspringgreen")
otvp["font"] = font.Font(size=11)
otvp.place(x=83, y=280)
otv = tkinter.Label(okn, width=15, height=1, bd=0, justify="center", text="", font=font.Font(size=11), bg="mediumspringgreen" )
otv.place(x=83, y=299)
b1["font"]=sh
b2["font"]=sh
b3["font"]=sh
b4["font"]=sh
b1.place(x=88, y=155)
b2.place(x=155, y=155)
b3.place(x=88, y=220)
b4.place(x=155, y=220)
okn.mainloop()

