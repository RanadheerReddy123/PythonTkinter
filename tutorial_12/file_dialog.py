from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
mw = Tk()
mw.title('Main Window')
mw.iconbitmap('icons/Photo.ico')
mw.geometry('400x300')
img = ''
def open_file():
    global img
    filename = filedialog.askopenfilename(initialdir='images', title="Select a File", filetypes=(("PNG files","*.png"),("ALL files","*.*")))
    sw = Toplevel()
    sw.title('Image Window')
    sw.iconbitmap('icons/icon.ico')
    sw.geometry('1280x720')
    img = ImageTk.PhotoImage(Image.open(filename))
    img_lbl = Label(sw, image=img)
    img_lbl.pack(padx=10, pady=10)
btn = Button(mw, text="Open File", font=('',14), command=open_file)
btn.pack(pady=(60,0))
mw.mainloop()