.intel_syntax noprefix
.global _start
.section .text
_start:
    MOV rax, [rsi]
    MOV rbx, [rsi + 8]
    ADD rax, rbx
    MOV [r12], rax
    mov rax, [rsi]
    xor rax, [rsi + 8]
    mov [r12 + 8], rax