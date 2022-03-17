from tkinter import *
root = Tk()
root.title('Tkinterlator')
e = Entry(root,width=35,borderwidth=2)
e.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

def buttonClick(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number)) 
def buttonClear():
    e.delete(0,END)

def buttonEqual():
    sn = e.get() # will be our second number passed into calc
    e.delete(0,END) # clears screen
    if math == 'addition':
        e.insert(0, int(fn)+int(sn))
    if math == 'subtract':
        e.insert(0,int(fn)-int(sn))
    if math == 'multiply':
        e.insert(0,int(fn)*int(sn))
    if math == 'divide':
        e.insert(0,int(fn)/int(sn))

    

def buttonAdd():
    func = 'addition'
    global math
    math = func
    n = e.get() #first number in calc
    global fn # first number, made into global var
    fn = int(n)
    e.delete(0,END)


def buttonSubtract():
    func = 'subtract'
    global math
    math = func
    n = e.get() #first number in calc
    global fn # first number, made into global var
    fn = int(n) #first number as a global variable
    e.delete(0,END)


def buttonMultiply():
    func = 'multiply'
    global math
    math = func
    n = e.get() #first number in calc
    global fn # first number, made into global var
    fn = int(n)
    e.delete(0,END)


def buttonDivide():
    func = 'divide'
    global math
    math = func
    n = e.get() #first number in calc
    global fn # first number, made into global var
    fn = int(n)
    e.delete(0,END)

            
b1 = Button(root,text='1',padx=10,pady=10,command= lambda: buttonClick(1))
b2 = Button(root,text='2',padx=10,pady=10,command=lambda: buttonClick(2))
b3 = Button(root,text='3',padx=10,pady=10,command=lambda: buttonClick(3))
b4 = Button(root,text='4',padx=9,pady=10,command=lambda: buttonClick(4))
b5 = Button(root,text='5',padx=10,pady=10,command=lambda: buttonClick(5))
b6 = Button(root,text='6',padx=10,pady=10,command=lambda: buttonClick(6))
b7 = Button(root,text='7',padx=10,pady=10,command=lambda: buttonClick(7))
b8 = Button(root,text='8',padx=10,pady=10,command=lambda: buttonClick(8))
b9 = Button(root,text='9',padx=10,pady=10,command=lambda: buttonClick(9))
b0 = Button(root,text='0',padx=10,pady=10,command=lambda: buttonClick(0))
b_add = Button(root,text='+',padx=10,pady=10,command=buttonAdd)
b_clear = Button(root,text='C',padx=9.5,pady=10,command=buttonClear)
b_equals = Button(root,text='=',padx=10,pady=10,command=buttonEqual)
b_divide = Button(root,text='/',padx=11,pady=10,command=buttonDivide)
b_subtract = Button(root,text='-',padx=10,pady=10,command=buttonSubtract)
b_multiply = Button(root,text='*',padx=10,pady=10,command=buttonMultiply)


b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)

b0.grid(row=4,column=0)
b_clear.grid(row=4,column=1)
b_equals.grid(row=4,column=2)
b_add.grid(row=1,column=3)
b_subtract.grid(row=2,column=3)
b_multiply.grid(row=3,column=3)
b_divide.grid(row=4,column=3)


root.mainloop()

