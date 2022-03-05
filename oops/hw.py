#1
class line():
    def __init__(self,coor1,coor2) -> None:
        self.coor1=coor1
        self.coor2=coor2
    def dist(self):
        a= self.coor1[0]
        b= self.coor1[1]
        c=self.coor2[0]
        d=self.coor2[1]
        e= (c-a)**2
        f = (d-b)**2
        g=(e+f)**.5
        return g

    def slope(self):
       a,b =self.coor1 # u can use this or above method to extract data in tuples
       c,d= self.coor2
       return     (d-b)/(c-a)
coor1= (3,2)
coor2=(8,10)

li = line(coor1,coor2)  
print(li.slope() )
print(li.dist() )
