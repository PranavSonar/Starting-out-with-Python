#Creating ASCII dictionary A->65
ascii_dict = dict()
ascii_in_number = range(65, 123)
for i in ascii_in_number:
    ascii_dict[chr(i)] = str(i)
#print(ascii_dict)

with open('output.txt') as f:
  while True:
    c = f.read(1)
    if not c:
      #print "End of file"
      break
    encrypted_contents = ascii_dict.get(c, '032')  #  'space ascii 032 not included in range'
    print encrypted_contents

