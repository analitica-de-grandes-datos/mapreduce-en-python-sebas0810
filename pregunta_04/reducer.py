#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    word_actual = None
    total = 0

    for line in sys.stdin:

        word, valor = line.split("\t")
        valor = int(valor)

        if word == word_actual:
            total += valor
        else:
            if word_actual is not None:
                sys.stdout.write("{},{}\n".format(word_actual, total))

            word_actual = word
            total = valor

    sys.stdout.write("{},{}\n".format(word_actual, total))