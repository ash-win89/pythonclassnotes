'''
import tkinter

#creating window
window = tkinter.Tk()
window.title('first title')
label = tkinter.Label(window, text = 'hello world').pack()
window.mainloop()


#using '*' will import every methods and properties in that library
from tkinter import *
from tkinter import ttk

window = Tk()
window.title('function')
label = Label(window, text = 'hello world', font=('Arial Bold',40)).pack()
window.geometry('400x300')


def clicked():
    print('button clicked')

bt = ttk.Button(window, text='click here', command=clicked)
bt.pack(side='top')
window.mainloop()


##combobox :
from tkinter import *
from tkinter import ttk

window = Tk()
window.title('Combobox')
window.geometry('300x300')

ttk.Label(window, text='giving front and background color',background='red', foreground='white',
          font=('Times New Roman',10)).grid(row=0, column=1)


n = StringVar()
choosen = ttk.Combobox(window, width=34, textvariable=n)

choosen['values'] = (
                    'January',
                    'feb',
                    'march',
                    'april',
                    'may',
                    'june',
                    'july',
                    'august',
                    'sept',
                    'nov',
                    'oct',
                    'dec'
                        )

choosen.grid(column=1, row=5)
choosen.current(5)#default value
window.mainloop()


from tkinter import *

window = Tk()
window.geometry('500x300')

label = Label(window, text = 'artificial intelligence', font ='50')
label.pack()

cbutton1 = IntVar()
cbutton2 = IntVar()
cbutton3 = IntVar()

Button1 = Checkbutton(window, text='python',variable=cbutton1,onvalue=1, offvalue=0,height=2, width=10)
Button2 = Checkbutton(window, text='javascript',variable=cbutton2,onvalue=1, offvalue=0,height=2, width=10)
Button3 = Checkbutton(window, text='java',variable=cbutton3,onvalue=1, offvalue=0,height=2, width=10)

Button1.pack()
Button2.pack()
Button3.pack()
mainloop()


from  tkinter import *

window = Tk()

def sayhi():
    print('say hello to everyone')

menubar = Menu(window)
menubar.add_command(label='hi',command=sayhi)
menubar.add_command(label='exit',command=window.quit)

#display as menubar
window.config(menu=menubar)
window.mainloop()

from tkinter import *

window = Tk()
menubar = Menu(window)
file = Menu(menubar, tearoff=0)

file.add_command(label='new')
file.add_command(label='open')
file.add_command(label='save')
file.add_command(label='save as')
file.add_command(label='close')
file.add_command(label='settings')
file.add_separator()
file.add_command(label='find propertties')

menubar.add_cascade(label='FILES',menu=file)

edit = Menu(menubar, tearoff=0)

edit.add_command(label='cut')
edit.add_command(label='copy')
edit.add_command(label='paste')
edit.add_command(label='delete')
edit.add_command(label='remove')
edit.add_command(label='join')
edit.add_separator()
edit.add_command(label='transpose')

menubar.add_cascade(label='Edit',menu=edit)
Help = Menu(menubar, tearoff=0)

Help.add_command(label='contact us')
Help.add_command(label='about')
menubar.add_cascade(label='help',menu=Help)
window.config(menu=menubar)
window.mainloop()


#spin box
from tkinter import *

window = Tk()
window.geometry('500x500')
window.title('spinbox')
current = StringVar(value=0)
spin = Spinbox(window,from_=0,to=15,textvariable=current,wrap=True)
spin.pack()
window.mainloop()

#simpler spin box:
from tkinter import *
window = Tk()
s =Spinbox(window,from_=0, to = 30)
s.pack()
window.mainloop()
#scroll box:


from tkinter import *

window = Tk()
window.geometry('200x200')

scroll = Label(window, text='this is about scroll bar message', font='50')
scroll.pack()

scroll_bar = Scrollbar(window)
scroll_bar.pack(side=RIGHT,fill=Y)
mylist = Listbox(window, yscrollcommand=scroll_bar.set)
for i in range(100):
    mylist.insert(END, "this is the line number"+ str(i))

mylist.pack(side=LEFT, fill=BOTH)
scroll_bar.config(command=mylist.yview)
window.mainloop()



The canvas widget is used to add the structured graphics to the python application.
 It is used to draw the graph and plots to the python application.'''

from tkinter import *
top = Tk()
top.geometry("200x200")
# creating a simple canvas
c = Canvas(top, bg="pink", height="200")
c.pack()
top.mainloop()

'''
from tkinter import *
top = Tk()
top.geometry("200x200")
# creating a simple canvas
c = Canvas(top, bg="pink", height="200", width=200)
arc = c.create_arc((5, 10, 150, 200), start=0, extent=150, fill="white")
c.pack()
top.mainloop()
'''

'''
The Entry widget is used to provde the single line text-box to the user 
to accept a value from the user.
 We can use the Entry widget to accept the text strings from the user. '''
