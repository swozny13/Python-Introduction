from datetime import *


class Person(object):

    def __init__(self, first_name, last_name, birthday, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.email = email
        self.phone = phone

    def __str__(self):
        print_person = ""
        print_person += "Imię i Nazwisko: " + self.first_name + " " + self.last_name + "\n"
        print_person += "Wiek: " + self.birthday + "\n"
        print_person += "Email: " + self.email + "\n"
        print_person += "Telefon: " + self.phone + "\n"
        return print_person


def menu():
    persons_list = []

    def add_person():
        person_first_name = input("Podaj imię: ")
        person_last_name = input("Podaj naziwsko: ")
        person_birthday = age_convert()
        person_email = email_generator(person_first_name, person_last_name)
        person_phone = number_validator()
        person = Person(person_first_name, person_last_name, person_birthday, person_email, person_phone)
        persons_list.append(person)
        return person

    def age_convert():
        age = input("Podaj date urodzenia (): ")
        convert_age = ""
        return convert_age

    def email_generator(name, surname):
        email = name.lower() + "." + surname.lower() + "@company.com.pl"
        return email

    def number_validator():
        number = input("Podaj nr telefonu (9 liczb): ")
        convert_number = ""
        if len(number) > 9:
            print("Wpisałeś za dużo cyfr")
            return number_validator()
        elif len(number) < 9:
            print("Wpisałeś za mało cyfr")
            return number_validator()
        else:
            convert_number += "+48 " + number[0:3] + " " + number[3:6] + " " + number[6:9]
        return convert_number

    def print_persons():
        if len(persons_list) == 0:
            print("Brak pracowników")
        else:
            print("Pracownicy w bazie:")
            for person in persons_list:
                print(person)

    flag = True
    while flag:

        print("MENU")
        print("1. Dodaj pracownika")
        print("2. Wyświetl liste pracowników")
        print("0. Zakończ")

        choice = int(input("Podaj opcje: "))

        if choice == 1:
            add_person()
        elif choice == 2:
            print("")
            print_persons()
            print("")
        elif choice == 0:
            flag = False
            print("Zakończono")
        else:
            print("Nie ma takiej opcji")


menu()
