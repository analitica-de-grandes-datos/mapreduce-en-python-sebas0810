#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    word_actual = None
    list_num =[]
    for line in sys.stdin:

        word, valor = line.split("\t")
        valor = str(int(valor.strip()))

        if word == word_actual:
            list_num.append(valor)
        else:
            if word_actual is not None:
                sys.stdout.write("{}\t{}\n".format(word_actual, ",".join(list_num)))
            word_actual = word
            list_num =[valor]
            
    sys.stdout.write("{}\t{}\n".format(word_actual, ",".join(list_num)))