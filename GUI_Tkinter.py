from tkinter import *
from tkinter import messagebox

# Create the main application window
a = Tk()
a.title("College Admission Registration Form")
a.geometry("1280x720")

# Label and Entry for Name
n = Label(a, text="Enter student name:", bg="yellow", fg="red")
n.grid(row=0, column=0)

e1 = Entry(a)
e1.grid(row=0, column=1)

# Branch selection
b = Label(a, text="Select your branch:")
b.grid(row=1, column=0)

rb1=Radiobutton(a, text="Computer Science", value=1)
rb1.grid(row=1, column=1)
rb2=Radiobutton(a, text="Information Technology", value=2)
rb2.grid(row=1, column=2)

# Favourite game selection
b = Label(a, text="Select your favourite game:")
b.grid(row=2, column=0)

cb1=Checkbutton(a, text="Cricket")
cb1.grid(row=2, column=1)
cb2=Checkbutton(a, text="Football")
cb2.grid(row=2, column=2)
cb3=Checkbutton(a, text="Badminton")
cb3.grid(row=2, column=3)

# submit function
def submit():
    messagebox.showinfo("Submission", "Your form has been submitted successfully!") 

# Submit button
bu = Button(a, text="Submit", command=submit)
bu.grid(row=3, column=1)

# run the application
a.mainloop()