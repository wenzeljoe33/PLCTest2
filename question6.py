# <start> ==> <function_a>;
# <function_a> ==> <function_a> '+' <function_b> | <function_a> '-' <function_b> | <function_b>;
# <function_b> ==> <function_b> '*' <function_c> | <function_b> '/' <function_c> | <function_b> '%' <function_c> | <function_c>;
# <function_c> ==> <INT> | '(' <start> ')'
 
## MATH
def start():
    lex()
    function_a()

def function_a():
    lex()
    function_a()
    while(next_token is ADD_OPERATOR):
        lex()
        function_b()
        function_a()
        while(next_token is SUBTRACTION_OPERATOR):
            lex()
            function_b()
            function_b()
def function_b():
    function_b()
    while(next_token is MULTIPLICATION_OPERATOR):
        lex()
        function_c()
        function_b()
        while(next_token is DIVIDING_OPERATOR):
            lex()
            function_c()
            function_b()
            while(next_token is MODULUS_OPERATOR):
                lex()
                function_c()
                function_c()
def function_c():
    if(next_token is INT):
        lex()
    elif(next_token is LEFT_PARENTHESIS):
        lex()
        start()
    elif(next_token is RIGHT_PARENTHESIS):
        lex()
    else:
        error()


## WHILE

def while_loop():
    if(next_token is not WHILE_CODE):
        error()
    elif (next_token is not LEFT_PARENTHESIS):
        error()
        else:   
            boolean_expression()
            if(next_token is not RIGHT_PARENTHESIS):
                error()
            else:
                start()
            

        
## IF

def if_statement():
    if(next_statement is not IF_CODE):
        error():
    else:
        lex()
        if(next_token is not LEFT_PARENTHESIS)
        error()
        else:
            lex()
            boolean_expression()
            if (next_token is not RIGHT_PARENTHESIS):
                error()
            else:
                lex()
                start()
                if(next_token is ELSE_CODE):
                    lex()
                    start()
