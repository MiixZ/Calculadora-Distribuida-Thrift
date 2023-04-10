from calculadora import Calculadora
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

transport = TSocket.TSocket("localhost", 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Calculadora.Client(protocol)

transport.open()

print("Haciendo ping al server.")
client.ping()

haciendo_operaciones = True

def pide_cociente():
    opcion_cociente = input('Elija qué operación desea hacer con los valores que introduzca en el cociente: \n'
          '1) Sumar. \n'
          '2) Restar. \n'
          '3) Multiplicar. \n'
          '4) Introducir valor directamente. \n')
    opcion_cociente = int(opcion_cociente)

    if opcion_cociente == 1:
        valores_cociente = input('Introduzca los valores que desee sumar separados por un espacio: \n')
        numeros_cociente = [float(x) for x in valores_cociente.split()]
        cociente = client.suma(numeros_cociente)
    elif opcion_cociente == 2:
        valores_cociente = input('Introduzca los valores que desee restar separados por un espacio: \n')
        numeros_cociente = [float(x) for x in valores_cociente.split()]
        cociente = client.resta(numeros_cociente)
    elif opcion_cociente == 3:
        valores_cociente = input('Introduzca los valores que desee multiplicar separados por un espacio: \n')
        numeros_cociente = [float(x) for x in valores_cociente.split()]
        cociente = client.multiplicacion(numeros_cociente)
    else:
        cociente = input('Introduzca el valor del cociente: \n')
        cociente = float(cociente)

    return cociente

def pide_divisor():
    divisor = 0

    while divisor == 0:
        opcion_divisor = input('Elija qué operación desea hacer con los valores que introduzca en el divisor: \n'
                                '1) Sumar. \n'
                                '2) Restar. \n'
                                '3) Multiplicar. \n'
                                'Cualquier otro número) Introducir valor directamente. \n')
        opcion_divisor = int(opcion_divisor)

        if opcion_divisor == 1:
            valores_divisor = input('Introduzca los valores que desee sumar separados por un espacio: \n')
            numeros_divisor = [float(x) for x in valores_divisor.split()]
            divisor = client.suma(numeros_divisor)
        elif opcion_divisor == 2:
            valores_divisor = input('Introduzca los valores que desee restar separados por un espacio: \n')
            numeros_divisor = [float(x) for x in valores_divisor.split()]
            divisor = client.resta(numeros_divisor)
        elif opcion_divisor == 3:
            valores_divisor = input('Introduzca los valores que desee multiplicar separados por un espacio: \n')
            numeros_divisor = [float(x) for x in valores_divisor.split()]
            divisor = client.multiplicacion(numeros_divisor)
        else:
            divisor = input('Introduzca el valor del divisor: \n')
            divisor = float(divisor)

        if divisor == 0:
            print('El divisor no puede ser 0.\n')

    return divisor

def pedir_vector_1():
    vector1 = input('Introduzca los valores del primer vector: ')
    primer_vector = [float(x) for x in vector1.split()]
    return primer_vector

def pedir_vector_2(op):
    not_in = True
    segundo_vector = []
    if op == 0:
        while not_in:
            vector2 = input('Introduzca los valores del segundo vector: ')
            segundo_vector = [float(x) for x in vector2.split()]
            not_in = False
            if 0 in segundo_vector:
                not_in = True
                print('¡No puedes introducir un 0!\n')
    else:
        vector2 = input('Introduzca los valores del segundo vector: ')
        segundo_vector = [float(x) for x in vector2.split()]

    return segundo_vector

def imprimir_resultado_vectores(resultado):
    if resultado == "ERROR":
        print("Ha ocurrido un error inesperado, inténtalo de nuevo.\n")
        exit(-1)

    print('Resultado: \n')
    for valores in resultado:
        print(valores)

def advertencia_vectores():
    print('Tenga en cuenta que si los vectores tienen diferentes tamaño, se mantendrá el que menor tamaño tenga.\n')

while haciendo_operaciones:
    print('Elige la operación que quieres realizar: \n')
    print('1) Sumar valores\n')
    print('2) Restar valores\n')
    print('3) Multiplicar valores\n')
    print('4) Dividir valores\n')
    print('5) Potencia de un número.\n')
    print('6) Raíz n-ésima de un número.\n')
    print('7) Sumar vectores.\n')
    print('8) Restar vectores.\n')
    print('9) Multiplicar vectores.\n')
    print('10) Dividir vectores.\n')
    print('Cualquier otro número) Abandonar programa.\n')
    opcion = input()
    try:
        opcion = int(opcion)
    except ValueError:
        print('No se ha podido leer el valor correctamente, por favor inténtelo de nuevo.\n')

    primer_vector = []
    segundo_vector = []

    if opcion == 1:
        valores = input('Introduzca los valores que desee sumar separados por un espacio: ')
        numeros = [float(x) for x in valores.split()]
        resultado = client.suma(numeros)
        print('Resultado: ' + str(resultado) + '\n')

    elif opcion == 2:
        valores = input('Introduzca los valores que desee restar separados por un espacio: ')
        numeros = [float(x) for x in valores.split()]
        resultado = client.resta(numeros)
        print('Resultado: ' + str(resultado) + '\n')

    elif opcion == 3:
        valores = input('Introduzca los valores que desee multiplicar separados por un espacio: ')
        numeros = [float(x) for x in valores.split()]
        resultado = client.multiplicacion(numeros)
        print('Resultado: ' + str(resultado) + '\n')

    elif opcion == 4:
        valor_1 = pide_cociente()
        valor_2 = pide_divisor()
        resultado = client.division(valor_1, valor_2)
        print('Resultado: ' + str(resultado) + '\n')

    elif opcion == 5:
        base = float(input('Introduzca la base de la potencia: \n'))
        potencia = float(input('Introduzca la potencia a la que desea elevar la base: \n'))
        resultado = client.potencia(base, potencia)
        print('Resultado: ' + str(resultado) + '\n')

    elif opcion == 6:
        dentro = -1
        potencia = -1
        while dentro < 0 or potencia <= 0:
            print('El radicando y el índice deben ser positivos.\n')
            dentro = float(input('Introduzca el radicando: \n'))
            potencia = float(input('Introduzca el índice de la raíz: \n'))

        resultado = client.raiz(dentro, potencia)
        print('Resultado: ' + str(resultado) + '\n')

    elif opcion == 7:
        advertencia_vectores()
        primer_vector = pedir_vector_1()
        segundo_vector = pedir_vector_2(1)
        resultado = client.sumavectores(primer_vector, segundo_vector)
        imprimir_resultado_vectores(resultado)

    elif opcion == 8:
        advertencia_vectores()
        primer_vector = pedir_vector_1()
        segundo_vector = pedir_vector_2(1)
        resultado = client.restarvectores(primer_vector, segundo_vector)
        imprimir_resultado_vectores(resultado)

    elif opcion == 9:
        advertencia_vectores()
        primer_vector = pedir_vector_1()
        segundo_vector = pedir_vector_2(1)
        resultado = client.multiplicarvectores(primer_vector, segundo_vector)
        imprimir_resultado_vectores(resultado)

    elif opcion == 10:
        advertencia_vectores()
        primer_vector = pedir_vector_1()
        segundo_vector = pedir_vector_2(0)
        resultado = client.dividirvectores(primer_vector, segundo_vector)
        imprimir_resultado_vectores(resultado)

    elif isinstance(opcion, int):
        print('Nada que operar. Cerrando programa.')
        haciendo_operaciones = False

    else:
        haciendo_operaciones = True

transport.close()