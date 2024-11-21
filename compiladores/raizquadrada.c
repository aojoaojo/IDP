#include <stdio.h>
#include <unistd.h>

//facao uma funcao para calcular fatoriais

int fatorial(int n)
{
    int result = 1;
    for (int i = 1; i <= n; i++)
    {
        result *= i;
    }
    return result;
}

// faca funcao para calcular potencias

double potencia(double base, int expoente)
{
    int result = 1;
    for (int i = 0; i < expoente; i++)
    {
        result *= base;
    }
    return result;
}

double exponencial(double x)
{
    double result = 1;
    double term = 1;
    for (int i = 1; i < 10; i++)
    {
        term *= x / i;
        result += term;
    }
    return result;
}

double logaritmo(double x)
{
    double result = 0;
    double term = (x - 1) / (x + 1);
    for (int i = 1; i < 10; i += 2)
    {
        result += term / i;
        term *= term * term;
    }
    return 2 * result;
}

// refaça a função a seguir utilizando a série de taylor, onde i pode ser igual a zero.
double seno(double x)
{
    double result = 0;
    double numerador = 0;
    double denominador = 0;
    double outra_parte = 0;
    double term = x;
    double atual = 0;

    for (int i = 0; i < 10; i++)
    {

        if (i % 2 == 0)
            numerador = 1;
        else
            numerador = -1;

        denominador = fatorial(2 * i + 1);
        outra_parte = potencia(x, 2 * i + 1);

        result = (numerador / denominador) * outra_parte;
        atual += result;
    }
    return atual;
}



double cosseno(double x)
{
    double result = 0;
    double numerador = 0;
    double denominador = 0;
    double outra_parte = 0;
    double term = x;
    double atual = 0;

    for (int i = 0; i < 10; i++)
    {

        if (i % 2 == 0)
            numerador = 1;
        else
            numerador = -1;

        denominador = fatorial(2 * i);
        outra_parte = potencia(x, 2 * i);

        result = (numerador / denominador) * outra_parte;
        atual += result;
    }
    return atual;
}