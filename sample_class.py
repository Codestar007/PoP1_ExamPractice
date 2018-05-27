class  Person:
    """Simple  example  of  a  class"""

    species = 'human' #  class variables
    def get_species():  # class method
        return Person.species

    # Instance methods
    def  __init__(self,  name,  age):
         self.name  =  name
         self.age  =  age

    def  get_older(self,  n  =  1):
         self.age  +=  n
         return  self.age

    def  get_first_name(self):
         return  self.name.split()[0]

    def  __str__(self):
         return  self.name

    def  __repr__(self):
         return  "Person('"  +  self.name  +  "',"  +  str(self.age) +  ")"

class  Employee(Person):
    """ Subclass employee"""
    pass

    def __init__(self, name, role):
        super().__init__(name, -1)
        self.role = role
        self.age = 'irrelevant'

    # Overriding
    def __str__(self):
        if self.role == 'professor':
            return 'Dr.  ' + self.name
        else:
            return self.name

jenny = Person("Jennifer Jones", 23)
print(jenny.name)
print(jenny)
print(repr(jenny))
eval(repr(jenny))

sam = Employee('Sam Smith', 40)
print(sam)

jennyD  =  Employee('Jennifer  Jones',  'professor')
samD = Employee('Sam Smith', 'clerk')
print(jennyD)
print(samD)

print(Person.get_species())
print(jenny.species)