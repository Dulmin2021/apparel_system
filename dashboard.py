from tkinter import *

window=Tk()

window.title('Dashboard')
window.geometry('1270x668+0+0')
window.resizable(0,0)
window.config(bg='white')

bg_Image=PhotoImage(file='assets/logo.png')
titleLabel =Label(window, image=bg_Image, compound=RIGHT, text='     CIB Apparel System  ', font=('times new roman', 40, 'bold'), bg='#010c48', fg='white', anchor='w', padx=20)
titleLabel.place(x=0, y=0, relwidth=1)



window.mainloop()
