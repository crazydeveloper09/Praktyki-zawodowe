#!/usr/bin/env python3
# Autor: Maciej Kuta
# Data utworzenie: 10.10.2020
# Cel: Użycie opcji

import tkinter

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def reveal(self):
        message = "Twoim ulubionym gatunkiem jest " + self.favourite.get()
        self.answer.delete(0.0, "end")
        self.answer.insert(0.0, message)
    def create_widgets(self):
        self.title = tkinter.Label(self)
        self.title["text"] = "Wybierz swój ulubiony gatunek filmu"
        self.title.grid(row = 0, column = 0, columnspan = 2, sticky = "W")

        self.checkbox_label = tkinter.Label(self)
        self.checkbox_label["text"] = "Wybierz jeden gatunek"
        self.checkbox_label.grid(row = 1, column = 0, columnspan = 2, sticky = "W")

        self.favourite = tkinter.StringVar()
        self.favourite.set(None)

        tkinter.Radiobutton(self,
                            text = "komedia",
                            variable = self.favourite,
                            value = "komedia.",
                            command = self.reveal
                            ).grid(row = 2, column = 0, sticky = "W")

        
        tkinter.Radiobutton(self,
                            text = "dramat",
                            variable = self.favourite,
                            value = "dramat.",
                            command = self.reveal
                            ).grid(row = 3, column = 0, sticky = "W")

       
        tkinter.Radiobutton(self,
                            text = "romans",
                            variable = self.favourite,
                            value = "romans.",
                            command = self.reveal
                            ).grid(row = 4, column = 0, sticky = "W")

        self.answer = tkinter.Text(self, width = 35, height = 5, wrap = "word")
        self.answer.grid(row = 5, column = 0, columnspa = 2, sticky = "W")
    

root = tkinter.Tk()
root.title("Wybór filmów 2.0")
root.geometry("325x300")

app = Application(root)


root.mainloop()