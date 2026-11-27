
for i in range(2,10):
    if i == 5:
     break 
    print(i) 


for i in range(1,6):
    if i ==3:
       continue
    print(i)


for i in range(1,5):
    if i ==3:
        pass
    print(i)

for i in range(1,15):
   if i == 6:
    continue
   if i == 9:
    break
   print(i)

num = int(input("Enter the number"))
for i in range(1,12):
   print(num, "x","=", num*i)