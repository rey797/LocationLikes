from tkinter import *


root = Tk()
#imports tkinter so you can use its properties

##makes a button
#pad x makes the x axis of the button bigger and pad y makes the y axis bigger
#def defines the function in this case is myClick 

def myClick():
    myLabel = Label(root, text="Welcome to Location Likes! lets get you started!")
    myLabel.pack() 

# then command is used to call the function, usually when doing this you would put () #
# after but if you did this in this case it would automatically click the button and the #
# button wouldnt do anything when the user clicks it #

mybutton = Button(root, text="Sign Up", padx=50, pady=25, command=myClick)
mybutton.pack()



root.mainloop()