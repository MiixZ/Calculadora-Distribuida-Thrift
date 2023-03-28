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
    valor = input('Introduzca el primer valor:')
    valor = float(valor)
    return valor

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
    print('5) Abandonar programa.\n')
    opcion = input()
    opcion = int(opcion)

    if(opcion == 1):
        valor_1 = pide_valor1()
        valor_2 = pide_valor2()
        resultado = client.suma(valor_1, valor_2)
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

print('Resultado: ' + str(resultado) + '\n')

transport.close()
