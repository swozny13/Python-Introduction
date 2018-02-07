class Person(object):

    def __init__(self, first_name, last_name, age, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.phone = phone
        self.person_list = []

    def set_person(self):
        self.first_name = input("Podaj imię: ")
        self.last_name = input("Podaj nazwisko: ")
        self.age = input("Podaj wiek: ")
        self.email = input("Podaj email: ")
        self.phone = input("Podaj nr telefonu: ")
        person = Person(self.first_name, self.last_name, self.age, self.email, self.phone)
        return person
        # self.add_person_to_list(person)

    def print_person(self, person):
        print("Name: {} \nSurname: {} \nAge: {} \nEmail: {} \nPhone: {}".format(person.first_name, person.last_name,
                                                                                person.age, person.email, person.phone))

    def add_person_to_list(self, person):
        self.person_list.append(person)
