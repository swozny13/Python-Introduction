from tkinter import *


class App(Frame):

    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.create_label()
        self.create_buttons()
        self.btn_clicks = 0

    def update_button_count(self):
        self.btn_clicks += 1
        self.b2["text"] = "Kliknąłeś: " + str(self.btn_clicks) + " razy"

    def create_label(self):
        self.l1 = Label(self, text="Kliknij tu: ")
        self.l1.grid()

    def create_buttons(self):
        self.b1 = Button(self, text="Klikaj")
        self.b1.grid()

        self.b2 = Button(self)
        self.b2["text"] = "Kliknałeś: 0 razy"
        self.b2["command"] = self.update_button_count
        self.b2.grid()

        self.b3 = Button(self, text="Open")
        self.b3.grid()


window = Tk()
window.title("Przyciski")
window.geometry("600x300")
app = App(window)
window.mainloop()
