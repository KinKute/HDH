#from _typeshed import IdentityFunction
from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title("Chương trình tạo file")

window.geometry('500x300')

frame1= Frame(window).pack(side=LEFT)
frame2 =Frame(window).pack(side=LEFT)


lbl = Label(frame1, text ="Tên thư mục").pack()
#lbl.grid(column =0, row =0)
txt = Entry(frame1, width=50).pack(side=BOTTOM)
#txt.grid(column=1, row=0)


lbl2 = Label(frame2, text ="Chọn đường dẫn")
lbl2.pack()
#lbl2.grid(column =0, row =0)
txt = Entry(frame2, width=50).pack()
#txt.grid(column=1, row=0)

button = Button(window, text='Add File!').pack()
window.mainloop()
