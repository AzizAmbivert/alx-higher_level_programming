#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    sumx = 0
    for i in my_list:
        try:
            if i <= x:
                sumx += 1
                print("{}".format(i), end="")
        except IndexError:
            pass
    print()
    return(sumx)
