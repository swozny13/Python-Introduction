from datetime import *

"""
Simple program to....
"""
HR_MENU = ["1. Dodaj pracownika", "2. Wyświetl liste pracowników", "3. Statystyki", "0. Wyloguj"]
DIRECTOR_MENU = ["1. Wyświetl liste pracowników", "2. Wprowadź wynagrodzenie", "3. Daj podwyżkę",
                 "4. Zwolnij pracownika", "0. Wyloguj"]
STATISTICS_MENU = ["1. Średnia pensja w firmie", "2. Średnia wieku w firmie"]

salary_list = []


# TODO: Add statistic about person (age average, salary average)


class Person(object):
    person_id = 1

    # @staticmethod
    # def set_person_id():
    #     print(Person.person_id)

    def __init__(self, first_name, last_name, birthday, pesel, email, phone, salary):
        self.id = Person.person_id
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.pesel = pesel
        self.email = email
        self.phone = phone
        self.salary = salary
        Person.person_id += 1

    # TODO: add salary (private function)
    def set_salary(self):
        self.salary = 0

    def __str__(self):
        print_person = ""
        print_person += str(self.id) + "\n"
        print_person += "Imię i nazwisko: " + self.first_name + " " + self.last_name + "\n"
        print_person += "Wiek: " + self.birthday + " lat" + "\n"
        print_person += "Email: " + self.email + "\n"
        print_person += "Telefon: " + self.phone + "\n"
        print_person += "Wynagrodzenie: " + str(self.salary) + " PLN"
        return print_person

    def give_salary(self):
        self.salary = float(input("Wprowadź kwotę wynagrodzenia: "))
        if self.salary < 0:
            print("Wynagrodzenie nie może być mniejszę niż 0 PLN")
        else:
            print("Wynagrodzenie " + self.first_name + " " + self.last_name + " wynosi teraz: " + str(
                self.salary) + " PLN")

    def give_salary_raise(self):
        if self.salary == 0:
            print("Nie możesz dać podwyżki, gdy wynagrodzenie wynosi 0 PLN")
        else:
            set_percent_increase = int(input("Wprowadź % podwyżki: "))
            if set_percent_increase <= 0:
                print("Podwyżka musi być większa niż 0%")
            else:
                self.salary = self.salary + ((self.salary * set_percent_increase) / 100)
                print(
                    "Dodano " + str(set_percent_increase) + "% podwyżki dla " + self.first_name + " " + self.last_name)
                print("Wynagrodzenie " + self.first_name + " " + self.last_name + " wynosi teraz: " + str(
                    self.salary) + " PLN")

    # TODO: continue
    def add_salary_to_list(self, *list):
        # todo: for loops????
        salary_list.append(self.salary)
        print(salary_list)
    # def salary_average(self):


class Account(object):

    def __init__(self, account_type, access, password):
        self.account_type = account_type
        self.access = access
        self.password = password


director = Account("Prezes", 1111, "admin")
hr_manager = Account("Szef HR", 2222, "hr")


def start():
    persons_list = []
    person_pesel_list = []

    def add_person():
        person_first_name = name_convert()
        person_last_name = surname_convert()
        person_birthday = age_convert()
        person_pesel = pesel_validator_finder()
        person_pesel_list.append(person_pesel)
        person_email = email_generator(person_first_name, person_last_name)
        person_phone = number_validator()
        person_salary = 0
        person = Person(person_first_name, person_last_name, person_birthday, person_pesel, person_email, person_phone,
                        person_salary)
        persons_list.append(person)
        for p in persons_list:
            print(p)
        return person

    def name_convert():
        name = input("Podaj imię: ")
        return name.capitalize().replace(" ", "")

    def surname_convert():
        surname = input("Podaj nazwisko: ")
        return surname.capitalize().replace(" ", "")

    # TODO: fix data format, count age with months and days
    def age_convert():
        now = int(datetime.now().year)
        age = input("Podaj date urodzenia (YYYY-MM-DD): ")
        cut_year = age[0:4]
        convert_age = now - int(cut_year)
        if convert_age < 18:
            print("Zła data. Nie zatrudniamy poniżej 18 lat")
            return age_convert()
        return str(convert_age)

    def pesel_validator_finder():
        pesel = input("Podaj PESEL: ")
        if len(pesel) == 11:
            if pesel in person_pesel_list:
                print("Pracownik o podanym PESELU znajduje się w bazie!")
                pesel_validator_finder()
            else:
                return pesel
        else:
            print("Podany numer PESEL musi zawierać 11 cyfr")
            pesel_validator_finder()

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

    def salary():
        if len(persons_list) == 0:
            print("Brak pracowników")
        else:
            print_persons()
            get_id = int(input("Podaj id pracownika: "))
            person_selected = persons_list[get_id - 1]
            Person.give_salary(person_selected)

    def increase():
        if len(persons_list) == 0:
            print("Brak pracowników")
        else:
            print_persons()
            get_id = int(input("Podaj id pracownika: "))
            person_selected = persons_list[get_id - 1]
            Person.give_salary_raise(person_selected)

    # TODO: not working perfect - fix them. delete person by object, not object in list
    def release():
        if len(persons_list) == 0:
            print("Brak pracowników")
        else:
            print_persons()
            get_id = int(input("Podaj id pracownika: "))
            person_selected = persons_list[get_id - 1]
            # print(person_selected['PESEL'])
            persons_list.remove(person_selected)
            print("Zwolniłeś pracownika")
            for p in person_pesel_list:
                print(p)

    def print_persons():
        if len(persons_list) == 0:
            print("Brak pracowników")
        else:
            print("Pracownicy w bazie:")
            print("")
            for person in persons_list:
                print(person)

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
            elif choice == 3:
                statistics_menu()
            elif choice == 0:
                flag = False
                print("Wylogowano: " + hr_manager.account_type)
                login()
            else:
                print("Nie ma takiej opcji")

    def statistics_menu():
        print("")
        for elem in STATISTICS_MENU:
            print(elem)
        print("")
        choice = int(input("Podaj opcje: "))

        if choice == 1:
            Person.add_salary_to_list(*persons_list)
        elif choice == 2:
            pass
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
                salary()
            elif choice == 3:
                increase()
            elif choice == 4:
                release()
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


start()
