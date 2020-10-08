# Autor: Maciej Kuta
# Data utworzenie: 8.10.2020
# Cel: Demonstracja zwracania i pobierania wartości funkcji

def display(message):
    print(message)

def give_me_five():
    
    return 5

def yes_or_no(question):
    answer = None
    while answer not in ("t", "n")
        answer = input(question)
    return answer
display("To wiadomość dla Ciebie")

number = give_me_five()
print("Oto, co otrzymałem z funkcji give_me_five():", number)

answer = yes_or_no("\nProszę wprowadzić \'t\' lub \'n\': ")
print("Dziękuję za wprowadzenie", answer)

input("\n\nNaciśnij klawisz Enter, aby zakończyć działąnie programu")