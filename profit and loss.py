cp= int(input("Input the COST price: "))
sp= int(input("Input the SELLING price: "))

if sp>cp:
    profit= sp-cp
    print(f"Profit: {profit}")
else:
    loss= cp-sp
    print(f"Loss: {loss}")