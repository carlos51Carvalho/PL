'''
    Program => Declaracoes Corpo
    

    Declaracoes => VARS Decls ENDVARS
                 | 
    Decls => Decl Decls
           | 
    Decl => int id


    Corpo => BEGIN Instrucoes END
    Instrucoes => Intrucao Intrucoes
                |
    Instrucao => print num
'''
import ply.yacc as yacc
import sys

#get tokens
from comp_lex import tokens


def p_Programa(p):
    "Progama : Declaracoes Corpo"
    p[0] = p[1] + p[2]
    print(p[0])



def p_Declaracoes(p):
    "Declaracoes : VARS Decls ENDVARS"
    p[0] = p[2]

def p_Declaracoes_vazio(p):
    "Declaracoes : "
    p[0] = ""

def p_Decls(p):
    "Decls : Decl Decls"
    p[0] = p[1] + p[2]

def p_Decls_vazio(p):
    "Decls : "
    p[0] = ""


def p_Decl(p):
    "Decl : int id"
    p[0] = "pushi 0"
    #save id



def p_Corpo(p):
    "Corpo : BEGIN Instrucoes END"
    p[0] = "start \n" + p[2] + "stop"

def p_Instrucoes(p):
    "Instrucoes : Instrucao Instrucoes"
    p[0] = p[1] + p[2]

def p_Instrucoes_vazio(p):
    "Instrucoes : "
    p[0] = ""


def p_Instrucao_print(p):
    "Instrucao : print num"             #print exp
    p[0] = "pushi " + p[2] +"\n" +"writei\n"




def p_error(p):         #rotina de erros
    print("Erro sintático no input: ",p)
    parser.success = False


# build the parser
parser = yacc.yacc()

# Creating the model
parser.registers={}


# read input an parse line by line
import sys
for Linha in sys.stdin:
    parser.success= True

    P=parser.parse(Linha)

    if parser.success:
        print()

    else:
        print("Frase inválida. Corrija e tente de novo...")
