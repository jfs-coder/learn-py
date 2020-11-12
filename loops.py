def line():
	print '-------------------'

# while loops
line()
ok = 0
while (ok < 10):
	print "Spam",ok
	ok += 1

line()

# for loops
admins = ["Skidy", "Ashu", "Dork"]

for i in admins:
	print(i)

line()

# for loops (more)
for j in range(0,10):
	print(j)

line()

# use third argument for increment size
for z in range(0,20,2):
	print(z)

for y in range(0,30,3):
	print(y)
else:
	print("Jobs Done")
