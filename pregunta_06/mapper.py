#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        linea=line.split("  ")
        word=linea[0]
        value=linea[2].strip()
        sys.stdout.write("{},{}\n".format(word,value))