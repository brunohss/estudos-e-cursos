#include <stdio.h>

int main() {

    float din;
    int a ,b, c,e;
      printf("Digite o valor para o troco: ");
      scanf("%f", &din);
      din= din*100;
      e= din;
      a = e % 25;
      b = a % 10;
      c = b % 5;
      printf("Ira receber as seguintes moedas: %.f de 25, %d de 10, %d de 5 e %d de 1 centavos ", din/25,a/10,b/5,c);


}