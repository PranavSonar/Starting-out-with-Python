#program that checks if list of 9 numbers = 15.
import random

numList = random.sample(range(10),9)

#numList = [8, 1, 6, 3, 5, 7, 4, 9, 2]   


sum1 = sum(numList[:3])
sum2 = sum(numList[3:6])
sum3 = sum(numList[6:])
sum4 = numList[0] + numList[4] + numList[8]
sum5 = numList[2] + numList[4] + numList[6]




if sum1 == sum2 == sum3 == sum4 == sum5 == 15:
    print(str(numList) + ' is in fact a magic square')
else:
    print('Sorry, but ' + str(numList) + ' is not a magic square')