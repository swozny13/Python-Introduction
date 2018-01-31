# *args -> jako parametr przyjmuje dowolną liczbe argumentow
# **kwargs - > jako parametr przyjmuje słownik

def average(*args):
    try:
        sum = 0
        for a in args:
            sum += a
        return sum / len(args)
    except ZeroDivisionError as ex:
        print("Nie dziel przez 0")


print(average())

students = {
    'Sebastian': {'wiek': 26, 'kierunek': 'informatyka', 'ocena': 5},
    'Karolina': {'wiek': 21, 'kierunek': 'dietetyka', 'ocena': 6},
    'Krzychu': {'wiek': 22, 'kierunek': 'sport', 'ocena': 3},
    'Janusz': {'wiek': 26, 'ocena': 5},
}


def get_students(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


print(get_students(**students))

slownik = {'el1': 10, 'el2': 2}
print(sorted(slownik.values()))
