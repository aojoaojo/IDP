; - Média

; Na maioria das linguagens de programação, existe uma estrutura chamada de
; laço de repetição, que permite executar um conjunto de instruções um número
; limitado de vezes. O número limitado de vezes pode ser conhecido antes ou
; durante a execução do programa, sendo que durante a execução o valor é
; determinado dinamicamente.

; Em assembly, estruturas de repetição utilizam a mesma base de controle de
; saltos condicionais e incondicionais, como o jmp e o cmp. Tome, por exemplo,
; o código abaixo, que realiza a soma dos números de 1 a n:

;     soma = 0
;     i = 1
;     while i <= n:
;       soma += i
;       i += 1

; Esse trecho de código pode ser traduzido para assembly da seguinte forma:

;     mov rax, 0
;     mov rcx, 1
;     loop:
;         add rax, rcx
;         inc rcx
;         cmp rcx, n
;         jle loop

; Nesta atividade, você deve calcular a média de n inteiros, que são quadwords
; consecutivos, onde:
;  - rdi = endereço de memória da primeira quadword
;  - rsi = quantidade de quadwords a serem somadas
;  - rax = local onde o resultado da média deverá ser armazenado

; Valores incializados:
;     - [0x404023:0x4042fb] = {n qwords]}
;     - rdi = 0x404023
;     - rsi = 91


.intel_syntax noprefix
.global _start
.section .text
_start:
    xor rax, rax
    xor rcx, rcx
    xor rdx, rdx

_loop:
    cmp rcx, rsi
    jge fim
    add rax, [rdi + rcx*8]
    inc rcx
    jmp _loop

fim:
    div rsi
    nop
