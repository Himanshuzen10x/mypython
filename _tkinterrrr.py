import tkinter as tk

root = tk.Tk()
root.title("Himanshu's GUI")
root.geometry("300x200")

label = tk.Label(root, text="Hello Himanshu!", font=("Arial", 16))
label.pack()

root.mainloop()
