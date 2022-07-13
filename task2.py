import random

class City():
    
    def __init__(self, name, citizens : list, elites : list, mayor : str or int):
        self.name = name
        self.citizens = citizens
        self.elites = elites
        self.mayor = mayor


    def switch_mayor(self, id:int or str):
        if self.elites.__contains__(id):
            print(self.elites)
            x = self.elites.index(id)
            self.elites.insert(x, self.mayor)
            self.mayor = id
            self.elites.remove(id)
            print(self.mayor)
            print(self.elites)
            

    def switch_elite(self):
        if len(self.citizens) > 0:
            print(self.citizens)
            print (self.elites)
            x = random.choice(self.citizens)
            y = self.citizens.index(x)
            a = random.choice(self.elites)
            b = self.elites.index(a)
            self.citizens.remove(x)
            self.elites.insert(b, x)
            self.citizens.insert(y, a)
            self.elites.remove(a)
            print(self.citizens)
            print (self.elites)

    def get_index(self, x:int, array: list = None):
        index = []
        for i in range(len(array)):
            if array[i] == x:
                index.append(i)
        print(index)

    def switch_city_elites(city_id:int, city2_id:int):
        print(city.elites)
        print(city2.elites)
        x = city2.elites.index(city2_id)
        y = city.elites.index(city_id)
        if city.elites.__contains__(city_id):
            if y < x:
                city2.elites.insert(x + 1, city_id)
            else:
                city2.elites.insert(x, city_id)
        if city2.elites.__contains__(city2_id): 
            if x < y:
                city.elites.insert(y + 1, city2_id)
            else:
                city.elites.insert(y, city2_id)
        if city.elites.__contains__(city_id) and city2.elites.__contains__(city2_id):
            city.elites.remove(city_id)
            city2.elites.remove(city2_id)
        print(city.elites)
        print(city2.elites)

            
city = City("City", [1, 5, 8, 2, 9], [10, 8, 3, 7, 9], 34)
city2 = City("City", [1, 2, 3, 4, 5, 8], [5, 2, 6, 4, 3, 7], 42)

if __name__ == "__main__":
    City.switch_city_elites(7,5)