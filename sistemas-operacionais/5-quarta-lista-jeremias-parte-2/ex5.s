.intel_syntax noprefix
.global _start
.section .text
_start:
    mov rax, 0
    mov rdi, 3
    mov rsi, 0x4040c0
    mov rdx, 100
    syscall
    mov rdx, rax
    mov rax, 1
    mov rdi, 1
    mov rsi, 0x4040c0
    syscall