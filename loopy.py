# For Loop Five Ways
x = [7,6,4,8]

def sep():
        print('-------')
sep()
for i in x:
    print(i)
sep()
for i in range(len(x)):
    print(x[i])
sep()
for i in range(4):
    print(i)
sep()
for i in range(1000,0,-200):
    print(i)
sep()
for index, element in enumerate(x):
    print(index, element)
sep()



