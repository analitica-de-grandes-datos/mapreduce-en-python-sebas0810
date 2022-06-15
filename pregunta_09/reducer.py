#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':
    cont=0
    for line in sys.stdin:
        linea = line.split(",")
        value=int(linea[0].strip())
        word=linea[1].strip()
        fecha=linea[2].strip()
        sys.stdout.write("{}  {}  {}\n".format(word,fecha,value))
        cont+=1
        if(cont==6):break