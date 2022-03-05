def panagram(str1,a):
    str1=str1.replace(' ','')
    str1=str1.lower()
    str1=set(str1)
    str2=set(a)
   # print(str1)
    return str1==str2
a='abcdefghijklmnopqrstuvwxyz'
str1='the quick brown fox jumps over the lazy dog'
print(panagram(str1,a))
print(panagram('abcdefghijklmnopqrstuvwxyz',a))
