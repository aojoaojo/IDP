; - Condicionais

; Switch-cases são um caso especial de if-else onde a condição passada para o
; teste é um número que determina o fluxo de controle.

; Segue um exemplo de um switch-case em C:
;     switch(num):
;         0: jmp executa_0 
;         1: jmp executa_1
;         2: jmp executa_2
;         default: jmp executa_default

; Nesse caso, o switch pode assumir os números 0, 1 ou 2, ou qualquer outro
; número que não seja um desses. Esse comportamento é similar ao de um if-else, e
; em x86 esse comportamento pode ser replicado com o uso de jump tables.
        
; Uma jump table é uma seção contígua de memória que guarda endereços de lugares
; para pular.

; Uma jump table para o exemplo acima seria:
;     [0x8ff7       ] = endereço de executa_0 
;     [0x8ff7 +  0x8] = endereço de executa_1
;     [0x8ff7 + 0x10] = endereço de executa_2
;     [0x8ff7 + 0x20] = endereço de executa_default

; Um dos propósitos de jump tables é reduzir a quantidade de comparações que
; precisamos fazer para determinar o fluxo de controle. Em vez de comparar o
; número com 0, 1 e 2, podemos simplesmente checar se o número é maior que 2,
; e caso não seja, podemos calcular diretamente o endereço para pular. Isso
; pode ser feito da seguinte forma:

;     if num > 2
;         jmp [0x8ff7 + 0x20]
;     caso contrário:
;         jmp [0x8ff7 + num * 8]

; Baseado na explicação anterior, escreva um programa que implemente o seguinte:
;     if rdi is 0:
;         jmp 0x40305b
;     else if rdi is 1:
;         jmp 0x403128
;     else if rdi is 2:
;         jmp 0x4031a2
;     else if rdi is 3:
;         jmp 0x403262
;     else:
;         jmp 0x40334e

; Para resolver a atividade, considere o seguinte:
; - RDI não será negativo
; - Será permitido apenas 1 instrução de comparação
; - São permitidos no máximo 3 jumps de qualquer tipo
; - O número para 'switch' estará no registrador RDI
; - O endereço base da jump table estará no registrador RSI
; - O programa realizará múltiplos testes, então seu código 
;   receberá diferentes valores para a jump table
; - O caso default deverá ter um deslocamento de 0x20 bytes, 
;   a partir do endereço base
        
; Segue um exemplo:
;     [0x404051] = 0x40305b (poderá mudar)
;     [0x404059] = 0x403128
;     [0x404061] = 0x4031a2
;     [0x404069] = 0x403262
;     [0x404071] = 0x40334e


.intel_syntax noprefix
.global _start
.section .text
_start:
    xor rax, rax 
    cmp rdi, 3
    ja else
    add rax, [rsi + rdi * 8]
    jmp rax

else:
    jmp [rsi + 0x20]
