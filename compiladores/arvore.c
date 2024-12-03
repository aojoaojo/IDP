
//código arvore
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAIS 1 // Define o símbolo "MAIS"

// Estrutura para armazenar os tokens
typedef struct Token {
    char valor[100]; // Pode conter números ou identificadores
    int tipo;        // Tipo do token, ex.: MAIS para '+'
} Token;

// Estrutura para os nós da árvore sintática
typedef struct No {
    char token[100];      // Valor do token
    struct No* esquerda;  // Ponteiro para a subárvore esquerda
    struct No* direita;   // Ponteiro para a subárvore direita
} No;

Token tokens[100];        // Array para armazenar os tokens
int indiceTokenAtual = 0; // Índice para o token atual

// Avança para o próximo token
void avancar() {
    indiceTokenAtual++; // Incrementa o índice
}

// Declaração de funções
No* analisarExpressao();

// Cria um nó da árvore sintática
No* criarNo(char* valorToken) {
    No* novoNo = (No*) malloc(sizeof(No));
    strcpy(novoNo->token, valorToken);
    novoNo->esquerda = NULL;
    novoNo->direita = NULL;
    return novoNo;
}

// Analisar números
No* analisarNumero() {
    No* no = criarNo(tokens[indiceTokenAtual].valor); // Usa o token atual
    avancar();                                       // Passa para o próximo token
    return no;
}

// Analisar identificadores
No* analisarIdentificador() {
    No* no = criarNo(tokens[indiceTokenAtual].valor); // Usa o token atual
    avancar();
    return no;
}

// Processa expressões
No* analisarExpressao() {
    No* no = analisarNumero(); // Lê o primeiro número

    // Trata operações com '+'
    while (tokens[indiceTokenAtual].tipo == MAIS) {
        avancar();                              // Consome o '+'
        No* novoNo = criarNo("+");              // Cria nó para o operador
        novoNo->esquerda = no;                  // Define o lado esquerdo
        novoNo->direita = analisarNumero();     // Define o lado direito
        no = novoNo;                            // Atualiza o nó
    }
    return no;
}

// Processa atribuições (ex.: x = 10 + 20)
No* analisarAtribuicao() {
    No* no = criarNo("=");                      // Cria nó para '='
    no->esquerda = analisarIdentificador();     // Lê o identificador
    avancar();                                  // Consome o '='
    no->direita = analisarExpressao();          // Processa a expressão
    return no;
}

// Função principal do analisador sintático
No* analisador() {
    return analisarAtribuicao(); // Processa a atribuição
}


// Lê a entrada e converte em tokens
void lexer(char* entrada) {
    int i = 0;
    char* token = strtok(entrada, " "); // Divide a entrada por espaços
    while (token != NULL) {
        if (strcmp(token, "+") == 0) {
            tokens[i].tipo = MAIS;
        } else {
            tokens[i].tipo = 0; // Assume número ou identificador
        }
        strcpy(tokens[i].valor, token); // Copia o valor do token
        token = strtok(NULL, " ");     // Próximo token
        i++;
    }
}

void imprimirArvoreHierarquica(No* no, int nivel) {
    if (no == NULL) return;

    // Primeiro, imprime a subárvore esquerda
    imprimirArvoreHierarquica(no->esquerda, nivel + 1);

    // Imprime o nó atual com deslocamento correspondente ao nível
    for (int i = 0; i < nivel; i++) {
        printf("    "); // Deslocamento de 4 espaços por nível
    }
    printf("%s\n", no->token);

    // Depois, imprime a subárvore direita
    imprimirArvoreHierarquica(no->direita, nivel + 1);
}

// Função principal
int main() {
    char entrada[] = "x = 2*(4 + 2);";            // Entrada para ser analisada

    lexer(entrada);                            // Divide a entrada em tokens
    No* arvoreSintaxe = analisador();          // Constrói a árvore sintática

    printf("Arvore de Sintaxe:\n");            // Título da saída
    imprimirArvoreHierarquica(arvoreSintaxe, 0); // Imprime a árvore de forma hierárquica

    return 0;
}
