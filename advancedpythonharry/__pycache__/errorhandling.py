'''
try:
   # result=10+10
    result=10+'10'
except:
    print('hey it looks like u arent adding it crrectly')
else:
    print('add went well')
    print(result)        
'''


'''
try:
    #f=open('testfile','w')
    f=open('testfile','r')
    f.write('write a testline')
except TypeError:
    print('there was a type error')
#except OSError:
    print('hey u have an os error')
except:
    print('all other exceptions')    
finally:
    print('i always run')        
'''


def ask_for_int():
    while True:
        try:
            a=int(input('please provide no.'))
           # result=int(a)
            break
        except:
            print('whoops!! Thats not a no.')
            continue    
        finally:
            print('end of try except and finally')
ask_for_int()            
