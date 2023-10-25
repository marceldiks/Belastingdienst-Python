
class Person:
    
    def __init__(self, name, residence):
        self.name = name
        self.residence = residence

    def tell(self):
        return f'Ik ben {self.name} en ik woon in {self.residence}.'

    def move(self, new_residence):
        self.residence = new_residence

# ---------------------------------------

# instantiation
p1 = Person('Peter', 'Lhee')
p2 = Person('Emma', 'Arnhem')

print(p1.tell())
print(p2.tell())

print(Person.tell(p1))
print(Person.tell(p2))

p1.move('Apeldoorn')

print(p1.tell())
