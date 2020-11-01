
print(f'Lustrzane odbicie podanego ciagu znakow.')
string = input("Podaj ciag znakow, quit zakonczy skrypt.")

while(string!='quit'):
    print(f'Podales {string}')
    string = string[::-1]
    print(f'Lustrzane odbicie: {string}')
    string = input("Podaj ciag znakow, quit zakonczy skrypt.")