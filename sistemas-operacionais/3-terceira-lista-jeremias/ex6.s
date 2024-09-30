.intel_syntax noprefix
.global _start
.section .text
_start:
    MOV RAX, [RSP]
    MOV RBX, [RSP + 8]
    MOV RCX, [RSP + 16]
    MOV RDX, [RSP + 24]
    MOV RSI, [RSP + 32]
    
    ADD RSP, 40

    ADD RAX, RBX
    ADD RAX, RCX
    ADD RAX, RDX
    ADD RAX, RSI

    MOV RBX, 5
    IDIV RBX

    SUB RSP, 8
    MOV [RSP], RAX
