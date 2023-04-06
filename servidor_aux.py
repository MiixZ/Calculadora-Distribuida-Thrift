import glob
import sys

from calculadora import Calculadora

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import logging

logging.basicConfig(level=logging.DEBUG)

class CalculadoraHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print("me han hecho ping()")

    def suma(self, numeros):
        print("Sumando los valores introducidos: \n")
        for x in numeros:
            print(str(x) + " ")

        return sum(numeros)

    def resta(self, numeros):
        print("Restando los valores introducidos: \n")
        for x in numeros:
            print(str(x) + " ")

        print("\n")
        return numeros[0] - sum(numeros[1:])

    def multiplicacion(self, numeros):
        print("Multiplicando los valores introducidos: \n")
        resultado = 1
        for x in numeros:
            print(str(x) + " ")
            resultado *= x

        print("\n")
        return resultado

    def division(self, cociente, divisor):
        print("dividiendo " + str(cociente) + " con " + str(divisor))
        return cociente / divisor

if __name__ == "__main__":
    handler = CalculadoraHandler()
    processor = Calculadora.Processor(handler)
    transport = TSocket.TServerSocket(host="127.0.0.1", port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print("iniciando servidor...")
    server.serve()
    print("fin")
