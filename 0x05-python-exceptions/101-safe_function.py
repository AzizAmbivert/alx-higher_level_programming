#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return(fct(*args))
    except Exception as detail:
        print("Exception: {}".format(detail), file=sys.stderr)
        return(None)
