#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int pid;

    pid = fork();

    if (pid == 0) {
        int pidf = fork();
        if(pidf == 0){
            sleep(1);
            printf("Neto dormiu por 1 segundo\n");
            printf("Neto %d terminando a execucao\n", getpid());
        }
        else{
        sleep(3);
        printf("Filho dormiu por 3 segundos\n");
        printf("Filho %d terminando a execucao\n", getpid());
        }
    } else {
        printf("Sou pai de um\n");
        wait(NULL);
        printf("Filho ja terminou sua execucao\n");


    }

    return 0;
}
