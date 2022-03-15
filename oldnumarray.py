import array 

input_ = 1
j=0
array_ = array.array('i', [])
print("***Oldnumber By Pimnapa***")
while  j < 10:
        input_ = int(input("Input Number :"))
        if ( input_ % 2 != 0):
          array_.append( input_ )
          j+=1
        elif( input_ % 2 == 0):
          j+=1

print("Old number is... ")
for i in array_:
    print(i, end = ' ')

