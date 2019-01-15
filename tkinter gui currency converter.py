from tkinter import *

root = Tk()
root.geometry("3840x2160")
root.title("Currency Converter")
root.configure(background='#00B6D5')

heading = Label(root, text = "WELCOME TO THE CURRENCY CONVERTER", font = ("arial 24 bold"), bg='#00B6D5').pack()

amount = Label(root, text = "Enter amount of money in Pounds: ", font = ("arial 18 bold"), bg = '#00B6D5').place(x=10, y=50)

value = IntVar()
inp = Entry(root, width = '50', textvariable = value).place(x=10, y=90)


def converterUS():
    valueCallUS = value.get()
    UScon = valueCallUS * 1.42
    USdisplay = Label(root, text = str(UScon) + " USD", font = ("arial, 22 bold"), bg = "red", fg = "white").place(x=10, y=200)

def converterEU():
    valueCallEU = value.get()
    EUcon = valueCallEU * 1.15
    EUdisplay = Label(root, text = str(EUcon) + " EUR", font = ("arial, 22 bold"), bg = "blue", fg = "gold").place(x=100, y=250)
   

USbtn = Button(root, text="Convert to USD", width=12, height=2, bg = "red", fg = "white", command = converterUS).place(x=10, y=130)

EUbtn = Button(root, text="Convert to EUR", width=12, height=2, bg = "blue", fg = "gold", command = converterEU).place(x=216, y=130)

root.mainloop()
