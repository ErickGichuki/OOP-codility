class Person:

    def __init__(self, name, age,gender):
        self.name = name
        self.age = age
        self.gender =gender

    def introduce(self):
        print(f"Hi! my name is {self.name} welcome to Erifa ltd am {self.age} years of age. It is good to say that am a {self.gender}.")

person = Person('Eric', 23, 'male')
person.introduce()