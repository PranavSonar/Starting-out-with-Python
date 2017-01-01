import random
count=1
list1 =[]

while count <= 7:
    number = random.randint(0,9)
    list1.append(number)
    count +=1

print "lottery numbers are :"
for i in list1:
    print i
