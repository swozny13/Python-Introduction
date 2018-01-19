class Raport():
    def template(self, template_name, id, number):
        self.template_name = template_name
        self.id = id
        self.number = number


class RaportView(Raport):
    def templateCSV(self, export):
        self.export = export


r = Raport()
r.template("www", 1, 11)
print(r.template_name)

