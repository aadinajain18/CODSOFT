from tkinter import *
import random, string

root = Tk()
root.geometry("500x350")
root.title("Password Generator")
root.config(bg="#f0f0f0")

label_font = ("Helvetica", 12)
button_font = ("Helvetica", 10, "bold")

def passgen():
    poor = string.ascii_uppercase + string.ascii_lowercase
    average = string.ascii_uppercase + string.ascii_lowercase + string.digits
    symbols = """'!@#$%^&*()_-+={}[]|\:;<>,.?/"""
    advanced = poor + string.digits + symbols

    if choice.get() == 1:
        return ''.join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return ''.join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return ''.join(random.sample(advanced, val.get()))

def callback():
    password = passgen() 
    result_label.config(text=password) 
top_frame = Frame(root, bg="#f0f0f0", pady=20)
top_frame.pack(fill="both")

middle_frame = Frame(root, bg="#f0f0f0", pady=10)
middle_frame.pack(fill="both")

bottom_frame = Frame(root, bg="#f0f0f0", pady=10)
bottom_frame.pack(fill="both")
title = Label(top_frame, text="Select Password Strength", font=label_font, bg="#f0f0f0")
title.pack()
choice = IntVar()
choice.set(1)  

R1 = Radiobutton(middle_frame, text="POOR", variable=choice, value=1, font=label_font, bg="#f0f0f0")
R1.pack(anchor=W, padx=20)
R2 = Radiobutton(middle_frame, text="AVERAGE", variable=choice, value=2, font=label_font, bg="#f0f0f0")
R2.pack(anchor=W, padx=20)
R3 = Radiobutton(middle_frame, text="ADVANCED", variable=choice, value=3, font=label_font, bg="#f0f0f0")
R3.pack(anchor=W, padx=20)
lenlabel = Label(middle_frame, text="Select Password Length:", font=label_font, bg="#f0f0f0")
lenlabel.pack(pady=10)
val = IntVar()
val.set(8)
spinlength = Spinbox(middle_frame, from_=8, to_=24, textvariable=val, width=5, font=label_font)
spinlength.pack(pady=5)

passgenButton = Button(bottom_frame, text="Generate Password", font=button_font, command=callback, bd=5, bg="#4CAF50", fg="white", padx=20, pady=10)
passgenButton.pack(pady=10)

result_label = Label(bottom_frame, text="", font=("Helvetica", 14), bg="#f0f0f0", fg="blue")
result_label.pack(pady=10)
root.mainloop()
