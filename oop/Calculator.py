#  metoda z dwoma podkreślnikami to metoda specjalna


class Calculator():
    def mnozenie(self, a, b):
        wynik = a * b
        print("Wynik: {}".format(wynik))

    def dzielenie(self, a, b):
        wynik = a / b
        print("Wynik: {}".format(wynik))


# na sztywno
calculator = Calculator()
calculator.mnozenie(3, 92)
calculator.dzielenie(535, 5)

# przez usera
a = int(input("Podaj liczbe:"))
b = int(input("Podaj liczbe:"))

calculator.mnozenie(a, b)
calculator.dzielenie(a, b)
