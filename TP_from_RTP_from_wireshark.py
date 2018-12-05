# Autor: Enrique Casale Linde

#Forma de uso:
#1º Parametro: Nombre del ficho pcap, incluyendo la extension
#2º Parametro: Numero del paquete a examinar

from scapy.all import *
from io import StringIO
import sys

#Requiere: pip3 install scapy

#Obtiene el campo Payload type de un paquete
def depurar_paquete(lista):
    indice = lista.index("ByteEnumField")
    return lista[indice+2]

#Obtiene el tipo de medio esta utilizndo un paquete
def obtener_tipo_RTP(tipo):
    print("Enconding | Media type")
    print("----------------------")
    if tipo == "0":
        print("PCMU      | Only audio")
    elif tipo == "1" or tipo == "2" or tipo == "18":
        print("Reserved  | Only audio")
    elif tipo == "3":
        print("GSM       | Only audio")
    elif tipo == "4":
        print("G723      | Only audio")
    elif tipo == "5" or tipo == "6" or tipo == "16" or tipo == "17":
        print("DVI4      | Only audio")
    elif tipo == "7":
        print("LPC       | Only audio")
    elif tipo == "8":
        print("PCMA      | Only audio")
    elif tipo == "9":
        print("G722      | Only audio")
    elif tipo == "10" or tipo == "11":
        print("L16       | Only audio")
    elif tipo == "12":
        print("QCELP     | Only audio")
    elif tipo == "13":
        print("CN        | Only audio")
    elif tipo == "14":
        print("MPA       | Only audio")
    elif tipo == "15":
        print("G728      | Only audio")
    elif tipo == "18":
        print("G729      | Only audio")
    elif tipo == "20" or tipo == "21" or tipo == "22" or tipo == "23":
        print("Unasigned | Only audio")
    elif tipo == "dyn":
        print("G726,G729,GSM-EFR,VDVI.... | Only audio or Only video")
    elif tipo =="24" or tipo == "27" or tipo == "29" or tipo == "30":
        print("Unasigned | Only video")
    elif tipo == "25":
        print("CelB      | Only video")
    elif tipo == "26":
        print("JPEG      | Only video")
    elif tipo == "28":
        print("nv        | Only video")
    elif tipo == "31":
        print("H261      | Only video")
    elif tipo == "32":
        print("MPV       | Only video")
    elif tipo == "33":
        print("MP2T      | Only video")
    elif tipo == "34":
        print("H263      | Only video")
    elif int(tipo) >= 35 and int(tipo) <= 71:
        print("UNASIGNED | ?")
    elif int(tipo) >= 72 and int(tipo) <= 76:
        print("reserved  | N/A")
    elif int(tipo) >= 77 and int(tipo) <= 95:
        print("UNASIGNED | ?")
    elif int(tipo) >= 96 and int(tipo) <= 127:
        print("Dynamic   | ?")

#Archivo a examinar
archivo = str(sys.argv[1])

#Numero de paquete a examinar
paquete = int(sys.argv[2])

#Abro el archivo pcap
packets = rdpcap(archivo)

#Redirijo la salida estandar para guardar el paquete en una lista
old_stdout = sys.stdout
sys.stdout = mystdout = StringIO()
ls(packets[paquete])
lista = str(mystdout.getvalue()).split()

#Devuelvo la salida estandar a la normalidad
sys.stdout = old_stdout

valor = ""
#Obtengo el campo TP y devuelvo su valor en string
valor = depurar_paquete(lista)

#Obtengo el tipo de transmision
obtener_tipo_RTP(valor)
