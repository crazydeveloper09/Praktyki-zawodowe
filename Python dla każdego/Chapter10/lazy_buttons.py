#!/usr/bin/env python3
# Autor: Maciej Kuta
# Data utworzenie: 10.10.2020
# Cel: Użycie przycisków

import tkinter

root = tkinter.Tk()
root.title("Leniwe przyciski")
root.geometry("325x200")

app = tkinter.Frame(root)

app.grid()

btn1 = tkinter.Button(app, text="Nic nie robię")
btn1.grid()
btn2 = tkinter.Button(app)
btn2.configure(text="Ja również")
btn2.grid()
btn3 = tkinter.Button(app)
btn3["text"] = "To samo mnie dotyczy"
btn3.grid()
root.mainloop()