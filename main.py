import Pracownik




def WypiszKierownikow(pracownik):
    if pracownik.get_stanowisko() == "Kierownik":
        print(pracownik)

def WypiszInzynierow(pracownik):
    if pracownik.get_stanowisko() == "Inzynier":
        print(pracownik)

if __name__ == '__main__':
    p1 = Pracownik.Pracownik("Jan","Los","Kierownik",4100.0,"123123123")
    p2 = Pracownik.Pracownik("Andrzej","Glowa","Inzynier",2800.0,"123456789")
    p3 = Pracownik.Pracownik("Michal","Kowal","Inzynier",3000.0,"123")
    p4 = Pracownik.Pracownik()

    listaPracownikow = [p1]
    listaPracownikow.append(p2)
    listaPracownikow.append(p3)
    listaPracownikow.append(p4)

    for Pracownik in listaPracownikow:
        print(Pracownik)

    p4.set_imie("Marek")
    p4.set_nazwisko("Nowak")
    p4.set_stanowisko("Inzynier")
    p4.set_pensja(2000)
    p4.set_nrTelefonu("121212121")

    print(p4)

    for i in range(3):
        p3.ZwiekszPensje()

    print(f'Lista kierownikow:')
    for Pracownik in listaPracownikow:
        WypiszKierownikow(Pracownik)

    print(f'Lista inzynierow: ')
    for Pracownik in listaPracownikow:
        WypiszInzynierow(Pracownik)

    p4.set_stanowisko("Stanowisko testowe")
    print(p4)