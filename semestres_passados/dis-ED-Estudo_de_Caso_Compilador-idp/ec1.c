#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lista.h"

void abrir_arquivo(FILE **arquivo, char *caminho) // função para abrir os arquivos
{
    *arquivo = fopen(caminho, "r");
    if (*arquivo == NULL) // falha ao abrir o arquivo
        printf("Erro ao abrir arquivo\n");
}

void eliminar_comentarios(char *string)
{
    while (*string != '\0')
    {
        if (*string == '#')
        {
            *string = '\0';
        }
        string++;
    }
}

void pegar_todo_o_texto_do_arquivo(FILE *arquivo, char *string, head *lista) // pega todo o texto do arquivo e armazena em uma string
{
    int numero_linhas = 1;

    while (!feof(arquivo))
    {
        if (fgets(string, 200, arquivo) == NULL)
            continue;
        eliminar_comentarios(string);
        inserir_no(lista, string, numero_linhas);
        numero_linhas++;
    }
}

void checa_comando(no *atual, int i, int j, int *k, int *entrar, FILE *file_log)
{
    for (int l = j; l < i; l++)
    {
        atual->comando[*k] = atual->texto_linhas[l]; // passa o conteúdo até o primeiro espaço como comando para o nó
        *k += 1;
    }
    atual->comando[*k] = '\0';          // coloca o '\0' no final do comando
    j = i + 1;                          // j = primeira posição após o espaço
    entrar++;                           // passa a entrar em parametro 1
    if (atual->texto_linhas[i] == '\0') // checa se o comando não tem parametros
    {
        fprintf(file_log, "LINHA %d: Faltam parametros na função\n", atual->numero_da_linha); // printa no arquivo que faltam parametros na funçao
    }
}

void checa_parametro_1(no *atual, int i, int j, int *k, int *entrar, FILE *file_log)
{
    for (int l = j; l < i; l++)
    {
        atual->parametro_1[*k] = atual->texto_linhas[l]; // passa o conteúdo de um espaço ao outro como parametro 1
        *k += 1;
    }
    atual->parametro_1[*k] = '\0'; // coloca '\0' como último elemento do par_1
    j = i + 1;                     // proxima posição depois do par_1
    entrar++;                      // passa pro par_2

    int tam = strlen(atual->parametro_1); // pega o tamanho do par_1

    for (int roda = 0; roda < tam; roda++) // checa e muda '\r' para '\0'
    {
        if (atual->parametro_1[roda] == '\r')
            atual->parametro_1[roda] = '\0';
    }
}

void checa_parametro_2(no *atual, int i, int j, int *k, int *entrar, FILE *file_log)
{
    for (int l = j; l < i; l++) // pega o conteúdo até o prox espaço ou fim do texto
    {
        atual->parametro_2[*k] = atual->texto_linhas[l]; // passa como par_2
        *k += 1 ;
    }
    atual->parametro_2[*k] = '\0'; // coloca '\0' no final do vetor

    int tam = strlen(atual->parametro_2); // checa tamano do par_2

    for (int roda = 0; roda < tam; roda++) // muda '\r' para '\0'
    {
        if (atual->parametro_2[roda] == '\r')
            atual->parametro_2[roda] = '\0';
    }

    entrar++;
}

void separar_linhas_em_parametros(head *lista, FILE *file_log) // separar as linhas em comando e parametros
{
    no *atual = lista->primeiro; // cria no para percorrer a lista

    while (atual != NULL) // percorre a lista até o último elemento
    {
        int entrar = EH_COMANDO;
        int i, j = 0;
        for (i = j; atual->texto_linhas[i] != '\0'; i++)
        {
            if (atual->texto_linhas[i] == ' ' || atual->texto_linhas[i] == '\0') // procura espaço ou '\0'
            {
                int k = 0;

                if (entrar == EH_COMANDO) // checa se é o comando
                    checa_comando(atual, i, j, &k, &entrar, file_log);
                else if (entrar == EH_PARAMETRO_1) // checa se é o parametro 1
                    checa_parametro_1(atual, i, j, &k, &entrar, file_log);
                else if (entrar == EH_PARAMETRO_2) // checa se é o par_2
                    checa_parametro_2(atual, i, j, &k, &entrar, file_log);
            }
        }
        if (entrar > 3)                                                                                       // olha se há mais parametros que o permitido
            fprintf(file_log, "LINHA %d: Numero maior de parâmetros que o esperado", atual->numero_da_linha); // print no file log
        atual = atual->proximo;
    }
}

