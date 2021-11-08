def getApples_Oranges_Appleprice_Orangeprice():
    _apples = int(input("How many apples? "))
    _orange = int(input("How many oranges? "))
    _apple_price = 20
    _orange_price = 25
    return _apples, _orange, _apple_price, _orange_price
def getTotalcost(ApplesF, ApplepriceF, OrangesF, OrangepriceF):
    _total_cost = (ApplesF * ApplepriceF) + (OrangesF * OrangepriceF)
    return _total_cost
def display(totalcostF):
    print(f"The total amount is {totalcostF}.") 


Apples, Oranges, Appleprice,  Orangeprice = getApples_Oranges_Appleprice_Orangeprice()
totalcost = getTotalcost(Apples, Appleprice, Oranges, Orangeprice)
display(totalcost)
