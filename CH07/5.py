list1 = []

file = open('acc_no.txt','r')
acc_no = file.readline()
for i in file:
        i = i.rstrip('\n')
        list1.append(i)

get_acc = raw_input('Enter acc no to check: ')
if get_acc in list1:
    print 'Number is valid!'
else:
    print 'Number is invalid!'