void comparar_regras_com_corrigir(head *lista_regras, head *lista_corrigir) // compara os comandos dos nós da lista de correção com as de regras
{
    no *atual_corrigir = lista_corrigir->primeiro, *atual_regras = lista_regras->primeiro;
    int num_linhas_corrigir = atual_corrigir->numero_da_linha, num_linhas_regras = atual_regras->numero_da_linha, i, j;

    for (i = 0; i < num_linhas_regras; i++) // roda todas as linhas de regras
    {
        atual_corrigir = lista_corrigir->primeiro; // volta para o inicio das linha de correção
        for (j = 0; j < num_linhas_corrigir; j++)  // roda todas as linhas para corrigir
        {
            if (strcmp(atual_corrigir->comando, atual_regras->comando) == 0) // compara se o comando de regras é igual ao comando dado na correção
                atual_corrigir->comando_reconhecido = 1;                     // caso os comandos sejam iguais, marca o no atual como comando reconhecido
            atual_corrigir = atual_corrigir->proximo;                        // muda a linha de correção
        }
        atual_regras = atual_regras->proximo; // muda a linha de regras
    }
}

int eh_inteiro(char *texto) // checa se uma string é um número inteiro
{
    int tam = strlen(texto);
    for (int i = 0; i < tam; i++)
    {
        if (i == 0 && texto[i] == '-')
            continue;
        if ((texto[i] < '0' || texto[i] > '9'))
            return 0;
    }
    if (texto[0] == '\0')
        return 0;
    return 1;
}

int eh_float(char *texto) // checa se uma string é um float
{
    int tam = strlen(texto);
    int quant_de_pontos = 0;
    for (int i = 0; i < tam; i++)
    {
        if (i == 0 && texto[i] == '-')
            continue;
        if (((texto[i] < '0' && texto[i] != '.') || texto[i] > '9' || texto[0] == '.') || (texto[0] == '-' && texto[1] == '.'))
        {
            return 0;
        }
        if (texto[i] == '.')
        {
            quant_de_pontos++;
            if (quant_de_pontos > 1)
                return 0;
        }
    }
    return 1;
}

int eh_natural(char *texto) // checa se uma string é um natural
{
    int tam = strlen(texto);
    for (int i = 0; i < tam; i++)
    {
        if ((texto[i] < '0' || texto[i] > '9'))
            return 0;
    }
    return 1;
}
void comando_read(no *atual, FILE *file_log) // checa se os parametros sao numeros permitidos e printa no file log
{
    if (eh_natural(atual->parametro_1) == 1 && atual->parametro_2[0] == '\0' && atual->parametro_1[0] != '\0')
        fprintf(file_log, "LINHA %d: Comando '%s' feito com sucesso e parametro correto\n", atual->numero_da_linha, atual->comando);
    else
    {
        if (atual->parametro_1[0] == '\0')
            fprintf(file_log, "Linha %d: O comando '%s' Não possui parâmetros\n", atual->numero_da_linha, atual->comando);
        else if (atual->parametro_2[0] != '\0')
            fprintf(file_log, "Linha %d: O comando '%s' possui parâmetros a mais\n", atual->numero_da_linha, atual->comando);
        else
            fprintf(file_log, "LINHA %d: O comando '%s' apresenta parâmetros com valores inválidos\n", atual->numero_da_linha, atual->comando);
    }
}

