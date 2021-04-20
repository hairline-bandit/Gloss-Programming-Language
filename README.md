# Gloss-Programming-Language

## To set up:

Make a folder on desktop called "gloss"

Put the hq.ps1 file and main.py file directly inside

Make sure you have the Python interpreter in your path and able to be ran with "python" command in prompt

Make sure you have the GoLang compiler installed

## To start programming:

Make a text file (or literally any other plaintext file) in the gloss folder you made

Use notepad or any other text editor to enter the code 

## To execute code:

Open Powershell command prompt and "cd" into the gloss folder

run .\hq.ps1 with 1 argument as the name of your text file with code in it

## Check docs.md for documentation

## How it works and why I made it this way

I didn't feel like learning Flex, Bison, and LLVM to make one the "traditional" way so I decided on this

How this works is the .txt file contains your code and it parsed by the python script

It will turn your code into its equivalent in GoLang (I chose GoLang because I dont' know C and because it's pretty fast with some good functions built in)

The Powershell script will run the python script with whatever file you specify and will also compile/execute and then delete the .go file that is created

This was much easier than Flex + Bison + LLVM
