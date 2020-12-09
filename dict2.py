# dict2.py
x = {'key1': 4}
print(x)
print(x['key1'])
x['key2'] = 5 # adds key2 to the dictionary
print(x)
print(x['key2'])
x['key3'] = 6 # adds key3 to dict
print(x)
print(x['key3'])
del x['key3'] # removed 'key3' from dict
print(x)
# checking to see if something is in the dictionary
print('key1' in x) # prints 'True' if it's there
# get all the values from the dictionary
print(x.values())
print(list(x.values())) # another way
print(list(x.keys())) # printing the keys
# adding a few keys for next example
x['key3'] = 67
x['key4'] = 89
x['key5'] = 34
x['key6'] = 17
# looping over the dictionary
for key, value in x.items(): # I guess x.items() is counted up to see how many keys there are
    print(key, value)
    print('-----')
# another way
for key in x:
    print(key, x[key])


