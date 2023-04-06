typedef list<double> valores

service Calculadora2 {
   void ping(),
   valores operacionvectores(1: i8 op, 2: valores vector1, 3: valores vector2);
}