void comando_write(no *atual, FILE *file_log) // checa se os parametros sao numeros permitidos e printa no file log
{
    if (eh_natural(atual->parametro_1) == 1 && atual->parametro_2[0] == '\0')

        fprintf(file_log, "LINHA %d: Comando '%s' feito com sucesso e parametros corretos\n", atual->numero_da_linha, atual->comando);
    else
    {
        if (atual->parametro_1[0] == '\0')
            fprintf(file_log, "Linha %d: O comando '%s' Não possui parâmetros\n", atual->numero_da_linha, atual->comando);
        else if (atual->parametro_2[0] != '\0')
            fprintf(file_log, "Linha %d: O comando '%s' possui parâmetros a mais\n", atual->numero_da_linha, atual->comando);
        else
            fprintf(file_log, "LINHA %d: O comando '%s' apresenta parâmetros com valores inválidos\n", atual->numero_da_linha, atual->comando);
    }
}

void comando_storeconst(no *atual, FILE *file_log) // checa se os parametros sao numeros permitidos e printa no file log
{
    if (eh_float(atual->parametro_1) == 1 && eh_natural(atual->parametro_2) == 1)
        fprintf(file_log, "LINHA %d: Comando '%s' feito com sucesso e parametros corretos\n", atual->numero_da_linha, atual->comando);
    else
    {
        if (atual->parametro_1[0] == '\0')
            fprintf(file_log, "Linha %d: O comando '%s' Não possui parâmetros\n", atual->numero_da_linha, atual->comando);
        else if (atual->parametro_2[0] == '\0')
            fprintf(file_log, "LINHA %d: O comando '%s' possui parâmetros a menos\n", atual->numero_da_linha, atual->comando);
        else
            fprintf(file_log, "LINHA %d: O comando '%s' apresenta parâmetros com valores inválidos\n", atual->numero_da_linha, atual->comando);
    }
}

void comando_operacao_art(no *atual, FILE *file_log) // checa se os parametros sao numeros permitidos e printa no file log
{
    if (eh_natural(atual->parametro_1) == 1 && eh_natural(atual->parametro_2) == 1)
        fprintf(file_log, "LINHA %d: Comando '%s' feito com sucesso e parametros corretos\n", atual->numero_da_linha, atual->comando);
    else
    {
        if (atual->parametro_1[0] == '\0')
            fprintf(file_log, "Linha %d: O comando '%s' Não possui parâmetros\n", atual->numero_da_linha, atual->comando);
        else if (atual->parametro_2[0] == '\0')
            fprintf(file_log, "LINHA %d: O comando '%s' possui parâmetros a menos\n", atual->numero_da_linha, atual->comando);
        else
            fprintf(file_log, "LINHA %d: O comando '%s' apresenta parâmetros com valores inválidos\n", atual->numero_da_linha, atual->comando);
    }
}

void comando_store(no *atual, FILE *file_log) // checa se os parametros sao numeros permitidos e printa no file log
{
    if (eh_natural(atual->parametro_1) == 1 && atual->parametro_2[0] == '\0')
        fprintf(file_log, "LINHA %d: Comando '%s' feito com sucesso e parametros corretos\n", atual->numero_da_linha, atual->comando);
    else
    {
        if (atual->parametro_1[0] == '\0')
            fprintf(file_log, "Linha %d: O comando '%s' Não possui parâmetros\n", atual->numero_da_linha, atual->comando);
        else if (atual->parametro_2[0] != '\0')
            fprintf(file_log, "LINHA %d: O comando '%s' possui parâmetros a mais\n", atual->numero_da_linha, atual->comando);
        else
            fprintf(file_log, "LINHA %d: O comando '%s' apresenta parâmetros com valores inválidos\n", atual->numero_da_linha, atual->comando);
    }
}
void comando_jump(no *atual, FILE *file_log) // checa se os parametros sao numeros permitidos e printa no file log
{
    if (eh_natural(atual->parametro_1) == 1 && eh_inteiro(atual->parametro_2) == 1)
        fprintf(file_log, "LINHA %d: Comando '%s' feito com sucesso e parametros corretos\n", atual->numero_da_linha, atual->comando);
    else
    {
        if (atual->parametro_1[0] == '\0')
            fprintf(file_log, "Linha %d: O comando '%s' Não possui parâmetros\n", atual->numero_da_linha, atual->comando);
        else if (atual->parametro_2[0] == '\0')
            fprintf(file_log, "LINHA %d: O comando '%s' possui parâmetros a menos\n", atual->numero_da_linha, atual->comando);
        else
            fprintf(file_log, "LINHA %d: O comando '%s' apresenta parâmetros com valores inválidos\n", atual->numero_da_linha, atual->comando);
    }
}

