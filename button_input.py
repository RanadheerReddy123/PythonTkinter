from tkinter import *
#Creating Window
main_window = Tk()

def clicked():
    mylabel = Label(main_window, text="Telugu Computer World", font=("Arial", 20), padx=30, pady=30)
    mylabel.pack(pady=10)
#Creating Input
user_input = Entry(main_window, width=20, font=("Arial", 18))
user_input.pack(pady=10)
#Creating Buttons
my_button = Button(main_window, text="Click Me!", font=("Arial", 12), padx=10, pady=10, command=clicked)
my_button.pack(padx=30, pady=30)
main_window.mainloop()
