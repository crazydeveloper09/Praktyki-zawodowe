#!/usr/bin/env python3
# Autor: Maciej Kuta
# Data utworzenie: 10.10.2020
# Cel: Podusumowanie orzdziału - gra mad lib
import tkinter

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def reveal(self):
        person = self.person_input.get()
        noun = self.noun_input.get()
        verb = self.verb_input.get()
        adjectives = ""
        if self.adject1.get():
            adjectives += "naglące, "
        if self.adject2.get():
            adjectives += "radosne, "
        if self.adject3.get():
            adjectives += "elektryzujące, "
        body_part = self.body.get()

        # create the story
        story = "Sławny badacz i odkrywca "
        story += person
        story += " o mało co nie zrezygnował z życiowej misji poszukiwania "
        story += "zaginionego miasta, które zamieszkiwały "
        story += noun
        story += ", gdy pewnego dnia "
        story += noun
        story += " znalazły "
        story += person + "a. "
        story += "Silne, "
        story += adjectives
        story += "osobliwe uczucie owładnęło badaczem. "
        story += "Po tak długim czasie poszukiwanie wreszcie się zakończyło. W oku "
        story += person + "a pojawiła się łza, która spadła na jego "
        story += body_part + ". "
        story += "A wtedy "
        story += noun
        story += " szybko pożarły "
        story += person + "a. "
        story += "Jaki morał płynie z tego opowiadania? Pomyśl, zanim zaczniesz coś "
        story += verb
        story += "."


        self.answer.delete(0.0, "end")
        self.answer.insert(0.0, story)
    def create_widgets(self):
        self.title = tkinter.Label(self)
        self.title["text"] = "Wprowadź informacje do nowego opowiadania"
        self.title.grid(row = 0, column = 0, columnspan = 2, sticky = "W")

        self.person_label = tkinter.Label(self)
        self.person_label["text"] = "Osoba:"
        self.person_label.grid(row = 1, column = 0, sticky = "W")
        self.person_input = tkinter.Entry(self)
        self.person_input.grid(row = 1, column = 1, sticky = "W")

        self.noun_label = tkinter.Label(self)
        self.noun_label["text"] = "Rzeczownik w liczbie mnogiej:"
        self.noun_label.grid(row = 2, column = 0, sticky = "W")
        self.noun_input = tkinter.Entry(self)
        self.noun_input.grid(row = 2, column = 1, sticky = "W")

        self.verb_label = tkinter.Label(self)
        self.verb_label["text"] = "Czasownik:"
        self.verb_label.grid(row = 3, column = 0, sticky = "W")
        self.verb_input = tkinter.Entry(self)
        self.verb_input.grid(row = 3, column = 1, sticky = "W")

        self.checkbox_label = tkinter.Label(self)
        self.checkbox_label["text"] = "Przymiotnik(i):"
        self.checkbox_label.grid(row = 4, column = 0, sticky = "W")

        self.adject1 = tkinter.BooleanVar(self)
        tkinter.Checkbutton(self,
                            text = "naglące",
                            variable = self.adject1
                            ).grid(row = 4, column = 1, sticky = "W")

        self.adject2 = tkinter.BooleanVar(self)
        tkinter.Checkbutton(self,
                            text = "radosne",
                            variable = self.adject2
                            ).grid(row = 4, column = 2, sticky = "W")

        self.adject3 = tkinter.BooleanVar(self)
        tkinter.Checkbutton(self,
                            text = "elektryzujące",
                            variable = self.adject3
                            ).grid(row = 4, column = 3, sticky = "W")

        self.radio_label = tkinter.Label(self)
        self.radio_label["text"] = "Część ciała:"
        self.radio_label.grid(row = 5, column = 0, sticky = "W")

        self.body = tkinter.StringVar()
        self.body.set(None)

        tkinter.Radiobutton(self,
                            text = "pępek",
                            variable = self.body,
                            value = "pępek"
                            ).grid(row = 5, column = 1, sticky = "W")

        
        tkinter.Radiobutton(self,
                            text = "duży palec u nogi",
                            variable = self.body,
                            value = "duży palec u nogi"
                            ).grid(row = 5, column = 2, sticky = "W")

       
        tkinter.Radiobutton(self,
                            text = "rdzeń przedłużony",
                            variable = self.body,
                            value = "rdzeń przedłużony"
                            ).grid(row = 5, column = 3, sticky = "W")
        self.btn1 = tkinter.Button(self, command = self.reveal)
        self.btn1["text"] = "Kliknij, by wyświelić opowiadanie"
        self.btn1.grid(row = 6, column = 0, sticky = "W")
        self.answer = tkinter.Text(self, width = 75, height = 15, wrap = "word")
        self.answer.grid(row = 7, column = 1, columnspan = 2, sticky = "W")
    

root = tkinter.Tk()
root.title("Mad Lib")


app = Application(root)


root.mainloop()