class person():
    def __init__(self, navn, id, timelonn):
        self.navn = navn
        self.id = id
        self.timelonn = timelonn

    def skrivut(self):
        print(f"Navn: {self.navn}\nId: {self.id}\nTimelonn: {self.timelonn}")