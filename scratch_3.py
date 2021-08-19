cena = input()
abc = int(cena[0]) + int(cena[1]) + int(cena[2])
cba = int(cena[3]) + int(cena[4]) + int(cena[5])
if abc == cba:
    print('Счастливый')
else:
    print('обычный')