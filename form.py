
import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

window = tkinter.Tk() 
#this creates the largest widget that the other widgets will sit inside of
window.title("Sign up")

frame = tkinter.Frame(window)
frame.pack()
#this creates a smaller box inside of the largest box

#saving user info
userInfoFrame = tkinter.LabelFrame(frame, text="User Info")
userInfoFrame.grid(row=0 , column=0, padx=20, pady=20)

#lables the text box for first name
firstNameLabel = tkinter.Label(userInfoFrame, text="First Name")
firstNameLabel.grid(row=0, column=0)
#and last name
lastNameLabel = tkinter.Label(userInfoFrame, text="Last Name")
lastNameLabel.grid(row=0, column=1)

#makes the text boxes for first and last name
firstNameEntry = tkinter.Entry(userInfoFrame)
lastNameEntry = tkinter.Entry(userInfoFrame)
firstNameEntry.grid(row=1, column=0)
lastNameEntry.grid(row=1, column=1)

titleLabel = tkinter.Label(userInfoFrame, text="title")
titleCombobox = ttk.Combobox(userInfoFrame, values=["Mr.","Mrs.","Miss.","Mx."])
titleLabel.grid(row=0, column=2)
titleCombobox.grid(row=1, column=2)


ageLabel =tkinter.Label(userInfoFrame, text="Age")
ageSpinbox = tkinter.Spinbox(userInfoFrame, from_= 18, to=110)
ageLabel.grid(row=2, column=0)
ageSpinbox.grid(row=3, column=0)

nationalityLabel = tkinter.Label(userInfoFrame, text= "nationality")
nationalityCombobox = ttk.Combobox(userInfoFrame, values=["Africa","Antartica","Asia","America (North)","America (South)","Europe","Oceania",])
nationalityLabel.grid(row=2, column=1)
nationalityCombobox.grid(row=3,column=1)



for widget in userInfoFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

##### 2nd label frame

##email
emailFrame = tkinter.LabelFrame(frame, text = "Email")
emailFrame.grid(row=1, column=0, )


def submit():
    email1 = email1_entry.get()
    email2 = email2_entry.get()

    if email1 == email2 and "@" in email1 and "." in email1 :
        frame2.tkraise()
    else:
        # Emails do not match or do not contain '@' sign
        messagebox.showerror("Error", "Emails do not match or are invalid- retype this")

root = tk.Tk()
root.geometry("400x300")

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nsew")

# Frame 1
tk.Label(frame1, text="Email one").pack()
email1_entry = tk.Entry(frame1)
email1_entry.pack()
email1_label = tk.Label(frame1, text="Enter your email here")
email1_label.pack()

tk.Label(frame1, text="Email two").pack()
email2_entry = tk.Entry(frame1)
email2_entry.pack()
email2_label = tk.Label(frame1, text="Enter your email here again")
email2_label.pack()

submit_button = tk.Button(frame1, text="Submit", command=submit, background="yellow", font=("Comic Sans MS", 12, "bold"))
submit_button.pack()

# Frame 2 (Empty frame for now, you can add content to it as needed)
tk.Label(frame2, text="Submission Successful!").pack()

frame1.tkraise()







window.mainloop()

