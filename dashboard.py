

from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
#################################################################################
###########FUNCTIONALITY PART####################################################
#################################################################################

def employee_form(window):

    global back_image
    employee_frame=Frame(window, width=1070, height=567, bg='white')
    employee_frame.place(x=200, y=100)
    heading_Label=Label(employee_frame, text='Manage Employee Details', font=('times new roman','16', 'bold'), bg='#0f4d7d', fg='white')
    heading_Label.place(x=0, y=0, relwidth=1)
    back_image=PhotoImage(file='assets/back_button.png')


    top_frame=Frame(employee_frame, bg='white')
    top_frame.place(x=0, y=40, relwidth=1, height=235)
    
    back_button=Button(top_frame, image=back_image, bd=0, cursor='hand2', bg='white', command=lambda: employee_frame.place_forget())
    back_button.place(x=10, y=0)

    search_frame=Frame(top_frame, bg='white')
    search_frame.pack()
    
    search_combobox=ttk.Combobox(search_frame, values=('ID', 'Name', 'Email'),font=('times new roman','12'), state='readonly', justify=CENTER)
    search_combobox.set('Search by')
    search_combobox.grid(row=0, column=0, padx=20)
    
    search_entry=Entry(search_frame, font=('times new roman','12'), bg='lightyellow')
    search_entry.grid(row=0, column=1)
    
    search_button=Button(search_frame, text='Search', font=('times new roman','12'), width=10, cursor='hand2', fg='white', bg='#0f4d7d')
    search_button.grid(row=0, column=2, padx=20)
    
    show_button=Button(search_frame, text='Show All', font=('times new roman','12'), width=10, cursor='hand2', fg='white', bg='#0f4d7d')
    show_button.grid(row=0, column=3)

    employee_treeview=ttk.Treeview(top_frame, columns=('empid', 'name', 'email', 'gender', 'dob', 'contact', 'employment_type', 'education', 'work_shift', 'address', 'doj', 'salary', 'usertype'), show='headings')
    employee_treeview.pack(pady=10)

    employee_treeview.heading('empid', text='EmpId')
    employee_treeview.heading('name', text='Name')
    employee_treeview.heading('email', text='Email')
    employee_treeview.heading('gender', text='Gender')
    employee_treeview.heading('dob', text='DOB')
    employee_treeview.heading('contact', text='Contact')
    employee_treeview.heading('employment_type', text='Employment Type')
    employee_treeview.heading('education', text='Education')
    employee_treeview.heading('work_shift', text='Work shift')
    employee_treeview.heading('address', text='Email')
    employee_treeview.heading('doj', text='Joined Date')
    employee_treeview.heading('salary', text='Salary')
    employee_treeview.heading('usertype', text='Type')

    employee_treeview.column('empid', width=60)
    employee_treeview.column('name', width=140)
    employee_treeview.column('email', width=180)
    employee_treeview.column('gender', width=180)
    employee_treeview.column('dob', width=180)
    employee_treeview.column('contact', width=180)
    employee_treeview.column('employment_type', width=120)
    employee_treeview.column('education', width=120)
    employee_treeview.column('work_shift', width=100)
    employee_treeview.column('address', width=200)
    employee_treeview.column('doj', width=100)
    employee_treeview.column('salary', width=140)
    employee_treeview.column('usertype', width=120)
    
#Detail Frame
    detail_frame=Frame(employee_frame, bg='white')
    detail_frame.place(x=20, y=280)
#EmpID Label
    empid_label=Label(detail_frame, text='EmpId',font=('times new roman', '12'), bg='white')
    empid_label.grid(row=0, column=0, padx=20, pady=10, sticky='W')
    empid_entry=Entry(detail_frame, font=('times new roman', '12'), bg='lightyellow')
    empid_entry.grid(row=0, column=1, padx=20, pady=10)
#Name Label
    name_label=Label(detail_frame, text='Name',font=('times new roman', '12'), bg='white')
    name_label.grid(row=0, column=2, padx=20, pady=10, sticky='W')
    name_entry=Entry(detail_frame, font=('times new roman', '12'), bg='lightyellow')
    name_entry.grid(row=0, column=3, padx=20, pady=10)
#Email Label
    email_label=Label(detail_frame, text='Email',font=('times new roman', '12'), bg='white')
    email_label.grid(row=0, column=4, padx=20, pady=10, sticky='W')
    email_entry=Entry(detail_frame, font=('times new roman', '12'), bg='lightyellow')
    email_entry.grid(row=0, column=5, padx=20, pady=10)
#Gender Label
    gender_label=Label(detail_frame, text='Gender',font=('times new roman', '12'), bg='white')
    gender_label.grid(row=1, column=0, padx=20, pady=10, sticky='W')
    gender_combobox=ttk.Combobox(detail_frame, values=('Male', 'Female'),font=('times new roman', '12'), width=18, state='readonly')
    gender_combobox.set('Select Gender')
    gender_combobox.grid(row=1, column=1)
