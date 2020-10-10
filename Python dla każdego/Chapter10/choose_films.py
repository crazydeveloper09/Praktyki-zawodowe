#!/usr/bin/env python3
# Autor: Maciej Kuta
# Data utworzenie: 10.10.2020
# Cel: Użycie Checkbuttona i BooleanVar

import tkinter

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def reveal(self):
        message = ""
        if self.comedy.get():
            message += "Lubisz filmy komediowe. \n"
        if self.drama.get():
            message += "Lubisz filmy dramatyczne. \n"
        if self.romans.get():
            message += "Lubisz filmy romantyczne. \n"
        self.answer.delete(0.0, "end")
        self.answer.insert(0.0, message)
    def create_widgets(self):
        self.title = tkinter.Label(self)
        self.title["text"] = "Wybierz swoje ulubione gatunki filmów"
        self.title.grid(row = 0, column = 0, columnspan = 2, sticky = "W")

        self.checkbox_label = tkinter.Label(self)
        self.checkbox_label["text"] = "Zaznacz wszystkie, które chciałbyś wybrać"
        self.checkbox_label.grid(row = 1, column = 0, columnspan = 2, sticky = "W")

        self.comedy = tkinter.BooleanVar(self)
        tkinter.Checkbutton(self,
                            text = "komedia",
                            variable = self.comedy,
                            command = self.reveal
                            ).grid(row = 2, column = 0, sticky = "W")

        self.drama = tkinter.BooleanVar(self)
        tkinter.Checkbutton(self,
                            text = "dramat",
                            variable = self.drama,
                            command = self.reveal
                            ).grid(row = 3, column = 0, sticky = "W")

        self.romans = tkinter.BooleanVar(self)
        tkinter.Checkbutton(self,
                            text = "romans",
                            variable = self.romans,
                            command = self.reveal
                            ).grid(row = 4, column = 0, sticky = "W")

        self.answer = tkinter.Text(self, width = 35, height = 5, wrap = "word")
        self.answer.grid(row = 5, column = 0, columnspa = 2, sticky = "W")
    

root = tkinter.Tk()
root.title("Wybór filmów")
root.geometry("325x300")

app = Application(root)


root.mainloop()