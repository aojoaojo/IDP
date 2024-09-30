.intel_syntax noprefix
.global _start
.section .text
_start:
    AND rax, 0
    OR rax, rdi
    AND rax, rcx
