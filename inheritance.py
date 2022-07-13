from typing import List

class Animal():

    def __init__(self, name:str, species:str):
        self.name = name
        self.species = species

    def make_sound(self):
        print("sound")

class Dog(Animal):
    
    def __init__(self, name:str):
        super().__init__(name, "dog")
    
    def make_sound(self):
        print("woof")

class Cat(Animal):

    def __init__(self, name:str):
        super().__init__(name, "cat")

    def make_sound(self):
        print("meow")

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "cow")

    def make_sound(self):
        print("moo")    

dog1 = Dog("dog1")
dog2 = Dog("dog2")
dog3 = Dog("dog3")
cow1 = Cow("cow1")
cow2 = Cow("cow2")
cow3 = Cow("cow3")
cat1 = Cat("cat1")
cat2 = Cat("cat2")
cat3 = Cat("cat3")
cat4 = Cat("cat4")

animal_list:List[Animal] = [dog1, cow3, dog3, cow1, cow2, dog2, cat1, cat2, cat3, cat4, "ERROR"]

for i, animal in enumerate(animal_list):
    try:
        animal.make_sound()
    except Exception as e:
        raise e
    finally:
        if i == (len(animal_list) - 1):
            print('done')
