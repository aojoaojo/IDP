#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int pid;

    pid = fork();

    if (pid == 0) {
        execl("/bin/ls", "ls", "-l", "-h", "-a", "/proc/self/", NULL);
    } else {
        wait(NULL);
        printf("Termino da execucao\n");
    }

    return 0;
}
