import os
def write_file():
    filename = 'random_chars.txt'
    with open(filename,'w') as file_object:
        file_object.write(str(os.urandom(1000)))
        file_object.close()
    
def read_file():
    filename = 'random_chars.txt'
    with open(filename) as file_object:
        lines = file_object.readlines()
    for line in lines:
        print (line)
write_file()
read_file()

