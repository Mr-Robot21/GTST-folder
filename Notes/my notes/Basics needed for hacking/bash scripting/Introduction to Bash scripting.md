## What is Bash Scripting

- Bash = bourne again shell
- Shell is used to interact with kernel.
- Script is a file that contains shell commands in a simple and clear algorithm.

## Uses of bash

- Script development
- Automating tasks
- Developing hacking skills

## Starting with Bash

- We use any editor and save our file using *.sh*  extension.
- To start every bash scripting use *shebang*.
        1. *#!/bin/bash* 
        2. *#!/bin/sh* 
- To display output on bash you use 
     Ex.  *echo  "Your text"* 
- To run your project you we use the following :
     1. */bin/bash  joel.sh* 
     2. *./joel.sh*   but you should change the permission ( *chmod +x  joel.sh* )
     3. *joel*     this also needs permission
##### Note
- You can only use *double quote ( " " )* and not *single quote ( ' ' )*

### Variables
- Bash variables are same with python variables, with some exceptions.
- Syntax :    *variable_name=value*         no space
- Exceptions :
     1. No space between the equal sign ( = ).
         - Name = "Joel"    -> Error
         - Name="Joel"      -> Correct
     2. Never start with numbers
     3. Use *double quotes* only
- To use variable we use the *dollar sign ( $ )* before the variable name.
- If you want to display the variable sticked with other text use *${variable_name}* 
- Bash variables are string by default.

#### set command
- can be used to assign values to positional parameters.
- Syntax :   *set*  value1 value2 value3 ......
     Ex.    set   Joel  Messi  Hazard   Palmer 
          echo $1 $3                   - displays  Joel   Hazard 
- It starts from *1* .

#### System variables
- Are variables declared by the system.
     Ex.  *$USER*    - display owner or the host

### Variables and Data Types
- To create other data types we use *declare*. 

#### Array
- are lists or tuples on python.
- Syntax :   
     1.   var = ("list1" "list2" "list3")
        -    to display    *echo "${var[0]}"* 
        -    to get all the elements    *echo  "${var[@]}"* 
        -    to get the index number    *echo  "${!var[@]}"* 
        -    to get the length       *echo  "${#var[@]}"*
        -    to add element to the array   *var[4]="Joel"* 
        -    to remove from the array    *unset var[4]* 



#### 1. Bash read
- used to accept input while the script is running.
- Syntax :  
     - *read  -p*  "text to display" variable_name
     - *read  -sp*  "Password:"  variable_name     (used to accept hidden texts like passwd)
     - *read  -a*   variable_name      (for accepting array or lists)

#### 2. Arguments
- These helps to get input before the script starts
- Syntax : 
     - Just use *$0-9* while you want to work with the input.

### comments
- On bash comments are written as follows :
- Syntax : 
     - *#*  - this is for single line comments.
     - *<<comments ............. comments* - this is for multi line comments.

### Bash sleep
- To make a good waiting on our script.
- Syntax : 
     - *sleep  (no)s*          Ex.  sleep 5s


### Operations
- to do mathematical operations you have to do *$ ((expression))* 
- we use *let* keyword for assigning variables

#### A. arithmetic operations
1. addition *$((a+b))* 
2. exponential *$((a ** b))*
3. ..........

#### B. Assignment operations
1. Increment *let* "*a+=3*"
2. Decrement *let* "*a-=3*"
3. Multiply  *let* "*a *=3*"
4.  .........

#### C. Comparison operations
- There are two methods 

##### 1. Alphabetic comparison
- These use words to compare two variables.
     -  greater than  =  *-gt*
     -  less than  =   *-lt*
     -  greater than and equals to  =  *-ge*
     -  less than and equals to   =  *-le* 
     -  equals   =   *-eq* 
     -  not equals   =    *-ne* 

##### 2. Sign comparison
- These use signs to compare two variables.
     -  greater than   =    *>* 
     -  less than     =    *<*
     -  greater than and equals to    =     *>=* 
     -  less than and equals to    =      *<=* 
     -  equals      =     *=* 
     -  not equals     =     *!=* 

### If - else conditions
- There are two ways : 

#### 1. using square brackets [ ]
- We use the square bracket ( [ ] ) when using *alphabetic comparison*.
- Syntax : 
         *if*  [ condition ]            * condition = [ 2 -gt 1 ]
         *then* 
         body or code 
         *else* 
         body
         *fi*


#### 2. using two parenthesis (( ))
- We use two parenthesis when we use *sign comparison*.
- Syntax : 
         *if*  (( condition ))            * condition  =  (( 2 > 1 )) 
         *then* 
         body
         *else*
         body
         *fi*  

##### Note
- On bash we don't have *indentation* so we use *fi* when we finish writing our body.