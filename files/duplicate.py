#check if 2 files are identical
with open('this.txt') as f:
    content1=f.read()
with open('copy.txt') as f:
    content2=f.read()    

if content1==content2:
    print('identical files')
else:
    print(' not identical files')