tp = 100
print('Welcom to SF Cinema')
m = int(input('How many movie tickets do you need?:'))
pm = tp*m
print('full price=', pm)
if m < 3:
    t = pm
    print('total ticket price:', t)
else:
    vat=(pm*20)/100;
    t=pm-vat
    print('Promotion Sale 20%')
    print('total ticket price:', t)
    
money=int(input("please pay:"))
if (money > t):
    change=money-t
    print(change, "baht change")
elif (money == t):
    print("No change")
else:
    print("not enough money")
