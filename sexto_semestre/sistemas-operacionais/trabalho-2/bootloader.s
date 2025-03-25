.code16
.intel_syntax noprefix
.global _start

_start:
    cli
    xor ax, ax

    mov ds, ax
    mov es, ax
    mov ss, ax
    
    mov sp, 0x7c00
    sti

    xor ax, ax
    int 0x13

    mov ax, 0x7E0
    mov es, ax
    mov ah, 0x02
    mov al, ah
    xor ch, ch
    mov cl, al
    xor dh, dh
    int 0x13

    mov ax, 0x117
    jmp 0x7E00

    .fill 510 - (.-_start), 1, 0x00
    .byte 0x55, 0xaa
