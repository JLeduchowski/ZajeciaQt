class Error(Exception):
    """Base class for other exceptions"""
    pass

class BledneStanowisko(Error):
    """Podane stanowisko nie istnieje"""
    pass


class Pracownik:
    imie = ""
    nazwisko = ""
    stanowisko = ""
    pensja = 0.0
    nrTelefonu = ""

    def __init__(self,imie=None,nazwisko=None,stanowisko=None,pensja=0,nrTelefonu=""):
        self.imie = imie
        self.nazwisko = nazwisko
        try:
            if(stanowisko != "Kierownik" and stanowisko != "Inzynier"):
                raise BledneStanowisko
            else:
                self.stanowisko = stanowisko
        except BledneStanowisko:
            print(f"Probowano ustawic nie istniejace stanowisko")
        self.stanowisko = stanowisko
        self.pensja = pensja
        if (len(nrTelefonu) == 9 and nrTelefonu.isdigit()):
            self.nrTelefonu = nrTelefonu
        else:
            self.nrTelefonu = "Bledny numer"

    def __str__(self):
        return 'Pracownik: {s.imie} {s.nazwisko} \nStanowisko: {s.stanowisko} \n' \
               'Pensja: {s.pensja} \nNumer telefonu: {s.nrTelefonu}\n'.format(s=self)

    def get_imie(self):
        return self.imie

    def get_nazwisko(self):
        return self.nazwisko

    def get_stanowisko(self):
        return self.stanowisko

    def get_pensja(self):
        return self.pensja

    def get_nrTelefonu(self):
        return self.nrTelefonu

    def set_imie(self,imie):
        self.imie = imie

    def set_nazwisko(self, nazwisko):
        self.nazwisko = nazwisko

    def set_stanowisko(self,stanowisko):
        try:
            if(stanowisko != "Kierownik" and stanowisko != "Inzynier"):
                raise BledneStanowisko
            else:
                self.stanowisko = stanowisko
        except BledneStanowisko:
            print(f"Probowano ustawic nie istniejace stanowisko")

    def set_pensja(self,pensja):
        if self.stanowisko == "Inzynier":
            if self.pensja + pensja <= 4000:
                self.pensja = pensja
            else:
                print(f'Pensja inzyniera nie moze przekraczac 4000')
        if self.stanowisko == "Kierownik":
            if self.pensja + pensja <= 5000:
                 self.pensja = pensja
            else:
                 print(f'Pensja kierownika nie moze przekraczac 5000')

    def set_nrTelefonu(self,nrTelefonu):
        if (len(nrTelefonu) == 9 and nrTelefonu.isdigit()):
            self.nrTelefonu = nrTelefonu
        else:
            self.nrTelefonu = "Bledny numer"

    def ZwiekszPensje(self):
        if self.stanowisko == "Inzynier":
            if self.pensja + 500 <= 4000:
                self.pensja = self.pensja + 500
                print(f'Pensja {self.imie} {self.nazwisko} po podwyzce: {self.pensja}')
            else:
                print(f'Pensja inzyniera nie moze przekraczac 4000')

        if self.stanowisko == "Kierownik":
            if self.pensja + 500 <= 5000:
                self.pensja = self.pensja + 500
                print(f'Pensja {self.imie} {self.nazwisko} po podwyzce: {self.pensja}')
            else:
                print(f'Pensja kierownika nie moze przekraczac 5000')


