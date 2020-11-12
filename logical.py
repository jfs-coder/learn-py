a = 1
b = 4

if(a == 2 or b == 4):
	print('it worked')
else:
	print('it failed')

if(a == 1 and b == 3):
	print('it worked')
else:
	print('it failed')

if(not(a == 2)):
	print("this should print if a equals 1")
else:
	print("this should print if a is not equal to 1")


secret = "thm{e46fg1927dh38721hd}"

if "thm" in secret:
	print(secret)
else:
	print("The secret is in another castle")

# Now, let's play with the 'is' operator

x = ['apple','banana','cherry']
h = ['apple','banana','cherry']
y = x
d = 5
f = d

print(x is y)
print(y is h)
print(d is f)


