#implement a student library sysytem using oops where students can borrow a book from the list of books
#create a separate library and studnt class. your program must be well driven
#you are free to choose meethod and attriutes of ur own choice to impleent the functinality
class library:
    def __init__(self,booklist) -> None:
        self.books=booklist
    def displayavailablebooks(self):
        print('The available book in the lirary are :')
        for book in self.books:
            print("*"+book)
    def borrowbook(self,bookname):
        if bookname in self.books:
            print(f"You have been issued a {bookname}. please keep it safe and return it within 30 days")
            self.books.remove(bookname)
        else:
            print("Sorry, This book is either not available been issued to someone else.Please wait until book is returned")    
    def returnbook(self,bookname):
        self.books.append(bookname)
        print('Thanks for returning the book! have a great day.')


class student:
    def requestbook(self):
        self.book=input('Enter a name of a book u want to borrow : ')
        return self.book

    def returnbook(self):
        self.book=input('Enter a name of a book you want to donate or return : ')
        return self.book

if __name__=="__main__":
    centrallibrary=library(["algorithms","datastructures","c","python notes"])
    student=student()
    while True:
        welcomemsg='''=====welcome to central library=====
        Please chhose an option
        1 Listing all the books
        2 Requeat a book
        3 Return  or donate a book
        4 Exit the library'''
        print(welcomemsg)
        a=int(input('enter your choice'))
        if a==1:
            centrallibrary.displayavailablebooks()
        elif a==2:
            centrallibrary.borrowbook(student.requestbook())
        elif a==3:
            centrallibrary.returnbook(student.returnbook())
        elif a==4:
            print('Thanks for using the library')
            exit()

            # centrallibrary.displayavailablebooks()
        else:
            print("invalid choice")


            

