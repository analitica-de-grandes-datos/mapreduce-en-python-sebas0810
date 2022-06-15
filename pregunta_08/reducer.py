#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    word_actual = None
    cont = float(0)
    total = float(0)

    for line in sys.stdin:

        word, valor = line.split(",")
        valor = float(valor)

        if word == word_actual:
            total+= valor
            cont+= 1
        else:
            if word_actual is not None:
                prom = total/cont
                sys.stdout.write("{}\t{}\t{}\n".format(word_actual, total, prom))

            word_actual = word
            cont = 1
            total = valor

    prom = total/cont
    sys.stdout.write("{}\t{}\t{}\n".format(word_actual, total, prom))