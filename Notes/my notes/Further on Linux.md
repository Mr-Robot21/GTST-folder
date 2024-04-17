# Linux file hierarchy
- *File system* is a directory structure that the OS uses.
- Linux system file appear under the **root directory ( / )**.
- To see more about file system check the following websites :
     * https://www.linuxfoundation.org/blog/blog/classic-sysadmin-the-linux-filesystem-explained 
     * https://www.javatpoint.com/linux-file-system

### /root
- _/root_ is the home directory of the superuser (also known as the “Administrator”) of the system.
- Only root user is allowed to write under this directory.

### /bin - binary executable
- _/bin_ is the directory that contains binaries, that is, some of the applications and programs you can run. 
- Essential commands binaries available in /bin are 
                                    * ls, cat, pwd, cp, ....

### /boot - boot loader files
- The _/boot_ directory contains files required for starting your system.
- **DO NOT TOUCH!**. If you mess up one of the files in here, you may not be able to run your Linux and it is a pain to repair.

### /dev - essential device file
- _/dev_ contains device files. 
- Many of these are generated at boot time or even on the fly. 
- For example, if you plug in a new webcam or a USB pen drive into your machine, a new device entry will automagically pop up here.

### /etc - et cetera
- contains configuration files required by all programs.
- also contains startup and shutdown shell scripts used to start/stop individual programs.
- For example, the files that contain the name of your system, the users and their passwords, the names of machines on your network and when and where the partitions on your hard disks should be mounted are all in here.

### /home - home directory
- _/home_ is where you will find your users’ personal directories.

### /lib 
- _/lib_ is where libraries live. 
- **Libraries** : are files containing code that your applications can use. They contain snippets of code that applications use to draw windows on your desktop, control peripherals, or send files to your hard disk.
- It is special in that it contains the all-important *kernel modules*. 
- **kernel modules** : are drivers that make things like your video card, sound card, WiFi, printer, and so on, work.

### /media
- The _/media_ directory is where external storage will be automatically mounted when you plug it in and try to access it.

### /mnt 
- is where you mount filesystems temporarily.
- This is where you would manually mount storage devices or partitions. It is not used very often nowadays.

### /opt - optional applications software packages
- The _/opt_ directory is often where software you compile (that is, you build yourself from source code and do not install from your distribution repositories) sometimes lands. 
- Applications will end up in the _/opt/bin_ directory and libraries in the _/opt/lib_ directory.

### /sbin 
- _/sbin_ is similar to _/bin_, but it contains applications that only the superuser (hence the initial _s_) will need. 
- You can use these applications with the `sudo` command that temporarily concedes you superuser powers on many distributions. 
- */sbin*  typically contains tools that can install stuff, delete stuff and format stuff.

### /tmp - temporary files
- _/tmp_ contains temporary files, usually placed there by applications that you are running. The files and directories often contain data that an application doesn’t need right now, but may need later on.
- You can also use _/tmp_ to store your own temporary files — _/tmp_ is one of the few directories hanging off / that you can actually interact with without becoming superuser.
- Files under this directory are **deleted** when the system is rebooted.

### /usr -user utilities
- _/usr_ contains a mish-mash of directories which in turn contain applications, libraries, documentation, wallpapers, icons and a long list of other stuff that need to be shared by applications and services.
- You will also find _bin_, _sbin_ and _lib_ directories in _/usr_.
- check the above link to better understand.

### /var
- _/var_ contains things like logs in the _/var/log_ subdirectories.
- *Logs* : are files that register events that happen on the system.

# Text Editors
- are programs that are used for text processing.
- Linux command line text editors : 
         * VIM
         * Nano
         * Emacs
         * Neovim
         * Mousepad
         * etc
- Linux graphical text editors :
         * Sublime
         * Vscode
         * Gedit
         * Pluma
         * etc

#### VIM
- The vim editor is :  
                 *  a very powerful
                 *  but at the same time it is cryptic
                 *  it is hard to learn, specially for windows users
    
- It has mainly two modes :
          * *Command mode* : where you write commands
          * *Insert mode* : where you write text

- Vim is by default on *command mode* when you open it.
         * to get to *insert mode* you have to type "*i*".
         * to get back to *command mode* you press "*esc*".

- In command mode you can : 
        * *save* -  type  " :w + enter "
        * *quit* -  type   " :q + enter "
        * *save & quit* -  type   " :wq! + enter "        * force = ! 
        * *undo* -  type   " :u + enter "
        * *execute commands* -  type " :%!yourcommand "


#### Nano
- The *GNU nano* text editor is a user-friendly, free and open-source text editor that usually comes pre-installed in modern Linux systems.

- Nano commands are as follows
        * *ctrl + s*  -  save
        * *alt + u*  -  undo                          *   ^ = ctrl
        * *alt + e*  -  redo
        * *ctrl + x*  -  exit
    
    * *ctrl + shift + c*  -  copy
    * *ctrl + shift + x*  -  cut
    * *ctrl + shift + v*  -  paste

- You can append texts from other files with : 
      * *ctrl + r*  and specify the path


# Linux User Management
- To know our name on Linux : 
                     * use the command - *whoami* 
- On Linux there are 2 kind of users :
             * *root*  - with id = 0
             * *normal user*  - id starts from 1000

### Creating Users
- On Linux, to create users you can use the following commands :
         * *Useradd* - to create simply
         * *adduser* - create detailed 

- The user files are stored inside */etc/passwd* 
- The user passwords are stored inside */etc/shadow* 

#### Note
- after creating a user using *adduser* command do the following
         1. add user to root group - *usermod - a -G sudo ( name of user )*. 
         2. then change the shell - *chsh -s /bin/bash ( name of user )*.

- to change the hostname we use the following command
      * *sudo hostnamectl set-hostname ( hostname name )* 

- to change the username we do the following :
         1. change to root user - *sudo su* 
         2. write the command - *usermod -l ( new username ) -d /home/kali -m (old username)*  
         3. change the group - *groupmod -n ( new username ) ( old username )* 