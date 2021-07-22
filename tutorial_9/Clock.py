from tkinter import *
from time import strftime
mw = Tk()
mw.title('Digital Clock')
mw.geometry('630x135')
mw.minsize(630,135)
mw.maxsize(630,135)
mw.config(bg = 'black')
def good_time():
    cur_time = strftime('%I:%M:%S %p')
    clock_label.config(text=cur_time)
    clock_label.after(1000, good_time)
clock_label = Label(mw, text="Digital Clock", font=('Arial', 80), bg = 'black', fg = '#03fc3d', padx=5, pady=5)
clock_label.pack()
good_time()
mw.mainloop()