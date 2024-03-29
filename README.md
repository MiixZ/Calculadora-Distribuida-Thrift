﻿Práctica 2: Thrift

Funcionamiento General

La calculadora, nuevamente estará programada con una interfaz gráfica (en la terminal), donde le iremos pasando valores en torno a la operación que hayamos elegido. Esta vez, la calculadora estará compuesta por dos servidores (uno para operaciones básicas y otro para operaciones complejas con vectores) y un cliente, los tres hechos en Python. Tendremos que abrir primero los dos servidores y después el cliente en terminales diferentes.

Terminal 1: python3 ./servidor.py

Terminal 2: python3 ./servidor\_aux.py

Terminal 3: python3 ./cliente.py

Esta vez no harán falta parámetros cuando iniciamos el cliente, caso contrario a como pasaba con RPC, donde teníamos que indicar la dirección de la red donde se encontraba el servidor.

Terminal 1:

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.001.jpeg)

Terminal 2:

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.002.jpeg)

Terminal 3:

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.003.jpeg)

Una vez iniciada la interfaz gráfica (Terminal 3), nos dará a elegir las opciones que se muestran, siendo un total de 10.

- Operaciones básicas con números reales (Suma, resta, multiplicación y división).
- Operaciones algo complejas con números reales (Potencia y raíz de un número real).
- Operaciones complejas con vectores dinámicos (Suma, resta, multiplicación y división de vectores).
  - Para la multiplicación y división, se multiplicará y dividirá cada componente de los vectores hasta alcanzar el tamaño mínimo de los vectores originales (esto último también se aplica para la suma y la resta).

Explicación del código

Existen dos ficheros .thrift, uno para cada servidor donde se indicarán las operaciones que queremos realizar en cada uno de ellos.

Nota: El cliente no se comunica directamente con el servidor de las operaciones complejas, sino que le indica al servidor básico que desea hacer una operación compleja, y este se encargará de establecer la posterior conexión con el servidor complejo.

Calculadora.thrift:

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.004.jpeg)

Se define una estructura “valores” para simular los vectores que se van a usar para las operaciones complejas, así como un vector con todos los números que se van a utilizar tanto para la suma, como para la resta y la multiplicación. También se usa para el otro servidor.

Para la división, podrá realizarse otra operación auxiliar (suma, resta, multiplicación o introducir el valor directamente) tanto para el cociente como para el divisor. Este último nunca podrá ser 0 y estas operaciones auxiliares realizarán también una llamada al servidor.

Llamar a las funciones “sumarvectores”, “restarvectores”, “multiplicarvectores” y “dividirvectores” implica hacer una conexión con el servidor auxiliar. En el último caso, ninguno de los valores introducidos en el segundo vector podrá ser 0.

Calculadora2.thrift:

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.005.png)

El argumento “op” indicará el tipo de operación que se va a realizar sobre los vectores (este valor se lo proporcionará el servidor principal.

El fichero del servidor realizará tanto las operaciones básicas con números reales, como operaciones algo complicadas con estos mismos números. Además se encargará de establecer la conexión con el servidor auxiliar en caso de que se le indique realizar una operación compleja. Para ello he creado una función “iniciarServicio”:

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.006.png)

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.007.jpeg)

Servidor\_aux.py:

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.008.jpeg)

Naturalmente, se comprobará desde el cliente que no se introduzcan valores inválidos, como dividir entre 0 o hacer raíces negativas.

Del lado del cliente, tenemos tanto las comprobaciones de los números introducidos, como la llamada al servidor principal para realizar una operación u otra. Irá leyendo dato por dato dependiendo de la operación elegida:

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.009.jpeg)

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.010.jpeg)

Ejemplos

1. Sumar

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.011.jpeg)

2. Restar.

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.012.jpeg)

3. Multiplicar.

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.013.jpeg)

4. Dividir.

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.014.jpeg)

5. Potencia de un número.

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.015.jpeg)

6. Raíz n-ésima de un número.

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.016.jpeg)

7. Sumar vectores

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.017.jpeg)

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.018.jpeg)

8. Restar vectores

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.019.jpeg)

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.020.jpeg)

9. Multiplicar vectores

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.021.jpeg)

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.022.jpeg)

10. Dividir vectores

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.023.jpeg)

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.024.jpeg)

Finalizar programa.

![](Aspose.Words.164cd79a-14fd-41b7-abef-fcccdbec7e81.025.jpeg)