#DOB Label    
    dob_label=Label(detail_frame, text='DOB',font=('times new roman', '12'), bg='white')
    dob_label.grid(row=1, column=2, padx=20, pady=10, sticky='W')
    dob_date_entry=DateEntry(detail_frame, width=18, font=('times new roman', 12), state='readonly', date_pattern='dd/mm/yyyy')
    dob_date_entry.grid(row=1, column=3)
#Contact Label
    contact_label=Label(detail_frame, text='Contact',font=('times new roman', '12'), bg='white')
    contact_label.grid(row=1, column=4, padx=20, pady=10, sticky='W')
    contact_entry=Entry(detail_frame, font=('times new roman', '12'), bg='lightyellow')
    contact_entry.grid(row=1, column=5, padx=20, pady=10)
#Employment Type Label
    employment_type_label=Label(detail_frame, text='Employment Type',font=('times new roman', '12'), bg='white')
    employment_type_label.grid(row=2, column=0, padx=20, pady=10, sticky='W')
    employment_type_combobox=ttk.Combobox(detail_frame, values=('Full Time', 'Part Time', 'Casual', 'Contract', 'Intern'),font=('times new roman', '12'), width=18, state='readonly')
    employment_type_combobox.set('Select Type')
    employment_type_combobox.grid(row=2, column=1)
#Education Label
    edcation_label=Label(detail_frame, text='Education',font=('times new roman', '12'), bg='white')
    edcation_label.grid(row=2, column=2, padx=20, pady=10, sticky='W')
    education_options=["O/L", "O/L Passed" "A/L", "A/L Passed", "Diploma", "Dregree"]
    edcation_combobox=ttk.Combobox(detail_frame, values=education_options, font=('times new roman', '12'), width=18, state='readonly')
    edcation_combobox.set('Select Education')
    edcation_combobox.grid(row=2, column=3)
#Work shift Label
    work_shift_label=Label(detail_frame, text='Work shift',font=('times new roman', '12'), bg='white')
    work_shift_label.grid(row=2, column=4, padx=20, pady=10)
    work_shift_combobox=ttk.Combobox(detail_frame, values=('Morning', 'Evening', 'Night'),font=('times new roman', '12'), width=18, state='readonly')
    work_shift_combobox.set('Select shift')
    work_shift_combobox.grid(row=2, column=5)
#Address Label
    address_label=Label(detail_frame, text='Address',font=('times new roman', '12'), bg='white')
    address_label.grid(row=3, column=0, padx=20, pady=10, sticky='W')
    address_text=Text(detail_frame, width=20, height=3, font=('times new roman', 12), bg='lightyellow')
    address_text.grid(row=3, column=1, rowspan=2)
#DOJ Label
    doj_label=Label(detail_frame, text='Joined Date',font=('times new roman', '12'), bg='white')
    doj_label.grid(row=3, column=2, padx=20, pady=10, sticky='W')
    doj_date_entry=DateEntry(detail_frame, width=18, font=('times new roman', 12), state='readonly', date_pattern='dd/mm/yyyy')
    doj_date_entry.grid(row=3, column=3)
#User Type Label    
    usertype_label=Label(detail_frame, text='User Type',font=('times new roman', '12'), bg='white')
    usertype_label.grid(row=4, column=2, padx=20, pady=10)
    usertype_combobox=ttk.Combobox(detail_frame, values=('Admin', 'Employee'),font=('times new roman', '12'), width=18, state='readonly')
    usertype_combobox.set('Select User type')
    usertype_combobox.grid(row=4, column=3)
#Salary Label
    salary_label=Label(detail_frame, text='Salary',font=('times new roman', '12'), bg='white')
    salary_label.grid(row=3, column=4, padx=20, pady=10, sticky='W')
    salary_entry=Entry(detail_frame, font=('times new roman', '12'), bg='lightyellow')
    salary_entry.grid(row=3, column=5, padx=20, pady=10)
#Password Label
    password_label=Label(detail_frame, text='Password',font=('times new roman', '12'), bg='white')
    password_label.grid(row=4, column=4, padx=20, pady=10, sticky='W')
    password_entry=Entry(detail_frame, font=('times new roman', '12'), bg='lightyellow')
    password_entry.grid(row=4, column=5, padx=20, pady=10)

