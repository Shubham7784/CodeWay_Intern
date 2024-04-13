import random as r
from tkinter import *

window = Tk()
window.minsize(350,300)
window.maxsize(350,300)
window.title("PASSWORD GENERATOR")
checkbutton1 = IntVar()
checkbutton2 = IntVar()
checkbutton3 = IntVar()
specific_symbol = StringVar()
pass_length = StringVar()
c_password = ""
password = ""
def generate_pass():
    check_b1 = checkbutton1.get()
    check_b2 = checkbutton2.get()
    check_b3 = checkbutton3.get()
    l = int(pass_length.get())
    pass_alpha = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']
    pass_num = ['0','1','2','3','4','5','6','7','8','9']
    pass_sym = ['@']
    global password
    global c_password
    global p
    password = ""
    c_password = ""
    p.destroy()    
    l_alpha = 0 
    l_num = 0
    if(check_b1==1 and check_b2==1 and check_b3==1):
        l_alpha = int(l/2) 
        l_num = l-(l_alpha+len(pass_sym))

    elif(check_b1==1 and check_b2==0 and check_b3==0):
        l_alpha = l
    elif(check_b1==0 and check_b2==1 and check_b3==0):
        l_num = l
    elif(check_b1==1 and check_b2==1):
        l_alpha = int(l/2)
        l_num = l- l_alpha   
    elif(check_b1==1 and check_b3==1):
        l_alpha = l - len(pass_sym)
    elif(check_b2==1 and check_b3==1):
        l_num = l - len(pass_sym)
    if(specific_symbol!=""):
        pass_sym.append(specific_symbol.get())
    if(check_b1==1):
        a = r.sample(pass_alpha,l_alpha)
        password+= "".join(a)
        l -= len(pass_sym)
    if(check_b2==1): 
        a = r.sample(pass_num,l_num)
        password+= "".join(a)
    if(check_b3==1):
        a = r.sample(pass_sym,len(pass_sym))
        password+= "".join(a)
    c_password = password
    p = Label(window,text=c_password,font=('aerial',10,'bold'))
    p.grid(row=9,column=1)
    copy_button = Button(window,text="COPY",font=('aerial',10,'bold'),command=copy)
    copy_button.grid(row=11,column=1)
    
def copy(): 
    global c_password
    window.clipboard_clear()
    window.clipboard_append(c_password)

msg = Label(window,text="What would you like include in your Password",font=('aerial',10,'bold'))
option1 = Checkbutton(window,text="Alphabets",variable=checkbutton1)
option2 = Checkbutton(window,text="Numbers",variable=checkbutton2)
option3 = Checkbutton(window,text="Symbols",variable=checkbutton3)
len_label = Label(window,text="Password Length",font=('aerial',10,'bold'))
len_val = Entry(window,textvariable=pass_length)
gen_button = Button(window,text="GENERATE",command=generate_pass)
sym_if = Label(window,text="Would you like to include any other symbol (only one )",font=('aerial',10,'bold'))
sym_if_var = Entry(window,textvariable=specific_symbol)
p = Label(window,text=c_password,font=('aerial',10,'bold'))
p.grid(row=9,column=1)
msg.grid(row=0,column=1)
option1.grid(row=1,column=1)
option2.grid(row=2,column=1)
option3.grid(row=3,column=1)
len_label.grid(row=4,column=1)
len_val.grid(row=5,column=1)
sym_if.grid(row=6,column=1)
sym_if_var.grid(row=7,column=1)
gen_button.grid(row=8,column=1)

window.mainloop()