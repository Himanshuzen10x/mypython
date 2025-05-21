from tkinter import *
from PIL import Image, ImageTk  # <-- import Pillow

def display():
    if x.get() == 1:
        print("You agree!")
    else:
        print("You don't agree!")

window = Tk()

x = IntVar()

# Load original image using PIL
original_image = Image.open('Python-logo-notext.png')

# Resize the image (width=40, height=40 for example)
resized_image = original_image.resize((40, 40))  # <-- size set karo

# Convert PIL image to Tkinter-compatible image
python_photo = ImageTk.PhotoImage(resized_image)

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           fg="#00FF00",
                           bg="black",
                           activebackground="#00FF00",
                           padx=25,
                           pady=10,
                           image=python_photo,
                           compound='left')

# Keep reference to the image
# check_button.image = python_photo

check_button.pack()
window.mainloop()
