# Autor: Maciej Kuta
# Data utworzenie: 8.10.2020
# Tytuł: Turniej wiedzy 3.0
# Cel: Zmodyfikowanie poprzedniej wersji w celu dodania najlepszych wyników

import sys, pickle, shelve

def open_file(name, mode):
    try:
        file = open(name, mode)
        return file
    except IOError as e:
        print("Nie ma takiego pliku")
        print(e)
        input("\n\nNaciśnij klawisz Enter, aby zakończyć działanie programu")
        sys.exit()
    else:
        return file

def next_line(the_file):
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line
def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    points = next_line(the_file)
    return category, question, answers, correct, explanation, points

def welcome(title):
    print("\t\t\t Witaj w turnieju wiedzy")
    print("\t\t\t", title, "\n")

def main():
    file = open_file("kwiz_punkty.txt", "r")
    title = next_line(file)
    welcome(title)
    score = 0
    category, question, answers, correct, explanation, points = next_block(file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])
        answer = input("Jaka jest twoja odpowiedź? ")
        if answer == correct:
            print("Gratulacje")
            score += int(points)
        else:
            print("Niewłasciwy wybór")
           
        
        print(explanation)
        category, question, answers, correct, explanation, points = next_block(file)
    file.close()
    print("To było ostatnie pytanie!")
    name = input("Podaj swoje imię ")
    s = shelve.open("best_results.dat")
    
    s["wynik"] = [name, score]
    s.sync()
    s.close()

    print("Twój końcowy wynik wynosi", score)
main()
input("\n\nNaciśnij klawisz Enter, aby zakończyć działanie programu")