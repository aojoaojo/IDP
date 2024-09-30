.intel_syntax noprefix
.global _start
.section .text
_start:
    mov rax, 0xe3e01a1ad15b
    push rax
    mov rax, 0x87916ccf627f
    push rax
    mov rax, 0x352cf0b13e89
    push rax
    mov rax, 0x23686a255923
    push rax
    mov rax, 0x7705a6c0f3a
    push RAX
    xor eax, eax
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