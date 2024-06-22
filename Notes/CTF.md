## 1. Cracking hashes 

- We can use the following :
     1. https://tunnelsup.com/hash-analyzer   - to check the hash type
     2. https://crackstation.net   - to crack easy hashes
     3. https://hashcat.net/wiki/doku.php?id=example_hashes - hashcat page
     4. https://www.youtube.com/watch?v=OFc0QNNhHOo
     5. https://bloggeroffer.blogspot.com/2023/10/tryhackme-write-ups-thm-walkthroughs.html   - note for the above video and using hashcat
     6. https://www.youtube.com/watch?v=IPZeg350Mrs - video best
     7. https://www.youtube.com/watch?v=euiuIzHaiLk - second best

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

