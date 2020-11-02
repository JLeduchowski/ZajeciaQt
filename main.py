import Auto

user_auto = Auto.Auto()

lista_aut = [Auto.Auto("Opel", "Astra", 2002, paliwo=True),
             Auto.Auto("Peugeot", "107", 2005, paliwo=False),
             Auto.Auto("Fiat", "Seicento", 2000, paliwo=True)]

try:
    x = input("Podaj marke pojazdu")
    user_auto.marka = x
    x = input("Podaj model pojazdu")
    user_auto.model = x
    x = int(input("Podaj rocznik pojazdu"))
    user_auto.rocznik = x
    print("Zatankowalem Twoje auto")
    user_auto.paliwo = True
    lista_aut.append(user_auto)

except TypeError:
    print("Podano zly typ danych")
except ValueError:
    print("Podano zla wartosc")


for auto in lista_aut:
    print(auto)
    if not auto.paliwo:
        print(f"Tankuje pojazd: {auto.marka} {auto.model}")
        auto.zatankuj()
    else:
        print(f"Pojazd {auto.marka} {auto.model} wyruszyl w droge")
        auto.jazda()
