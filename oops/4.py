from multiprocessing import AuthenticationError
from turtle import title


mylist=[1,2,3]
print(len(mylist))

#magic method
class Books():
    def __init__(self,title,author,pages):
        self.title =title
        self.author= author
        self.pages= pages
    def __str__(self) -> str:                  #this is magic method which will be useful
        return f'{self.title } by {self.author}'    
    def len(self):
        return self.pages
    def __del__(self):
        return print('the book object has been deleted')   
b=Books('python rocks','jose',200)
print(b)
str(b)
print(b.len())

del(b)  # to delete b from comp memory
