def parse_string(chars, list):
    for char in chars:
        if char.isalnum() is False:
            perl_check(char,list)
            string_check(char,list)
            
        elif char[0].isdigit():
            check_float(char,list)
            check_int(char,list)
        
    for char in chars: 
        non_alpha(char,list)
        check_char(char,list)
    print("\nOrdered List:\n\n",list)

def perl_check(char,list):
    for c in char:
        if c is "$" or c is "@" or c is "%":
            print("PERL ==> ", char)
            list.append(char)

def string_check(char, list):
    if char.startswith('"') and char.endswith('"'):
        print("STRING ==> ", char)
        list.append(char)

def check_float(char, list):
    for c in char:
        if c is "E" or c is "e" or c is "F" or c is "f":
            print("FLOAT ==> ", char)
            list.append(char)
        
def check_int(char, list ):
    if char.isdigit() is True:
        print("INTEGER ==> ", char)
        list.append(char)

def non_alpha(char, list):
    if char.isalnum() is False and char[0] is not "@" and char[0] is not "$" and char[0] is not "%" and char[0] is not '"' and char[0] is not ".":
            print("NONALPHA ==> ", char)
            list.append(char)

def check_char(char, list):
    if char.isalpha() is True:
            print("CHAR LITERAL ==> ", char) 
            list.append(char)

def main_function():
    ordered_list = []
    strings = open("strings.txt", "r")
    buffered_reader = strings.read().replace("\n"," ")
    chars = buffered_reader.split()
    parse_string(chars, ordered_list)

main_function()

