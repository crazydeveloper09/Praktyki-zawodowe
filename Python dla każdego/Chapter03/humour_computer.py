# Autor: Maciej Kuta
# Data utworzenie: 6.10.2020
# Cel: Poznanie instrukcji warunkowej elif

import random

print("Wyczuwam Twoją energię. Twoje prawdziwe emocje znajdują odbicie na moim ekranie.")
print("Jesteś...")


number = random.randint(1,3)

if number == 1:
     print( \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | .     . |
       |  `...`  |
       -----------
                   """)
elif number == 2:
      print( \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | ------  |
       |         |
       -----------
                   """)
elif number == 3:
     print( \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       |  .'.    |
       | '   '   |
       -----------
                   """)
else:
    print("Nieprawidłowa wartość nastroju! (Musisz być naprawdę w złym humorze)")

print("...dzisiaj")

input("\nNaciśnij przycisk Enter, aby zakończyć działanie programu")
