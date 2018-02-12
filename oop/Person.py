from datetime import *

HR_MENU = ["1. Dodaj pracownika", "2. Wyświetl liste pracowników", "0. Wyloguj"]
DIRECTOR_MENU = ["1. Wyświetl liste pracowników", "2. Wprowadź wynagrodzenie", "3. Daj podwyżkę", "0. Wyloguj"]


class Person(object):

    # TODO: add id and generate this maybe by function
    def __init__(self, first_name, last_name, birthday, email, phone, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.email = email
        self.phone = phone
        self.salary = salary

    # TODO: add salary (private)
    def salary(self):
        self.salary = 0

    def __str__(self):
        print_person = ""
        print_person += "Imię i Nazwisko: " + self.first_name + " " + self.last_name + "\n"
        print_person += "Wiek: " + self.birthday + " lat" + "\n"
        print_person += "Email: " + self.email + "\n"
        print_person += "Telefon: " + self.phone + "\n"
        print_person += "Wynagrodzenie: " + str(self.salary) + " PLN"
        return print_person


class Account(object):

    def __init__(self, account_type, access, password):
        self.account_type = account_type
        self.access = access
        self.password = password


director = Account("Prezes", 1111, "admin")
hr_manager = Account("Szef HR", 2222, "hr")


def menu():
    persons_list = []

    def add_person():
        person_first_name = name_convert()
        person_last_name = surname_convert()
        person_birthday = age_convert()
        person_email = email_generator(person_first_name, person_last_name)
        person_phone = number_validator()
        person_salary = 0
        person = Person(person_first_name, person_last_name, person_birthday, person_email, person_phone, person_salary)
        persons_list.append(person)
        return person

    def name_convert():
        name = input("Podaj imię: ")
        return name.capitalize().replace(" ", "")

    def surname_convert():
        surname = input("Podaj nazwisko: ")
        return surname.capitalize().replace(" ", "")

    def age_convert():
        now = int(datetime.now().year)
        age = input("Podaj date urodzenia (YYYY-MM-DD): ")
        cut_year = age[0:4]
        convert_age = now - int(cut_year)
        if convert_age < 18:
            print("Zła data. Nie zatrudniamy poniżej 18 lat")
            return age_convert()
        return str(convert_age)

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
            print("")
            id = 0
            for person in persons_list:
                id += 1
                print(id)
                print(person)

    # TODO: FIX THIS. id -> object, not list!
    def raise_salary():
        print_persons()
        id = int(input("Wybierz pracownika"))
        print(persons_list[id] - 1)
        salary = float(input("Podaj wynagrodzenie"))

    def hr_menu():
        flag = True
        while flag:
            print("")
            print("Witam " + hr_manager.account_type)
            print("MENU HR")
            for elem in HR_MENU:
                print(elem)

            choice = int(input("Podaj opcje: "))

            if choice == 1:
                add_person()
            elif choice == 2:
                print("")
                print_persons()
                print("")
            elif choice == 0:
                flag = False
                print("Wylogowano: " + hr_manager.account_type)
                login()
            else:
                print("Nie ma takiej opcji")

    def director_menu():
        flag = True
        while flag:
            print("")
            print("Witam " + director.account_type)
            print("MENU DYREKTORSKIE")
            for elem in DIRECTOR_MENU:
                print(elem)

            choice = int(input("Podaj opcje: "))

            if choice == 1:
                print("")
                print_persons()
                print("")
            elif choice == 2:
                raise_salary()
            elif choice == 3:
                print()
            elif choice == 0:
                flag = False
                print("Wylogowano: " + director.account_type)
                login()
            else:
                print("Nie ma takiej opcji")

    def login():
        flag = True
        print("LOGOWANIE")
        access_key = int(input("Podaj 4-cyfrowy kod dostępu: "))
        password = input("Podaj hasło: ")
        while flag:
            if access_key == director.access and password == director.password:
                director_menu()
                flag = False
            elif access_key == hr_manager.access and password == hr_manager.password:
                hr_menu()
                flag = False
            else:
                print("Niepoprawne dane!")
                login()

    login()


menu()
