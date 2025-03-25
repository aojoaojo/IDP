#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lista.h"

head *criar_lista()
{
    head *cabeca = (head *)malloc(sizeof(head));
    if (cabeca == NULL)
    {
        printf("Não conseguiu alocar a memoria");
    }
    cabeca->primeiro = NULL;
    return cabeca;
}

int verificar_lista_vazia(head *cabeca)
{
    return cabeca->primeiro == NULL;
}

void inserir_no(head *cabeca, char *string, int num_linha)
{
    no *novo = (no *)malloc(sizeof(no));
    if (novo == NULL)
        printf("Não conseguiu alocar a memoria");
    strcpy(novo->texto_linhas, string);
    novo->comando_reconhecido = 0;
    novo->numero_da_linha = num_linha;
    novo->proximo = cabeca->primeiro;
    cabeca->primeiro = novo;
}

void imprimir_lista_texto_linhas(head *cabeca)
{
    no *atual = cabeca->primeiro;
    while (atual != NULL)
    {
        printf("%s\n", atual->texto_linhas);
        atual = atual->proximo;
    }
}
void imprimir_lista_comando(head *cabeca)
{
    no *atual = cabeca->primeiro;
    while (atual != NULL)
    {
        printf("%s\n", atual->comando);
        atual = atual->proximo;
    }
}
void imprimir_lista_parametro_1(head *cabeca)
{
    no *atual = cabeca->primeiro;
    while (atual != NULL)
    {
        printf("%s\n", atual->parametro_1);
        atual = atual->proximo;
    }
}
void imprimir_numero_de_linhas(head *cabeca)
{
    no *atual = cabeca->primeiro;
    printf("%d", atual->numero_da_linha);
}
void imprimir_lista_parametro_2(head *cabeca)
{
    no *atual = cabeca->primeiro;
    while (atual != NULL)
    {
        printf("%s\n", atual->parametro_2);
        atual = atual->proximo;
    }
}

void retirar_no(head *cabeca, char *string)
{
    no *aux = NULL;
    no *atual = cabeca->primeiro;
    while (atual != NULL)
    {
        if (atual->texto_linhas == string)
        {
            if (aux == NULL)
            {
                cabeca->primeiro = atual->proximo;
                free(atual);
                return;
            }
            else
            {
                aux->proximo = atual->proximo;
                free(atual);
                return;
            }
        }
        aux = atual;
        atual = atual->proximo;
    }
}

void desalocar_lista(head *cabeca)
{
    int cont = 0;
    no *atual = cabeca->primeiro;
    no *aux = NULL;
    while (atual != NULL)
    {

        aux = atual;
        atual = atual->proximo;
        free(aux);
        cont++;
    }
    printf("%d nós foram desalocados", cont);
    free(cabeca);
}
