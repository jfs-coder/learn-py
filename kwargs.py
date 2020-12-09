# *args and **kwargs
def sep():
    print('----')

def funk():
    def funky():
        print('2nd function being called')
    return funky
funk()()
sep()
x = [1,5,3,78,34]
# unpack operator *  ... pointers?
print(x)
sep()
print(*x)
sep()
print(x[0])
sep()

def disp(x,y):
    print(x,y)

pairs = [(1,2), (3,4)]
# non-pythonic way of doing it, but works.
for x in pairs:
    disp(x[0], x[1])
sep()
# pythonic way of going about it.
for x in pairs:
    disp(*x)
sep()    
# works with dicts
disp(**{'x': 5, 'y': 6}) # dicts need two * asterisks
sep()
disp(**{'y': 6, 'x': 5}) # order of keys doesn't matter
sep()
def func(*args, **kwargs):
    print(args, kwargs) 
    print(*args)
    print(*kwargs)
    # print(**kwargs)  <- doesn't work 

func(1,2,3,4,5, one=0, two=1)
sep()
# works with dicts too, just needs two asterisks to access

def show(x, y):
    print(x, y)

dt = {'x': 8, 'y': 9}

show(**dt)  # dicts need two asterisks
sep()




                                                                                

