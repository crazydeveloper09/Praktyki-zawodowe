#!/usr/bin/env python3
# Autor: Maciej Kuta
# Data utworzenie: 10.10.2020
# Cel: Użycie etykiet

import tkinter

root = tkinter.Tk()
root.title("Metkownica")
root.geometry("325x200")

app = tkinter.Frame(root)

app.grid()

lbl = tkinter.Label(app, text="Jestem etykietą")
lbl.grid()

root.mainloop()