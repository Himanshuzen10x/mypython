from tkinter import *
from PIL import Image, ImageTk

food = ["Burger" , "Hotdog" , "Momos"]

window = Tk()

img1 = Image.open("hamburger-emoji-2048x1780-gc068svc.png").resize((30, 30))
img2 = Image.open("pngtree-hot-dog-grill-with-mustard-isolated-png-image_9080663.png").resize((30, 30))
img3 = Image.open("s11728_momo_isolated_on_white_background_-stylize_200_-v_6_9b0110b7-19f8-499b-bcad-c1c6bcc0b770_1-photoroom-png-photoroom_11zon.png").resize((30, 30))

# Convert PIL images to Tkinter-compatible PhotoImage
burgerimage = ImageTk.PhotoImage(img1)
hotdogimage = ImageTk.PhotoImage(img2)
momosimage = ImageTk.PhotoImage(img3)

foodimage = [burgerimage, hotdogimage, momosimage]  

x = IntVar()
for index in range(len(food)):
    Radiobbutton = Radiobutton(
        window, text=food[index], variable=x, value= index
        ,padx=25
        ,font=("Impact" , 50),
        image= foodimage[index],
        command="left"
        )
    Radiobbutton.pack(anchor=W)

window.mainloop()