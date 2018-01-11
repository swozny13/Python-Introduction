class Employee:

    def addName(self):
        employeeName = []
        name = input("Podaj imie pracownika: ")
        employeeName.append(name)

    def addAge(self):
        employeeAge = []
        age = int(input("Podaj wiek pracownika: "))
        employeeAge.append(age)


employees = Employee()
employees.addName()
employees.addAge()