#Buttons
    button_frame=Frame(employee_frame, bg='white')
    button_frame.place(x=200, y=520)

    add_button=Button(button_frame, text='Add', font=('times new roman','12'), width=10, cursor='hand2', fg='white', bg='#0f4d7d')
    add_button.grid(row=0, column=0, padx=20)

    update_button=Button(button_frame, text='Update', font=('times new roman','12'), width=10, cursor='hand2', fg='white', bg='#0f4d7d')
    update_button.grid(row=0, column=1, padx=20)

    delete_button=Button(button_frame, text='Delte', font=('times new roman','12'), width=10, cursor='hand2', fg='white', bg='#0f4d7d')
    delete_button.grid(row=0, column=2, padx=20)

    clear_button=Button(button_frame, text='Clear', font=('times new roman','12'), width=10, cursor='hand2', fg='white', bg='#0f4d7d')
    clear_button.grid(row=0, column=3, padx=20)



#######################################################
######################GUI PART#########################
#######################################################

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


#Menu and Menu Buttons###################################################################

menuLabel=Label(leftFrame, text='Menu', font=('times new roman', '20'), bg='#009688')
menuLabel.pack(fill=X)


employee_icon=PhotoImage(file='assets/employee.png')
employee_button=Button(leftFrame, image=employee_icon, compound=LEFT, text='  Employees', font=('times new roman', '20', 'bold'), anchor='w', padx=10, command=lambda: employee_form(window))# Bind the button to the function
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

##############################################################################################################



##################################FRAMES################FRAMES################FRAMES##########################

#Employee Frame
emp_frame=Frame(window, bg='#2C3E50', bd=3, relief=RIDGE)
emp_frame.place(x=400, y=125, height=170, width=280) 
total_emp_icon=PhotoImage(file='')
total_emp_icon_label=Label(emp_frame, image=total_emp_icon, bg='#2C3E50',)
total_emp_icon_label.pack()

total_emp_label=Label(emp_frame, text= 'Total Employees', bg='#2C3E50', fg='white', font=('times new roman', '15', 'bold'))
total_emp_label.pack()
total_emp_count_label=Label(emp_frame, text= '0', bg='#2C3E50', fg='white', font=('times new roman', '30', 'bold'))
total_emp_count_label.pack()


#Supplier Frame
sup_frame=Frame(window, bg='#8E44AD', bd=3, relief=RIDGE)
sup_frame.place(x=800, y=125, height=170, width=280) 
total_sup_icon=PhotoImage(file='')
total_sup_icon_label=Label(sup_frame, image=total_sup_icon, bg='#8E44AD',)
total_sup_icon_label.pack()

total_sup_label=Label(sup_frame, text= 'Total Suppliers', bg='#8E44AD', fg='white', font=('times new roman', '15', 'bold'))
total_sup_label.pack()
total_sup_count_label=Label(sup_frame, text= '0', bg='#8E44AD', fg='white', font=('times new roman', '30', 'bold'))
total_sup_count_label.pack()


#Category Frame
cat_frame=Frame(window, bg='#27AE60', bd=3, relief=RIDGE)
cat_frame.place(x=400, y=310, height=170, width=280) 
total_cat_icon=PhotoImage(file='')
total_cat_icon_label=Label(cat_frame, image=total_cat_icon, bg='#27AE60',)
total_cat_icon_label.pack()

total_cat_label=Label(cat_frame, text= 'Total Categories', bg='#27AE60', fg='white', font=('times new roman', '15', 'bold'))
total_cat_label.pack()
total_cat_count_label=Label(cat_frame, text= '0', bg='#27AE60', fg='white', font=('times new roman', '30', 'bold'))
total_cat_count_label.pack()


#Products Frame
prod_frame=Frame(window, bg='#2C3E50', bd=3, relief=RIDGE)
prod_frame.place(x=800, y=310, height=170, width=280) 
total_prod_icon=PhotoImage(file='')
total_prod_icon_label=Label(prod_frame, image=total_prod_icon, bg='#2C3E50',)
total_prod_icon_label.pack()

total_prod_label=Label(prod_frame, text= 'Total Products', bg='#2C3E50', fg='white', font=('times new roman', '15', 'bold'))
total_prod_label.pack()
total_prod_count_label=Label(prod_frame, text= '0', bg='#2C3E50', fg='white', font=('times new roman', '30', 'bold'))
total_prod_count_label.pack()


#Sales Frame
sales_frame=Frame(window, bg='#E74C3C', bd=3, relief=RIDGE)
sales_frame.place(x=600, y=495, height=170, width=280) 
total_sales_icon=PhotoImage(file='')
total_sales_icon_label=Label(sales_frame, image=total_sales_icon, bg='#E74C3C',)
total_sales_icon_label.pack()

total_sales_label=Label(sales_frame, text= 'Total Sales', bg='#E74C3C', fg='white', font=('times new roman', '15', 'bold'))
total_sales_label.pack()
total_sales_count_label=Label(sales_frame, text= '0', bg='#E74C3C', fg='white', font=('times new roman', '30', 'bold'))
total_sales_count_label.pack(pady=10)





window.mainloop()