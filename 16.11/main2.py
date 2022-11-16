import tkinter
from tkinter import font
okn = tkinter.Tk()

def c_b0():
    otv["text"] = ""
    otv["text"] = str(int(ch1.get()) + int(ch2.get()))
    otv["bg"] = "mediumspringgreen"

sh = font.Font(size=10)
okn.geometry('300x700+111+111')
okn.title("what the dog doing")
okn ["bg"]=("light goldenrod")
ch1 = tkinter.Text(okn, width=30, height=10, bd=0, bg="lightblue")
ch1.place(x=30, y=30)



b1 = tkinter.Button(okn, width=17, height=1, text="what the button doing", bg="pink2", command=c_b0, bd=0)
b1["font"]=sh
b1.place(x=77, y=234)




otvp = tkinter.Label(okn, width=30, height=2, bd=0, justify="center", text="what the ''what the button doing'' doing", bg="mediumspringgreen")
otvp["font"] = font.Font(size=9)
otvp.place(x=46, y=280)



otvp = tkinter.Text(okn, width=37, height=15, bd=0, bg="mediumspringgreen", state=["disabled"])
otvp["font"] = font.Font(size=9)
otvp.place(x=20, y=321)
okn.mainloop()

