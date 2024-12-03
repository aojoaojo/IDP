.code16
.intel_syntax noprefix
.global _start

_start:
    cli                     # Desabilitar as interrupções
    xor ax, ax              # Limpar os registradores de segmento
    mov ds, ax
    mov es, ax
    mov ss, ax
    mov sp, 0x7c00          # Mover o ponteiro de pilha para 0x7c00
    sti                     # Habilitar as interrupções
    mov ah, 0x00            # Resetar o sistema de disco
    int 0x13
    mov ax, 0x7E0           # Setar o segmento estendido
    mov es, ax
    mov ah, 0x02            # Configurar leitura de setores do disco
    mov al, 0x02            # Ler 2 setores
    mov ch, 0x00            # Cilindro 0
    mov cl, 0x02            # Setor 2
    mov dh, 0x00            # Cabeça 0
    int 0x13                # Chamar interrupção 0x13 para carregar o kernel
    mov ax, 0x117            # Inserir os últimos três dígitos da matrícula em hexadecimal
    jmp 0x7E00              # Saltar para o kernel

    .fill 510 - (.-_start), 1, 0x00 # Preencher com zeros até 510 bytes
    .byte 0x55, 0xaa         # Assinatura do bootloader
