# from cProfile import label
# from msilib.schema import RadioButton
from tkinter import *
# from turtle import bgcolor, width
from tkinter import filedialog, Label, Button, Entry, StringVar
from tkinter.filedialog import askopenfilename

root = Tk()
root.configure(bg="light blue")
root.geometry("900x400")
root.title("Email Spam Detection ")
# root.configure(file="my_background.png")

file_path = ""


def select():
    global file_path
    file_path = askopenfilename(filetypes=[('csv Files', '*csv')])
    if file_path is not None:
        txt["text"] = "file is uploaded"
        print(file_path)
    return file_path


var1 = IntVar()
var2 = IntVar()

def fun():
    pass


labelframe = LabelFrame(root, text="claaification")
labelframe.grid(row=0, column=2, sticky='W', padx=5, pady=170, ipadx=100, ipady=65)

labelframe2 = LabelFrame(root, text="Validation")
labelframe2.grid(row=0, column=5, sticky='W', padx=5, pady=170, ipadx=100, ipady=65)

labelframe3 = LabelFrame(root, text="result")
labelframe3.grid(row=0, column=7, sticky='W', padx=5, pady=80, ipadx=230, ipady=150)

lab1 = Label(root, text="Email Spam Detection", font="280", bg="white", fg="black", width="150")
lab1.place(x=50, y=30, width=750, height=25)

lab2 = Button(root, text="Select DS ", font="250", bg="red", fg="white", width="10", command=select)
lab2.place(x=280, y=103, width=80, height=30)

txt = Label(root, text="enter the file", width="20", font="280", bg="white", fg="black", height="2")
txt.place(x=65, y=100)
txt.place(anchor=NW)

# lab3=Label(root,text=" - Classification",fg="black" ,font="200" , width="15")
# lab3.place(x=0 , y=200)


rdbtn1 = Radiobutton(labelframe, text="KNN", variable=var1, value=1)
rdbtn1.place(x=0, y=0)

rdbtn2 = Radiobutton(labelframe, text="Decision Tree", variable=var1, value=2)
rdbtn2.place(x=0, y=40)

rdbtn3 = Radiobutton(labelframe, text="Naive Bayes", variable=var1, value=3)
rdbtn3.place(x=0, y=80)

# lab4=Label(root,text=" - Validation",bg="white",fg="black")
# lab4.place(x=0 , y=350)

rdbtn4 = Radiobutton(labelframe2, text="Confusion Matrix", variable=var2, value=1)
rdbtn4.place(x=0, y=0)

img = PhotoImage(file="")

rdbtn5 = Radiobutton(labelframe2, text="Accuracy", variable=var2, value=2)
rdbtn5.place(x=0, y=40)

butn = Button(root, text="run", font="240", bg="red", fg="black", command=fun)
butn.place(x=70, y=320, width=120, height=30)

butn2 = Button(root, text="exit", font="240", bg="red", fg="black")
butn2.place(x=210, y=320, width=120, height=30)

root.mainloop()
