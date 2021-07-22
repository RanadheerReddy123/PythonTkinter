from tkinter import *
from tkinter import messagebox
mw = Tk()
mw.title('Message Boxes')
mw.iconbitmap('icon.ico')
mw.geometry('400x300')
def show_msg():
    #messagebox.showinfo('RR-Web Developers', 'RR-Web Developers')
    #messagebox.showwarning('RR-Web Developers', 'RR-Web Developers')
    #res = messagebox.showerror('RR-Web Developers', 'RR-Web Developers')
    #res = messagebox.askyesno('RR-Web Developers', 'RR-Web Developers')
    res = messagebox.askquestion('RR-Web Developers', 'Do you want to save this file?')
    #res = messagebox.askokcancel('RR-Web Developers', 'RR-Web Developers')
    if res == 'yes':
        Label(mw, text='File has been saved!', font=('', 16)).pack(pady=(20, 0))
    else:
        messagebox.showwarning('RR-Web Developers', 'Your file is trashed!')
Button(mw, text='Show Message!', font=('',16), command=show_msg).pack(pady=(50,0))
mw.mainloop()