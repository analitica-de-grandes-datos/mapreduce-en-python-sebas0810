#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        proposito=line.split(",")[3]
        monto=line.split(",")[4]
        sys.stdout.write("{}\t{}\n".format(proposito,monto))