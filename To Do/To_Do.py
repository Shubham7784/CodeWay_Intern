from tkinter import *
import sqlite3 as sql
from tkinter import ttk,messagebox
import os
con = sql.connect("To_Do.db")
cur = con.cursor()
def create_table():
    try:
        query = '''create table Tasks(Title varchar(100),Description varchar(200),Timing Date,Status varchar(10),Primary Key(Description));'''
        cur.execute(query)
        con.commit()
        return
    except sql.OperationalError as e:
        return

def add_task(win,title,des,time,status):
    try:
        query = f'''insert into Tasks(Title,Description,Timing,Status) values('{title}','{des}','{time}','{status}')'''
        cur.execute(query)
        con.commit()
        messagebox.showinfo('Completion','Task Added Sucessfully')
        
    except sql.IntegrityError:
        messagebox.showerror('Repeted Task','This task has already been added !')
    

def show_task(win):
    win.destroy()
    window1 = Tk()
    window1.title("Your Tasks")
    window1.geometry("500x500")
    head = Label(window1,text="TASKS",font=('calibri',15,'bold'))
    head.pack()
    table = Frame(window1)
    table.pack()
    my_table = ttk.Treeview(table)
    my_table['columns'] = ('S_No.','Title','Description','Timing','Status')
    my_table.column("#0", width=0,  stretch=NO)
    my_table.column("S_No.",anchor=CENTER, width=40)
    my_table.column("Title",anchor=CENTER, width=150)
    my_table.column("Description",anchor=CENTER,width=150)
    my_table.column("Timing",anchor=CENTER,width=80)
    my_table.column("Status",anchor=CENTER,width=80)
    my_table.heading("#0",text="",anchor=CENTER)
    my_table.heading("S_No.",text="S No.",anchor=CENTER)
    my_table.heading("Title",text="Title",anchor=CENTER)
    my_table.heading("Description",text="Description",anchor=CENTER)
    my_table.heading("Timing",text="Timing",anchor=CENTER)
    my_table.heading("Status",text="Status",anchor=CENTER)
    cur.execute("select * from Tasks;")
    data = cur.fetchall()
    for i in range(len(data)):
        value = [i+1]+list(data[i])
        my_table.insert("",'end',iid=i,text='',values=value)
    my_table.pack()
    del_button = Button(window1,text="Delete a Task",command=lambda:delete_task(window1))
    update_button = Button(window1,text="Update a Task",command=lambda:update(window1))
    del_button.pack()
    update_button.pack()
    window1.mainloop()
    main()
def main():
    window = Tk()
    window.title("TO DO App")
    window.geometry("300x300")
    title = StringVar()
    des = StringVar()
    time = StringVar()
    status = "Pending"
    head = Label(window,text="ADD TASK",font=('Algerian',15))
    form = Frame(window)
    title_text = Label(window,text="Title : ",font=('Aerial',10,'bold'))
    title_entry = Entry(window,textvariable=title,font=('Aerial',10,'bold'))
    des_text = Label(window,text="Description : ",font=('Aerial',10,'bold'))
    des_entry = Entry(window,textvariable=des,font=('Aerial',10,'bold'))
    time_text = Label(window,text="Timing",font=('Aerial',10,'bold'))
    time_entry = Entry(window,textvariable=time,font=('Aerial',10,'bold'))
    submit = Button(window,text="ADD",font=('Aerial',10,'bold'),command=lambda: add_task(window,title.get(),des.get(),time.get(),status))
    show = Button(window,text="Show Tasks",font=('Aerial',10,'bold'),command=lambda:show_task(window))
    head.pack()
    title_text.pack()
    title_entry.pack()
    des_text.pack()
    des_entry.pack()
    time_text.pack()
    time_entry.pack()
    submit.pack()
    form.pack()
    show.pack()
    window.mainloop()
def delete_task(win):
    win.destroy()
    window2 = Tk()
    s_no = StringVar()
    window2.title("Delete Your Task")
    window2.geometry("200x200")
    ind_label = Label(window2,text="Enter S No. ",font=('Aerial',10,'bold'))
    ind_entry = Entry(window2,textvariable= s_no)
    ind_label.pack()
    ind_entry.pack()
    del_button = Button(window2,text="Delete",command=lambda:del_task(s_no.get()))
    del_button.pack()
    s_no.set("")

def del_task(id):
    data = cur.execute("select * from Tasks;").fetchall()
    data = data[int(id)-1]
    data = data[1]
    try:
        query = f'''delete from Tasks where Description = '{data}';'''
        cur.execute(query)
        con.commit()
        messagebox.showinfo("Deletion Sucessful","Task Deleted Sucessfully")
    except sql.OperationalError as ms:
        messagebox.showerror("Deletion Failed",ms)
def update(win):
    win.destroy()
    window_u = Tk()
    window_u.title("Update Task")
    s_no = StringVar()
    checkbutton1 = IntVar()
    checkbutton2 = IntVar()
    checkbutton3 = IntVar()
    ind_label = Label(window_u,text="Enter S No. ",font=('Aerial',10,'bold'))
    ind_entry = Entry(window_u,textvariable=s_no)
    head = Label(window_u,text="Update the Status of the Task",font=('Aerial',15,'bold'))
    check1 = Checkbutton(window_u,text="Pending",variable=checkbutton1,font=('Aerial',10,'bold'))
    check2 = Checkbutton(window_u,text="Completed",variable=checkbutton2,font=('Aerial',10,'bold'))
    check3 = Checkbutton(window_u,text="Cancelled",variable=checkbutton3,font=('Aerial',10,'bold'))
    update_button = Button(window_u,text="Update",command=lambda:up_task(window_u,checkbutton1.get(),checkbutton2.get(),checkbutton3.get(),s_no),font=('Aerial',10,'bold'))
    ind_label.pack()
    ind_entry.pack()
    check1.pack()
    check2.pack()
    check3.pack()
    update_button.pack()
    window_u.geometry("300x300")
    window_u.mainloop()
def up_task(win,c1,c2,c3,id):
    win.destroy()
    upd = ""
    id = int(id.get())
    query = f'select * from Tasks;'
    try:
        data = cur.execute(query).fetchall()
        data = data[id-1]
        data = data[1]
    except IndexError :

        messagebox.showerror("An Error Occured","No Such Record Exist!!")
        return
    if(c1==1):
        upd = "Pending"
    elif(c2==1):
        upd = "Completed"
    elif(c3==1):
        upd = "Cancelled"
    query = f'''update Tasks set Status = '{upd}' where Description = '{data}'; '''
    try:
        cur.execute(query)
        con.commit()
        messagebox.showinfo("Task Updated","Task Updated Successfully")
    except sql.OperationalError as e:
        messagebox.showerror("An Error Occured",e)
if __name__ == "__main__":
    create_table()
    main()