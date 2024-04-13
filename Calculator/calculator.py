from tkinter import *
import unicodeit
import math
from tkinter import messagebox

expression = ""
def press(key,var):
    global expression
    temp = var.get() + str(key)
    var.set(temp)
    expression = expression + str(key)

def press_clear(var):
    global expression
    var.set("")
    expression = ""
    

def press_equal(var):
    global expression
    if("^" not in expression):
        try:
            temp = str(eval(expression))
            var.set(temp)
        except SyntaxError:
            messagebox.showerror("Error","Enter a valid value after the operand!!")
        except ZeroDivisionError:
            messagebox.showerror("Error","A number cannot be divided by Zero!!")
    else:
        expression = expression.split("^")
        if("("in expression[1]):
            expression[1] = str(eval(expression[1]))
        try:
            temp = math.pow(float(expression[0]),float(expression[1]))
            expression = str(temp)
            var.set(str(temp))
        except Exception as e:
            messagebox.showerror("Error",e)

def cal_log(var):
   global expression
   temp = math.log(float(var.get()))
   var.set(str(temp))
   expression =str(temp)

def cal_exp(var):
    global expression
    temp = math.exp(float(var.get()))
    var.set(str(temp))
    expression=str(temp)

def cal_sq(var):
    global expression
    temp = float(var.get())
    temp = temp**2
    var.set(str(temp))
    expression=str(temp)

def cal_cube(var):
    global expression
    temp = float(var.get())
    temp = temp**3
    var.set(str(temp))
    expression=str(temp)
def press_pow(var):
    global expression
    expression = var.get() + "^"
    var.set(expression)
def press_back(var):
    global expression
    temp = var.get()
    temp = temp[:len(temp)-1]
    var.set(temp)
    expression = temp

def press_brac(br,var):
    global expression
    temp = var.get()
    temp+=br
    var.set(temp)
    expression = temp
def main():
    global expression
    window = Tk()
    window.title("Calculator")
    window.maxsize(300,350)
    window.minsize(300,350)
    var = StringVar()
    display = Entry(window,width=50,textvariable=var)
    display.grid(columnspan=4)
    b_7 = Button(window,text="1",command=lambda:press(1,var),width=7,height=2)
    b_8 = Button(window,text="2",command=lambda:press(2,var),width=7,height=2)
    b_9 = Button(window,text="3",command=lambda:press(3,var),width=7,height=2)
    b_4 = Button(window,text="4",command=lambda:press(4,var),width=7,height=2)
    b_5 = Button(window,text="5",command=lambda:press(5,var),width=7,height=2)
    b_6 = Button(window,text="6",command=lambda:press(6,var),width=7,height=2)
    b_1 = Button(window,text="7",command=lambda:press(7,var),width=7,height=2)
    b_2 = Button(window,text="8",command=lambda:press(8,var),width=7,height=2)
    b_3 = Button(window,text="9",command=lambda:press(9,var),width=7,height=2)
    b_0 = Button(window,text="0",command=lambda:press(0,var),width=7,height=2)
    clr = Button(window,text="AC",command=lambda:press_clear(var),width=7,height=2)
    plus = Button(window,text="+",command=lambda:press("+",var),width=7,height=2)
    min = Button(window,text="-",command=lambda:press("-",var),width=7,height=2)
    mul = Button(window,text="*",command=lambda:press("*",var),width=7,height=2)
    div = Button(window,text="/",command=lambda:press("/",var),width=7,height=2)
    equal = Button(window,text="=",command=lambda:press_equal(var),width=7,height=2)
    log = Button(window,text="log",command=lambda:cal_log(var),width=7,height=2)
    exp = Button(window,text=unicodeit.replace("exp"),command=lambda:cal_exp(var),width=7,height=2)
    sq = Button(window,text=unicodeit.replace("x^2"),command=lambda:cal_sq(var),width=7,height=2)
    cube = Button(window,text=unicodeit.replace("x^3"),command=lambda:cal_cube(var),width=7,height=2)
    pow = Button(window,text=unicodeit.replace("x^y"),command=lambda:press_pow(var),width=7,height=2)
    dec = Button(window,text=".",command=lambda:press(".",var),width=7,height=2)
    back = Button(window,text="Clr",command=lambda:press_back(var),width=7,height=2)
    o_b = Button(window,text="(",command=lambda:press_brac("(",var),width=7,height=2)
    c_b = Button(window,text=")",command=lambda:press_brac(")",var),width=7,height=2)
    log.grid(row=1,column=0)
    exp.grid(row=1,column=1)
    sq.grid(row=1,column=2)
    back.grid(row=1,column=3)
    b_1.grid(row=2,column=0)
    b_2.grid(row=2,column=1)
    b_3.grid(row=2,column=2)
    plus.grid(row=2,column=3)
    b_4.grid(row=3,column=0)
    b_5.grid(row=3,column=1)
    b_6.grid(row=3,column=2)
    min.grid(row=3,column=3)
    b_7.grid(row=4,column=0)
    b_8.grid(row=4,column=1)
    b_9.grid(row=4,column=2)
    mul.grid(row=4,column=3)
    b_0.grid(row=5,column=1)
    clr.grid(row=7,column=1)
    div.grid(row=5,column=3)
    equal.grid(row=6,column=2)
    dec.grid(row=5,column=0)
    pow.grid(row=6,column=3)
    cube.grid(row=5,column=2)
    o_b.grid(row=6,column=0)
    c_b.grid(row=6,column=1)
    window.mainloop()


if __name__ == "__main__":
    main()