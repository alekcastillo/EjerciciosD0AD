class Person:
  name: str

  def print_name(self):
    print(self.name)


person_1 = Person()
person_1.name = "Alek"

person_2 = Person()
person_2.name = "John"

person_1.print_name()
person_2.print_name()
