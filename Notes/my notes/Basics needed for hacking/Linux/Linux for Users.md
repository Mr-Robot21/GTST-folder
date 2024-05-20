
# Overview of Kali Linux

- Kali Linux was previously known as **Backtrack**.
- Kali Linux is a Linux distribution designed for 
                                    * digital forensics &
                                    * penetration testing 
- It is maintained and funded by *Offensive Security*. 
- The software is based on the *Debian* Testing branch: most packages Kali uses are imported from the Debian repositories.

# Understanding Kali Linux tools

There are different tools in kali used for different tasks :

### Information Gathering
- Tools used for information gathering are  [[Pasted image 20240416141738.png]] 
- Mostly used tools are  
                * *Maltego*
                * *nmap*
                * *recon-ng*

### Vulnerability Analysis
- Tools used for finding vulnerabilities are  [[Pasted image 20240416142131.png]] 
- Mostly used tools are 
                 * *nikto*
                 * *nmap*


### Web Application Analysis
- Tools used for finding vulnerability and exploiting on websites [[Pasted image 20240416142454.png]] 
- Mostly used tools are 
                 * *burpsuite*
                 * *sqlmap*
                 * *zap*
                 * *wpscan*


### Database Assessment 
- Tools for finding vulnerabilities and exploits on databases [[Pasted image 20240416142807.png]] 
- Mostly used tools are 
                 * *JSQL injection*
                 * *sqlmap*


### Password Attacks
- Tools for exploiting Passwords for login, websites, application, windows [[Pasted image 20240416143125.png]]
- Mostly used tools are 
                 * *hashcat*
                 * *john* (john the ripper)


### Wireless Attacks
- Tools for exploiting wireless systems like wifi, bluetooth [[Pasted image 20240416143435.png]] 
- Mostly used tools are 
                  * *aircrack-ng*
                  * *wifite*
                  * *reaver*


### Reverse Engineering
*Reverse Engineering* is a process or method through which one attempts to understand through deductive reasoning how a previously made device, process, system, or piece of software accomplishes a task with very little (if any) insight into exactly how it does so.

- Tools for exploiting software, mobile applications and binary files [[Pasted image 20240416143729.png]]
- Mostly used tools are
                 * *apktool*
                 * *ghidra*

### Exploitation Tools
- Tools for exploiting software, mobile, computers, websites and anything [[Pasted image 20240416144504.png]]
- Mostly used tools are 
                 * *Metasploit framework*

### Sniffing & spoofing
*Sniffing* is intercepting network traffic to listen for and read unencrypted data actively.
*Spoofing* attacks are man-in-the-middle attacks in which the attacker impersonates another person.

- Tools for listening or hijacking networks [[Pasted image 20240416145000.png]]
- Mostly used tools are 
                    * *wireshark*

### Post exploitation
Post exploitation is also called maintaining access.

- Tools for maintaining our access  [[Pasted image 20240416145425.png]] 
- Mostly used tools are 
                    * *backdoor framework*

### Forensics
*Forensic* is the branch that determines who is responsible for a digital intrusion or other cybercrime committed.

- Tools for doing research and investigating a cyber attack [[Pasted image 20240416145841.png]]
- Mostly used tools are
                    * *hashdeep*

### Reporting tools
- Tools for report preparation. These tools help you to write report  [[Pasted image 20240416150119.png]] 
- Mostly used tools are
                    * *recordmydesktop*

### Social Engineering tools
*Social Engineering* is the tactic of manipulating, influencing, or deceiving a victim in order to gain control over a computer system, or to steal personal and financial information.

- Tools used for social engineering attacks [[Pasted image 20240416150452.png]]
- Mostly used tools are
                    * *maltego*
                    * *backdoor framework*

### System services
- Buttons used to start some services.  [[Pasted image 20240416150717.png]] 

# Folder managers

- File managers are necessary for efficiently managing our daily operations.
- We may use file managers to **_copy, move, rename_**, and **_delete files_**, and **_manage space_** and **_storage._** 
- There are different file managers in Linux :
                                    * Dolphin
                                    * Thunar
                                    * Nautilus
- For more information check this website https://www.javatpoint.com/best-file-manager-for-kali-linux 

# Linux Commands overview

- Linux systems use *shell* ( terminal ).
- The shell help us to Communicate with kernel and execute codes.

The terminal have 5 parts.  [[Pasted image 20240416152517.png]] 
- Username 
- Hostname
- Current Directory
- Privilege
- Command place

# Linux commands Basic
**Command** is a directive to a computer program to perform a specific task.
- On Linux there are over 100 commands. 
- These commands have their own *options*  and *arguments*.
website for Linux commands  https://www.digitalocean.com/community/tutorials/linux-commands 

#### ls / list directory
- list information about a file or directory.  [[Pasted image 20240416153559.png]] 

#### cd / change directory
- used to change current working directory. [[Pasted image 20240416153807.png]] 

#### pwd / print working directory
- it prints the path of the working directory, starting from the root.

#### echo
- is used to display line of text/string that are passed as an argument.
- mostly used in shell scripts and bash files to output status text to the screen or file.
- see this pic  [[Pasted image 20240416154329.png]] 

#### cat / head / tail / less
- used to show the content of a file

#### touch
- creates any kind of files with the name you give it but the file is empty.

#### mkdir /make directory
- creates folder with the name you give it.  [[Pasted image 20240416154815.png]] 

#### clear 
- clears the screen 
- you can also use **ctrl + l** 

#### rm / remove
- removes a file.  [[Pasted image 20240416155122.png]] 

#### cp | mv / copy, move
- copy / move files and folders.
- *mv* command is also used to rename a file.

#### grep / global search for regular expression
- The **grep** filter searches a file for a particular pattern of characters, and displays all lines that contain that pattern.  
- The pattern that is searched in the file is referred to as the regular expression.
- how to use grep  [[Pasted image 20240416203155.png]] 

#### wc / word count
- it is used to find out                            in the files specified in the file arguments.
                 * *number of lines*
                 * *word count* 
                 * *character count* 
- check this pic for more info [[Pasted image 20240416203815.png]] 

# Multiple command Executions
- You can run & execute multiple commands in 1 line using 3 methods :
                                                         * *And* ( && )
                                                         * *or* ( || )
                                                         * *piping* ( | )
### AND ( && )  &  OR ( || )
- The **&&** and **||** characters play special roles when commands depend on the success or failure of previous commands.
- learn more about && and || in  https://www.networkworld.com/article/972419/the-power-of-and-on-linux.html 

### Piping ( | )
- pipe helps you run commands by using the output of the 1st command as the input for the next one.

# Awk, sed, and tee commands

