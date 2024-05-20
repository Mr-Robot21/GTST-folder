## Regular expression (regex)
- is used to check if our input is an email or not.
- Most filter validation on any platform done by Regular expression.
- They are patterns that helps to filter texts, space, tabs & symbols.
- Regex is Pattern.
- Regex are used on Linux tools called grep, awk and sed.
- The pattern is same but the implementation may differ on programming language.
- On python .......

### Metacharacters
- They are regex pattern symbols for filter.
- They are :   ........

#### 1. Dot ( . )
- used to get all the line except new lines.
- Syntax :  *.* 
     - this means give me all lines except the new lines.

#### 2. Caret ( ^ )  -  Assertion
- used to get line that start with pattern.
- Syntax :  *^hello* 
     -  This means lines that start with hello

#### 3. Dollar sign ( $ ) - Assertion
- used to get line that ends with some pattern
- Syntax :  *hello$*
     - That ends with hello

#### 4. Plus ( + ) - Quantity
- used to get line that have pattern that occurs 1 and more times.
- Syntax :   *hellos+* 
     - A text hello that have s at least 1 times and more.

#### 5. Asterisk ( * )  - Quantity
- used to get line that have pattern that occurs 0  and more times.
- Syntax :  hellos*
     - a text hello that have s at least 0 times and more.

#### 6. Question mark ( ? )   - Quantity
- used to get line that have pattern that occurs 0 and 1 times.
- Syntax : *hello?* 
     - a text hello that  have s at least 0 times or 1 times.

#### 7. Curly bracket ({ min , max })  - Quantity
- used to get line that have pattern that occurs min and max times. It is custom
- Syntax :  *hellos{1,3}* 
     - a text hello that have s at least 0 times and more.

#### 8.   \w 
- used to get Alphanumeric ( texts and numbers ).
- Syntax :   *\w* 
     - All texts except newlines and symbols.

#### 9. ( \ W )
- used to get all except Alphanumeric.
- Syntax :  *\W*

#### 10.  \s
- used to get whitespace. (space between words)
- Syntax :  *\s*

#### 11.  \S
- used to all except whitespace.
- Syntax :  *\S*

#### 12.  \d
- used to get digits (numbers)
- Syntax :  *\d*

#### 13.  \D
- used to get all except digits.
- Syntax :  *\D*

#### 14. Pipe ( | )  - OR
- used to search 2 different things.
- Syntax : *a | b*

#### 15. Escape ( \ )
- used to search symbols that are metacharacters.
- Syntax :  *\sign* 

#### 16. Square Brackets ( [ ] )  -  Custom pattern
- used to create your own patterns.
- Syntax : *[ pattern ]* 

## Bash Regex
- You can use it on awk, sed and grep.

### Bash for regex
- we use *=~* operator for regex check with if condition statements.
- we use *double square brackets* for our conditional statements.
- Syntax :   
     *pattern = "your regex"*
     *if [[ $input =~ {pattern}]]* 

