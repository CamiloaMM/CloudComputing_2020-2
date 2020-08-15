from socket import *

def saldo():
    arch = open("saldo.txt","r")
    saldo = float(arch.readlines()[0])
    return str(saldo)

def debitar(X):
    arch = open("saldo.txt","r")
    saldo = float(arch.readlines()[0])
    arch.close()

    arch = open("saldo.txt","w")
    if saldo-X<0:
        arch.write(str(saldo))
        arch.close()
        return "Saldo insuficiente"
    else:
        saldo = round(saldo - X,2)
        print(saldo)        
        arch.write(str(saldo))
        arch.close()
        return "OK"

def acreditar(Y):
    arch = open("saldo.txt","r")
    saldo = float(arch.readlines()[0])
    arch.close()

    saldo = round(saldo + Y,2)
    arch = open("saldo.txt","w")
    arch.write(str(saldo))
    arch.close()
    return "Nuevo Saldo: " + str(saldo)


servidorPuerto = 12000
servidorSocket = socket(AF_INET,SOCK_STREAM)
servidorSocket.bind(('',servidorPuerto))
servidorSocket.listen(1)
print("El servidor está listo para recibir mensajes")
while 1:
    conexionSocket, clienteDireccion = servidorSocket.accept()
    print("Conexión establecida con ", clienteDireccion)
    mensaje = str( conexionSocket.recv(1024), "utf-8" )
    print("Mensaje recibido de ", clienteDireccion)
    print(mensaje)
    msj = mensaje.split(" ")
    print(msj)
    print(msj[0])
    if msj[0] == "saldo":
        mensajeRespuesta = saldo()
    if msj[0] == "debitar":
        mensajeRespuesta = debitar(float(msj[1]))
    if msj[0] == "acreditar":
        mensajeRespuesta = acreditar(float(msj[1]))
    elif msj[0] != "saldo" and msj[0] != "debitar" and msj[0] != "acreditar":
        mensajeRespuesta = "Instruccion no valida"

    print(mensajeRespuesta)
    conexionSocket.send(bytes(mensajeRespuesta, "utf-8"))
    conexionSocket.close()