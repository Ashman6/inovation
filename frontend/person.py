 


class Person():
    def __init__(self, name, age, height):
        self.name = name
        self.height = height
        self.age = age

    def talk(self):
        print(f"hello my name is{self.name}, i am {self.age} years old and im {self.height} tall")

ash = Person("ash", 36, "5'9''")     





print(ash.height)
ash.talk()

