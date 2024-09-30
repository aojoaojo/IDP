.intel_syntax noprefix
.global _start
.section .text
_start:
    MOVZX rbp, byte ptr [0x404000]
    MOVZX r14, word ptr [0x404004]
