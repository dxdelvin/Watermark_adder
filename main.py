import time
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("WaterMark Adder")
window.geometry("300x250")
window.config(bg="#0f0f0f")
window.resizable('False','False')

o_img = None
w_img = None


def original_file():
    global o_img
    f_types = [('Png Files', '*.png'),('Jpg Files','*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    o_img = Image.open(filename).convert("RGBA")
    # o_img = ImageTk.PhotoImage(file=filename)

def watermark_file():
    global w_img
    f_types = [('Png Files', '*.png'),('Jpg Files','*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    w_img = Image.open(filename).convert("RGBA")
    # w_img = ImageTk.PhotoImage(file=filename)

def process():
    global o_img
    global w_img
    warning = Label(window, text="PLEASE PUT SOME IMAGES", bg="#0f0f0f", fg="red")
    if o_img and w_img:
        x, y = o_img.size
        w_img = w_img.resize((x,y))
        o_img.putalpha(225)
        w_img.putalpha(45)
        img3 = Image.alpha_composite(o_img, w_img)
        img3.show()
    else:
        messagebox.showwarning(title="WARNING!",message="You need to add Images to Process")


l1 = Label(window,text="Input Your Image:",bg="#0f0f0f", fg="white").place(relx=0.5, rely=0.2, anchor=CENTER)
b1 = Button(window, text='Upload Main File',
   width=20, command = original_file, bg="#616161", fg="white").place(relx=0.5, rely=0.3, anchor=CENTER)



l2 = Label(window,text="Input Your WaterMark Image (PNG):", bg="#0f0f0f", fg="white").place(relx=0.5, rely=0.5, anchor=CENTER)
b2 = Button(window, text='Upload WaterMark File',
   width=20, command = watermark_file, bg="#616161", fg="white").place(relx=0.5, rely=0.6, anchor=CENTER)


b3 = Button(window,text="Process",width=15,bg="#57753f", fg="white", command=process).place(relx=0.5, rely=0.8, anchor=CENTER)








window.mainloop()