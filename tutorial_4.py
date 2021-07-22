from tkinter import *
mw = Tk()
mylabel1 = Label(mw, text = "Telugu Computer World", font = ('Arial', 20), fg = 'red')
mylabel2 = Label(mw, text = "Ranadheer Reddy", font = ('Arial', 20), fg = 'green')
mybtn = Button(mw, text = "Submit", font = ('Arial', 20), bg = '#ffae2c')
mylabel1.grid(row = 0,column = 0, padx = 20, pady = 20)
mylabel2.grid(row = 1,column = 1, padx = 20, pady = 20)
mybtn.grid(row = 2,column = 1, padx = 20, pady = 20)
mw.mainloop()