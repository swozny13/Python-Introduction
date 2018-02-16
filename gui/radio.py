from tkinter import *


class RadioBox(Frame):

    def __init__(self, master):
        super(RadioBox, self).__init__(master)
        self.grid()
        self.create_fields()

    def create_fields(self):
        self.lbl = Label(self, text="Wybierz ulubioną potrawę: ").grid(row=0, column=0, sticky=W)

        self.favorite = StringVar()
        self.favorite.set(None)
        Radiobutton(self, text="schabowy", variable=self.favorite, value="schabowy", command=self.update_text).grid(
            row=1, column=0, sticky=W)
        Radiobutton(self, text="stek", variable=self.favorite, value="stek", command=self.update_text).grid(
            row=2, column=0, sticky=W)
        Radiobutton(self, text="sałatka", variable=self.favorite, value="sałatka", command=self.update_text).grid(
            row=3, column=0, sticky=W)
        Radiobutton(self, text="rosół", variable=self.favorite, value="rosół", command=self.update_text).grid(
            row=4, column=0, sticky=W)

        self.result_text = Text(self, width=40, height=5, wrap=WORD)
        self.result_text.grid(row=5, column=0, columnspan=3)

        self.button = Button(self, text="Prześlij").grid(row=6, column=2, sticky=W)

    def update_text(self):
        message = "Twoją ulubioną potrawą jest " + str(self.favorite.get()) + ". :)"

        self.result_text.delete(0.0, END)
        self.result_text.insert(0.0, message)


window = Tk()
window.title("RadioBox title")
window.geometry("300x250")
app = RadioBox(window)
app.mainloop()
