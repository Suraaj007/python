'''class Animal():
    def __init__(self):
        print('animal created')
    def who_am_i(self):
        print('i am an animal')
    def eat(self):
        print('i am eating')
    def bark(self):
        print('woof!')    
myanimal=Animal()
#print(myanimal)            
myanimal.eat()

#inheritance = we use some of methods from base class in our derived class wo writing them again

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('dog created')
    def who_am_i(self):
        print('i am an dog')    
mydog= Dog()    
mydog.eat()
mydog.who_am_i()
mydog.bark()'''

#polymorphism
class Dog():
    def __init__(self,name) -> None:
        self.name=name
    def speak(self):
        return self.name +' says woof!'
class cat():
    def __init__(self,name) -> None:
        self.name=name
    def speak(self):
        return self.name +' says meow!'            
niko=Dog('niko')
felix=cat('felix')
print(niko.speak())
print(felix.speak())

def petspeak(pet):
    print(pet.speak())
petspeak(niko)
petspeak(felix)
    