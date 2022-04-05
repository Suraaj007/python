class college():
    def __init__(self,colgid,name,city,rating) -> None:
        self.colgid=colgid
        self.name=name
        self.city=city
        self.rating=rating
class university():
    def __init__(self,universityname, colgcollection) -> None:
        self.universityname=universityname
        self.colgcollection=colgcollection   
    def findcolgbycity(self,searchcity):
        obj=None
        #citynames=['mumbai','pune','banglore']
        #r=input('enter a city name')
        for item in self.colgcollection:
            if item.city.lower() == searchcity.lower():
                obj= item
                break
        if obj==None:
            return None
        else:
            return obj

        
    def sortcolgbyrating(self,rating):
        if len(self.colgcollection)<=0:
            return None
        else:
            sortedcc=[]
            sortedids=[]
            sortedcc= sorted(collegecollection,key=lambda x:x.rating) 

            for item in sortedcc:
                sortedids.apppend(item.colgid)
                return sortedids
n=int(input('enter no of colges'))
collegecollection=[]
for i in range (n):
    colgid=int(input())
    name= input()
    city= input()
    rating=int(input())
    collegecollection.append(college(colgid,name,city,rating))


y= university('abc',collegecollection)
searchcity=input()
val=y.findcolgbycity(searchcity)
res=y.sortcolgbyrating()

if val==None:
    print('no data found')
else:
    print(val.colgid,val.name,val.city,val.rating,sep='\n')  

if res==None:
    print('no data found')
else:
    for item in res:
        print(item)    

