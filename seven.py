num1=int(input("Enter num 1:"))
num2=int(input("Enter num 2:"))
num3=int(input("Enter num 3:"))
s=0
while num1 < num2:
 if num1 == 7:
    s +=1
    num1+=1
 else:
    num1 +=1
while num2 < num3:
 if num2 == 7:
    s +=1
    num2+=1
 else:
    num2 +=1
print("7=",s)
