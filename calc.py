def dodawanie():
    print("DODAWANIE")
    a = input("Wpisz pierwsza liczbe: ")
    b = input("Wpisz druga liczbe: ")
    wynik = float(a) + float(b)
    print("Wynik działania: {}".format(wynik))


def odejmowanie():
    print("ODEJMOWANIE")
    a = input("Wpisz pierwsza liczbe: ")
    b = input("Wpisz druga liczbe: ")
    wynik = float(a) - float(b)
    print("Wynik działania: {}".format(wynik))


def mnozenie():
    print("MNOZENIE")
    a = input("Wpisz pierwsza liczbe: ")
    b = input("Wpisz druga liczbe: ")
    wynik = float(a) * float(b)
    print("Wynik działania: {}".format(wynik))


def dzielenie():
    print("DZIELENIE")
    a = input("Wpisz pierwsza liczbe: ")
    b = input("Wpisz druga liczbe: ")
    if b == 0:
        print("Nie dziel przez 0!")
    else:
        wynik = float(a) / float(b)
    print("Wynik działania: {}".format(round(wynik, 2)))


def potegowanie():
    print("POTĘGOWANIE")
    a = input("Podaj liczbe potęgowaną: ")
    b = int(input("Podaj, do której potęgi chcesz podnieść liczbe {}: ".format(a)))
    wynik = float(a) ** int(b)
    print("Wynik potęgowania dla: {}^{} wynosi: {}".format(a, b, wynik))


def silnia(a):
    if a > 1:
        wynik = 0
        wynik = a * silnia(a - 1)
    else:
        return 1
    return wynik


def start():
    flaga = True
    while flaga:
        print("KALKULATOR")
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnożenie")
        print("4. Dzielenie")
        print("5. Potęgowanie")
        print("6. Silnia")
        print("7. Zakończ program")
        opcjaWyboru = int(input("Wybierz działanie: "))

        if opcjaWyboru == 1:
            dodawanie()
        elif opcjaWyboru == 2:
            odejmowanie()
        elif opcjaWyboru == 3:
            mnozenie()
        elif opcjaWyboru == 4:
            dzielenie()
        elif opcjaWyboru == 5:
            potegowanie()
        elif opcjaWyboru == 6:
            print("SILNIA")
            a = int(input("Podaj liczbe do obliczenia silni: "))
            wynik = silnia(a)
            print("Wynik silni z liczby {} wynosi: {}".format(a, wynik))
        elif opcjaWyboru == 7:
            print("ZAKOŃCZONO")
            break
        else:
            print("Nie ma takiej opcji. Zakończono program")
            flaga = False
            break


start()
