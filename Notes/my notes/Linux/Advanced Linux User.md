## Some Advanced user commands

- To change password of a user 
         * *sudo passwd username* 
- To change user id
         * *sudo usermod -u new_id  username* 
    - to see the user id 
             * *id username* 
- To delete user
         * *sudo userdel -r  username* 
- To change users on terminal 
         * *su - username* 

## Sudoers file
- The **sudoers file** is a file Linux and Unix administrators use to allocate system rights to system users. This allows the administrator to control who does what.
- The new user we create doesn't have power to use *sudo* as we do. This is because it is not added in the sudoers file. 
- To access the sudoers file :
           1.  *sudo visudo*  - this opens the file
           2.  find the *user privilege specification* and add the user 
                 * e.g  john ALL=ALL
        3. then save the file.

- to see more about sudoers file check this website https://www.digitalocean.com/community/tutorials/how-to-edit-the-sudoers-file 

## Linux File permission
- Every file on Linux has its own : 
                         1. *owner*
                         2. *permission*
- When we long list ( *ls -l* ) our folder or file we 5 main parts :
              1. *permission*
              2. *owner*
              3. *date*
              4. *size*
              5. *filename*

### Ownership
- Ownership is the owner of the file or the person who created the file.
- There are 2 kinds owners :
                 1. *User*
                 2. *Group* 
- To change the owner of a file we use the command :
         * *chown user:group filename* 

### Permission
- There are three types of permissions :
         1. *Read ( r )*
         2. *Write ( w )*
         3. *Execute ( x )* 
- The folders and files are differentiated with "d" and "-" respectively.
- There are 3 members in the permission :
             1. *User ( u )* : permission of user
             2. *Group ( g )* : permission of group
             3. *Other ( o )* : permission of other users
             4. *All ( a )* : permission of all the 3 members above
- Command to change permissions of a file or directory :
         * *chmod (option) filename* 
- The parameters can be in numbers and symbols see the picture given below                    [[Pasted image 20240418143155.png]]
- For detailed information on file permissions check the following website given below     https://www.javatpoint.com/linux-file-permissions

#### Special File Permissions
- Special permissions in Linux, including *SUID*, *SGID*, and the *sticky bit*, provide additional control and flexibility over file and directory access. 
- They are permissions like the execute(x), but they will set the execute permission to the user who settled them.
- for more info https://www.scaler.com/topics/special-permissions-in-linux/
##### SUID - set user id 
- *SUID* allows users to temporarily assume the privileges of the file owner.
- we add *4* in front of our numeric value  e.g   *4*777

##### SGID - set group id
- *SGID* enables temporary group ownership.
- we add *2* in front of our numeric value  e.g   *2*777

##### Sticky bit  - set other id 
- *sticky bit* enables temporary others ownership.
- we add *1* in front of our numeric value e.g  *1*777 

## Package Installation on Linux
- On Linux to install software you use package managers.
           * Ex. *apt*, *pacman*, *pkg* ......
- On Debian the package manager is called  *APT* and sometimes we use *dpkg*.

#### Package manager
- *Package manager* is a free-software user interface that work with an online server to handle the installation and removal of software  on Debian, and Debian-based Linux distributions.
- In simpler words, a package manager is a tool that allows users to install, remove, upgrade, configure and manage software packages on an operating system.
- A picture showing package manager  [[Pasted image 20240418174850.png]] 

#### Repository
- A *Linux repository* is a storage location from which your system retrieves and installs OS updates and applications. 
- Each repository is a collection of software hosted on a remote server and intended to be used for installing and updating software packages on Linux systems.
- There are 2 repositories :
         1. *local repository* : found in **/etc/apt/sources**
         2. *online repository* : found in https://www.kali.org/

#### Advanced package tool ( apt ) 
- *APT* : is a free-software user interface that works with core libraries to handle the installation and removal of software on Debian and Debian-based Linux distributions.
- Before apt we use *apt-get*.
- The apt syntax are :
         1. *sudo apt update* - for update the system
         2. *sudo apt search ( software name )* - for searching the software to install
         3. *sudo apt install ( software name )*  - for installing the software
         4. *sudo apt remove ( software name )* - for removing installed software 
         5. *sudo apt upgrade* - for upgrading the system
         6. *sudo apt purge ( software name )* - for removing the configuration files
- for more info on apt https://www.geeksforgeeks.org/apt-get-command-in-linux-with-examples/
#### Package dependencies
- *Dependencies* are libraries, packages, or modules installed in order to run a program smoothly.
- A *module* is a set of code or functions with the.py extension. 
- A *library* is a collection of related modules or packages.
- When a package manager installs the software it installs the *software + dependencies*.

#### Debian package manager ( Dpkg )
- The *Dpkg* command is a powerful tool in Linux that allows you to install, remove, and manage Debian software packages. It is often used in conjunction with *apt* to handle dependencies, but it can also be used independently.
- To understand more about Dpkg see this link https://www.digitalocean.com/community/tutorials/dpkg-command-in-linux

### Note
- Dpkg can not handle dependencies automatically. While installing a package you have to download the package dependencies otherwise it will show an error. On the other hand apt resolves dependencies automatically. You only use a single command and it will download the package with all its necessary dependencies.