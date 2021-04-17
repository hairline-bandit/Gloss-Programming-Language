"""
Ideas:
Actually make the thing
Use -_- strategy and make a new text file with script (turn into program) and then run through python interpreter
"""
# imma do the -_- version


# Write Powershell script to execute this file
# This file converts .gloss code file to .txt file with go equivalent from .gloss
# Powershell turns .txt file into go and runs and then deletes .txt and .go files


import sys

file = sys.argv[1]
types = ["int", "str", "flt", "char", "bool", "[]int", "[]str", "[]flt", "[]char", "[]bool"]
func_types = ["int", "str", "flt", "char", "bool", "[]int", "[]str", "[]flt", "[]char", "[]bool", "null"]
ifs = ["if", "else", "nor"]
defed_funcs = []

with open(file, "r") as f:
    code_lines = [i.replace("\n", "") for i in f.readlines()]

new_f = open("123123123123.go", "w")
new_f.write("package main\nimport (\n\t\"fmt\"\n)\n")
for line in enumerate(code_lines):
    # whitespace
    if line[1] == "":
        continue
    # comments
    elif line[1][0:3] == "//":
        new_f.write(line + "\n")
    # variables
    elif len(line[1].split(" ")) > 1 and line[1].split(" ")[1] in types:
        if line[1][-1] is not ";":
            raise Exception(f"Missing \";\" on line {line[0]}")
        for i in line[1].split(" ")[0]:
            if i is ">":
                new_f.write("\t")
            elif i is "<":
                new_f.write("}")
        type_of = ""
        name_of = ""

        if line[1].split(" ")[1] == "int":
            type_of = "int"
        elif line[1].split(" ")[1] == "str":
            type_of = "string"
        elif line[1].split(" ")[1] == "flt":
            type_of = "float64"
        elif line[1].split(" ")[1] == "char":
            type_of = "rune"
        elif line[1].split(" ")[1] == "bool":
            type_of = "bool"
        elif line[1].split(" ")[1] == "[]int":
            type_of = "[]int"
        elif line[1].split(" ")[1] == "[]str":
            type_of = "[]string"
        elif line[1].split(" ")[1] == "[]flt":
            type_of = "[]float64"
        elif line[1].split(" ")[1] == "[]char":
            type_of = "[]rune"
        elif line[1].split(" ")[1] == "[]bool":
            type_of = "[]bool"

        for i in line[1].split(" ")[2]:
            if i is not ":":
                name_of += i
            elif i is ":":
                break

        if "[]" in type_of:
            new_f.write(name_of + " := " + type_of + "{")
            after_colon = False
            for i in enumerate(line[1]):
                if not after_colon:
                    if i[1] is ":":
                        after_colon = True
                        continue
                elif after_colon and i[0] != line[1].index(":") + 1:
                    if i[1] is not "[" and i[1] is not "]" and i[1] is not ";":
                        new_f.write(i[1])
            new_f.write("}\n")
        elif "[]" not in type_of and type_of is not "":
            new_f.write("var " + name_of + " " + type_of + " = ")
            after_colon = False
            for i in enumerate(line[1]):
                if not after_colon:
                    if i[1] is ":":
                        after_colon = True
                        continue
                elif after_colon and i[0] != line[1].index(":") + 1:
                    if i[0] != len(line[1]) - 1:
                        new_f.write(i[1])
            new_f.write("\n")
    # printing
    elif len(line[1].split(" ")) > 1 and line[1].split(" ")[1] == "dis:":
        for i in line[1].split(" ")[0]:
            if i is ">":
                new_f.write("\t")
            elif i is "<":
                new_f.write("}")
        new_f.write("fmt.Println(")
        after_colon = False
        for i in enumerate(line[1]):
            if not after_colon:
                if i[1] is ":":
                    after_colon = True
                    continue
            elif i[0] != len(line[1]) - 1 and after_colon and i[0] != line[1].index(":") + 1:
                new_f.write(i[1])
        new_f.write(")\n")
    # functions
    elif len(line[1].split(" ")) > 1 and line[1].split(" ")[0] in func_types:
        type_of = line[1].split(" ")[0]
        name_of = ""
        params = {}
        for i in line[1].split(" ")[1]:
            if i is "(":
                break
            name_of += i
        defed_funcs.append(name_of)
        if type_of != "null":
            if len(line[1][line[1].index("(") + 1: line[1].index(")")].split(", ")) > 1:
                a = line[1][line[1].index("(") + 1: line[1].index(")")].split(", ")
                for i in a:
                    b = i.split(" ")
                    params[b[1]] = b[0]
            elif len(line[1][line[1].index("(") + 1: line[1].index(")")].split(", ")) == 1:
                a = line[1][line[1].index("(") + 1: line[1].index(")")].split(" ")
                params[a[1]] = a[0]
        new_f.write("func " + name_of + "(")
        if type_of != "null":
            list_params = list(params)
            for i in list_params:
                new_f.write(i + " ")
                if params[i] is "str":
                    new_f.write("string")
                    if i is list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
                elif params[i] is "flt":
                    new_f.write("float64")
                    if i is list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
                elif params[i] is "char":
                    new_f.write("rune")
                    if i is list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
                elif params[i] is "[]str":
                    new_f.write("[]string")
                    if i is list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
                elif params[i] is "[]flt":
                    new_f.write("[]float64")
                    if i is list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
                elif params[i] is "[]char":
                    new_f.write("[]rune")
                    if i is list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
                else:
                    new_f.write(params[i])
                    if i is list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
            new_f.write(") ")
            if type_of is "str":
                new_f.write("string {\n")
            elif type_of is "flt":
                new_f.write("float64 {\n")
            elif type_of is "char":
                new_f.write("rune {\n")
            elif type_of is "[]str":
                new_f.write("[]string {\n")
            elif type_of is "[]flt":
                new_f.write("[]float64 {\n")
            elif type_of is "[]char":
                new_f.write("[]rune {\n")
            else:
                new_f.write(type_of + " {\n")
        elif type_of == "null":
            new_f.write(") {\n")
    # end of function bracket
    elif line[1][0] is "<":
        new_f.write("}\n")

    # returning
    elif len(line[1].split(" ")) > 1 and line[1].split(" ")[1] == "return":
        counter = 0
        for i in line[1].split(" ")[0]:
            if i is ">":
                new_f.write("\t")
            counter += 1
        new_f.write(line[1][counter + 1:-1] + "\n")

    # calling funcs
    elif len(line[1].split(" ")) > 1 and line[1].split(" ")[1].split("(")[0] in defed_funcs:
        for i in line[1].split(" ")[0]:
            if i == ">":
                new_f.write("\t")
        new_f.write(line[1][line[1].index(" ") + 1:-1] + "\n")

    # declaring funcs (so you can define them below main)
    elif line[1].startswith("#dec"):
        defed_funcs.append(line[1].split(" ")[1])

    # if else else if (nor)
    elif len(line[1].split(" ")) > 1 and line[1].split(" ")[1] in ifs:
        for i in line[1].split(" ")[0]:
            if i is ">":
                new_f.write("\t")
            elif i is "<":
                new_f.write("}")

        if line[1].split(" ")[1] == "if":
            new_f.write("if " + line[1][line[1].index(" ") + 5:-2] + " {\n")
        elif line[1].split(" ")[1] == "else":
            new_f.write(" else {\n")
        elif line[1].split(" ")[1] == "nor":
            new_f.write(" else if " + line[1][line[1].index(" ") + 6:-2] + "{\n")

    # for loop
    elif len(line[1].split(" ")) > 1 and line[1].split(" ")[1] == "for":
        for i in line[1].split(" ")[0]:
            if i is ">":
                new_f.write("\t")
            elif i is "<":
                new_f.write("}")

        data = line[1][line[1].index(" ") + 6:-2]
        if data.split(" ")[1] == ">>":
            new_f.write("for " + data[0] + " := " + data.split(" ")[2][:-1] + "; " + data[0] + " < " + data.split(" ")[-1] + "; " + data[0] + "++ {\n")
        elif data.split(" ")[1] == "<<":
            new_f.write("for " + data[0] + " := " + data.split(" ")[-1] + "; " + data[0] + " > " + data.split(" ")[2][:-1] + "; " + data[0] + "-- {\n")

    # change var values
    elif "--" in line[1] or "++" in line[1] or "=" in line[1]:
        counter = 0
        for i in line[1].split(" ")[0]:
            if i is ">":
                new_f.write("\t")
            elif i is "<":
                new_f.write("}")
            counter += 1
        new_f.write(line[1][counter + 1:-1] + "\n")

    # for lines with a > and a <
    else:
        for i in line[1]:
            if i == ">":
                new_f.write("\t")
            elif i == "<":
                new_f.write("}")
        new_f.write("\n")