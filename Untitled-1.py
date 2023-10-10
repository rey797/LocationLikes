
import tkinter as tk
from tkinter import messagebox


def submit():
    email1 = email1_entry.get()
    email2 = email2_entry.get()

    if email1 == email2 and "@" in email1:
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
