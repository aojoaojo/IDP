.intel_syntax noprefix
.global _start
.section .text
_start:
    MOV r8, [0x404000]
    MOV rax, r8
    ADD rax, 0x42
    MOV [0x404000], rax