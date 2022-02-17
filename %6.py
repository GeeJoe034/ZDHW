i=1
count=0
while i < 1001:
   if( (i % 6) == 0 ):
       print(i,":divide evenly")
       count +=1
       i +=1
   else:
       print(i,":undivided")
       i +=1
print("count=",count)
