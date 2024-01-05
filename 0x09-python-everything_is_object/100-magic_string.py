#!/usr/bin/python3
def magic_string(my_list=[]):    
    my_list.append("BestSchool")    
    return ', '.join(my_list)

for i in range(10):
    print(magic_string())