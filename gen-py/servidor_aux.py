import glob
import sys

from calculadora2 import Calculadora2

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
        print('Servidor auxiliar activo. Me han hecho ping.\n')

    def operacionvectores(self, op, vector1, vector2):
        resultado = []
        if op == 1:
            print('Sumando vectores...\n')
            for i in range(min(len(vector1), len(vector2))):
                resultado.append(vector1[i] + vector2[i])
        elif op == 2:
            print('Restando vectores...\n')
            for i in range(min(len(vector1), len(vector2))):
                resultado.append(vector1[i] - vector2[i])
        elif op == 3:
            print('Multiplicando vectores...\n')
            for i in range(min(len(vector1), len(vector2))):
                resultado.append(vector1[i] * vector2[i])
        elif op == 4:
            print('Dividiendo vectores...\n')
            for i in range(min(len(vector1), len(vector2))):
                resultado.append(vector1[i] / vector2[i])
        else:
            resultado = "ERROR"

        return resultado

if __name__ == "__main__":
    handler = CalculadoraHandler()
    processor = Calculadora2.Processor(handler)
    transport = TSocket.TServerSocket(host="127.0.0.1", port=9094)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print("Iniciando servidor...")
    server.serve()
    print("fin")
