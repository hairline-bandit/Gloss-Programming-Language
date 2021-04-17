# Info:

Gloss is a statically typed hybrid language (hybrid meaning it is interpreted by and interpreted language and then ran through a compiled)

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
