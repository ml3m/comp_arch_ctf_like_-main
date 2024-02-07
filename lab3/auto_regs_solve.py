from pwn import *

def main():
    conn = remote("85.120.206.124", 31343)
    for _ in range(2):
        start = conn.recvuntil(b"> ").decode()
        print(start)
        conn.sendline(b"2")    
        recv = conn.recvuntil(b"R3):").decode()
        print(recv)
        conn.sendline("R3")    
        start = conn.recvuntil(b"> ").decode()
        print(start)
        conn.sendline(b"1")
        recv = conn.recvuntil(b"R3):").decode()
        print(recv)
        conn.sendline("R2")
        start = conn.recvuntil(b"> ").decode()
        conn.sendline(b"3")
        recv = conn.recvuntil(b"R3):").decode()
        print(recv)
        conn.sendline(b"R2")
        recv = conn.recvuntil(b"R3):").decode()
        print(recv)
        conn.sendline(b"R3")
        start = conn.recvuntil(b"> ").decode()
        conn.sendline(b"3")
        recv = conn.recvuntil(b"R3):").decode()
        print(recv)
        conn.sendline(b"R2")
        recv = conn.recvuntil(b"R3):").decode()
        print(recv)
        conn.sendline(b"R1")
    start = conn.recvuntil(b"> ").decode()
    print(start)
    conn.sendline(b"4141")
    recv = conn.recvuntil(b"R3):").decode()
    conn.sendline(b"R1")
    flag = conn.recv().decode()
    print(flag)
    conn.sendline("4")

    conn.interactive()

if __name__ == "__main__":
    main()