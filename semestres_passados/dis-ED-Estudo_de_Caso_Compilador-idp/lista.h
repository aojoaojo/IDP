#ifndef meu_nome
#define meu_nome
#define EH_COMANDO 0
#define EH_PARAMETRO_1 1
#define EH_PARAMETRO_2 2
#define TAMANHO_MAX 200

typedef struct no no;
struct no
{
    char texto_linhas[200];
    char comando[20];
    char parametro_1[20];
    char parametro_2[20];
    no *proximo;
    int numero_da_linha;
    int comando_reconhecido;
};

typedef struct head head;
struct head
{
    no *primeiro;
};

head *criar_lista();

int verificar_lista_vazia(head *cabeca);

void inserir_no(head *cabeca, char *string, int num_linha);

void imprimir_lista_texto_linhas(head *cabeca);

void retirar_no(head *cabeca, char *string);

void desalocar_lista(head *cabeca);

void imprimir_numero_de_linhas(head *cabeca);

void imprimir_lista_comando(head *cabeca);

void imprimir_lista_parametro_1(head *cabeca);

void imprimir_lista_parametro_2(head *cabeca);

#endif