def get_large(list1,n):
    for i in list1:
        if i>n:
            print i,' is greater than ', n
        else:
            pass
list1 = raw_input('Enter comma separated numbers: ')
n = raw_input('Enter number: ')
get_large(list1,n)