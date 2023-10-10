from tkinter import *

root = Tk()

e = Entry(root)
e.pack()
e.get()
# this creates an input box 
def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text= hello)
    myLabel.pack() 

mybutton = Button(root, text="Enter your name:", padx=50, pady=25, command=myClick)
mybutton.pack()

root.mainloop()