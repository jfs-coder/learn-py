orders = {
        "orderType": "NULL", 
        "amount": 0.0,
}

print(orders["orderType"])
print(orders["amount"])


orders["orderType"] = "SELL"
orders["amount"] = 0.357
#add new dict entries
orders["time"] = "19:04"
orders["orderID"] = 15734

#print(orders)
print(orders["orderType"])
print(orders["amount"])
print(orders["time"])
print(orders["orderID"])

#print the whole orders dict
print('-----')
print(orders)

