# Autor: Maciej Kuta
# Data utworzenie: 6.10.2020
# Cel: Demonstruje podstawowe metody łańcucha znaków

quote = "Myślę, że istnieje światowy rynek dla może pięciu komputerów"

print("Oryginalny cytat w tłumaczeniu na język polski:")
print(quote)

print("\nDużymi literami:")
print(quote.upper())

print("\nMałymi literami:")
print(quote.lower())

print("\nWszystkie wyrazy od dużej litery:")
print(quote.title())

print("\nZ drobną zmianą:")
print(quote.replace("pięciu", "milionów"))

print("\nOryginalny cytat pozostał bez zmian:")
print(quote)

input("\n Kliknij klawisz Enter, by zakończyć program")