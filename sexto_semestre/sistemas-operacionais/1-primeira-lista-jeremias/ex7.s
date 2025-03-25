.intel_syntax noprefix
.global _start
.section .text
_start:
    MOV rdx, 0
    MOV rax, rdi
    DIV rsi
