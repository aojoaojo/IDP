#include "raizquadrada.h"

int main()
{
    double x = 2;
    double r = exponencial(x);
    printf("O exponencial de %f é %f\n", x, r);
    r = logaritmo(x);
    printf("O logaritmo de %f é %f\n", x, r);
    r = seno(x);
    printf("O seno de %f é %f\n", x, r);
    r = cosseno(x);
    printf("O cosseno de %f é %f\n", x, r);
    return 0;
}