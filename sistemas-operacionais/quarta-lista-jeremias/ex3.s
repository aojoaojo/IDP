.intel_syntax noprefix
.global _start
.section .text
_start:
    mov rax, [r12]
    and rax, 1
    cmp rax, 1
    jz even
odd:
    mov rax, 1
    jmp end
even:
    mov rax, 0
end:
    nop