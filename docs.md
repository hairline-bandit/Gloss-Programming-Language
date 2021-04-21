# Info:

Gloss is a statically typed hybrid language (hybrid meaning it is interpreted by an interpreted language and then ran through a compiled)

It is designed to use the least amount of "hard to hit" characters as possible so that you might be able to program faster using it

You will always need a "main" function

You will always need a semicolon where there should be semicolons

## To define a main function:

Type "null" (This means that a function will not return anything)

Type "main()<" note the "<" symbol replacing the "{" symbol, this goes back to "less hard to hit" characters

**Instead of typing a tab, type a ">" for each line** (For any place an indent would be used)

"<" functions as both an opening and a closed bracket

### You can check the "examples.txt" file for code examples for each of these as Gloss contains many characters that upsets markdown

## To print:

Type "dis: " (display)

Type what you want to print afterwards

Follow with a semicolon

### Check "examples.txt" for examples of printing

## To define variables:

Type the type of the variable

There are...

int (int) str (string) flt (float64) char (char) bool (boolean) and a 1d array version of all of those

Then type the name of the variable and a colon (no space between the 2)

Finally type the value (you have to make sure it matches what you declared the variable would be, ofc) and a semicolon

### Check "examples.txt" for examples on variable declaration

## To change variables:

Use the same format that you would for any other "C/Cpp/Java" "Style" language

### Check "examples.txt" for examples on variable editing

## To define functions:

First type the return type (or "null" if it doesn't return anything)

There are these return types...

int (int) str (string) flt (float64) char (char) bool (boolean) and a 1d array version of all of those

Next type the name of the function followed by "(" **There cannot be a space in between name and "("; it upsets the parser**

After the "(" type any parameters in the format "type name" "type" being the type of the parameter (refer to variables section) and "name" being the name of the parameter

Make sure that you use a ")" afterwards and a "<" (no space between those 2 characters) and a ">" for tabs and "<" for brackets

For returning use no parentheses and make sure that you use a semicolon

**Due to the nature of the parser, defining functions after their use (run a function in main and define the function below main), will cause them not to be recognized. Either define the function before or put __"#dec funcname"__ at the top of the program (where "funcname" is the name of the function)**

### Check "examples.txt" for examples of defining functions

## If, else, else if

Now that you know what replaces indents and brackets, I will only need to give you the names of the "conditional checkers"

"if" is "if

"else" is "else"

"nor" (it's not that or could it be this) is "else if"

### Check "examples.txt" for examples of If, else, else if

## Math operators

\* is multiplication

/ is subtraction

\+ is addition

\- is subtraction

\% is modulo

## For loop

"for" stays as "for"

for loops are non inclusive in their range

use >> to loop from first value to second

use << to loop from second to first

### Check "examples.txt" for examples on for loops

## Built ins:

"pop" removes the last item from an array

"push" adds a value to the end of an array

"remove" removes a value from an array by index

"strIndex" gets the leftmost index of a substring from a string

"strRindex" gets the rightmost index of a substring from a string

"split" splits string by a delimeter

"join" joins arr string by a separator 

"arrIndex" gets the leftmost index of a value from an arr < There are 5 1 character suffixes for the function  

"arrRindex" gets the rightmost index of a value from an arr < There are 5 1 character suffixes for the function

"scan" scans user input and assigns a variable to what is entered

"int" "str" "flt" "bool" "char" all dump the conversion of a specified var type to type specified by function name

To use pop, put the pop keyword followed by a colon and a space

Then put the array that you'd like to pop from (followed by a semicolon ofc)

To use push, put the push keyword followed by a colon and a space

Then put the array you'd like to push to followed by a comma and a space, then the value (followed by a semicolon ofc)

To use remove, put the remove keyword followed by a colon and a space

Then put the array that you'd like to remove from followed by a comma and a space, then the index that you'd like to remove (followed by a semicolon ofc)

To use strIndex, put the strIndex keyword followed by a colon and a space

Then put the array you'd like to get from followed by a comma and a space, then the substring, then a comma and a space followed by the variable that you'd like to dump the index result to (it creates a new variable so make sure that you haven't declared it yet) (followed by a semicolon ofc)

To use strRindex, do the same thing as strIndex

To use split, put the split keyword followed by a colon and a space

Then put the string you'd like to split followed by a comma and a space, then the delimeter, then a comma and a space followed by the variable you'd like to dump the result to (it makes a new variable) (followed by a semicolon ofc)

To use join, put the join keyword followed by a colon and a space

Then put the string array variable followed by a comma and a space, then the separator, then a comma and a space followed by the variable you'd like to dump the result to (it makes a new variable) (followed by a semicolon ofc)

To use arrIndex, put the arrIndex keyword followed by either a "S" for string (string arrays), "I" for int, "F" for float, "C" for char, or "B" for boolean (ie. arrIndexS) followed by a colon and a space

Then put the array (corresponding type) followed by a comma and a space, then the value you are searching for, then a comma and a space followed by the variable you'd like to dump the result to (it makes a new variable) (followed by a semicolon ofc)

To use scan, put the scan keyword followed by a colon and a space

Then put the type of the variable that you want to assign to (str, int, flt, bool, char) followed by a comma and a space, then the variable (it has to be declared already) that you'd like to assign to, then a comma and a space followed by the message that you'd like to print for the user input (this is because dis: prints a newline and it looks bad for user input) (The message has to be in quotes; it can't be a str variable). (This is followed by a semicolon ofc)

To use int str flt bool char, put the keyword followed by a colon and a space

Then put the type of the variable you are converting from followed by a commma and a space, then the variable you are converting from, then a comma and a space followed by the name of the variable you'd like to dump the contents to (it creates a new variable) (This is followed by a semicolon ofc)

### Check "examples.txt" for examples of built in functions
