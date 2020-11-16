## MATH
<start> ==> <function_a>
<function_a> ==> <function_a> '+' <function_b> | <function_a> '-' <function_b> | <function_b>
<function_b> ==> <function_b> '*' <function_c> | <function_b> '/' <function_c> | <function_b> '%' <function_c> | <function_c>
<function_c> ==> <INTEGER_TYPE> | '(' <start> ')'

def start():
    lex()
    function_a()

def function_a():
    lex()
    function_a()
    while(subsequent_token is ADD_OPERATOR):
        lex()
        function_b()
        function_a()
        while(subsequent_token is SUBTRACTION_OPERATOR):
            lex()
            function_b()
            function_b()
def function_b():
    function_b()
    while(subsequent_token is MULTIPLICATION_OPERATOR):
        lex()
        function_c()
        function_b()
        while(subsequent_token is DIVIDING_OPERATOR):
            lex()
            function_c()
            function_b()
            while(subsequent_token is MODULUS_OPERATOR):
                lex()
                function_c()
                function_c()
def function_c():
    if(subsequent_token is INTEGER_TYPE):
        lex()
    elif(subsequent_token is LEFT_PARENTHESIS):
        lex()
        start()
    elif(subsequent_token is RIGHT_PARENTHESIS):
        lex()
    else:
        error_message()


## WHILE
<while_statement> ==> while '('<boolean_expression>')' <statement>



def while_statement():
    if(subsequent_token is while):
        lex()
        else:
            error_message()
            if(subsequent_token is LEFT_PARENTHESIS):
                lex()
                boolean_expression()
                else:
                    error_message()
                    if(subsequent_token is RIGHT_PARENTHESIS):
                        lex()
                        statement()
                        else:
                            error_message()

            

        
## IF
<if_statement> ==> if (<boolean_expression>) <statement>
[else <statement>]

def if_statement():
    if(subsequent_token is not IF_STATEMENT):
        error_message():
    else:
        lex()
        if(subsequent_token is not LEFT_PARENTHESIS)
        error_message()
        else:
            lex()
            boolean_expression()
            if (subsequent_token is not RIGHT_PARENTHESIS):
                error_message()
            else:
                lex()
                statement()
                if(subsequent_token is ELSE_STATEMENT):
                    lex()
                    statment()
                    else:
                        error_message()


## MATH ASSIGNMENT
<start> ==> <variable> = <function_a>
<function_a> ==> <function_a> ("+"|"-") <function_b> | <function_b>
<function_b> ==> <function_b> ("*"| "/") <function_c> | <function_c>
<function_c> ==> (<function_a>) | <variable>
<variable> ==> "a" | "b" | "c" 


def start():
    variable():
    if(subsequent_token is EQUAL_OPERATION):
        lex()
        function_a()
    else:
        error_message()

def function_a():
    function_a()
    while(subsequent_token is ADDITION_OPERATION or subsequent_token is SUBTRACTION_OPERATION):
        lex()
        function_b()
        function_b()

def function_b():
    function_b()
    while(subsequent_token is MULTIPLICATION_OPERATION or subsequent_token is DIVISION_OPERATION):
        lex()
        function_c()
        function_c()

def function_c():
    if(subsequent_token is LEFT_PARENTHESIS):
        lex()
        function_a()
        if(subsequent_token is RIGHT_PARENTHESIS):
            lex()
            variable()

def variable():
    if(variable is "a" or variable is "b" or variable is "c"):
        lex()
    else:
        error_message()
        
    
# Reference: Class notes and lectures 