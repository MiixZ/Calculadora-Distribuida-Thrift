typedef list<double> valores

service Calculadora {
   void ping(),
   double suma(1: valores val),
   double resta(1: valores val),
   double multiplicacion(1: valores val),
   double division(1: double cociente, 2: double divisor);
}