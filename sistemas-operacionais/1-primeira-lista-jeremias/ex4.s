.intel_syntax noprefix
.global _start
.section .text
_start:
    MOV RCX, RDX;
    XCHG RDX, RDI;
    MOV RDI, RCX;