void rodar_comando_reconhecido(head *lista_corrigir, FILE *file_log) // roda os nós que foram dados como comando reconhecido
{
    no *atual = lista_corrigir->primeiro;
    while (atual != NULL)
    {
        if (atual->comando_reconhecido == 1)
        {
            if (strcmp(atual->comando, "read") == 0) // olha se o comando reconhecido é read
                comando_read(atual, file_log);
            else if (strcmp(atual->comando, "write") == 0) // olha se o comando reconhecido é write
                comando_write(atual, file_log);
            else if (strcmp(atual->comando, "storeconst") == 0) // olha se o comando reconhecido é storeconst
                comando_storeconst(atual, file_log);
            else if (strcmp(atual->comando, "mul") == 0 || (strcmp(atual->comando, "div") == 0) || (strcmp(atual->comando, "add") == 0) || (strcmp(atual->comando, "sub") == 0)) // olha se o comando reconhecido é mul
                comando_operacao_art(atual, file_log);
            else if (strcmp(atual->comando, "store") == 0) // olha se o comando reconhecido é store
                comando_store(atual, file_log);
            else if (strcmp(atual->comando, "jump") == 0) // olha se o comando reconhecido é jump
                comando_jump(atual, file_log);
        }
        else
        {
            fprintf(file_log, "LINHA %d: Comando '%s' não identificado\n", atual->numero_da_linha, atual->comando); // comando não identificado
        }
        atual = atual->proximo;
    }
}

int main(int argc, char *argv[])
{
    head *lista_texto_corrigir = criar_lista(), *lista_texto_regras = criar_lista(); // cria lista
    FILE *file_log;                                                                  // cria arquivo log
    file_log = fopen("analise.log", "w");                                            // abre arquivo log
    if (file_log == NULL)                                                            // checa se abriu
        printf("Falha ao criar arquivo log");
    FILE *arquivo_corrigir, *arquivo_regras; // criar files
    char texto_corrigir[TAMANHO_MAX] = {}, texto_regras[TAMANHO_MAX] = {};
    char caminho_arq_corrigir[TAMANHO_MAX] = "",
         caminho_arq_regras[TAMANHO_MAX] = "";                                             // pega caminho do arquivo a ser aberto
    abrir_arquivo(&arquivo_corrigir, argv[1]);                                             // abre arquivo corrigir
    abrir_arquivo(&arquivo_regras, argv[2]);                                               // abre arquivo regras
    pegar_todo_o_texto_do_arquivo(arquivo_regras, texto_regras, lista_texto_regras);       // pega todo o texto do arquivo de regras e armazena em uma string
    pegar_todo_o_texto_do_arquivo(arquivo_corrigir, texto_corrigir, lista_texto_corrigir); // pega todo o texto a ser corrigido e armazena em uma string
    separar_linhas_em_parametros(lista_texto_regras, file_log);                            // separa comando e parametros de regras
    separar_linhas_em_parametros(lista_texto_corrigir, file_log);                          // separa comando e parametros de correção
    comparar_regras_com_corrigir(lista_texto_regras, lista_texto_corrigir);                // compara regras com correção
    rodar_comando_reconhecido(lista_texto_corrigir, file_log);                             // roda comandos que foram reconhecidos
    no *atual_corrigir = lista_texto_corrigir->primeiro;
    while (atual_corrigir != NULL)
    {
        no *aux = atual_corrigir;
        atual_corrigir = atual_corrigir->proximo;
        free(aux);
    }
    no *atual_regras = lista_texto_regras->primeiro;
    while (atual_regras != NULL)
    {
        no *aux = atual_regras;
        atual_regras = atual_regras->proximo;
        free(aux);
    }
    return 0;
}