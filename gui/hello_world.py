import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.pack()
        self.create_fields()

    def create_fields(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=window.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("HELLO WORLD")


window = tk.Tk()
window.title("Hello world app GUI")
window.geometry("300x200")
app = Application(window)
app.mainloop()
