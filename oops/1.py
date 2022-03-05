class Dog():
    #CLASS OBJECT ATTRIBUTE
    #SAME FOR ANY INSTANCE OF CLASS
    species='mammal'

    def __init__(self,breed,name,spots):
        #attrributes
        #we take in argument
        #assign it using self.attribute_name
        self.breed=breed
        self.name=name
        #expect boolean true or false
        self.spots=spots
    # operations /actions---methods
       
    def bark(self,number):
        print('woof!! my name is {} and number is {}'.format(self.name, number))    
my_dog=Dog(breed='lab',name='sammy',spots=False)        
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)
my_dog.bark(10)

