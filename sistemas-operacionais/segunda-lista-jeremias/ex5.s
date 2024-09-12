.intel_syntax noprefix
.global _start
.section .text
_start:
    OR rbx, rdx
    AND rbx, 1
    XOR rax, rax
    OR rax, rbx
    XOR rax, 1
