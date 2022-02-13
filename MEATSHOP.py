j=1
i=0
k=0
l=1
while k < l:
    money = 0
    while i < j:
        print("*******MEAT SHOP*******")
        print("1.Pork         200 baht / 1 kg\n2.Beef         150 baht / 1 kg\n3.Chicken meat 100 baht / 1 kg\n4.ผู้จัดทำ\n0.Checkbill")
        meat = input("choose meet: ")
        if meat == "1":
            print("Pork")
            kg = float(input("How many Kg do you want:"))
            price = kg*200
            print("Pork",kg,"Kg price",price,"baht")
            money = money+ price
            j += 1
        elif meat == "2":
            print("Beef")
            kg = float(input("How many Kg do you want:"))
            price = kg*150
            print("Beef",kg,"Kg price",price,"baht")
            money = money+ price
            j += 1
        elif meat == "3":
            print("Chicken meat")
            kg = float(input("How many kg do you want:"))
            price = kg*100
            print("Chicken meat",kg,"Kg price",price,"baht")
            money = money+ price
        elif meat == "4":
            print("************************************") 
            print("             จัดทำโดย                ")
            print("name") 
            print("************************************")
            j += 1
        elif meat == "0":
            print("Check bill")
            break

    print(money,"baht")
    m=float(input("please pay:"))
    if m > money:
        change= m-money
        print("chang = ",change,"baht")
        print("*****Thankyou*****")
    elif m == money:
        print("get enough money")
        print("*****Thankyou*****")
    else:
        print("not enough money")
    
    j += 1  
