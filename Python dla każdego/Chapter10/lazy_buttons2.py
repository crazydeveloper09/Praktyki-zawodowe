#!/usr/bin/env python3
# Autor: Maciej Kuta
# Data utworzenie: 10.10.2020
# Cel: Użycie przycisków przy użyciu klas

import tkinter

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.btn1 = tkinter.Button(self, text="Nic nie robię")
        self.btn1.grid()
        self.btn2 = tkinter.Button(self)
        self.btn2.configure(text="Ja również")
        self.btn2.grid()
        self.btn3 = tkinter.Button(self)
        self.btn3["text"] = "To samo mnie dotyczy"
        self.btn3.grid()

root = tkinter.Tk()
root.title("Leniwe przyciski 2.0")
root.geometry("325x200")

app = Application(root)


root.mainloop()