.intel_syntax noprefix
.global _start
.section data
.section .text
_start:
    mov rax, [0x40bca8]
    lea rdi, [rip + str]
    mov rsi, 0x4040a0
    mov rdx, 0x4053e0
    mov rcx, 0x408b20
    sub rsp, 8
    call rax
    ret
str: .asciz "%s%s%s\n"