import math
import tkinter
from tkinter import *
from tkinter import ttk, Entry
from tkinter import messagebox as m
from warnings import showwarning
import matplotlib.pyplot as mt
import numpy as np



initial_width = 600
initial_height = 350

window_width = initial_width
window_height = initial_height


aken = Tk()

aken.geometry(f'{window_width}x{window_height}')
aken.title('Решение кв. уравнений')
#aken.iconbitmap('math.ico')
tekst = 'Решение квадратного уравнения'
k = 0
str0 = ".,:;!_*-+()/#¤%&"
str1 = 'qwertyuiopasdfghjklzxcvbnm'
step = 4
roundTo=1

def equals():
    try:

        a_ = float(tekstbox1.get())
        b_ = float(tekstbox2.get())
        c_ = float(tekstbox3.get())

        solution = b_ * b_ - 4 * a_ * c_
        if solution > 0:
            x1_ = round((-1 * b_ + math.sqrt(solution)) / (2 * a_), 2)
            x2_ = round((-1 * b_ - math.sqrt(solution)) / (2 * a_), 2)
            pealkiri2.config(text=f"D = {solution}\nx1 = {x1_}\nx2 = {x2_}")
        elif solution == 0:
            x1_ = round((-1 * b_) / (2 * a_), 2)
            pealkiri2.config(text=f"D = {solution}\nx1 = {x1_}")
        else:
            pealkiri2.config(text=f'Корней нет!')

    except ValueError:
        pealkiri2.config(text="Ошибка ввода чисел")






def tekst1_psse():
    t = tekstbox1.get()
    t2 = tekstbox2.get()
    t3 = tekstbox3.get()
    if t or t2 or t3 == str0 or str1:
        m.showwarning('Только цифры')
    else:
        pealkiri2.configure()
        tekstbox1.delete(0, END)
        tekstbox2.delete(0, END)
        tekstbox3.delete(0, END)


def Kala():
    x1 = np.arange(0, 9.5, 0.5) #min max step
    y1=(2/27)*x1*x1-3
    x2 = np.arange(-10, 0.5, 0.5)#min max step
    y2=0.04*x2*x2-3
    x3 =np.arange(-9, -2.5, 0.5) #min max step
    np.arange(-9, -2.5, 0.5) #min max step
    y3=(2/9)*(x3+6)**2+1
    x4 = np.arange(-3, 9.5, 0.5) #min max step
    y4=(-1/12)*(x4-3)**2+6
    x5 = np.arange(5, 9, 0.5) #min max step
    y5=(1/9)*(x5-5)**2+2
    x6 = np.arange(5, 8.5, 0.5) #min max step
    y6=(1/8)*(x6-7)**2+1.5
    x7 = np.arange(-13, -8.5, 0.5) #min max step
    y7=(-0.75)*(x7+11)**2+6
    x8 = np.arange(-15, -12.5, 0.5) #min max step
    y8=(-0.5)*(x8+13)**2+3
    x9= np.arange(-15, -10, 0.5)#min max step
    y9=[1]*len(x9)
    #x10 = np.arange(3, 4, 0.5)#min max step
    #y10=[3]*len(x10)
    mt.figure()
    mt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9)
    mt.show()

def prillid():
    x1 = np.arange(-9,-1)
    y1 = -1*1/16*(x1 + 5)**2+2
    x2 = np.arange(1,9)
    y2 = -1*1/16*(x2 -5)**2+2
    x3 = np.arange(-9, -1)
    y3 = 1/4*(x3+5)**2-3
    x4 = np.arange(1, 9)
    y4 = 1/4*(x4 - 5)**2-3
    x5 = np.arange(-9,-6)
    y5 = -1*(x5-5)**2+5
    x6 = np.arange(6, 9)
    #y6 =
    mt.figure()
    mt.plot(x1, y1 )
    mt.show()


def graph():
    a_ = float(tekstbox1.get())
    b_ = float(tekstbox2.get())
    c_ = float(tekstbox3.get())
    x = round(abs(b_) / (2 * a_), roundTo)
    x1 = np.arange(x - step, x + step, float(f"0.{step}"))
    y = a_ * x ** 2 + b_ * x1 + c_
    y1 = a_ * x1 ** 2 + b_ * x1 + c_
    fig = mt.figure()
    mt.plot(x1, y1, 'b-d')
    mt.title('Ruutvõrrand')
    mt.ylabel('y')
    mt.xlabel('x')
    mt.grid(True)
    mt.show()






def suurenda_ja_vahenda():
    global window_width, window_height
    if window_width == initial_width and window_height == initial_height:
        window_width += 100
        window_height += 100
        kala.configure(state='normal')

    else:
        window_width = initial_width
        window_height = initial_height
        kala.configure(state='disabled')
    aken.geometry(f'{window_width}x{window_height}')





pealkiri = Label(
    aken,
    text=tekst,
    bg='green',
    fg='black',
    font='Calibri 15',
    height=4,
    width=len(tekst),
    cursor='cross'
)
tekst2 = 'x**2+'
tekst_ = Label(
    aken,
    text=tekst2,
    fg='red',
    font='Calibri 15',
    height=2,
    width=len(tekst2)
)
tekst3 = 'x+'
tekst_2 = Label(
    aken,
    text=tekst3,
    fg='red',
    font='Calibri 15',
    height=2,
    width=len(tekst3)
)
tekst4 = '=0'
tekst_3 = Label(
    aken,
    text=tekst4,
    fg='red',
    font='Calibri 15',
    height=2,
    width=len(tekst3)
)
tekstbox1 = Entry(
    aken,
    bg='green',
    fg='black',
    font='Calibri 15',
    width=6,
    cursor='cross'
)
tekstbox2 = Entry(
    aken,
    bg='green',
    fg='black',
    font='Calibri 15',
    width=6,
    cursor='cross',

)
tekstbox3 = Entry(
    aken,
    bg='green',
    fg='black',
    font='Calibri 15',
    width=6,
    cursor='cross'
)
pealkiri2 = Label(
    aken,
    text='',
    bg='green',
    fg='black',
    font='Calibri 15',
    height=4,
    width=len(tekst),
    cursor='cross',

)



nupp = Button(
    aken,
    text='Решить',
    bg='green',
    fg='black',
    font='Calibri 15',
    width=6,
    cursor='cross',
    command=equals
)
graffik = Button(
    aken,
    text='Граффик',
    bg='green',
    fg='black',
    font='Calibri 15',
    width=6,
    command = graph
)
suurend = Button(
    aken,
    text = 'Размер экрана',
    bg='green',
    fg='black',
    font='Calibri 15',
    width=15,
    command = suurenda_ja_vahenda
)

var = IntVar()
kala = Radiobutton(aken, text = 'Кит', variable = var, value = 1, font='Calibri 15', command=Kala)
prill = Radiobutton(aken, text = 'Очки', variable = var, value = 1, font='Calibri 15', command=prillid)



kala.config(state='disabled')

pealkiri.pack()
tekstbox1.place(x=0, y=118)
# tekstbox1.pack(anchor = SW, pady = 20)
tekst_.place(x=80, y=111)
tekstbox2.place(x=140, y=118)
tekst_2.place(x=220, y=111)
tekstbox3.place(x=250, y=118)
tekst_3.place(x=330, y=111)
nupp.place(x=370, y=118)
pealkiri2.place(x=170, y=160)
graffik.place(x=470, y=118)
suurend.place(x=200, y =270)
kala.place(x=200, y =350)
prill.place(x=200, y =390)

aken.mainloop()
