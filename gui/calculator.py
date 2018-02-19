from tkinter import *


class Calculator(Frame):

    def __init__(self, master):
        super(Calculator, self).__init__(master)
        self.grid()
        self.create_widgets()
        # self.btn7 = 7

    def create_widgets(self):
        # results
        self.results = Text(self, height=3, width=23).grid(row=0, column=0, columnspan=4, sticky=W)

        # digits
        self.btn7 = Button(self, text=7, height=3, width=5).grid(row=1, column=0, sticky=W)
        self.btn8 = Button(self, text=8, height=3, width=5).grid(row=1, column=1, sticky=W)
        self.btn9 = Button(self, text=9, height=3, width=5).grid(row=1, column=2, sticky=W)
        self.btn4 = Button(self, text=4, height=3, width=5).grid(row=2, column=0, sticky=W)
        self.btn5 = Button(self, text=5, height=3, width=5).grid(row=2, column=1, sticky=W)
        self.btn6 = Button(self, text=6, height=3, width=5).grid(row=2, column=2, sticky=W)
        self.btn1 = Button(self, text=1, height=3, width=5).grid(row=3, column=0, sticky=W)
        self.btn2 = Button(self, text=2, height=3, width=5).grid(row=3, column=1, sticky=W)
        self.btn3 = Button(self, text=3, height=3, width=5).grid(row=3, column=2, sticky=W)
        self.btn0 = Button(self, text=0, height=3, width=5).grid(row=4, column=0, sticky=W)

        # point
        self.dot = Button(self, text=".", height=3, width=5).grid(row=4, column=1, sticky=W)

        # remove
        self.delete = Button(self, text="C", height=3, width=5).grid(row=4, column=2, sticky=W)

        # functions
        self.addition = Button(self, text="+", height=3, width=5).grid(row=1, column=3, sticky=W)
        self.subtraction = Button(self, text="-", height=3, width=5).grid(row=2, column=3, sticky=W)
        self.multiplication = Button(self, text="*", height=3, width=5).grid(row=3, column=3, sticky=W)
        self.division = Button(self, text="/", height=3, width=5).grid(row=4, column=3, sticky=W)

        # equal
        self.equals = Button(self, text="=", height=3, width=25).grid(row=5, column=0,
                                                                      columnspan=4,
                                                                      sticky=W)


window = Tk()
window.title("CALCULATOR")
app = Calculator(window)
app.mainloop()
