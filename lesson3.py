class Human():
    
    def __init__(self, height:float, weight:float or int):
        self.height = height
        self.weight = weight
        self.tall = False
        if height > 1.80:
            self.tall = True

    def isFat(self) -> bool:
        if self.weight > 60:
            return True
        return False


sagi = Human(1.81, 56)

print(sagi.isFat())