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
        cociente = client.resta(numeros_cociente)
    else:
        cociente = input('Introduzca el valor del cociente: \n')
        cociente = float(cociente)

    return cociente

def pide_divisor():
    opcion_divisor = input('Elija qué operación desea hacer con los valores que introduzca en el divisor: \n'
                            '1) Sumar. \n'
                            '2) Restar. \n'
                            '3) Multiplicar. \n'
                            '4) Introducir valor directamente. \n')
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
        divisor = client.resta(numeros_divisor)
    else:
        divisor = input('Introduzca el valor del divisor: \n')
        divisor = float(divisor)

    return divisor

def advertencia_vectores():
    print('Tenga en cuenta que si los vectores tienen diferentes tamaño, se mantendrá el que menor tamaño tenga.\n')

while haciendo_operaciones:
    print('Elige la operación que quieres realizar: \n')
    print('1) Sumar valores\n')
    print('2) Restar valores\n')
    print('3) Multiplicar valores\n')
    print('4) Dividir valores\n')
    print('5) Sumar vectores.\n')
    print('6) Restar vectores.\n')
    print('7) Multiplicar vectores.\n')
    print('8) Dividir vectores.\n')
    opcion = input()
    opcion = int(opcion)

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
        advertencia_vectores()
        vector1 = input('Introduzca los valores del primer vector: ')
        primer_vector = [float(x) for x in vector1.split()]
        vector2 = input('\nIntroduzca los valores del segundo vector: ')
        segundo_vector = [float(x) for x in vector1.split()]
        resultado = client.sumavectores(primer_vector, segundo_vector)

    elif opcion == 6:
        advertencia_vectores()
        vector1 = input('Introduzca los valores del primer vector: ')
        primer_vector = [float(x) for x in vector1.split()]
        vector2 = input('\nIntroduzca los valores del segundo vector: ')
        segundo_vector = [float(x) for x in vector1.split()]
        resultado = client.sumavectores(primer_vector, segundo_vector)

        print('Resultado: \n')
        for valores in resultado:
            print(valores)

    else:
        resultado = 'Nada que operar.'
        transport.close()

print('Resultado: ' + str(resultado) + '\n')
transport.close()