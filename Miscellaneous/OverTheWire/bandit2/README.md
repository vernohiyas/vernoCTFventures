ssh bandit2@bandit.labs.overthewire.org -p 2220

Simple, just list the directory and read the file.
In most shells, there is a function known as "Tab completion". You can typing part of the file and pressing the Tab key will complete the rest of the file for you.
```
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ cat spaces\ in\ this\ filename
<flag will be shown here>
```
Note: "\\" is know as an escape character. It tells the program that should not be read as a special character but a string. This will become clearer to you in the future.
