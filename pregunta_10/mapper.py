#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
maxi = 2
if __name__ == "__main__":
    for line in sys.stdin:
        num, list_abc = line.split('\t')
        list_abc =list(list_abc.strip().split(','))
        num = num.zfill(maxi)
        for x in list_abc:
            sys.stdout.write("{}\t{}\n".format(x,num))