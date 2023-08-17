from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

window = Tk()
window.title("WaterMark Adder")
window.geometry("300x250")
window.config(bg="#0f0f0f")

def original_file():
    global o_img
    f_types = [('Png Files', '*.png'),('Jpg Files','*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    o_img = Image.open(filename)
    o_img = ImageTk.PhotoImage(file=filename)
    return o_img

def watermark_file():
    global w_img
    f_types = [('Png Files', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    w_img = Image.open(filename)
    w_img = ImageTk.PhotoImage(file=filename)

def process(o_img,w_img):
    pass


l1 = Label(window,text="Input Your Image:",bg="#0f0f0f", fg="white").place(relx=0.5, rely=0.2, anchor=CENTER)
b1 = Button(window, text='Upload Main File',
   width=20, command = original_file, bg="#616161", fg="white").place(relx=0.5, rely=0.3, anchor=CENTER)



l2 = Label(window,text="Input Your WaterMark Image (PNG):", bg="#0f0f0f", fg="white").place(relx=0.5, rely=0.5, anchor=CENTER)
b2 = Button(window, text='Upload WaterMark File',
   width=20, command = watermark_file, bg="#616161", fg="white").place(relx=0.5, rely=0.6, anchor=CENTER)


b3 = Button(window,text="Process",width=15,bg="#57753f", fg="white", command=process).place(relx=0.5, rely=0.8, anchor=CENTER)








window.mainloop()