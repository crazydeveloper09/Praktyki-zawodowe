# Autor: Maciej Kuta
# Data utworzenie: 8.10.2020
# Cel:Pokazanie operacji zapisu i przechowywania złożonych struktur w plikach

import pickle, shelve

print("Marynowanie list")
variety = ["łagodny", "pikantny", "kwaszony"]
shape = ["cały", "krojony wzdłuż", "w plasterkach"]
brand = ["Dawtona", "Klimex", "Vortumnus"]

f = open("pikiel.dat", "wb")
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print("\nOdmarynowanie list")
f = open("pikiel.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
print(variety)
print(shape)
print(brand)
f.close()

print("\nOdkładanie list na półkę")
s = shelve.open("pikle2.dat")
s["odmiana"] = ["łagodny", "pikantny", "kwaszony"]
s["kształt"] = ["cały", "krojony wzdłuż", "w plasterkach"]
s["marka"] = ["Dawtona", "Klimex", "Vortumnus"]
s.sync()
print("\nPobieranie list z pliku półki: ")
print("marka -", s["marka"])
print("kształt -", s["kształt"])
print("odmiana -", s["odmiana"])
s.close()


input("\n\nNaciśnij klawisz Enter, aby zakończyć działanie programu")