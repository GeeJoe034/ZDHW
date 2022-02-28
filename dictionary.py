class dictionary ():
    def __init__(self,v,t,m):
        self.v = v
        self.t = t
        self.m = m
    def details(self):
        print("{}".format(self.v),"        {}".format(self.t),"      {}".format(self.m))
i = 1
j = 2
num=0
while i < j:
  print("พจนานุกรม\n1) เพิ่มคำศัพท์\n2) แสดงคำศัพท์\n3) ลบคำศัพท์\n4) ออกจากโปรแกรม\n")
  choice=int(input("Input choice:"))
  if choice == 1 :
    print("เพิ่มคำศัพท์")
    v =input("คำศัพท์: ")
    t =input("ประเภท (n. , v. , adj. , adv.): ")
    m =input("ความหมาย: ")
    a = dictionary(v,t,m)
    print("เพิ่มคำศัพท์เรียบร้อย")
    num = +1
  elif  choice == 2 :
    print("           แสดงคำศัพท์           ")
    print("________________________________")
    print("     คำศัพท์มีทั้งหมด",num,"คำ     ")
    print("________________________________")
    print("คำศัพท์       ประเภท     ความหมาย")
    a.details()
  elif  choice == 3 :
    print("ลบคำศัพท์")
  elif  choice == 4 :
    print("ออกจากโปรแกรม")
    
