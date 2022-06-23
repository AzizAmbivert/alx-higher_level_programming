#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
         return(True)
     except Exception as printing:
         print("Exception: {}".format(printing), file=sys.stderr)
         return(False)
