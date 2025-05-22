from tkinter import *
from PIL import Image, ImageTk  # <-- import Pillow

def show_delection():
    selected = var.get()
    print("Your option is:", selected)

window = Tk()
window.title("Radiobutton Example")

# Load and resize images
original_image1 = Image.open('hamburger-emoji-2048x1780-gc068svc.png').resize((20, 20))
original_image2 = Image.open('steaming-bowl-emoji-498x512-z9jgkqxi.png').resize((20, 20))
original_image3 = Image.open('sandwich-emoji-2048x1807-66diz3iy.png').resize((20, 20))

# Convert to PhotoImage
burger_img = ImageTk.PhotoImage(original_image1)
noodles_img = ImageTk.PhotoImage(original_image2)
sandwich_img = ImageTk.PhotoImage(original_image3)

# Store references to avoid garbage collection
images = [burger_img, noodles_img, sandwich_img]

var = StringVar()

r1 = Radiobutton(window, text="Burger", variable=var, value="Burger",
                 command=show_delection, image=burger_img, compound="left")
r1.pack()

r2 = Radiobutton(window, text="Noodles", variable=var, value="Noodles",
                 command=show_delection, image=noodles_img, compound="left")
r2.pack()

r3 = Radiobutton(window, text="Sandwich", variable=var, value="Sandwich",
                 command=show_delection, image=sandwich_img, compound="left")
r3.pack()

window.mainloop()
