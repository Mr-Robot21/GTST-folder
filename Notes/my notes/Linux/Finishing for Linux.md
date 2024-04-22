## Script Installation
- Some hacking tools are developed by people and they make them open-source thus we can get them from *GitHub*.
- To download and use the tools from GitHub we use the following syntax :
         *  *git  clone  ( link of the script )* 
         *  Ex.   git  clone  https://github.com/aboul3la/Sublist3r

## Script modules
- Scripts are written with scripting languages like  ( python, bash, go, ruby, ....... ).
- When using the scripting languages, we need *modules/libraries* to run the script as dependency. Ex :
         1. *Python* : to install python modules we use 
             * **pip install ( module name )**
             * for requirements file -  **pip install -r  requirements.txt** 
         2. *go* : to install go modules 
             * **go install ( module name )** 
         3. *Ruby* : to install ruby modules
             * **gem install ( module name )** 
### Note :
- In computer hardware, a module is a component that is designed for easy replacement. 
- In computer software, a module is an extension to a main program dedicated to a specific function. 
- In programming, a module is a section of code that is added in as a whole or is designed for easy reusability.

## Errors we may encounter

When installing packages or scripts things to do or not do :
1. Don't close apt while installing.
2. If you encounter *Repository errors* you can fix it using 
         *  **sudo apt edit-sources**

### Commands we use to get help 

We can use the following commands to get help in Linux :
1. *man ( manual )* : this command gives the whole manual and instruction of a tool or command.  
             * Ex.  **man ( your command )** 
2. *help* : some commands have help options. It only shows the *options* of the command.
             * Ex. **( your command )  -h**
             * Ex. **( your command )  -help**
             * Ex. **( your command )  --help**

## Linux Processes & services
- As we interact with Linux, we create a number of instances of running programs called  "*processes*".
- *Processes* : an instance of executing a program or command.
- To view the processes we use the command :
         * **ps  ( option )** 
- More commands :
         1. **ps** :  to view processes running on my shell.
         2. **ps  -A** :  to view all running processes.
         3. **ps -u  username** :  to view the user's processes.

- To stop a process use the command :
         * **kill (option) (PID)**                            PID : process id
- More on Kill command :
         1. **kill -19 PID** :  to stop the process
         2. **kill -18 PID** :  to resume the process we stopped
         3. **kill -9 PID** :  to stop a process immediately 
         4.  ............ more options ( 31 options )

### Note 
- To view processes use *htop* which is easy to use and colorful but install it first.

## Foreground & background
- *Foreground job* a process that connects to the terminal. A job is said to be in the foreground because it can communicate with the user via the screen and the keyboard. 
- Processes that require a user to start them or to interact with them are called foreground processes.
- *Background job* a process that disconnects from the terminal and cannot communicate with the user.
- Processes that are run independently of a user are referred to as background processes.
### Note
- Programs and commands run as foreground processes by default.

- We use "**&**" operator to run programs in the "*background*" or press "**ctrl + z**"
- To get the background process back to foreground use the command :
         *   **fg** 
- To stop a process going inside your shell just press  *ctrl + c* 

## Null device
- The *null device* is typically used for disposing of unwanted output streams of a process, or as a convenient empty file for input streams.
- */dev/null* - redirects output to nowhere.
- The null device is a special file that throws away whatever is fed to it.
- Sometimes it is referred to as *bit bucket*.
- if you don't want to see errors on your screen and you don't wan to save them to a file, you can redirect them to */dev/null*.
- On the shell output there are 2 ways :
         1. *STDERR* = 2
         2. *STDOUT* = 1
##### STDERR 
- used to redirect *errors* from command result to the given file.
     Ex.  **command 2> filename** 

##### STDOUT 
- used to redirect *error free* output to the given file.
     Ex. **command 1> filename** 


## Symbolic linking
- A *symbolic link* sometimes called a *symlink* or *soft link* is a file in Linux that points to other files or directories (folders) and represents their absolute or relative path.
- A symlink is similar to shortcuts in Windows and is useful when you need quick access to files or folders with long paths.
- Symbolic linked file show "*l*" when listing with "*ls*" command. Also there will be a "*->*" to show the linked file.
- Syntax is :  
         *   **ln  -s  [source_filePATH]  myfilename** 
- see the given pic [[Pasted image 20240422145203.png]] 

## alias
- An *alias* in Linux is a user-defined shortcut for a command or a group of commands.
- You can create an alias using the *'alias'* command followed by the name of the alias and the command it should execute.
      Ex.   **alias joe = 'ls -l'** 
- But it doesn't work after we close the terminal, thus to make it permanent we should add it to the *shell config file*.
- see the pic [[Pasted image 20240422150022.png]] 

## Tmux - Terminal Multiplexer
- tmux is **a terminal multiplexer tool** in Linux. Essentially, it enables us to create and maintain multiple pseudo-terminal (PTS) instances.
- On kali it is built-in but if not install it using apt.
- To start tmux we just type "*tmux*".
- But first we must create a config file type and type some commands. See the given picture [[Pasted image 20240422150613.png]]
- To understand more about tmux check the link below https://www.linuxtrainingacademy.com/tmux-tutorial/
- In my kali i use the following commands [[Pasted image 20240422151354.png]] 


### Most useful commands 

##### Wget
- *Wget* (short for World Wide Web Get) : is an open-source utility that allows you to retrieve content from web servers via HTTP, HTTPS, and FTP protocols. 
- It is designed for non-interactive downloads, meaning it can operate in the background without user input, making it great for scheduled downloads.
- Syntax : 
         *   **wget  (options) (link)** 

##### find
- To use the '*find'* command in Linux, you specify the directory to search and the criteria for the search. 
- The syntax for the command is, 
       * **find (directory/to/search) (parameter) (filename)** 
- check the given websites for more :
     1. https://ioflood.com/blog/find-linux-command/
     2. https://www.geeksforgeeks.org/find-command-in-linux-with-examples/