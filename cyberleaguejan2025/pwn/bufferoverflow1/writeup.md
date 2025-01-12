![[Pasted image 20250111192417.png]]
So here, we are presented with a buffer overflow challenge

We will download it and examine the binary.
![[Pasted image 20250111192632.png]]
Now lets take a look at it using ida and gdb

![[Pasted image 20250111192510.png]]
Looking at ida's graph overview, this is a particularly small code.
![[Pasted image 20250111192902.png]]

![[Pasted image 20250111192543.png]]
As we proceed down the code, we see an "Enter the magic word:" this means that our buffer will only be used after this part of the program. Below, we see fgets. Here, fgets will read our string of len 0x20 and write it into rbp+s. Above we see that rbp+s is located in -20h of rbp and var_4 is located in -4 of ebp. This means that s is only 1Ch (0x20-4=0x1C) long. However, fgets pulls 0x20 bytes.

![[Pasted image 20250111193054.png]]
As we proceed further down the code block, here we see that var_4 is being compared to the static value of 1. This means that if we can use fgets to overwrite var_4 into 1, we can pass the cmp and get our flag.

```
buf = b"\x41"*32
print(buf)
```
Lets try overflowing the buffer up to fgets' limits
![[Pasted image 20250111193511.png]]
We will attach gdb and place a breakpoint right before the cmp
![[Pasted image 20250111193825.png]]
here we see that our rbp-4 is filled with our \x41, this means that our cmp will fail, but we also overwrite rbp-4, if we send 0x01 instead, we will get our flag!

```
buf = "\x41"*28
buf += "\x01\x00\x00"
print(buf)
```
![[Pasted image 20250111194057.png]]
Great! Its 1, let execution continue and we should get the flag!
![[Pasted image 20250111194126.png]]
Done!