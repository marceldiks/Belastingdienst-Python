class Person:
    
    def __init__(self, name, residence):
        self.name = name
        self.residence = residence

    def tell(self):
        return f'Ik ben {self.name} en ik woon in {self.residence}.'

    def move(self, new_residence):
        self.residence = new_residence


class Customer(Person):

    def __init__(self, name, residence, customernr):
        super().__init__(self, name, residence)
        self.customernr = customernr
            
    def tell(self):
        return f'Ik ben {self.name} en ik woon in {self.residence}. Ik ben een trouwe klant! Nr {self.customernr}'


class Vip(Customer):
    pass

# ---------------------------------------

# instantiation
p1 = Person('Peter', 'Lhee')
p2 = Customer('Emma', 'Arnhem', '3478536785')

print(p1.tell())
print(p2.tell())

p1.move('Apeldoorn')

print(p1.tell())
