#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
maximo = 3
if __name__ == "__main__":
    for line in sys.stdin:
        linea=line.split("  ")
        word=linea[0]
        fecha=linea[1].strip()
        value=linea[2].strip().zfill(maximo)
        sys.stdout.write("{},{},{}\n".format(value,word,fecha))