; - Condicionais

; Condicionais são um dos mecanismos mais poderosos e fundamentais em programação.
; Eles permitem que um programa tome decisões com base em valores dinâmicos
; fornecidos ao programa. Um estrutura de condição pode ser escrita da seguinte
; forma:

;     if x for par:
;         y = 1
;     else:
;         y = 0

; Nessas estruturas, podemos controlar o fluxo de controle do programa com base em
; valores dinâmicos fornecidos ao programa. Em linguagens de baixo nível, esse
; fluxo pode ser controlado com uma de diversas instruções de salto condicional.
; Em todas elas, o ZF (Zero Flag) é fundamental. O ZF é definido como 1 quando uma
; comparação é igual e 0 caso contrário.

; Utilizando estruturas condicionais, implemente o seguinte:
;     if [x] is 0x7f45cafe:
;         y = [x+4] + [x+8] + [x+12]
;     else if [x] is 0x00005AAD:
;         y = [x+4] - [x+8] - [x+12]
;     else:
;         y = [x+4] * [x+8] * [x+12]

; onde:
;     x = rdi
;     y = eax

; Assuma que cada valor é um inteiro de 32 bits com sinal. Ou seja, 
; os valores podem começar negativos em cada posição de memória.

; Nesta atividade, serão executados múltiplos casos de testes. Aqui está um
; exemplo:

;   (data) [0x404000] = {4 random dwords]}
;   rdi = 0x404000

; Obs: Lembre-se de não deixar o seu programa executar trechos de código que 
; seriam pertencentes a um fluxo diferente do condicional testado, que é um 
; erro comum em códigos assembly.


.intel_syntax noprefix
.global _start
.section .text
_start:
    mov rax, 0
    mov ebx, [rdi]
    cmp ebx, 0x7f45cafe
    je if
    cmp ebx, 0x00005AAD
    je else_if
    jmp else
if:
    mov eax, [rdi+4]
    add eax, [rdi+8]
    add eax, [rdi+12]
    jmp end
else_if:
    mov eax, [rdi+4]
    sub eax, [rdi+8]
    sub eax, [rdi+12]
    jmp end
else:
    mov eax, [rdi+4]
    imul eax, [rdi+8]
    imul eax, [rdi+12]
end:
    nop