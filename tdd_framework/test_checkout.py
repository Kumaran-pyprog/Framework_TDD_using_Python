class Checkout:
    class Discount:
        def __init__(self,nbrItems,price):
            self.nbrItems=nbrItems
            self.price=price

    def __init__(self):
        self.prices={}
        self.total=0
        self.discounts={}
        self.items={}
    def addItemPrice(self,item,price):
        self.prices[item]=price

    def addItem(self,item):
        if item not in self.prices:
            raise Exception("Bad Item")
        if item in self.items:
            self.items[item]+=1
        else:
            self.items[item]=1

    def calculateTotal(self):
        total=0
        for item,cnt in self.items.items():
            if item in self.discounts:
                discount=self.discounts[item]
                if cnt>=discount.nbrItems:
                    nbrofDiscounts=cnt/discount.nbrItems
                    total+=nbrofDiscounts*discount.price
                    remaining=cnt%discount.nbrItems
                    total+=remaining*self.prices[item]
                else:
                    total+=self.prices[item]*cnt
            else:
                total+=self.prices[item]*cnt
            total+=self.prices[item]*cnt
        return total


    def addDiscount(self,item,nbrfofitem,price):
        discount=self.Discount(nbrfofitem,price)
        self.discounts[item]=discount




