class circle():
    #CLASS OMJECT ATTRIBUTE
    pi=3.14

    def __init__(self,radius=1):
        self.radius=radius
        self.area= self.pi*radius*radius
    #methd
    def get_cicumference(self):
        return self.radius*self.pi*2  #u can replaace self.pi by circle.pi
my_circle= circle(2)
print(my_circle.pi)
print(my_circle.radius)    
print(my_circle.area)    
print(my_circle.get_cicumference())    
