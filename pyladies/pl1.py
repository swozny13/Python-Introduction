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
    print("1. Zapytaj o kraj")
    print("2. Zapytaj o imię")
    print("3. Sprawdź czy kraj jest w mojej strukturze")
    print("4. Wyświetl coś....")
    print("5. Koniec programu")

    a = input("Wybierz opcje")

    if a == 1:
        get_country()
    if a == 2:
        get_name()
    if a == 3:
        found_country()
    if a == 4:
        print_sth()
    if a == 5:
        print()


# flag = false


def get_country():
    print()


def get_name():
    print()


def found_country():
    x = input("Podaj nazwe kraju...")

    if x in country.keys():
        print("Kraj istnieje")
    else:
        print("Kraj nie istieje")


def print_sth():
    print()
