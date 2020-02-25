In this challenge, we just need to SSH(Secure Shell) to the game server with the credentials provided to us.  
There are numerous tools we can use.  
If you are on windows, you can install ssh onto your command prompt.  
If you are on linux, it should come pre-installed.  
A very popular tool used for SSH is PuTTY.  

With PuTTY, just enter the correct values into the respective fields.  
Host: bandit0@bandit.labs.overthewire.org  
Port: 2220  
Pass: bandit0  

With SSH
```
ssh bandit0@bandit.labs.overthewire.org -p 2220  
```

Note: You can directly login as a user in this format <username>@<host>  

List and read the file for the flag.
```
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme
<flag will be shown here>
```
