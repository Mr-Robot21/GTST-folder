## Indexing

-  *Indexing* refers to the process of accessing a specific element in a sequence, such as a string or list, using its position or index number. 
- Indexing in Python starts at *0*, which means that the first element in a sequence has an index of 0, the second element has an index of 1, and so on.

- *negative indexing* : is the reverse of normal indexing Ex. start from *-1* 

- Calling texts by indexes also works for *strings* and *tuples*. 
- See the given example :
     Ex.  **name = "Joel"**
         *print* (**name[ 2 ]**)            - the output is the letter *e*    
         *print* (**name[ -3 ]**)           - the output is the letter *o* 


## Slicing

- *Slicing* is the extraction of a part of a string, list, or tuple. It enables users to access the specific range of elements by mentioning their indices.
- The *slicing operator* is  ( **:** )
- Syntax : Object [start : stop : step] “Start” specifies the starting index of a slice. “Stop” specifies the ending element of a slice.
- See the given example :
     Ex.   name = ["Ethiopia" , "Kenya" , "Chelsea" , "Messi"]
         print (name[-1 : 0 : -2])      - output is (Messi, Kenya)
         print (name[::-2])                - same output (Messi, Kenya)

##### Note
- *Negative indexing* is also used.
- it is more applicable for *strings*.
- Python uses default *step* as **1** and default *stopping index* is the **last index**.

## User Input handling

- Python provides us with *two inbuilt functions* to read the input from the keyboard.
- These are :
     1. by input function
     2. by arguments

##### 1. by input function ( input () )

- **input ():** This function first takes the input from the user and converts it into a *string*. The type of the returned object always will be <class ‘str’>. It does not evaluate the expression it just returns the complete statement as String.
- Syntax : var = input ("text you like to display")
- Accepts the input and stores on variables.
- By default input accepts strings so we should change to the data types we want.
     Ex.     name = int (input ("Enter your number"))
          name = eval (input ("Enter your number"))
         print (type(name))       - show the data type of name

##### 2. by arguments
- This help us to get the input form the command lines
- Syntax :  
         *import sys*
         *name = sys.argv[1]*
         *print (f "hello {name}!")*
        then write on the command line the following
         *python ( name of python file ) the thing we want to write*
        Ex python practice1.py "Joel Mengstab"

### Note 
- Steps to use by arguments methods are :
     1. First write the *import sys* 
     2. Second write your arguments and code
     3. Save your file 
     4. Don't run your code but write your arguments on the terminal and hit enter.
         Ex. *python test.py arg1 arg2 .........*


## Operators

- *Operators* are special symbols, combinations of symbols, or keywords that perform operations on variables and values. Ex . **print ( 5 + 6 )** 
- There are a lot of operators type in python :

### 1. Arithmetic operators
- They are simple math operations .
- Inputs have to be in *int , eval, float* only.
- These are some of the few operators [[Pasted image 20240425185141.png]] 
     Ex.    print ("power :" , a ** b )
         print ("modulo:" , a %b )
         print ("division:" , a / b )

### 2. Assignment operators
- are used to assign values to variables.
- you write the arithmetic operators first then the equal sign.
- Here some of the operators  [[Pasted image 20240425185703.png]]  
     Ex.    a+= b       -    a = a + b
         a**= b       -    a = a ** b
         a%= b       -    a = a % b

### 3. Comparison operators
- used to compare variables and return Boolean result.
- *Boolean* means either *True* or *false*.
- Here are some operators  [[Pasted image 20240425191059.png]] 

### 4. Logic Operators
- are used to check if an expression is *True* or *false*.
- They use truth table.
- Here are some logic operators  [[Pasted image 20240425191633.png]]
- The truth table of *and (&&)*  ,     only T & T gives T                                                       [[Pasted image 20240425191736.png]]
- The truth table of *or ( | | )* ,  only F & F gives F                                                             [[Pasted image 20240425191840.png]]
- The truth table of *not*   [[Pasted image 20240425191932.png]]

### 5. Bitwise operators
-  used to perform operations on binary numbers, i.e., numbers represented in the      base-2 number system.
- On our computers everything has a binary value. (also called *bit*)
- On python there is a keyword called *bin* used to show the binary value of a decimal no.
     Ex.   bin (114) 
- *Bitwise operators* are used to do *math* and *Logical operations* on the binary value of the expression.
- Understanding bitwise operations is critical if you work on *cryptography*.
These are bitwise operators :

#### A. Complement ( NOT ) ( ~ )
- It takes one number and inverts all bits of it. When bitwise operator is applied on bits then, all the 1's become 0's and vice versa.
- In other words, 10 is actually 00001010, not just 1010. Flip them and you get 11110101, which is -11, or 245 if using an unsigned integer.
- In simple math, it will add 1 to the number and then makes it negative.
     Ex.    print ( ~ 12 )                     - output is -13

#### B. And ( & )
- compares each bit of the first operand to the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0.
- Here is an example :
     Ex.    10   ->  1010
         7     ->  0111
         and  =   0010     = 2
##### Note 
- You can add a *0* before a binary number if it is not a four digit binary no.
     Ex.    7 -> 111     but we can write 
         7 -> 0111
#### C. Or ( | )
- compares the values (in binary format) of each operand and yields a value whose bit pattern shows which bits in either of the operands has the value 1. If both of the bits are 0 , the result of that bit is 0 ; otherwise, the result is 1 .
- Here is an example :
     Ex.   10  ->  1010
         7   ->  0111
         or   =   1111     = 15

