class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_info(self):
        print(f'Name: {self.name}  Age: {self.age}')

p1 = Person("John", 36)

p1.get_info()

class Order: 
    def __init__(self, orderType, amount):
        self.orderType = orderType
        self.amount = amount
        
    def get_info(self):
        print(f'Order Type: {self.orderType}  Amount: {self.amount}')

orderTable = Order("SELL", 0.375)

orderTable.get_info()



