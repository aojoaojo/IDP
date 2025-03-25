#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <x86intrin.h>
#include <emmintrin.h>
#define PASSWORD_LEN 0x4
#define NR_AMOSTRAS 1000
#define DELAY

unsigned long long int amostras[NR_AMOSTRAS];
char correct_password[0x1000];

int compare(const void *a, const void *b)
{
    return (*(unsigned long long int *)a - *(unsigned long long int *)b);
}

void carrega_password()
{
    int fd = open("password.txt", O_RDONLY);
    read(fd, correct_password, PASSWORD_LEN);
}

void delay()
{
    volatile int t;
    for (t = 0; t < 100; t++)
        ;
}

int verifica_password(char *password, int len)
{
    if (len != PASSWORD_LEN)
    {
        return 0;
    }
#ifdef DELAY
    delay();
#endif

    for (int i = 0; i < len; i++)
    {
        if (password[i] != correct_password[i])
        {
            return 0;
        }
#ifdef DELAY
        delay();
#endif
    }

    return 1;
}

int main()
{
    unsigned long long int t1, t2, tf;
    int user_len, res;
    char buffer[0x100];

    write(1, "Digite o password: ", 19);
    user_len = read(0, buffer, 0x100);
    user_len--;

    carrega_password();

    for (int i = 0; i < NR_AMOSTRAS; i++)
    {
        _mm_lfence();
        t1 = __rdtsc();
        res = verifica_password(buffer, user_len);
        t2 = __rdtsc();
        _mm_lfence();
        amostras[i] = t2 - t1;
    }

    qsort(amostras, NR_AMOSTRAS, sizeof(unsigned long long int), compare);
    tf = amostras[NR_AMOSTRAS / 2];

    printf("Tempo: %llu\n", tf);

    if (res)
    {
        write(1, "Password correto e ele eh a resposta para a atividade!\n", 56);
    }
    else
    {
        write(1, "Password incorreto!\n", 20);
    }

    return 0;
}