#### D. XOR ( ^ )
- *XOR* stands for *"exclusive or."* If input bits are the same, then the output will be false(0) else true(1).
       *same* = *0*    Ex.   1 ^ 1  = 0      ,     0  ^ 0  = 0 
       *different*      Ex.    1 ^ 0 = 1
- Here is an example :
     Ex.   10  ->  1010
         7   ->  0111
         xor =  1101    =  13

#### E. Left shift ( << )
- causes the bits in shift-expression to be shifted to the left by the number of positions specified by additive-expression . The bit positions that have been vacated by the shift operation are zero-filled.
- Here is an example : 
     Ex.   10  ->       1010.*00*00         *10<<2*
                 101000.00
            <<         101000         =  40

#### F. Right shift ( >> )
- moves the bits of an integer or enumeration type expression to the right.
- Here is an example :
     Ex.   10  ->       10*10*.0000         *10>>2*
                 10.100000
            <<         10         =  2


## Indentations

- *Indentation* refers to the spaces at the beginning of a code line. 
- Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important. 
- Python uses indentation to indicate a *block of code*.

## If-else conditions

- The *if-else statement* is used to execute both the true part and the false part of a given condition. If the condition is true, the if block code is executed and if the condition is false, the else block code is executed.
- For example, assigning grades ( A, B, C ) based on marks obtained by a student.
     1.  if the percentage is above *90*, assign grade *A*.
     2.  if the percentage is above *75*, assign grade *B*.
     3.  if the percentage is above *65*, assign grade *C*.
- In python there are 3 forms of the if - else statement.

#### 1. if statement
- An *if statement* is a condition statement used to check a condition, and execute it if the condition holds true. 
- It is also a control flow statement, which utilizes decision-making to control the flow of execution.
- Syntax :   *if condition :* 
           # *body of if statement*
- Check this example   [[Pasted image 20240426163215.png]]

#### 2. if-else statement
- The *if-else statement* is used to execute both the true part and the false part of a given condition.
- Syntax :    *if  condition :*
             # *block of code if True*
         *else* : 
             # *block of code if false* 
 - Check this example  [[Pasted image 20240426163657.png]]

#### 3. if - elif - else statement
1. It checks the if statement condition. 
2. If that is false, the elif statement is evaluated. 
3. In case the elif condition is false, the else statement is evaluated.
- Syntax :    *if  condition :*
             # *code block 1*
         *elif condition :*
             # *code block 2*
         *else :*
             # *code block 3*
 - Check this example   [[Pasted image 20240426164305.png]]

#### Nested if statements
- *Nested if statements* are if statements inside another if statement. These can be very useful to make complex decisions in your script.
- In nested if statement two requirements have to be true to run the code of condition.
- Syntax :    *if  condition1 :*
             # *statements*
             *if  condition2 :*
                 # *statements* 
- Here is an example  [[Pasted image 20240426164955.png]] 

## Logical Errors ( Exceptions )

- *A logical error* occurs in Python when the code runs without any syntax or runtime errors but produces incorrect results due to flawed logic in the code. 
- These types of errors are often caused by incorrect assumptions, an incomplete understanding of the problem, or the incorrect use of algorithms or formulas.
- For instance, they occur when we 
     * try to call an index that is greater than the list have causes ( *index Error* )
     * try to divide a number by zero ( *zero division error* )
     * When you have an error in your syntax ( *Name error* ) and so on.
- Thus when errors occur on runtime this causes a huge damage on our program so we have to handle it.

### Error handling
- For handling errors we use *try .... except* blocks.
- Syntax :      *try :* 
             # *code that may cause exception* 
         *except :* 
             # *code to run when exception occurs* 
- Check this example [[Pasted image 20240426175953.png]]   

## Python Loops

- *loop* is a sequence of instructions that is continually repeated until a certain condition is reached.
- are used to *repeat a block of code*.
- There are 2 types of loops in Python :

#### 1. For Loops
- A *for loop* in Python is used to iterate over a sequence (list, tuple, set, dictionary, and string).
- when it's implemented, executes a piece of code over and over again "for" a certain number of times, based on a sequence.
- Syntax :     *for  x in  sequence :* 
             # statements
- Understanding for loop with diagram  [[Pasted image 20240426180811.png]]
##### Note 
- *range()* is series of values between two numeric intervals. Ex.  range (5) - range ( 0, 5 )
- *len()* is used to show the length of a sequence like list, tuple, or staffing. 
     Ex.   [[Pasted image 20240426181309.png]]  

#### 2. While loops 
- A *while loop* is a control flow statement which repeatedly executes a block of code until the condition is satisfied. It stops executing the block only if the condition fails. 
- used to execute a set of statements as long as a condition is true.
- One should use a 'while' loop when one needs to perform a repeated operation, but doesn't know in advance how many iterations would be needed.
- Syntax :    *while  condition :*
             # *body of while loop* 
- See the given example  [[Pasted image 20240426181724.png]] 
- You can do *infinite loop* using while.   Ex.   *while True :* 
                                      # *write code* 
##### Note 
- Differences between *for loop* and *while loop* 
     1. For loop is used when number of *iteration is known* and while loop is used when number of *iteration is unknown* ( when we have a condition ).
     2. For loop ends when the *iteration is finished* and while loop ends when the *condition is false*.

## Break

- *Break* allows you to exit a loop when an external condition is met. 
- Normal program execution resumes at the next statement. You can use a break statement with both for loops and while loops. In a nested loop, break will stop execution of the innermost loop.
- used to exit from an *infinite loop*.
- See the given example  [[Pasted image 20240426182852.png]] 


 