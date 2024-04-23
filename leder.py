from person import person

class leder(person):
    def __init__(self, navn, id, timelonn, bonusandel):
        super().__init__(navn, id, timelonn)
        self.bonusandel = bonusandel

    def skrivut(self):
        print("Leder:")
        super().skrivut()
        print(f"Bonusandel: {self.bonusandel}")

    def regnUtLonn(self, antall_timer):
        return antall_timer * self.timelonn + (self.bonusandel/100)



