class Auto:

    marka = None
    model = None
    rocznik = None
    paliwo = False

    def __init__(
            self,
            marka=None,
            model=None,
            rocznik=None,
            paliwo=False):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.paliwo = paliwo

    def __str__(self):
        return f'Auto marka: {self.marka} | model: {self.model}'

    def zatankuj(self):
        paliwo = True

    def jazda(self):
        paliwo = False