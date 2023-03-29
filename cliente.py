from calculadora import Calculadora
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

transport = TSocket.TSocket("localhost", 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Calculadora.Client(protocol)

def pide_valor1():
    try:
        valor = input()
        valor = float(valor)
        return valor
    except EOFError:
        return False

def pide_valor2():
    valor = input('Introduzca el segundo valor:')
    valor = float(valor)
    return valor

transport.open()

print("Haciendo ping al server.")
client.ping()

haciendo_operaciones = True

while(haciendo_operaciones):
    print('Elige la operación que quieres realizar: \n')
    print('1) Sumar valores\n')
    print('2) Restar valores\n')
    print('3) Multiplicar valores\n')
    print('4) Dividir valores\n')
    print('4) Sumar vectores\n')
    print('5) Abandonar programa.\n')
    opcion = input()
    opcion = int(opcion)

    if(opcion == 1):
        cogiendo_valores = True
        resultado = 0
        print('Introduzca los valores que desee sumar separados por un espacio: ')
        while cogiendo_valores:
            valor = pide_valor1()
            if valor:
                resultado += client.suma(resultado, valor)
            else:
                cogiendo_valores = False
                print('Resultado: ' + str(resultado) + '\n')
    elif(opcion == 2):
        valor_1 = pide_valor1()
        valor_2 = pide_valor2()
        resultado = client.resta(valor_1, valor_2)
        print('Resultado: ' + str(resultado) + '\n')
    elif(opcion == 3):
        valor_1 = pide_valor1()
        valor_2 = pide_valor2()
        resultado = client.multiplicacion(valor_1, valor_2)
        print('Resultado: ' + str(resultado) + '\n')
    elif(opcion == 4):
        valor_1 = pide_valor1()
        valor_2 = pide_valor2()
        resultado = client.division(valor_1, valor_2)
        print('Resultado: ' + str(resultado) + '\n')
    elif(opcion == 5):
        resultado = 'Se acabaron las operaciones, finalizando programa...\n'
        haciendo_operaciones = False
    else:
        resultado = 'Nada que operar, operación fallida.'

print('Resultado: ' + str(resultado) + '\n')

transport.close()