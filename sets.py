#playing with sets in python

x = set() # use this for empty sets.
y = {1,5,3,8,5,1,9,10,9,8,5}
z = {} # dont do this, this creates a dict, not a set, use set() for empty sets
print(x)
print(y)

#add to the set
y.add(7)
print(y)
y.remove(1)
print(y)
print(5 in y) # returns True is 5 is in our set
print(11 in y) # returns False as 11 is not in the set
y.add(11) # add 11 to the set
print(y)
print(11 in y) # returns True because we added 11 to the set


