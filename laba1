class Human:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def work(self):
        return "Людина працює"


class Student(Human):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def work(self):
        return "Студент навчається"


h = Human("Андрій", 18)
s = Student("Тарас", 19, "ЛНУ")

print(h.work())
print(s.work())
