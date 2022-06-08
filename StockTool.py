import yfinance as yf
from tkinter import *


def share():
    global mes
    stk = stock.get()
    stk = stk.upper()
    data = yf.Ticker(stk)
    stkmsg = data.major_holders
    mes.destroy()
    mes = Label(root,text= stkmsg)
    mes.place(x=100, y=50)

def div():
    global mes
    stk = stock.get()
    stk = stk.upper()
    data = yf.Ticker(stk)
    divyield =  data.info['dividendYield']*100
    mes.destroy()
    mes = Label(root,text= divyield)
    mes.place(x=100, y=50)

def genInfo():
    global mes
    stk = stock.get()
    stk = stk.upper()
    data = yf.Ticker(stk)
    nam = data.info["shortName"]
    mes.destroy()
    mes = Label(root,text= nam)
    mes.place(x=100, y=50)

def holdr():
    global mes
    stk = stock.get()
    stk = stk.upper()
    data = yf.Ticker(stk)
    hol = data.institutional_holders
    mes.destroy()
    mes = Label(root,text= hol)
    mes.place(x=50, y=50)

def clearit():
    global mes
    mes.destroy()
    mes = Label(root,text="Please enter a stock ticker symbol bellow", font='arial 15 bold')
    mes.place(x=100, y=100)

root = Tk()
root.geometry('600x400')
root.title("Stock Analyzer")
root.resizable(0,0)
stock = Entry(root, width = 30,)
stock.place(x=100, y=200)
mes = Label(root,text="Please enter a stock ticker symbol bellow", font='arial 15 bold')
mes.place(x=100, y=100)


but1 = Button(root,text= 'Name', font= 'arial 12', bg='#5CA', command = genInfo).place(x=80, y=300)
but2 = Button(root,text= 'Dividend', font= 'arial 12', bg='#5AC', command = div).place(x=170, y=300)
but3 = Button(root,text= 'Ownership', font= 'arial 12', bg='#A5C', command = share).place(x=280, y=300)
but4 = Button(root,text= 'Holders', font= 'arial 12', bg='#CA5', command = holdr).place(x=400, y=300)
clr = Button(root, text= 'Clear', font= 'arial 12', bg='#5FF', command= clearit).place(x=300, y=350)

root.mainloop()
