#!/usr/bin/env python3
# Autor: Maciej Kuta
# Data utworzenie: 10.10.2020
# Cel: Użycie zdarzeń na widżetach

import tkinter

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.btn_clicks = 0
        self.create_widget()
    def update_count(self):
        self.btn_clicks += 1
        self.btn1["text"] = "Licznik kliknięć: " + str(self.btn_clicks)
    def create_widget(self):
        self.btn1 = tkinter.Button(self)
        self.btn1["text"] = "Licznik kliknięć: " + str(self.btn_clicks)
        self.btn1["command"] = self.update_count
        self.btn1.grid()
    

root = tkinter.Tk()
root.title("Licznik kliknięć")
root.geometry("325x200")

app = Application(root)


root.mainloop()