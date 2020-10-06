# Autor: Maciej Kuta
# Data utworzenie: 6.10.2020
# Tytuł: Sprzedawca samochodów
# Cel: Obliczanie całkowitej ceny auta

car_price = int(input("Podstawowa cena samochodu: "))
tax = car_price * 1.23
register_price = 180.50
provision = car_price * 0.01
deliver_price = 100

print("Cena samochodu z opłatami wynosi:", tax + register_price + provision + deliver_price)