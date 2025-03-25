.intel_syntax noprefix
.global _start
.section .text
_start:
    XOR rcx, rcx
    MOVB cl, [0x404000]
    XOR rdi, rdi
    MOVW di, [0x404004]
