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

#get tokens and literals
from cond_lex import tokens
from cond_lex import literals

#----------------------------------------------------
#---------------------- Programa -----------------------
def p_Main(p):
    "Main : Condicao"
    p[0] = p[1]
    print(p[0])


def p_Condicao_init(p):
    "Condicao : '(' Condicaobase ')'"
    p[0] = p[2]

def p_Condicao_single(p):
    "Condicaobase : Cond"
    p[0] = p[1]

def p_Condicao_list(p):
    "Condicaobase : LCondd OperLogico Cond"
    p[0] = p[1] + p[3]+p[2]

def p_LCondd(p):
    "LCondd : Condicaobase"
    p[0] = p[1]

def p_Conddd(p):
    "Cond : '(' Condicaobase ')'"
    p[0] = p[2]

def p_Conddd_not(p):
    "Cond : '!' '(' Condicaobase ')'"
    p[0] = p[3] + "not\n"




def p_Cond(p):
    "Cond : Exp Oper Exp"
    p[0] = p[1] + p[3] + p[2]
    print("Cond")
def p_Cond_not(p):
    "Cond : '!' Exp"
    p[0] = p[2] + "not\n"
    print("Cond_not")
def p_Cond_sem_oper(p):
    "Cond : Exp"
    p[0] = p[1]
    print("Cond_single")



def p_OperLogico_and(p):
    "OperLogico : '&' '&' "
    p[0] = "mul\n"

def p_OperLogico_or(p):
    "OperLogico : '|' '|' "
    p[0] = "add\npushi 0\nsup\n"


def p_Oper_equal(p):
    "Oper : '=' '=' "
    p[0] = "equal\n"
def p_Oper_diff(p):
    "Oper : '!' '=' "
    p[0] = "equal\nnot\n"
def p_Oper_sup(p):
    "Oper : '>' "
    p[0] = "sup\n"
def p_Oper_inf(p):
    "Oper : '<' "
    p[0] = "inf\n" 
def p_Oper_supeq(p):
    "Oper : '>' '=' "
    p[0] = "supeq\n"
def p_Oper_infeq(p):
    "Oper : '<' '=' "
    p[0] = "infeq\n"




#------------- expressões/termos/fatores---------------
def p_Exp_add(p):
    "Exp : Exp '+' Termo"
    p[0] = p[1] + p[3] + "add\n"

def p_Exp_sub(p):
    "Exp : Exp '-' Termo"
    p[0] = p[1] + p[3] + "sub\n"

def p_Exp_termo(p):
    "Exp : Termo"
    p[0] = p[1]



def p_Termo_mul(p):
    "Termo : Termo '*' Fator"
    p[0] = p[1] + p[3] + "mul\n"

def p_Termo_div(p):
    "Termo : Termo '/' Fator"
    p[0] = p[1] + p[3] + "div\n"

def p_Termo_mod(p):
    "Termo : Termo '%' Fator"
    p[0] = p[1] + p[3] + "mod\n"

def p_Termo_fator(p):
    "Termo : Fator"
    p[0] = p[1]



def p_Fator_exp(p):
    "Fator : '(' Exp ')'"
    p[0] = p[2]

def p_Fator_num(p):
    "Fator : num"
    p[0] = "pushi " + p[1] + "\n"

def p_Fator_id(p):
    "Fator : id"
    p[0] = "pushg " +p[1] +"\n"

def p_Fator_id_arr(p):
    "Fator : id '[' Exp ']'"
    p[0] = "pushg " +p[1]+ "\n"


def p_error(p):         #rotina de erros
    print("Erro sintático no input: ",p)
    parser.success = False


# build the parser
parser = yacc.yacc()

# Creating the model
parser.registers={}     # Registers-> {Nome da variavel: (tipo, offset, tamanho)}
parser.varsoffset=0
parser.labelid=1


# read input by line and append
import sys
Total=""
for Linha in sys.stdin:
    # ToDo: read 
    parser.success= True

    P=parser.parse(Linha)

    if parser.success:
        print()

    else:
        print("Frase inválida. Corrija e tente de novo...")




# maybe criar ID => id ou id[Exp]