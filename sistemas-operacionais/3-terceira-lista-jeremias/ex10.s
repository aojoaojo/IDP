.intel_syntax noprefix
.global _start
.section .text
_start:
    jmp short jump_relative

jump_relative:
    mov rdi, [rsp]
    jmp 0x400200
