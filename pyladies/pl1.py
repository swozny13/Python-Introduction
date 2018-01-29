friends = {"Sebastian": "Poznań", "Krzysztof": "Koło", "Adam": "Kraków", "Maciej": "Wrocław", }

# count all dictionary item
print(len(friends))

print(friends.values())
print(friends.keys())

items = {"el1": 7, "el2": 1, "el3": 5, "el4": 3}


#
# f = input("Wpisz imię...")
# m = input("Wpisz miasto...")
# if f in friends.keys():
#     friends[f] = f
# if m in friends.values():
#     print("Nie potrzebuje więcej przyjaciół z {}".format(m))
# else:
#     friends[f] = m
# print(friends)

def some_string():
    print("Something...")


def prspscn(a, b, c):
    some_string()
    return a * b * c


print(prspscn(3, 5, 77))

# def get_string(first, second):
#     print("First: %s" % first)
#     print("Second: %s" % second)
#
#
# get_string(5, 1)


country = {"Poland": "Witaj", "England": "Hello", "Germany": "Hallo", "Italy": "Ciao", "France": "Salut", }


# language = input("Podaj kraj pochodzenia np. PL...")
#
# if language in country.keys():
#     print(country[language])
#
#

def menu():
    print()

    flaga = True
    while flaga:
        print("1. Zapytaj o kraj")
        print("2. Zapytaj o imię")
        print("3. Sprawdź czy kraj jest w mojej strukturze")
        print("4. Wyświetl coś....")
        print("5. Koniec programu")

        a = int(input("Wybierz opcje: "))

        if a == 1:
            get_country()
        elif a == 2:
            get_name()
        elif a == 3:
            found_country()
        elif a == 4:
            print_sth()
        elif a == 5:
            print("ZAKOŃCZONO")
            flaga = False
        else:
            print("Nie ma takiej opcji")


def get_country():
    print()
    country = input("Hej! Z jakiego kraju jesteś?: ")
    print("Super! :-) Pozdrowienia dla {}".format(country))
    print()


def get_name():
    print()
    name = input("Napisz mi jak masz na imię: ")
    print("Cześć, {}!".format(name))
    print()


def found_country():
    print()
    x = input("Podaj nazwe kraju (po angielsku): ")

    if x in country.keys():
        print("{} istnieje w moim słowniku".format(x))
    else:
        print("{} nie istieje w moim słowniku".format(x))
    print()


def print_sth():
    print()
    file = open("cos.txt", "r", encoding='utf-8')
    print(file.readlines())
    file.close()
    print()


def exit_program(flaga):
    flaga = False


menu()
