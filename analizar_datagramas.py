#Enrique Casale Linde
import sys
import codecs

#Este programa precisa un parametro
#1º Parametro: Ruta hacia el archivo .txt

#Lee un fichero txt. Necesita la ruta hasta el fichero. Ejemplo: datagrama/0/ao.txt
def leer_fichero(ruta):
    archivo = open(ruta)
    fichero = archivo.read()
    archivo.close()
    return fichero

def imprimir_datagrama(array_de_bytes):
    acumulador = ""
    array_de_bytes = str(array_de_bytes)
    for i in range(0,len(array_de_bytes),1):
        if array_de_bytes[i] != " ":
            acumulador += array_de_bytes[i]
        else:
            print(acumulador)
            acumulador = ""

def es_http(cadena):
    if "HTTP" not in cadena:
        return False
    else:
        return True

def es_RTSP(cadena):
    if "RTSP" not in cadena:
        return False
    else:
        return True

def es_RTP(cadena):
    if "RTP" not in cadena:
        return False
    else:
        return True

ruta = str(sys.argv[1])
fichero = leer_fichero(ruta)
fichero = fichero.split()


#for i in range(0,len(fichero),2):
#print(bytes.fromhex(str(fichero[i]+fichero[i+1])).decode("base64"))
resultado = bytearray()
for i in range(0,len(fichero),1):
    if(fichero[i] != fichero[48]):
        resultado += bytearray.fromhex(fichero[i])

if es_http(str(resultado)):
    print("Es un datagrama HTTP")

if es_RTSP(str(resultado)):
    print("Es un datagrama RTSP")
elif es_RTP(str(resultado)):
    print("Es un datagrama RTP")


imprimir_datagrama(resultado)
