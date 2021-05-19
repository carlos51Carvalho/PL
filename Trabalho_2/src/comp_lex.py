import ply.lex as lex


tokens=["VARS", "ENDVARS", 
		"BEGIN", "END", 
		"num", "id",
        "str",
		"int", "print", "read", 
		"if", "else"]

literals=['(', ')', 
            '[', ']', 
            '{', '}', 
			'+', '-', '*', '/', '%',
			'>', '<', '=']

def t_VARS(t):
    r'VARS'
    return t

def t_ENDVARS(t):
    r'ENDVARS'
    return t

def t_BEGIN(t):
    r'BEGIN'
    return t

def t_END(t):
    r'END'
    return t

def t_int(t):
    r'int'
    return t

def t_print(t):
    r'print'
    return t

def t_read(t):
    r'read'
    return t

def t_if(t):
    r'if'
    return t

def t_else(t):
    r'if'
    return t


def t_num(t):                   #t <- (t_type (neste caso é NUM), t_VALUE, t_lineo, t_column)
    r'\d+'
    return t  

def t_str(t):                   
    r'\"[^"]*\"'
    return t

def t_id(t):                   
    r'[a-z][a-zA-Z0-9]*'
    return t


t_ignore = " \t\n"

def t_error(t):
    print("Caracter Ilegal",t.value[0])
    t.lexer.skip(1)

lexer =lex.lex()


if __name__ == '__main__':
	import sys
	for linha in sys.stdin:
		lexer.input(linha)
		for tok in lexer:
			print(tok)