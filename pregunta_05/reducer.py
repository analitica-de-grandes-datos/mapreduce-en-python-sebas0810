#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    mes_actual = None
    total = 0

    for line in sys.stdin:

        mes, valor = line.split("\t")
        valor = int(valor)

        if mes == mes_actual:
            total += valor
        else:
            if mes_actual is not None:
                sys.stdout.write("{},{}\n".format(mes_actual, total))

            mes_actual = mes
            total = valor

    sys.stdout.write("{},{}\n".format(mes_actual, total))