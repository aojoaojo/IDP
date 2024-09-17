.intel_syntax noprefix
.global _start
.section .text
_start:
    PUSH rbx
    PUSH r8
    POP rbx
    POP r8