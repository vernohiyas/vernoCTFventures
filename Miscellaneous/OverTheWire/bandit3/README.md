<b>Bandit Level 3 → Level 4</b>  
Level Goal  
The password for the next level is stored in a hidden file in the inhere directory.  
  
Commands you may need to solve this level  
ls, cd, cat, file, du, find  
<hr>  
ssh bandit3@bandit.labs.overthewire.org -p 2220  

Lets list the directory.  

```
bandit3@bandit:~$ ls -la
total 24
drwxr-xr-x  3 root root 4096 Oct 16  2018 .
drwxr-xr-x 41 root root 4096 Oct 16  2018 ..
-rw-r--r--  1 root root  220 May 15  2017 .bash_logout
-rw-r--r--  1 root root 3526 May 15  2017 .bashrc
drwxr-xr-x  2 root root 4096 Oct 16  2018 inhere
-rw-r--r--  1 root root  675 May 15  2017 .profile
```  

As you can see, there is a directory, the "d" at the left most of each file represents a directory.
Note: "." and ".." represents current and parent directory respectively.  
  
Lets navigate inside
```
bandit3@bandit:~/inhere$ ls -la
total 12
drwxr-xr-x 2 root    root    4096 Oct 16  2018 .
drwxr-xr-x 3 root    root    4096 Oct 16  2018 ..
-rw-r----- 1 bandit4 bandit3   33 Oct 16  2018 .hidden
bandit3@bandit:~/inhere$
```
Note: the dot(.) infront of a file tells the filesystem to hide it. A normal ls will not show this file. So it is a good habit to always run ls -la instead of ls.  
Now is probably a good time to talk about command arguments.  
Every command takes whatever after the dash(-) as an argument.  
ls -la,  
l means to list in long format, showing the permissions, drwx-xr-x for example.  
a means to list all, including hidden files.

[Click here for bandit4](../bandit4)
