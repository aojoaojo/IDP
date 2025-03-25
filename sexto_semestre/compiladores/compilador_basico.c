#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

typedef enum {
    IDENTIFICADOR, NUMERO, IGUAL, MAIS, MENOS, MULTIPLICACAO, DIVISAO, ABRE_PARENTESE, FECHA_PARENTESE, PONTO_E_VIRGULA, FIM
} TipoToken;

typedef struct {
    TipoToken tipo;
    char valor[100];
} Token;

Token tokens[100];
int indiceToken = 0; 
int indiceAtual = 0;

int ehCaractereIdentificador(char c) {
    return isalpha(c) || c == '_';
}

void lexer(char* entrada) {
    int i = 0;

    while (entrada[i] != '\0') {
        if (isspace(entrada[i])) {
            i++;
        } else if (ehCaractereIdentificador(entrada[i])) {
            int j = 0;
            Token t;
            t.tipo = IDENTIFICADOR;
            while (ehCaractereIdentificador(entrada[i]) || isdigit(entrada[i])) {
                t.valor[j++] = entrada[i++];
            }
            t.valor[j] = '\0';
            tokens[indiceToken++] = t;
        } else if (isdigit(entrada[i])) {
            int j = 0;
            Token t;
            t.tipo = NUMERO;
            while (isdigit(entrada[i])) {
                t.valor[j++] = entrada[i++];
            }
            t.valor[j] = '\0';
            tokens[indiceToken++] = t;
        } else if (entrada[i] == '=') {
            Token t;
            t.tipo = IGUAL;
            strcpy(t.valor, "=");
            tokens[indiceToken++] = t;
            i++;
        } else if (entrada[i] == '+') {
            Token t;
            t.tipo = MAIS;
            strcpy(t.valor, "+");
            tokens[indiceToken++] = t;
            i++;
        } else if (entrada[i] == '-') {
            Token t;
            t.tipo = MENOS;
            strcpy(t.valor, "-");
            tokens[indiceToken++] = t;
            i++;
        } else if (entrada[i] == '*') {
            Token t;
            t.tipo = MULTIPLICACAO;
            strcpy(t.valor, "*");
            tokens[indiceToken++] = t;
            i++;
        } else if (entrada[i] == '/') {
            Token t;
            t.tipo = DIVISAO;
            strcpy(t.valor, "/");
            tokens[indiceToken++] = t;
            i++;
        } else if (entrada[i] == '(') {
            Token t;
            t.tipo = ABRE_PARENTESE;
            strcpy(t.valor, "(");
            tokens[indiceToken++] = t;
            i++;
        } else if (entrada[i] == ')') {
            Token t;
            t.tipo = FECHA_PARENTESE;
            strcpy(t.valor, ")");
            tokens[indiceToken++] = t;
            i++;
        } else if (entrada[i] == ';') {
            Token t;
            t.tipo = PONTO_E_VIRGULA;
            strcpy(t.valor, ";");
            tokens[indiceToken++] = t;
            i++;
        } else {
            printf("Caractere desconhecido: %c\n", entrada[i]);
            exit(1);
        }
    }

    Token t;
    t.tipo = FIM;
    strcpy(t.valor, "FIM");
    tokens[indiceToken++] = t;
}

typedef struct No {
    Token token;
    struct No* esquerda;
    struct No* direita;
} No;

No* novoNo(Token token) {
    No* no = (No*)malloc(sizeof(No));
    no->token = token;
    no->esquerda = NULL;
    no->direita = NULL;
    return no;
}

Token obterProximoToken() {
    return tokens[indiceAtual++];
}

Token olharProximoToken() {
    return tokens[indiceAtual];
}

No* fator();
No* termo();
No* expressao();

No* fator() {
    Token token = obterProximoToken();
    if (token.tipo == NUMERO || token.tipo == IDENTIFICADOR) {
        printf("Fator: %s\n", token.valor);
        return novoNo(token);
    } else if (token.tipo == ABRE_PARENTESE) {
        printf("Abrindo parêntese\n");
        No* no = expressao();
        if (obterProximoToken().tipo != FECHA_PARENTESE) {
            printf("Erro: Parêntese fechado esperado!\n");
            exit(1);
        }
        printf("Fechando parêntese\n");
        return no;
    }
    printf("Erro: Fator inválido!\n");
    exit(1);
}

No* termo() {
    No* no = fator();
    while (olharProximoToken().tipo == MULTIPLICACAO || olharProximoToken().tipo == DIVISAO) {
        Token token = obterProximoToken();
        printf("Operador de termo: %s\n", token.valor);
        No* novo = novoNo(token);
        novo->esquerda = no;
        novo->direita = fator();
        no = novo;
    }
    return no;
}

No* expressao() {
    No* no = termo();
    while (olharProximoToken().tipo == MAIS || olharProximoToken().tipo == MENOS) {
        Token token = obterProximoToken();
        printf("Operador de expressão: %s\n", token.valor);
        No* novo = novoNo(token);
        novo->esquerda = no;
        novo->direita = termo();
        no = novo;
    }
    return no;
}

void gerarCodigo(No* no, const char* variavel) {
    if (no == NULL) return;

    gerarCodigo(no->esquerda, variavel);
    gerarCodigo(no->direita, variavel);

    switch (no->token.tipo) {
        case NUMERO:
        case IDENTIFICADOR:
            printf("PUSH %s\n", no->token.valor);
            break;
        case MAIS:
            printf("ADD\n");
            break;
        case MENOS:
            printf("SUB\n");
            break;
        case MULTIPLICACAO:
            printf("MUL\n");
            break;
        case DIVISAO:
            printf("DIV\n");
            break;
        default:
            break;
    }

    if (no->esquerda == NULL && no->direita == NULL) {
        printf("STORE %s\n", variavel);
    }
}

void imprimirArvoreHierarquica(No* no, int nivel) {
    if (no == NULL) return;

    imprimirArvoreHierarquica(no->esquerda, nivel + 1);

    for (int i = 0; i < nivel; i++) {
        printf("    ");
    }
    printf("%s\n", no->token);

    imprimirArvoreHierarquica(no->direita, nivel + 1);
}


int main() {
    char entrada[] = "x = 2 * (4 + 2);";
    printf("Entrada: %s\n", entrada);

    printf("Léxica: \n");
    lexer(entrada);
    for (int i = 0; i < indiceToken; i++) {
        printf("Token: %d, valor: %s\n", tokens[i].tipo, tokens[i].valor);
    }

    printf("Sintática:\n");
    Token primeiro = obterProximoToken();
    if (primeiro.tipo != IDENTIFICADOR) {
        printf("Erro: Identificador esperado no início!\n");
        return 1;
    }

    if (obterProximoToken().tipo != IGUAL) {
        printf("Erro: '=' esperado após o identificador!\n");
        return 1;
    }

    No* raiz = expressao();


    if (obterProximoToken().tipo != PONTO_E_VIRGULA) {
        printf("Erro: ';' esperado no final!\n");
        return 1;
    }

    printf("\nGeração de Código\n");
    gerarCodigo(raiz, "x");

    return 0;
}