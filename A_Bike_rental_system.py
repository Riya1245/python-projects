
class TharShop:
    def __init__(self, Stock):
        self.Stock = Stock

    def displayThar(self):
        print("Total Thar:", self.Stock)

    def rentForThar(self, q):
        if q <= 0:
            print("Enter a positive value greater than zero")
        elif q > self.Stock:
            print("Enter a value less than or equal to the stock")
        else:
            self.Stock -= q
            print("Total price:", q * 100)
            print("Total Thar:", self.Stock)

while True:
    obj = TharShop(100)
    uc = int(input('''
    1. Display Stock
    2. Rent a Thar
    3. Exit
    '''))
    if uc == 1:
        obj.displayThar()
    elif uc == 2:
        n = int(input("Enter the quantity: "))
        obj.rentForThar(n)
    else:
        break




          
              