'''
from tkinter import *
top = Tk()
top.geometry("400x250")
name = Label(top, text="Name").place(x=30, y=50)
email = Label(top, text="Email").place(x=30, y=90)
password = Label(top, text="Password").place(x=30, y=130)
sbmitbtn = Button(top, text="Submit", activebackground="pink", activeforeground="blue").place(x=30, y=170)
e1 = Entry(top).place(x=80, y=50)
e2 = Entry(top).place(x=80, y=90)
e3 = Entry(top).place(x=95, y=130)
top.mainloop()'''

'''
import tkinter as tk
from functools import partial
def call_result(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1) + int(num2)
    label_result.config(text="Result = %d" % result)
    return
root = tk.Tk()
root.geometry('400x200+100+200')
root.title('Calculator')
number1 = tk.StringVar()
number2 = tk.StringVar()
labelNum1 = tk.Label(root, text="A").grid(row=1, column=0)
labelNum2 = tk.Label(root, text="B").grid(row=2, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=7, column=2)
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
call_result = partial(call_result, labelResult, number1, number2)
buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=3, column=0)
root.mainloop()'''

#Tkinter Frame
'''
Python Tkinter Frame widget is used to organize the group of widgets.
 It acts like a container which can be used to hold the other widgets.'''

'''
from tkinter import *
top = Tk()
top.geometry("140x100")
frame = Frame(top)
frame.pack()
leftframe = Frame(top)
leftframe.pack(side=LEFT)
rightframe = Frame(top)
rightframe.pack(side=RIGHT)
btn1 = Button(frame, text="Submit", fg="red", activebackground="red")
btn1.pack(side=LEFT)
btn2 = Button(frame, text="Remove", fg="brown", activebackground="brown")
btn2.pack(side=RIGHT)
btn3 = Button(rightframe, text="Add", fg="blue", activebackground="blue")
btn3.pack(side=LEFT)
btn4 = Button(leftframe, text="Modify", fg="black", activebackground="white")
btn4.pack(side=RIGHT)
top.mainloop()'''

#Tkinter Scale
'''
from tkinter import *
def select():
    sel = "Value = " + str(v.get())
    label.config(text=sel)

top = Tk()
top.geometry("200x100")
v = DoubleVar()
scale = Scale(top, variable=v, from_=1, to=50, orient=HORIZONTAL)
scale.pack(anchor=CENTER)
btn = Button(top, text="Value", command=select)
btn.pack(anchor=CENTER)
label = Label(top)
label.pack()
top.mainloop()'''

#PanedWindow
'''
from tkinter import *
def add():
    a = int(e1.get())
    b = int(e2.get())
    leftdata = str(a + b)
    left.insert(1, leftdata)

w1 = PanedWindow()
w1.pack(fill=BOTH, expand=1)
left = Entry(w1, bd=5)
w1.add(left)
w2 = PanedWindow(w1, orient=VERTICAL)
w1.add(w2)
e1 = Entry(w2)
e2 = Entry(w2)
w2.add(e1)
w2.add(e2)
bottom = Button(w2, text="Add", command=add)
w2.add(bottom)
mainloop()'''

#LabelFrame
'''
The LabelFrame widget is used to draw a border around its child widgets.
 We can also display the title for the LabelFrame widget.
'''

'''
from tkinter import *

top = Tk()
top.geometry("300x200")
labelframe1 = LabelFrame(top, text="Positive Comments")
labelframe1.pack(fill="both", expand="yes")
toplabel = Label(labelframe1, text="Place to put the positive comments")
toplabel.pack()
labelframe2 = LabelFrame(top, text="Negative Comments")
labelframe2.pack(fill="both", expand="yes")
bottomlabel = Label(labelframe2, text="Place to put the negative comments")
bottomlabel.pack()
top.mainloop()'''

#messagebox
'''
The messagebox module is used to display the message boxes in the python applications.
 There are the various functions which are used to display the relevant messages depending 
 upon the application requirements.'''

#showinfo()--The showinfo() messagebox is used where we need to show some relevant information to the user.
'''
from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("100x100")
messagebox.showinfo("information", "Information")
top.mainloop()
'''
#This method is used to display the warning to the user. Consider the following example.

# !/usr/bin/python3
'''
from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("100x100")
messagebox.showwarning("warning", "Warning")
top.mainloop()

'''
#This method is used to display the error message to the user. Consider the following example.

'''
from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("100x100")
messagebox.showerror("error", "Error")
top.mainloop()
'''
#This method is used to ask some question to the user which can be answered in yes or no.
# Consider the following example.

'''
from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("100x100")
messagebox.askquestion("Confirm", "Are you sure?")
top.mainloop()
'''

#This method is used to confirm the user's action regarding some application activity. Consider the following example.
'''
from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("100x100")
messagebox.askokcancel("Redirect", "Redirecting you to www.javatpoint.com")
top.mainloop()'''

#This method is used to ask the user about some action to which, the user can answer in yes or no.
# Consider the following example.
'''
from tkinter import *  
from tkinter import messagebox  
  
top = Tk()  
top.geometry("100x100")  
messagebox.askyesno("Application","Got It?")  
top.mainloop()

#This method is used to ask the user about doing a particular task again or not.
# Consider the following example.

from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("100x100")
messagebox.askretrycancel("Application", "try again?")
top.mainloop()'''