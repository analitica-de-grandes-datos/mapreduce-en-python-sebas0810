#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    word_actual = None
    max = 0
    min = 0

    for line in sys.stdin:

        word, valor = line.split(",")
        valor = float(valor)

        if word == word_actual:
            if(valor>max):
                max = valor
            elif(valor<min):
                min = valor
        else:
            if word_actual is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(word_actual, max, min))

            word_actual = word
            max = valor
            min = valor

    sys.stdout.write("{}\t{}\t{}\n".format(word_actual, max, min))