from socket import *

servidorPuerto = 12000
servidorSocket = socket(AF_INET,SOCK_STREAM)
servidorSocket.bind(('',servidorPuerto))
servidorSocket.listen(1)
print("El servidor está listo para recibir mensajes")

#retorna saldo del archivo saldo.txt
def saldo(): 
    archivo = open("saldo.txt", "r")
    x = archivo.readlines()
    archivo.close()
    return x

def debitar(x):
    #lee archivo
    archivo = open("saldo.txt", 'r')
    r = archivo.readlines()
    #print(r[0])
    y = 0
    if x <= float(r[0]):
        y = round(float(r[0])-x,2)
        #print(y)
        archivo.close()

        #modifica archivo
        archivo = open("saldo.txt", 'w')
        archivo.write(str(y))
        archivo.close()
        return ("OK")
    else:
        return ("Saldo insuficiente")
        


def acreditar(x):
    #lee archivo
    archivo = open("saldo.txt", 'r')
    r = archivo.readlines()
    #print(r[0])
    y = round(float(r[0])+x,2)
    #print(y)
    archivo.close()

    #modifica archivo
    archivo = open("saldo.txt", 'w')
    archivo.write(str(y))
    archivo.close()
    
    return ("Nuevo saldo: "+str(y))
        
    
while 1:
    conexionSocket, clienteDireccion = servidorSocket.accept()
    print("Conexión establecida con ", clienteDireccion)
    mensajenum = str( conexionSocket.recv(1024), "utf-8" )
    mensaje = str( conexionSocket.recv(1024), "utf-8" )
    print("Mensaje recibido de ", clienteDireccion)
    print("mensajenum: ",mensajenum)
    print("mensaje: ",mensaje)
    if mensajenum == "1":
        L = saldo() # retorna una lista con el saldo en str en la posicion 0
        mensajeRespuesta = L[0] 
    elif mensajenum == "2":
        mensajeRespuesta = debitar(float(mensaje))
    elif mensajenum == "3":
        mensajeRespuesta = acreditar(float(mensaje))
        
    conexionSocket.send(bytes(mensajeRespuesta, "utf-8"))
    conexionSocket.close()
