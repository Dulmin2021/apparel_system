from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from employees import connect_database


def add_category(id, name, description):
    if id == '' or name == '' or description == '':
        messagebox.showerror('Error', 'All fields are required')
    else:
        cursor, connection = connect_database()
        if not cursor or not connection:
            return
        cursor.execute('USE inventory_system')
        cursor.execute('CREATE TABLE IF NOT EXISTS category_data (id INT PRIMARY KEY, name VARCHAR(100), description TEXT)')
        cursor.execute('SELECT * from category_data WHERE id=%s', id)
        if cursor.fetchone():
            messagebox.showerror('Error', 'Id already exists')
            return
        cursor.execute('INSERT INTO category_data VALUES (%s, %s, %s)', (id, name, description))
        connection.commit()
        messagebox.showinfo('Info', 'Data is inserted')
        treeview_data(treeview)   



def category_form(window):
    category_frame=Frame(window, width=1070, height=567, bg='white')
    category_frame.place(x=200, y=100)

    heading_Label=Label(category_frame, text='Manage Category Details', font=('times new roman','16', 'bold'), bg='#0f4d7d', fg='white')
    heading_Label.place(x=0, y=0, relwidth=1)
    global back_image, logo
    back_image=PhotoImage(file='assets/back_button.png')
    back_button=Button(category_frame, image=back_image, bd=0, cursor='hand2', bg='white', command=lambda: category_frame.place_forget())
    back_button.place(x=10, y=30)

    logo=PhotoImage(file='assets/categories2.png')
    label=Label(category_frame, image=logo, bg='white')
    label.place(x=30, y=100)  

    details_frame=Frame(category_frame, bg='white')
    details_frame.place(x=500, y=60)

    id_label=Label(details_frame, text='Id:', font=('times new roman',14, 'bold'), bg='white')
    id_label.grid(row=0, column=0, padx=20, sticky='W')
    id_entry=Entry(details_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
    id_entry.grid(row=0, column=1)

    category_name_label=Label(details_frame, text='Category Name:', font=('times new roman',14, 'bold'), bg='white')
    category_name_label.grid(row=1, column=0, padx=20, sticky='W')
    category_name_entry=Entry(details_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
    category_name_entry.grid(row=1, column=1, pady=20)

    description_label=Label(details_frame, text='Description:', font=('times new roman',14, 'bold'), bg='white')
    description_label.grid(row=2, column=0, padx=20, sticky='nw')
    description_text=Text(details_frame, width=25, height=6, bd=2, bg='lightyellow')
    description_text.grid(row=2, column=1)

    button_frame=Frame(category_frame, bg='white')
    button_frame.place(x=650, y=280)

    add_button=Button(
        button_frame,
        text='Add',
        font=('times new roman','14'),
        width=8,
        cursor='hand2',
        fg='white',
        bg='#0f4d7d',
        command=lambda: add_category(id_entry.get(), category_name_entry.get(), description_text.get(1.0,END).strip()))
    add_button.grid(row=0, column=0, padx=20)

    delete_button=Button(
        button_frame,
        text='Delete',
        font=('times new roman','14'),
        width=8,
        cursor='hand2',
        fg='white',
        bg='#0f4d7d')
    delete_button.grid(row=0, column=1, padx=20)
    
    treeview_frame=Frame(category_frame, bg='lightyellow')
    treeview_frame.place(x=530, y=340, height=200, width=500)

    scrolly=Scrollbar(treeview_frame, orient=VERTICAL)
    scrollx=Scrollbar(treeview_frame, orient=HORIZONTAL)
    treeview = ttk.Treeview(treeview_frame, column=('id', 'name', 'description'), show='headings', yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
    scrolly.pack(side=RIGHT, fill=Y)  
    scrollx.pack(side=BOTTOM, fill=X)
    scrollx.config(command=treeview.xview) 
    scrolly.config(command=treeview.yview) 
    treeview.pack(fill=BOTH, expand=1)
    treeview.heading('id', text='ID')
    treeview.heading('name', text='Category Name')
    treeview.heading('description', text='Description')

    treeview.column('id', width=80)
    treeview.column('name', width=140)
    treeview.column('description', width=300)