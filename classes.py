class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1)
print(p1.name)
print(p1.age)

class Order: 
    def __init__(self, orderType, amount):
        self.orderType = orderType
        self.amount = amount

orderTable = Order("SELL", 0.375)

print(orderTable)

print(orderTable.__dict__)

