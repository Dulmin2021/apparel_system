from tkinter import *

window=Tk()

window.title('Dashboard')
window.geometry('1270x668+0+0')
window.resizable(0,0)
window.config(bg='white')

bg_Image=PhotoImage(file='assets/logo.png')
titleLabel =Label(window, image=bg_Image, compound=LEFT, text=' CIB Apparel System  ', font=('times new roman', 40, 'bold'), bg='#010c48', fg='white', anchor='w', padx=20)
titleLabel.place(x=0, y=0, relwidth=1) 

logoutButton=Button(window, text='Logout', font=('times new roman', '20', 'bold'), fg='#010c48')
logoutButton.place(x=1100, y=10)

subtitleLabel=Label(window, text="Welcome Admin\t\t Date: 14-04-2025\t\t Time: 12:00:00PM", font=('times new roman','15'), bg='#4d636d', fg='white')
subtitleLabel.place(x=0, y=70, relwidth=1)

leftFrame=Frame(window)


leftFrame.place(x=0, y=102, width=200, height=555)

logoImage=PhotoImage(file='assets/logo3.png')
imageLabel=Label(leftFrame, image=logoImage)
imageLabel.pack()


#######################################Menu and Menu Buttons###################################################################

menuLabel=Label(leftFrame, text='Menu', font=('times new roman', '20'), bg='#009688')
menuLabel.pack(fill=X)


employee_icon=PhotoImage(file='assets/employee.png')
employee_button=Button(leftFrame, image=employee_icon, compound=LEFT, text='  Employees', font=('times new roman', '20', 'bold'), anchor='w', padx=10)
employee_button.pack(fill=X)

supplier_icon=PhotoImage(file='assets/supplier.png')
supplier_button=Button(leftFrame, image=supplier_icon, compound=LEFT, text='  Suppliers', font=('times new roman', '20', 'bold'), anchor='w', padx=10)
supplier_button.pack(fill=X)

category_icon=PhotoImage(file='assets/category.png')
category_button=Button(leftFrame, image=category_icon, compound=LEFT, text='  Categories', font=('times new roman', '20', 'bold'), anchor='w', padx=10)
category_button.pack(fill=X)

product_icon=PhotoImage(file='assets/product.png')
product_button=Button(leftFrame, image=product_icon, compound=LEFT, text='  Products', font=('times new roman', '20', 'bold'), anchor='w', padx=10)
product_button.pack(fill=X)

sales_icon=PhotoImage(file='assets/sales.png')
sales_button=Button(leftFrame, image=sales_icon, compound=LEFT, text='  Sales', font=('times new roman', '20', 'bold'), anchor='w', padx=10)
sales_button.pack(fill=X)

exit_icon=PhotoImage(file='assets/exit.png')
exit_button=Button(leftFrame, image=exit_icon, compound=LEFT, text='  Exit', font=('times new roman', '20', 'bold'), anchor='w', padx=10)
exit_button.pack(fill=X)


######################################################################################################################


window.mainloop()