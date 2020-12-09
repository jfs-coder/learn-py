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
