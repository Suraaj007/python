class vector():

    def __init__(self,vec1,vec2):
        self.vec1=vec1
        self.vec2=vec2

    def add(self):
        x1,y1,z1=self.vec1
        x2,y2,z2=self.vec2
        r1=x1+x2
        r2=y1+y2
        r3=z1+z2
        
        print(f'{r1}i+{r2}j+{r3}k')

    def subtract(self):
        x1,y1,z1=self.vec1
        x2,y2,z2=self.vec2
        r1=x1-x2
        r2=y1-y2
        r3=z1-z2
        
        print(f'{r1}i+{r2}j+{r3}k')   
    
    def dotproduct(self):
        x1,y1,z1=self.vec1
        x2,y2,z2=self.vec2
        r1=x1*x2
        r2=y1*y2
        r3=z1*z2
        
        print(r1+r2+r3)
    def crossproduct(self):
        x1,y1,z1=self.vec1
        x2,y2,z2=self.vec2
        r1=(y1*z2)-(z1*y2)
        r2=(x2*z1)-(x1*z2)
        r3=(x1*y2)-(y1*x2)
        
        print(f'{r1}i+{r2}j+{r3}k')             
        
a=(3,2,1)
b=(1,2,3)
v=vector(a,b)
v.add()
v.subtract()
v.dotproduct()
v.crossproduct()
