from tkinter import *


class CheckBox(Frame):

    def __init__(self, master):
        super(CheckBox, self).__init__(master)
        self.grid()
        self.create_fields()

    def create_fields(self):
        self.init_label = Label(self, text=" Wybierz swoje ulubione dyscypliny sportowe:").grid(row=0, column=0,
                                                                                                sticky=W)
        self.check_footbal = BooleanVar()
        Checkbutton(self, text="piłka nożna", variable=self.check_footbal, command=self.update_text).grid(row=1,
                                                                                                          column=0,
                                                                                                          sticky=W)
        self.check_basketball = BooleanVar()
        Checkbutton(self, text="koszykówka", variable=self.check_basketball, command=self.update_text).grid(row=2,
                                                                                                            column=0,
                                                                                                            sticky=W)
        self.check_voleyball = BooleanVar()
        Checkbutton(self, text="siatkówka", variable=self.check_voleyball, command=self.update_text).grid(row=3,
                                                                                                          column=0,
                                                                                                          sticky=W)
        self.check_snooker = BooleanVar()
        Checkbutton(self, text="snooker", variable=self.check_snooker, command=self.update_text).grid(row=4,
                                                                                                      column=0,
                                                                                                      sticky=W)

        self.info_text = Text(self, width=40, height=5, wrap=WORD)
        self.info_text.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        options = ""

        if self.check_footbal.get():
            options += "Lubisz piłkę nożną \n"
        if self.check_basketball.get():
            options += "Lubisz koszykówkę \n"
        if self.check_voleyball.get():
            options += "Lubisz siatkówkę \n"
        if self.check_snooker.get():
            options += "Lubisz snookera \n"

        self.info_text.delete(0.0, END)
        self.info_text.insert(0.0, options)


window = Tk()
window.title("Check boxes")
window.geometry("300x250")
app = CheckBox(window)
app.mainloop()
