#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#! /usr/bin/ python
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        credit_type=line.split(",")[2]
        sys.stdout.write("{}\t1\n".format(credit_type))