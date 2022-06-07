#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    cp_list = []
    for num in my_list:
        if num % 2 == 0:
            cp_list.append(True)
        else:
            cp_list.append(False)
    return cp_list
