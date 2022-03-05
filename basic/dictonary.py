

#to search value quickly using key
from winreg import KEY_CREATE_SUB_KEY


dict={'apple':'3','orange':'4','mango':'5'}

print(dict['apple'])

#to find data inside key
d={'k1':'123','k2':['0','1','2'],'k3':{'insidekey':'100'}}
print(d)
print(d['k2'][1])

# to slect object iside list from dictonary and convert into upercase using upper()
a={'k4':['a','b','c']}
print(a['k4'][1].upper())

#to add new data ina dict
d['k5']='8'
print(d)

#to see KEy
print(d.keys())
print(d.values())
print(d.items())
