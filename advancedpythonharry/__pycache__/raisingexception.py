def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError('this is not good harry')

a=increment('364f') 
print(a)           
