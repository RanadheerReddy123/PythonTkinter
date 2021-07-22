from tkinter import *
mw = Tk()
mw.iconbitmap('images/icon.ico')
mw.title('RR-Web Developers')
def say_hello():
    name = userinput.get()
    greeting = 'Hello '+name+'!'
    if name!= '':
        text.config(text=greeting)
        userinput.delete(0, END)
    else:
        text.config(text = "Enter your name! ")
userinput = Entry(mw, width=20, font=('Arial', 18))
userinput.pack(padx = 10, pady = 10)
text = Label(mw, text='Say Hello!', font=('Arial', 14))
text.pack(pady=5)
btn = Button(mw,  text='Say Hello!', font=('Arial', 12), command=say_hello)
btn.pack(pady=20)
mw.mainloop()

