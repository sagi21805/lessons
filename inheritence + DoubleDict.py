class Animal():

    def __init__(self, kind: str) -> object:
        self.name = "animal"
        self.type = kind
    
    def make_sound(self):
        print("Animal sound")

class Dog(Animal):

    def __init__(self ,kind: str, breed: str):
        super().__init__(kind)
        self.breed = breed

    def bark(self):
        print("woof")

class puppy(Dog):

    def __init__(self, kind: str, breed: str):
        super().__init__(kind, breed)

    def make_sound(self):
        print("puppy sound")



cow = Animal( "cow")
rex = Dog( "dog", "labrador")
mitzi = puppy( "dog", "labrador")

rex.make_sound()
mitzi.make_sound()
rex.bark()
mitzi.bark()

class DoubleDict(dict):
    def __init__(self, *args, **kwargs):
        super(DoubleDict, self).__init__(*args, **kwargs)
        self.__dict__ = {}

    def item_to_key(self, item):
        itemList = list(self.values())
        for i, val in enumerate(itemList):
            if val == item:
                x = i
                break
        keyList = list(self.keys())
        return keyList[x]

Double = DoubleDict({1:2})
print(Double[1])
print(Double.item_to_key(2))