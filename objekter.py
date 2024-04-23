from leder import leder
from ansatt import ansatt

ansatt1 = ansatt("Ole", 1, 100)
ansatt2 = ansatt ("Gunnar", 2, 150)
ansatt3 = leder ("Bob", 3, 250,3)

#ansatt1.skrivut()
#ansatt2.skrivut()
#ansatt3.skrivut()

print(ansatt1.regnUtLonn(23))
print(ansatt3.regnUtLonn(10))