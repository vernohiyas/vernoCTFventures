ssh bandit1@bandit.labs.overthewire.org -p 2220

```
bandit1@bandit:~$ ls -la
total 24
-rw-r-----  1 bandit2 bandit1   33 Oct 16  2018 -
drwxr-xr-x  2 root    root    4096 Oct 16  2018 .
drwxr-xr-x 41 root    root    4096 Oct 16  2018 ..
-rw-r--r--  1 root    root     220 May 15  2017 .bash_logout
-rw-r--r--  1 root    root    3526 May 15  2017 .bashrc
-rw-r--r--  1 root    root     675 May 15  2017 .profile 
bandit1@bandit:~$  
```

So as you can see here, there is a file called -.
This is a tricky one, anyone would just try, cat - right?
```
bandit1@bandit:~$ cat -


^C
bandit1@bandit:-$
```
So this is what cat - actually does. cat - will just print STDIN to STDOUT. It doesn't recognise - as a file name.  
In programs, the dash (-) actually denotes an argument.  
To get the command to read - as a filename instead of an argument input, we need to define a path. Many ways works but this is a simple solution.
```
bandit1@bandit:~$ cat ./-
<flag is printed here>
bandit1@bandit:~$ cat /home/bandit1/-
<flag is printed here>
bandit1@bandit:~$ cat ~/-
<flag is printed here>
bandit1@bandit:~$ cat $PWD/-
<flag is printed here>
```

Notes:  
~ represent home directory for current user  
$PWD is an environment variable that prints the current directory you are in.  
[Click here for bandit2](../bandit2)
