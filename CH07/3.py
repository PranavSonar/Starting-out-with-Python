count = 1
total_rain=0
list1=[]
print 'Enter rainfall from Jan to Dec: '

while count <=12:
    get_rain = int(raw_input())
    list1.append(get_rain)
    total_rain = total_rain + get_rain
    avg_rain = total_rain/12
    count += 1
    
print 'Total rain fall :', total_rain
print 'Avg rain fall is: ', avg_rain
print 'Max rain fall in ',max(list1) ,"Min rain fall in ",min(list1)