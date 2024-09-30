.intel_syntax noprefix
.global _start
.section .text
_start:
    POP rax
    IMUL rax, rcx
    PUSH rax