from socket import *

servidorNombre = "127.0.0.1" 
servidorPuerto = 12000

mensajenum = 1
while mensajenum != "0":
    clienteSocket = socket(AF_INET, SOCK_STREAM)
    clienteSocket.connect((servidorNombre,servidorPuerto))
    print("Opciones:")
    print("1. Saldo")
    print("2. Debitar")
    print("3. Acreditar")
    print("0. Salir")
    numero = input("Ingrese el numero correspondiente a la opcion que desea:")
    print("Numero ingresado: ", numero)

    if numero == "1":
        mensajenum = numero
        mensaje = numero
        clienteSocket.send(bytes(mensajenum, "utf-8"))
        clienteSocket.send(bytes(mensaje, "utf-8"))
        mensajeRespuesta = clienteSocket.recv(1024)
        print("Respuesta:\n" + str(mensajeRespuesta, "utf-8")+"\n")
    elif numero == "2" or numero == "3":
        mensajenum = numero
        mensaje = input("Ingrese el valor: ")
        clienteSocket.send(bytes(mensajenum, "utf-8"))
        clienteSocket.send(bytes(mensaje, "utf-8"))
        mensajeRespuesta = clienteSocket.recv(1024)
        print("Respuesta:\n" + str(mensajeRespuesta, "utf-8")+"\n")
    elif numero == "0":
        mensajenum = numero
        clienteSocket.close()
    else:
        print("Numero invalido\n")

