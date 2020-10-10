#!/usr/bin/env python3
# Autor: Maciej Kuta
# Data utworzenie: 10.10.2020
# Cel: Użycie Entry, Text i grida

import tkinter

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def reveal(self):
        password  = self.password_input.get()
        if password == "sekret":
            message = "Oto tajemny przepis na dożycie 100 lat: dożyj 99 lat, " \
                        "a potem bądź BARDZO ostrożny."
        else:
            message = "To nie jest poprawne hasło, więc nie mogę się z Tobą " \
            "podzielić swoim sekretem."
        self.answer.delete(0.0, "end")
        self.answer.insert(0.0, message)
    def create_widgets(self):
        self.title = tkinter.Label(self)
        self.title["text"] = "Wprowadź hasło do sekretu długowieczności"
        self.title.grid(row = 0, column = 0, columnspan = 2, sticky = "W")
        self.password_label = tkinter.Label(self)
        self.password_label["text"] = "Hasło:"
        self.password_label.grid(row = 1, column = 0, sticky = "W")
        self.password_input = tkinter.Entry(self)
        self.password_input.grid(row = 1, column = 1, sticky = "W")
        self.btn1 = tkinter.Button(self, command = self.reveal)
        self.btn1["text"] = "Akceptuj"
        self.btn1.grid(row = 2, column = 0, sticky = "W")
        self.answer = tkinter.Text(self, width = 35, height = 5, wrap = "word")
        self.answer.grid(row = 3, column = 0, columnspa = 2, sticky = "W")
    

root = tkinter.Tk()
root.title("Długowieczność")
root.geometry("325x200")

app = Application(root)


root.mainloop()