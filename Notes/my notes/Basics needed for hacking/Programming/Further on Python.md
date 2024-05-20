## Functions

- *Function* : is a block of code that performs a specific task.
- Dividing a complex problem into smaller chunks ( pieces ) makes our program easy to understand and reuse.

### Types of functions
- There are 2 types of functions :

#### 1. Standard library functions 
- These are built-in functions in python that are available to use.
- Almost all keywords are functions. Ex. *print ( ) , len ( ) ,  input ( ) ........* 

#### 2. User-defined functions
- We create our own functions based on our requirements.

### Creating Functions
- Syntax :      *def  Joel ( ) :* 
               *print( "Hey this is Joel" )*   # function body
- We have to call the function in order for the function to run.
     Ex.     *Joel ( )* 

### Function Arguments
- They are used to take value while calling and inserting it inside the function.
     Ex .   *def  add_numbers ( num1 , num2 ) :*       or   *def  add_no (num1=5, num2=4)*
             sum = num1 + num2 
             print ( sum ) 

         add_numbers (5,4)      # output is 9
### Return statement
- A python function may or may not return a value.
- If we want our function to return some value to a function call, we use the *return* statement.
- When you use return on a function it doesn't display anything thus when calling the function use *print*.  

## Recursion

- Recursion is process of defining something in terms of itself. 
- In Python , we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.
- For example , writing a function for factorial.

#### Advantages of recursion
1. Recursive functions make the code look clean and elegant
2. A complex task can be broken down into simpler sub-problems using recursion
3. Sequence generation is easier with recursion than using some nested iteration.

#### Disadvantages of recursion
1. Sometimes the logic behind recursion is hard to follow through.
2. Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
3. Recursive functions are hard to debug.

## Anonymous / lambda function

- If function doesn't have name it is called lambda function.
- Lambda function is a special type of function without the function name.
- Syntax :   **lambda**  *arguments  : expression*  
     Ex.   greet = **lambda** :  *print* ("Hello world") 
         greet ()                                   # calling the function
         numbers = lambda a, b  :   a + b
         print (numbers ( 2,4 ))                        # calling the function

## Function takers function

- Filter, map  

### 1. Filter Function
- are used to filter or search some function from sequences.
     Ex.   num = [2,3,4,5,6,7,8]
         evens = list(filter(lambda n: n%2 == 0 , num))
         print (evens)

### 2. Map Function
- used to do some operations on sequences.
     Ex.  num = [2,3,4,5,6,7,8]
         def double (n) :
             return n * 2 
         doubles = list (map(double, num))
         print (doubles) 

## Append Keyword

- Is used to add new element to an existing list.
- Syntax :   *mylist_append ("New element")* 

## Object-oriented programming / OOP

- Python is an OOP, this means more things in python are objects.
- Objects are anything which can have action and name.
- Objects have attributes (properties) and methods (action or function).

### Python class
- Class is a place where we create our objects attributes and behavior.
- Class is a blueprint for objects.
- Syntax :   *class  Computer :*  
             name = " "                         # here we create attributes
             CPU = " " 
- Conventionally class name start with *capital letter*.

### Creating Objects
- We can create many Objects based on 1 class.
- Syntax :  
         * *var* = classname()
         * *var.attribute* = "value"
- Here is an example :  [[Pasted image 20240430221305.png]] 

#### checking the type () of our object
- When we check our type it is similar with type of int, both are classes.
- Here is an example :  [[Pasted image 20240430221548.png]] 

### Giving behaviors == Creating Methods
- Functions are called methods on OOP.
- Syntax on calling :
     -  *classname.method(object)* 