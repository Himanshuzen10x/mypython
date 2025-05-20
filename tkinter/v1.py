import tkinter as tk
from tkinter import messagebox
#***********************
def greet():
    print("Mario Is Game Character!")

def show_name():
    yourname = entry.get()  # ✅ Get text from input box
    label_output.config(text=f"Hello, {yourname}!") 
    
def warning():
    messagebox.showinfo("Warning", "Name Should be in Capital Letter")
    
def confirm_exit():
    response = messagebox.askyesno("Exit", "are you sure want to exit")
    if response:
        root.destroy()
#***********************

root = tk.Tk()

root.geometry("500x700")
root.title("tkinter project")
#text inside tkinter
label = tk.Label(root, text="Hello I am MARIO" , font=("Arial", 12))
label.pack()
#photo
photo = tk.PhotoImage(file="tkinter/image.png")
photo = photo.subsample(7,7)
label2 = tk.Label(root, image=photo)
label2.pack()

#button
# btn = tk.Button(root, text="Greet Me", font=("Arial", 14), command=greet)
# btn.pack()
btn = tk.Button(root, text="Who is This?", font=("Arial", 14) , command=greet)
btn.pack()

lable3 = tk.Label(root, text="What is Your Name")
lable3.pack()

#messagebox

btn3 = tk.Button(root, text="Warning! Click Here", font=("Arial", 8), command=warning)
btn3.pack()

#entry

entry = tk.Entry(root,)
entry.pack()

btn2 = tk.Button(root, text="Submit", font=("Arial", 12), command=show_name)
btn2.pack(pady=10)

label_output = tk.Label(root, text="", font=("Arial", 14), fg="green")
label_output.pack(pady=3)

#exit
btn4 = tk.Button(root, text="Exit Here", command=confirm_exit)
btn4.pack()

root.mainloop()