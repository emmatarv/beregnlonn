from person import person

class ansatt(person):
    def __init__(self, navn, id, timelonn):
        super().__init__(navn, id, timelonn)

    def skrivut(self):
        print("Ansatt:")
        super().skrivut()

    def regnUtLonn(self, antall_timer):
        regnelonnansatt
        return antall_timer * self.timelonn
