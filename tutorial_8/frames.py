from tkinter import *
mw = Tk()
mw.title('RR-Web Developers')
mw.geometry('900x720')
#Creating Frames
frame1 = LabelFrame(mw, text='This is frame1', padx=10, pady=10, font=('', 14))
frame1.grid(row=0, column=0, padx=20, pady=10)
exit_btn = Button(frame1, text="Exit!", padx=30, pady=12, font=('',14))
exit_btn.pack()
#Creating Radio Buttons
def rv_res():
    rv_lbl.config(text=rv.get())
rv = StringVar()
rv.set('Chicken Biryani')
Radiobutton(frame1, text='Option 1', value='Chicken Biryani', variable = rv, font=('',14),command=rv_res).pack(pady=(30,10))
Radiobutton(frame1, text='Option 2', value='Mutton Biryani', variable = rv, font=('',14),command=rv_res).pack(pady=(0,20))
rv_lbl = Label(frame1, text=rv.get(), font=('',14))
rv_lbl.pack()
#Creating Check Buttons/Boxes
def cv_res():
    cv_lbl.config(text=cv.get())
cv = StringVar()
cb = Checkbutton(frame1, text="Do you want Parcel?", variable=cv, font=('',14), onvalue='Yes', offvalue='No', command=cv_res)
cb.deselect()
cb.pack(pady=(30,10))
cv_lbl = Label(frame1, text=cv.get(), font=('',14))
cv_lbl.pack(pady=(0,30))
#DropDown menu
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
selected = StringVar()
selected.set('March')
opts = OptionMenu(frame1, selected, *months)
opts.config(font=('',14))
opts.pack(pady=(0,30))
opts_menu = frame1.nametowidget(opts.menuname)
opts_menu.config(font=('',12))
#Creating Sliders
def box_ver(num_v):
    box_lbl.config(pady=num_v)
def box_hor(num_h):
    box_lbl.config(padx=num_h)
#Creating Frame2
frame2 = LabelFrame(mw, text='This is frame2', width=300, padx=10, pady=10, font=('', 14))
frame2.grid(row=0, column=1, padx=20, pady=10)

ver = Scale(frame2, from_=0, to=200, command=box_ver)
ver.grid(row=0, column=0, pady=(0,20))

hor = Scale(frame2, from_=0, to=200, orient=HORIZONTAL, command=box_hor)
hor.grid(row=0, column=1, pady=(0,20))

#Creating Frame3
frame3 = LabelFrame(mw, text='This is frame3', width=300, padx=10, pady=10, font=('', 14))
frame3.grid(row=0, column=3, padx=20, pady=10)

box_lbl = Label(frame3, text='box', bg='blue')
box_lbl.pack(pady=20)
mw.mainloop()