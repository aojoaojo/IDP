.intel_syntax noprefix
.global _start
.section .text
_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, 0x4042cc
    mov rdx, 50
    syscall