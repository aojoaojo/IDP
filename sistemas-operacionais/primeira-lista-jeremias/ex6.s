.intel_syntax noprefix
.global _start
.section .text
_start:
    MOV rax, r9
    ADD rax, r8
    MOV r15, rax
