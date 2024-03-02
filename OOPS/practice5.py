#WAP to Qs. Create a class called Order which stores item & its price. 
#Use Dunder function __gt__() to convey that: order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    
    def __gt__(self,obj2):
        return self.price>obj2.price
    def __ls__(self,obj2):
        return self.price<obj2.price

item1 = Order("Maggie",99)
item2 = Order("random string",100)

print(item1>item2)
print(item1<item2)