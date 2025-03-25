.intel_syntax noprefix
.global _start
.section .text
_start:
    MOV rbx, [0x404000]
    SHL rbx, 16
    SHR rbx, 16