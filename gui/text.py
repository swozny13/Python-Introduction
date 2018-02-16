from tkinter import *


class TextApp(Frame):

    def __init__(self, master):
        super(TextApp, self).__init__(master)
        self.grid()
        self.create_fields()

    def create_fields(self):
        self.lbl = Label(self, text="LOGOWANIE")
        self.lbl.grid(row=0, column=1, sticky=W)

        self.login_label = Label(self, text="Podaj login: ")
        self.login_label.grid(row=1, column=0, sticky=W)

        self.login_entry = Entry(self)
        self.login_entry.grid(row=1, column=1, sticky=W)

        self.password_label = Label(self, text="Podaj hasło: ")
        self.password_label.grid(row=2, column=0, sticky=W)

        self.pasword_entry = Entry(self)
        self.pasword_entry.grid(row=2, column=1, sticky=W)

        self.send_button = Button(self, text="Akceptuj", command=self.check_login)
        self.send_button.grid(row=3, column=1, sticky=W)

        self.info_field = Text(self, width=30, height=5, wrap=WORD)
        self.info_field.grid(row=5, column=0, columnspan=2, sticky=W)

    def check_login(self):
        login = self.login_entry.get()
        password = self.pasword_entry.get()

        if login == 'admin' and password == 'admin':
            message = "Hasło i login poprawne!"
        else:
            message = "Hasło lub login niepoprawne!"

        self.info_field.delete(0.0, END)
        self.info_field.insert(0.0, message)


window = Tk()
window.title("Working with text")
window.geometry("300x200")
app = TextApp(window)
window.mainloop()
