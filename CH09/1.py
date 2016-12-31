room_dict = {}
ins_dict = {}
time_dict = {}
n=1
def create_dict():
   
    room_dict['CS101'] = '3004'
    room_dict['CS102'] = '4501'
    room_dict['CS103'] = '6755'
    room_dict['NT110'] = '1244'
    room_dict['CM241'] = '1411'
    
    ins_dict['CS101'] = 'Haynes'
    ins_dict['CS102'] = 'Alvarado'
    ins_dict['CS103'] = 'Rich'
    ins_dict['NT110'] = 'Burke'
    ins_dict['CM241'] = 'Lee'
    
    time_dict['CS101'] = '8.00 a.m.'
    time_dict['CS102'] = '9.00 a.m.'
    time_dict['CS103'] = '10.00 a.m.'
    time_dict['NT110'] = '11.00 a.m.'
    time_dict['CM241'] = '1.00 p.m'
    
create_dict()
print "List of courses:  "
for i in room_dict:
    print str(n)+") " + i
    n+=1
get_course = (raw_input("Select course to get details: "))

if get_course in room_dict:
    get_room = room_dict.get(get_course, 'default')
    get_ins = ins_dict.get(get_course, 'default')
    get_time = time_dict.get(get_course, 'default')
    
    print "Here are details for %r course" %(get_course)
    print "Room No: ", get_room
    print "Instructor Name: ", get_ins
    print "Course Time: ", get_time
else:
    print "Enter correct course Number."