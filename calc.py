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


def start():
    flaga = True
    while flaga:
        print("KALKULATOR")
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnożenie")
        print("4. Dzielenie")
        print("5. Zakończ")
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
            print("ZAKOŃCZONO")
            break
        else:
            flaga = False
            break


start()
