'''
text type(String)
'''
''''
s = 'this is a string'
print(s)
print(type(s))
'''

#==============================================


'''
numeric type(integer, float, complex)
'''
''''
x = 0.123456789084758
print(type(x))
print(x)
'''



'''
sequence type (list, tuple, range)
'''
'''
#list
x = [10, 2.5, 'hello']
print(x[1:3])

#mutable
x[2] = 'pthyon'
print(x)
'''
#======================
'''
#tuple 
tuple = ()
tuple = ("cat", [4,3,2], (1,2,3))
tuple = 'hello',
print(type(tuple)) 

'''
#range =========================
'''
x = range(1,21)
for n in x:
  print(n)
'''

#mapping type (dict (dictionary))
# dict = {} -empty dict
# print (type(dict))

#========
'''
dict = {'name': 'louis', 'age':32}
print(dict['age'])
# or
print(dict.get('name'))

dict['age'] = 26
print(dict.get('age'))
'''

# SET
# Set only has single values set = set() is an empty set
'''
set = {1,2,3,4,5}
print(type(set))
print (set)
'''
'''
# set does not support indexing or duplicates

# Boolean (true or false or yes and no)

#Boolean as numbers
print(type(True))
print(True == 1)
print(False == 0)
#intresting logic
print(True + False)
#not Boolean operator
print(not True)
print(not False)
#and boolean operator
print(True and False)
print(True and True)
print(False and False)
#or boolean operator
print(True or False)
print(True or True)
print(False or False)
'''