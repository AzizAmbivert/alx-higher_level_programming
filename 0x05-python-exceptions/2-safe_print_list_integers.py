#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    sumx = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            sumx += 1
        except TypeError:
            pass
        except ValueError:
            pass
    print()
    return(sumx)
