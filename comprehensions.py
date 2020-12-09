# comprehensions - populate a list in declaration.
# populates a list with numbers 0 to 99
x = [x for x in range(100)]
print(x)
# adds 2 to the start of the range
x = [x + 2 for x in range(10)]
print(x)
# puts 100 zeroes in a list
x = [0 for x in range(100)]
print(x)
# puts 100 'a' in a list
z = ['a' for x in range(100)]
print(z)
# populate lists of lists
d = [[7 for x in range(10)] for x in range(5)]
print(d)
# add conditions (modulo example here)
m = [i for i in range(100) if i % 5 == 0] # will print out 0, 5, 10, 15, ... 95
print(m)
# also works for dictionaries
dct = {i:0 for i in range(10) if i % 2 == 0} # will populate dict with all even numbers between 0-10
print(dct)
# and sets
st = {i for i in range(60) if i % 3 == 0} # will populate set with all modulo results
print(st)
# dont forget tuples
tp = tuple(i for i in range(40) if i % 4 == 0)
print(tp)

