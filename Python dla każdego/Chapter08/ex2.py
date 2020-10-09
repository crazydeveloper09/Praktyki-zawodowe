# Autor: Maciej Kuta
# Data utworzenie: 9.10.2020
# Tytuł: Telewizor
# Cel: Przećwiczenie klas

class Television(object):
    def __init__(self, brand, model, volume = 1, channel = ["TVP", "Eurosport", "Nsport", "Vh1", "Eleven Sport"]):
        self.brand = brand
        self.model = model
        self.volume = volume
        self.channel = channel
    def choose_channel(self, channel):
        if channel in range(5):
            print("Wybrałeś kanał: ", self.channel[channel])
        else:
            print("Nie ma takiego kanału")
    def volume_up(self, new_volume):
        self.volume += new_volume
        if 1 <= self.volume <= 50:
            print("Prawidłowa głośność:", self.volume)
        else:
            print("Nie ma takiej głośności")
    def volume_down(self, new_volume):
        self.volume -= new_volume
        if 1 <= self.volume <= 50:
            print("Prawidłowa głośność:", self.volume)
        else:
            print("Nie ma takiej głośności")
            
def main():
    brand = input("Podaj producenta telewizora: ")
    model = input("Podaj model telewizora: ")
    tv = Television(brand, model)

    choice = None  
    while choice != "0":
        print("""
            0 - zakończ
            1 - wybierz kanał
            2 - zmniejsz głośność
            3 - zwiększ głośność
            """
        )
        choice = input("Wybierasz: ")
        if choice == "0":
            print("Do widzenia")
        elif choice == "1":
            try:
                channel = int(input("Wybierz kanał: (0-4)"))
            except ValueError:
                print("To musi być liczba")
            else:
                tv.choose_channel(channel)
              
        elif choice == "2":
            try:
                new_volume = int(input("Wybierz poziom zmniejszenia głośności: "))
            except ValueError:
                print("To musi być liczba")
            else:
                tv.volume_down(new_volume)
        elif choice == "3":
            try:
                new_volume = int(input("Wybierz poziom zwiększenia głośności: "))
            except ValueError:
                print("To musi być liczba")
            else:
                tv.volume_up(new_volume)
        else:
            print("Nie ma takiego czegoś w menu")
main()
input("\n\nNaciśnij klawisz Enter, aby zakończyć program")