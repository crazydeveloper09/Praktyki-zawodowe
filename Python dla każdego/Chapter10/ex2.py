# Autor: Maciej Kuta
# Data utworzenie: 6.10.2020
# Cel: Przećwiczenie  wiedzy z warunków i pętli

import random, tkinter
tries = 1
number = random.randint(1, 100)
class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()

    def play(self):
        
        guess = int(self.num_input.get())
        

        while number != guess:
        
            if guess > number:
                self.big = tkinter.Label(self)
                self.big["text"] = self.num_input.get() + ": Ta liczba jest za duża"
                self.big.grid(row = 4, column = 0, columnspan = 2, sticky = "W")
                
            else:
                self.small = tkinter.Label(self)
                self.small["text"] = self.num_input.get() + ": Ta liczba jest za mała"
                self.small.grid(row = 4, column = 0, columnspan = 2, sticky = "W")
            self.create_input()
            guess = int(self.num_input.get())    
           
            tries += 1
        self.winner = tkinter.Label(self)
        self.winner["text"] = "Odgadłeś to! Ta liczba to: " + self.num_input.get()
        self.winner.grid(row = 4, column = 0, columnspan = 2, sticky = "W")
        
    def create_input(self): 
        self.num_label = tkinter.Label(self)
        self.num_label["text"] = "Twoja liczba:"
        self.num_label.grid(row = 1, column = 0, sticky = "W")
        
        self.num_input = tkinter.Entry(self)
        self.num_input.grid(row = 1, column = 1, sticky = "W")
        
        self.btn1 = tkinter.Button(self, command = self.play)
        self.btn1["text"] = "Sprawdź"
        self.btn1.grid(row = 2, column = 0, sticky = "W")
        
    def create_widget(self):
        self.title = tkinter.Label(self)
        self.title["text"] = "\t\tWitaj w grze 'Jaka to liczba' \n" \
                            "Mam na myśli pewną liczbę z zakresu od 1 do 100 \n" \
                            "Spróbuj ją odgadnąć w jak najmniejszej liczbie prób"
        self.title.grid(row = 0, column = 0, columnspan = 2, sticky = "W")
        
        self.create_input()
    

root = tkinter.Tk()
root.title("Jaka to liczba")

app = Application(root)


root.mainloop()