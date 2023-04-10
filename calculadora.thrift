typedef list<double> valores

service Calculadora {
   void ping(),
   double suma(1: valores val),
   double resta(1: valores val),
   double multiplicacion(1: valores val),
   double division(1: double cociente, 2: double divisor),
   double potencia(1: double base, 2: double potencia),
   double raiz(1: double dentro, 2: double potencia),
   valores sumavectores(1: valores vector1, 2: valores vector2),
   valores restarvectores(1: valores vector1, 2: valores vector2),
   valores multiplicarvectores(1: valores vector1, 2: valores vector2),
   valores dividirvectores(1: valores vector1, 2: valores vector2);
}