from signal import raise_signal


class Iter():
    
    def __init__(self, id: int, name: str, adress: str):
        self.id = id
        self.name = name
        self.adress = adress
        self.phone = "phone"
        
    def __iter__(self):
        self.i = -1
        self.value_list = list(self.__dict__.values())
        return self
    
    def __next__(self):
        self.i += 1
        if self.i == len(self.value_list):
            raise StopIteration
        return self.value_list[self.i]
    
    def __call__(self):
        print("hi")
        
test = Iter(3, "liad", "onot Hashana")
test()