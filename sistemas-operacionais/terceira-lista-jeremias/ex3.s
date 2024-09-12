.intel_syntax noprefix
.global _start
.section .text
_start:
    MOV rax, 0xcafec4f3c0c4c01a
    MOV [0x404658], rax
    MOV rax, 0xfeedbeeffeedb0d3
    MOV [0x4046c8], rax