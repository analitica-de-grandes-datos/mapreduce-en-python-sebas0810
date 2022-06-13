#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    actual_proposito = None
    monto_max = 0

    for line in sys.stdin:

        proposito, monto = line.split("\t")
        monto = int(monto)

        if proposito == actual_proposito:
            if(monto > monto_max):
                monto_max = monto
        else:
            if actual_proposito is not None:
                sys.stdout.write("{}\t{}\n".format(actual_proposito, monto_max))
            actual_proposito = proposito
            monto_max = monto

    sys.stdout.write("{}\t{}\n".format(actual_proposito, monto_max))