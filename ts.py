import datetime

import time

print('hello world')
print('TEST')
print('hello world')

# pobieranie od usera za pomoca input
name = input("What is your name?\n")
# print wyswietli mi to co chce w konsoli, czyli tak jak sout w Javie
print("Witaj " + name)

print("Kalkulator".upper())


#  jakies proste metody
def add():
    a = input("Podaj 1 liczbe\n")
    b = input("Podaj 2 liczbe\n")
    result = float(a) + float(b)
    print("Twoj wynik to: ")
    print(result)


def sub():
    a = input("Podaj 1 liczbe\n")
    b = input("Podaj 2 liczbe\n")
    result = float(a) - float(b)
    print("Twoj wynik to: ")
    print(result)


# add()
# sub()

# petla while = sympatycznie, tak jak w Javie - prawie :)
x = 0
while x < 10:
    x += 1
    print(x)

# lista (operacje na listach)

listOfNames = ["Seba", "Marek", "Jarek", "Szymon", "Asia", "Karolina"]
print(listOfNames)
# dodawanie elementu do listy, append doda na koniec listy i moze byc to tylko pojedynczy el
listOfNames.append("Krzychu")
print(listOfNames)
# dodawanie kilku elementow, czyli nowej listy mozna za pomoca extend
listOfNames.extend(["Janusz", "Robert", "Alicja"])
print(listOfNames)
# usuwanie pojedyńczego el za pomoca remove - trzeba wpisac stringa z tym
# co znajduje sie w liscie, jak wpiszemy cos co nie jest
# w liscie to rzuci wyjatkiem
listOfNames.remove("Robert")
print(listOfNames)
# usuwanie calej listy
# listOfNames.clear()
# print(listOfNames)

#  pętla for

print()
for name in listOfNames:
    print(name)

# inna budowa pętli for niż w Javie.
# przeczytałbym to tak: dla każdego imienia w liście imion wypisz mi imię


# pętla for z instrukcja warunkowa
# jakiś tam pzykładzik

print()
for name in listOfNames:
    if name == "Asia":
        print("Szukałem Cię " + name)
    else:
        print("Ciebie nie szukałem " + name)

# fajna opcja z funkcją range

# range(start, koniec, krok)
range(50, 100, 2)

# gdy przejdziemy pętlą for...

for x in range(50, 101, 2):
    print(x)

# to ładnie wyprintuje nam przedział liczb od 50 do 100, co 2 kroki czyli co 2 liczby
# oczywiscie range moze przyjmowac również: tylko przedział startowy, startowy-koncowy


# funkcja enumerated
# uzyskujemy dostep tak jakby do interatora? tak mi się wydaję
# enumarated przyjmuje dwa argumenty - naszą liste oraz indeks elementu

print()
for i, name in enumerate(listOfNames):
    if i == 3:
        break
    print(i)
    print(name)

# format
# myślę, że przeda się do konkatencji różnych zmianncyh
# np łączenia stringa z intem, floatem

print()


def mnozenie():
    x = input("Podaj 1 liczbe\n")
    y = input("Podaj 2 liczbe\n")
    wynikMnozenia = int(x) * int(y)
    # tak jak poniżej nie działa... to nie Java...
    # print("Wynik to: " + wynikMnozenia)

    # trzeba użyć funkcji format na Stringu
    # magia dzieje się wtedy gdy wpiszemy klamry {}
    # chodzi o to że w miejsce klamry wpisze się nasz "wynikMnozenia" z funkcji format
    # jesli chcielibysmy dołączyć wiecej liczb, to kolejne {} i elementy w funkcji format beda sobie odpowiadac
    # tak jak przykład -> "Wynik mnożenia liczby {} i liczby {} wynosi: {}.format(x,y,wynikMnozenia)
    print("Wynik mnożenia: {}".format(wynikMnozenia))


mnozenie()

print()

# przykladzik z lista i inputem
# ify moze traktowac identycznie jak fory... ciekawe

listaOwocow = ["jabłko", "gruszka", "winogron", "banan", "kiwi", "pomarańcz", "mandarynka", "truskawka"]


# while True:
def szukanieOwocow():
    podajOwoc = input("Podaj nazwę owoca, a sprawdzę czy jest w mojej liście zakupów\n")
    if podajOwoc.lower() in listaOwocow:
        print("{} znajduje się w mojej liście zakupów".format(podajOwoc.capitalize()))
    else:
        print("{} nie znajduje się w mojej liście zakupów".format(podajOwoc.capitalize()))


szukanieOwocow()
print()
print("Jeśli nie ma owoca jakiego sobie życzysz to dodaj go!")

dodajOwoc = input("Wpisz owoc\n")
listaOwocow.append(dodajOwoc)

szukanieOwocow()

# data i czas

timer = time.time()
# while True:
aktualnyCzas = datetime.datetime.now()
if time.time() - timer > 2:
    print(aktualnyCzas.strftime("%H:%M:%S %d %B %Y"))
    timer = time.time()
