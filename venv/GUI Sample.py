from tkinter import *
import tkinter.font as font

window = Tk()
window.geometry("380x400")
window.title("calculator")
window.resizable(0, 0)
window.configure(bg="black")

textinput = StringVar()
operator = ""

pad = Entry(window, font=("Courier New", 25, 'bold'), width=17, bg='cyan', bd=7, textvar=textinput)
pad.pack(ipady=25)

customFont = font.Font(family='Calibri', size=12, weight='bold')


def click(number):
    global operator
    operator = operator + str(number)
    textinput.set(operator)


def equal_but():
    global operator
    add = str(eval(operator))
    textinput.set(add)
    operator = ''


DoubleZeroButton = Button(window, padx=15, pady=14, bd=4, bg='white', text="00", font=customFont,
                          command=lambda: click(00))
DoubleZeroButton.place(x=10, y=330)

OneButton = Button(window, padx=20, pady=14, bd=4, bg='white', text="1", font=customFont,
                   command=lambda: click(1))
OneButton.place(x=10, y=260)

FourButton = Button(window, padx=20, pady=14, bd=4, bg='white', text="4", font=customFont,
                    command=lambda: click(4))
FourButton.place(x=10, y=190)

SevenButton = Button(window, padx=20, pady=14, bd=4, bg='white', text="7", font=customFont,
                     command=lambda: click(7))
SevenButton.place(x=10, y=120)

ZeroButton = Button(window, padx=20, pady=14, bd=4, bg='white', text="0", font=customFont,
                    command=lambda: click(0))
ZeroButton.place(x=85, y=330)

DotButton = Button(window, padx=22, pady=14, bd=4, bg='white', text=".", font=customFont,
                   command=lambda: click("."))
DotButton.place(x=160, y=330)

TwoButton = Button(window, padx=20, pady=14, bd=4, bg='white', text="2", font=customFont,
                   command=lambda: click(2))
TwoButton.place(x=85, y=260)

FiveButton = Button(window, padx=20, pady=14, bd=4, bg='white', text="5", font=customFont,
                    command=lambda: click(5))
FiveButton.place(x=85, y=190)

EightButton = Button(window, padx=20, pady=14, bd=4, bg='white', text="8", font=customFont,
                     command=lambda: click(8))
EightButton.place(x=85, y=120)

ThreeButton = Button(window, padx=20, pady=14, bd=4, bg='white', text="3", font=customFont,
                     command=lambda: click(3))
ThreeButton.place(x=160, y=260)

SixButton = Button(window, padx=20, pady=14, bd=4, bg='white', text="6", font=customFont,
                   command=lambda: click(6))
SixButton.place(x=160, y=190)

NineButton = Button(window, padx=20, pady=14, bd=4, bg='white', text="9", font=customFont,
                    command=lambda: click(9))
NineButton.place(x=160, y=120)

ModButton = Button(window, padx=19, pady=14, bd=4, bg='white', text="%", font=customFont,
                   command=lambda: click("%"))
ModButton.place(x=235, y=260)

ClearButton = Button(window, padx=20, pady=14, bd=4, bg='white', text="C", font=customFont)
ClearButton.place(x=235, y=190)

BackButton = Button(window, padx=19, pady=14, bd=4, bg='white', text="<", font=customFont)
BackButton.place(x=235, y=120)

DivButton = Button(window, padx=21, pady=14, bd=4, bg='cyan', text="/", font=customFont,
                   command=lambda: click("/"))
DivButton.place(x=310, y=120)

MulButton = Button(window, padx=19, pady=14, bd=4, bg='cyan', text="x", font=customFont,
                   command=lambda: click("x"))
MulButton.place(x=310, y=190)

PlusButton = Button(window, padx=18, pady=14, bd=4, bg='cyan', text="+", font=customFont,
                    command=lambda: click("+"))
PlusButton.place(x=310, y=260)

EqualButton = Button(window, padx=56, pady=14, bd=4, bg='cyan', text="=", font=customFont, command=equal_but)
EqualButton.place(x=235, y=330)

window.mainloop()
