from tkinter import *
from PIL import Image, ImageTk
mw = Tk()
mw.title('Main Windoow')
mw.iconbitmap('images/Photo.ico')
mw.geometry('400x300')
img = ''
def open_window():
    global img
    second_window = Toplevel()
    second_window.title('Second Window')
    second_window.iconbitmap('images/icon.ico')
    img = ImageTk.PhotoImage(Image.open('images/lamb.jpg'))
    img_label = Label(second_window, image=img)
    img_label.pack(padx=10, pady=10)
    exit_btn = Button(second_window, text="Exit Window", font=('',16), command=second_window.destroy)
    exit_btn.pack(padx=20, pady=20)
ow_btn = Button(mw, text="Open Window", font=('',16), command=open_window)
ow_btn.pack(pady=(60,0))
mw.mainloop()