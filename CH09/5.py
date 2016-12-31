my_dict = {}
my_dict['user1'] = 'user1@someplace.com'
my_dict['user2'] = 'user2@someplace.com'
my_dict['user3'] = 'user3@someplace.com'
my_dict['user4'] = 'user4@someplace.com'
my_dict['user5'] = 'user5@someplace.com'

import pickle
file = open('output.txt','rb')
my_dict = pickle.load(file)
file.close()

get_input = int(raw_input('Select option:\n1. Display email of user\n2.Add new user and email\n3.Change email address\n4.Delete user\n'))
if get_input == 1:
    for i in my_dict:
        get_user = raw_input('Enter user name: ')
        user_email = my_dict.get(get_user,'User not found.')
        print user_email
        break
elif get_input == 2:
    get_user = raw_input('Enter user name:')
    get_email = raw_input('Enter email: ')
    my_dict[get_user] = get_email
    print 'User added successfully.'
elif get_input == 3:
    get_user = raw_input('Enter user name to edit email:')
    get_email = raw_input('Enter new email address: ')
    my_dict[get_user] = get_email
elif get_input == 4:
    get_user = raw_input('Enter user to delete: ')
    del my_dict[get_user]
else:
    print 'Select correct option.'
    
file = open('output.txt','wb')
write_data = pickle.dump(my_dict,file)
file.close()