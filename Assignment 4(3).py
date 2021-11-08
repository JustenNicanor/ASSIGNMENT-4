def getMoneyamount_Appleprice():
    _money_amount = float(input("Enter your money amount: "))
    _apple_price = float(input("Enter the price of an apple you want: "))
    return _money_amount, _apple_price 
def getappleamount_maxapplesremmoney(MoneyamountF, ApplepriceF):
    _apple_amount= (MoneyamountF / ApplepriceF)
    _max_apples_rem_money = (MoneyamountF % ApplepriceF)
    return _apple_amount, _max_apples_rem_money
def display(AppleamountF, MaxapplesremmoneyF):
    print(f"You can buy {AppleamountF} apples and your change is {MaxapplesremmoneyF} pesos.")


Moneyamount, Appleprice = getMoneyamount_Appleprice()
Appleamount, Maxapplesremmoney = getappleamount_maxapplesremmoney(Moneyamount, Appleprice)
display(Appleamount, Maxapplesremmoney)

