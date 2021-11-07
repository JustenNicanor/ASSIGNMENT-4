def getNameAgeAdress():
    _name = input("What is your name? ")
    _age = input("What is your age? ")
    _address = input("what is your address? ")
    return _name, _age, _address
def display(NameF, AgeF, AddressF):
    print (f"Hi, my name is {NameF}. I am {AgeF} years old and I live in {AddressF}")

Name, Age, Adress = getNameAgeAdress()
display(Name, Age, Adress)

