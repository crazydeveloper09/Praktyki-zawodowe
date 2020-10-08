# Autor: Maciej Kuta
# Data utworzenie: 8.10.2020
# Cel:Pokazanie operacji zapisu na plikach

print("Utworzenie pliku tekstowego za pomocą metody write()")
text_file = open("zapisz_to.txt", "w")
text_file.write("Wiersz 1\n")
text_file.write("To jest wiersz 2\n")
text_file.write("Ten tekst tworzy wiersz 3\n")
text_file.close()

print("Odczytywanie zawartości nowo utworzonego pliku")
text_file = open("zapisz_to.txt", "r")
for line in text_file:
    print(line)
text_file.close()

print("Utworzenie pliku tekstowego za pomocą metody writelines()")
text_file = open("zapisz_to_lines.txt", "w")
text_file.writelines(["Wiersz 1\n", "To jest wiersz 2\n", "Ten tekst tworzy wiersz 3\n"])
text_file.close()

print("Odczytywanie zawartości nowo utworzonego pliku")
text_file = open("zapisz_to.txt", "r")
for line in text_file:
    print(line)
text_file.close()

input("\n\nNaciśnij klawisz Enter, aby zakończyć działanie programu")