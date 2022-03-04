class Person:
    def __init__(self, param_name):
        self.name = param_name

    def talk(self):
        print(f"My name is {self.name}")


person_1 = Person("박명수")
person_1.talk()
person_2 = Person("유재석")
person_2.talk()
