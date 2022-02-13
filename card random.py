import random
for i in range(5):
 c1=(random.randint(1,10))
 c2=(random.randint(1,10))
 print("ไพ่ใบที่ 1 =",c1)
 print("ไพ่ใบที่ 2 =",c2)
 total=c1+c2
 print("รวม=",total)
 if total == 8:
   print("ป็อกเด้ง")
   break
 elif total == 9:
   print("ป็อกเด้ง")
   break
 elif total < 5 :
   print("ขอไพ่ใบที่ 3")
