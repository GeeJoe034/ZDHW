price = 0
print("Bang Sue Central Station\nPlease select a destination")
print("1.Prachuap Khiri Khan\n2.Chumphon\n3.Ranong\n4.Siratthani")
d = (int(input("enter destination:")))
if d == 1:
    des = "Prachuap Khiri Khan"
elif d == 2:
    des = "Chumphon"
elif d == 3:
    des = "Siratthani"
print(des)
print("***Choose a train model***")
print("1.Seated air conditioner\n2.bed air conditioner\n3.Seated fan cabinet\n4.mattress cabinet fan")
t = int(input("select train:"))
if t == 1:
    tran = "Seated air conditioner"
    price = 1500
elif t == 2:
    tran = "bed air conditioner"
    price = 1500
elif t == 3:
    tran = "Seated fan cabinet"
    price = 1000
elif t == 4:
    tran = "mattress cabinet fan"
    price = 1000
print(tran)
f=input("Do you need food packages on the go (y/n)")
if f=="y":
  food = 350
  price=price+food
choice = input("Want to use the discount(y/n)")
if choice == "n":
  print("don't want a discount")
elif choice == "y":
    code = input("Please enter a discount code:")
    if code =="mile92":
      print("20% discount on travel expenses")
      sale = (price*20)/100
      price=price-sale
print("*****Bang Sue Central Station********")
print("travel list Bankok to ", des)
print("price = ", price)
money = int(input("please pay:"))
if(money >price):
    change = money-price
    print("change=",change)
elif(money ==price):
   print("get enough money")
else:
   print("Your balance is not enough")
print("*****thankyou********")
