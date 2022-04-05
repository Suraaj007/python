import os
#f=open('sample.txt','r')
f=open('sample.txt')  #by default the mode is read r


#data=f.read()
data=f.read(5)  #it will read starting 5 char of files
print(data)


f.close()