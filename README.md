# Gloss-Programming-Language

As of 4/16/21 WIP 

Works by parsing a text file and converting it to its equivalent in GoLang. Powershell script will control everything by executing python script on text file and then executing GoLang file

For anyone wondering why I didn't use Flex, Bison, and LLVM, it's because I don't know C (That's also why implementation language is Python and GoLang) and also because I was too lazy to learn them. This is also a lot easier to make as (let's be honest here) most programming languages are basically the same, but with what does what changed. This essentially means that I can use a script to parse and then quite easily turn the commands into commands in a different language. 

Python is used as parser language as it is quite good for making parsers (and because I know python). GoLang is used as the language in the final steps that's compiled because I heard that it is actually pretty speedy (and because I know GoLang).

Yes, I know that this is going to be extremely slow because it will run an interpreted language (Powershell) to run and interpreted language (Python) to parse a program and then it will still have to Compile and execute (and 2 of these languages have garbage collection).
