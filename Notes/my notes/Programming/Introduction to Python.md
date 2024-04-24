## What is programming language
- It is a language which helps us to communicate with computers.
- There  are many different programming languages namely :
     1. *Assembly*
     2. *C* , *C++*
     3. *Ruby*, *Perl*
     4. *Java*, *JavaScript* 
     5. *Python* .....
- Programming languages help us to write code/program.

## What is a Program
- A program is an *algorithm* expressed in programming language.
- An algorithm is a *detailed sequence of actions* to perform or accomplish a task.
- Technically, an algorithm must reach a result after a finite number of steps.

## Evolution of I/O ( input / output )
- Early in the history of computing, programs were submitted on *punch cards with all the date* they required and executed together with other programs that used the same libraries.
- Later developments introduced *interactive processing* which allowed the user to provide date while program was running. It was question and answer format.

## Generation of computers

1. 1st generation : vacuum tubes - punch cards
2. 2nd generation : transistors - programming started here with *assembly*
3. 3rd generation : integrated circuits - *BASIC, COBOL,  Pascal, Fortran, C, C++, Perl,*
4. 4th generation : Microprocessors - *Python, SQL , MATLAB* 
5. 5th generation : Artificial Intelligence 

- First generation could only solve one problem at a time. It would take days or even weeks to set up a new Program on First Generation.

## Types of Programming Languages

- Computers understand *binary ( 0/1 )*, humans don't understand this.
- Based on the *closeness of the language to humans understanding* we classify it into 3.
- The more they become *low* to the machine they are *faster*.
- The more they become *like human language* they are *slower*.

### Low level programming language
- These languages are  more like machines but with lots of efforts people can understand them. Ex *Assembly*

### High level programming language
- They are more close to human languages. Ex. *Python* , *C++* , *java* , ..........

### Medium level
- Languages between Low level and High level, they combine both. Ex. *C - language* 

## How do high level languages work

1. *Compilers* : are tools which help us to *convert* the whole code to *bytecode* then computer will execute it.  Ex. *Java, C, C++*
2. *Interpreter* : can directly execute the code by reading the source code line by line
        Ex. *Python* 

## Use of Programming language

1. To develop hacking tools
2. To develop android applications
3. To develop website
4. For artificial intelligence
5. To develop games ..........



## What is python Programming
- *Python* : is a High level & interpreted programming language.
- is very easy to learn because it is simplified language.

## History of Python
- developed by *Guido van Rossum* in *early 1990* at the *National Research Institute for Mathematics and Computer Science* in the *Netherlands*.
- is derived from many other languages like :
            * *ABC , Modula-3* 
            * *C* , *C ++* 
            * *Algol-68, SmallTalk*
            * *Unix Shell* and other *Scripting languages*
- is now maintained by *core development team* at the *Institute*.

## Uses of Python

1. to write hacking script
2. for machine learning
3. for data analysis
4. for artificial intelligence
5. for game development
6. for back-end web development ( like Django and flask )


## IDE & Code editors

### IDE ( integrated Development Environment )
- is a software that helps to write & run a specific programming language.                     Ex.   *python IDE* 

### Code Editor 
- a software that can help to write any kind of programming languages.
- can also add some *compiling/ interpreting* features so you can run *programs* & *scripts*. Ex.  *Sublime*, *Vscode* ....

#### Note 
- check the course material to see how to use Vscode.


## Python Commands

### outputs
- to display output we use the keyword *print* 
- Syntax :  **print ( object = ' ' ,  sep= ' ' , end= ' ')**
-    **\n** = new line     **\t** = tab space  

### comments 
- This are simple notes written on our code to help us remember the function of the code or to make it simple for people to understand our code.
- comments are not executed.
- Syntax :     **#** - this is a comment line.

### user input
- to receive user input 
- Syntax:   **input**    
- Ex.  *num = input ("Enter a number : ")* 

### python keywords
- *Keywords* are predefined, reserved words used in python that have special meaning to the compiler.
- check this website  https://realpython.com/python-keywords/

### variables
- are a value holders ( containers ).
- They store data.  Ex. **x = 10** 
- The process of giving value to a word is called *Variable declaration*.
- The word that holds the data is called *identifier*.
- We can print value of the variable by giving the identifier.
     Ex.     **cold = 21**
         *print ( "You are ",  **cold** , "years old." )*   
         output : You are 21 years old.

- We can change the value of the variable in a code. 
     Ex.   **cold = 21** 
         **cold = 10** 

- You can print the variable with *{variable name}* on print keyword.
     Syntax :   **print (f "your text  {variable}")**
      Ex.   **name = 'Joel'**
         **print (f "My name is {name}.")** 

#### Note
- On naming the identifier :
      1. Don't use space between words, instead use *underscore ( _ )*
      2. Don't use numbers as identifiers.

### Data types
- There are a lot of Data types on python.
- See the link for more info  https://www.geeksforgeeks.org/python-data-types/

##### A. Numeric data type
- *integer ( int )* : It contains positive or negative whole numbers (without fractions or decimals)
- *float* : It is a real number with a floating-point representation. It is specified by a decimal point. It's accurate up to 15 decimal point.
- *complex* : - It is specified as (real part) + (imaginary part)j. For example – 2+3j

#### Note
-  *type()* function is used to determine the type of Python data type.

Ex.    **num1 = 2 + 3j** 
     *print ( num1 , " is of type " , **type(num1)**)*   

##### B. String data types
- *String* is a sequence of characters represented by either single or double quotes .
     Ex.   **var = " "**    or   **var = ' '** 
         **message = ' Python for beginners '**
         *print ( **message** )* 

##### C. Sequence Data 

#### 1. Lists
- *list* is an ordered collection of similar or different types of items separated by commas and enclosed within *brackets [ ]*.
- To access items from a list, we use index number ( 0, 1, 2, .......)
- We can *add / modify* objects to the list. Use *append* 
     Ex.  **languages = ["English" , "Swahili" , "Amharic"]**
         *print (**languages[0]**)*  -       this displays English
         *languages. **append**("Amharic")*     -     this adds Amharic to the list

#### 2. Tuples 
- *Tuples* is an ordered sequence of items same as a list. The only difference is that tuples are *immutable* meaning once created *can't be modified*.
- We use the *parenthesis ( )* to store items in tuples.
- Similar to lists we use index number to access tuple items.
     Ex.   **product = ('laptop' , 'phone' , 500)** 
         *print (**product[0]**)*    -       this displays laptop

##### D. Dictionary data
- *dictionary* is an unordered collection of items. It stores elements in *key / value*  pairs.
- We use *keys* to retrieve the *respective value*, but we can't use the vice versa.
- We use *curly brackets { }* to store key / value pairs.
     Ex.   **capital_city = {'England' : 'London' , 'Italy' : 'Rome' , 'Kenya' : 'Nairobi'}** 
         *print (**capital_city['England']**)* 

### Exercise 
- This is the picture of the exercise [[Pasted image 20240424142757.png]]