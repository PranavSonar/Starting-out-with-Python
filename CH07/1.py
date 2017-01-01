i=0
list1 =[]
total_sale=0
print 'Enter sale of Monday to Saturday: '
while i<=5:
    get_sale = int(raw_input())
    i += 1
    list1.append(get_sale)
for i in list1:
    total_sale = i+total_sale
print 'Total sale of week is = ',total_sale