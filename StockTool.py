import yfinance as yf
from tkinter import *


def Hello():
    print("Hi I'm Daisy!!")


    
    
    

def srch():
    global mes
    stk = stock.get()
    stk = stk.upper()
    data = yf.Ticker(stk)
    stkmsg = data.major_holders
    holdit = data.institutional_holders
    mes.destroy()
    mes = Label(root,text= stkmsg)
    mes.place(x=100, y=50)
    print(holdit)
    
    
    

root = Tk()
root.geometry('600x400')
root.title("Stock Analyzer")
root.resizable(0,0)
stock = Entry(root, width = 30,)
stock.place(x=100, y=200)
mes = Label(root,text="Please enter a stock ticker symbol bellow", font='arial 15 bold')
mes.place(x=100, y=100)


Button(root,text= 'Search', font= 'arial 12', bg='#5CA', command = srch).place(x=150, y=300)


root.mainloop()