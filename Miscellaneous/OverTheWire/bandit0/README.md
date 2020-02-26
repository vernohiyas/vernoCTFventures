<b>Bandit Level 0</b>
Level Goal
The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.

Commands you may need to solve this level
ssh

Helpful Reading Material
[Secure Shell (SSH) on Wikipedia](https://en.wikipedia.org/wiki/Secure_Shell)
[How to use SSH on wikiHow](https://www.wikihow.com/Use-SSH)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<b>Bandit Level 0 → Level 1</b>
Level Goal
The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

Commands you may need to solve this level
ls, cd, cat, file, du, find

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
[Click here for bandit1](../bandit1)
