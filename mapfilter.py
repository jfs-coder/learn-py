#playing with lambda, map, filter
x = [6,5,8,2,4,3]

def sep():
    print('------')

def funky(i):
        return i * 2
        
def filthy(f):
    return f % 2 == 0 #returns true if number is divisible by 2
            
#maps
sep()
mp1 = map(funky, x)
print(list(mp1)) # we convert the map to a list form before printing it out
sep()
mp2 = map(lambda i: i + 10, x) #we use lambda for anon function to apply +10 to each element
print(list(mp2)) 
sep()
mp3 = map(lambda z: z * 10, x) #multiply each element by 10 with lambda func
print(list(mp3))
sep()

#filter
fil = filter(filthy, x)
print(list(fil))
sep()
fil2 = filter(lambda i: i < 4, x)
print(list(fil2))
sep()

