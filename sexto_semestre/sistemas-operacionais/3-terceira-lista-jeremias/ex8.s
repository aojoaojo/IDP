.intel_syntax noprefix
.global _start
.section .text
_start:
    jmp short .skip
    
    .rept 0x47
        nop
    .endr
    
    .skip:
        mov r12, 0x4759fc9c