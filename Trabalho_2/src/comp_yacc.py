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
from comp_lex import tokens
from comp_lex import literals

#----------------------------------------------------
#---------------------- Programa -----------------------
def p_Programa(p):
    "Progama : Declaracoes Corpo"
    p[0] = p[1] + p[2]
    print(p[0])


#----------------------------------------------------
#---------------------- Declaracoes -----------------------
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

def p_Decl_int(p):
    "Decl : int DecIntList"
    p[0] = p[2]

def p_DecIntList(p):
    "DecIntList : DeclInt RestoDeclInt"
    p[0] = p[1] + p[2]
def p_RestoDeclInt(p):
    "RestoDeclInt : ',' DecIntList"
    p[0] = p[2]
def p_RestoDeclInt_vazio(p):
    "RestoDeclInt : "
    p[0] = ""

def p_DeclInt(p):
    "DeclInt : id"
    p[0] = "pushi 0\n"
    offset=p.parser.varsoffset
    p.parser.registers.update({p[1]: ('int',str(offset),1)})
    p.parser.varsoffset+=1

def p_DeclInt_attr(p):
    "DeclInt : id '=' num"
    p[0] = "pushi " + p[3] + "\n"
    offset=p.parser.varsoffset
    p.parser.registers.update({p[1]: ('int',str(offset),1)})
    p.parser.varsoffset+=1

def p_DeclInt_arrayInt(p):
    "DeclInt : id '[' num ']'"
    p[0] = "pushn " + p[3] + "\n"
    offset=p.parser.varsoffset
    p.parser.registers.update({p[1]: ('arrayInt',str(offset),p[3])})
    p.parser.varsoffset+=int(p[3])

#----------------------------------------------------
#---------------------- Corpo -----------------------
def p_Corpo(p):
    "Corpo : BEGIN Instrucoes END"
    p[0] = "start \n" + p[2] + "stop"

def p_Instrucoes(p):
    "Instrucoes : Instrucao Instrucoes"
    p[0] = p[1] + p[2]

def p_Instrucoes_vazio(p):
    "Instrucoes : "
    p[0] = ""


#----------------------------------------------------
#----------------------- Prints --------------------------
def p_Instrucao_print_str(p):
    "Instrucao : print str"             
    p[0] = "pushs " + p[2] + "\n" + "writes\n"

def p_Instrucao_print_exp(p):
    "Instrucao : print Exp"             
    p[0] = p[2] + "writei\n"



#---------------------- Atribs ----------------------
def p_Instrucao_attr_int_exp(p):
    "Instrucao : id '=' Exp"             #set exp
    (t,off,size)=p.parser.registers.get(p[1])
    p[0] = p[3] +"storeg " + off + "\n"

def p_Instrucao_attr_arrayint_exp(p):
    "Instrucao : id '[' Exp ']' '=' Exp"             #set exp lo array
    (t,off,size)=p.parser.registers.get(p[1])
    p[0] = "pushgp\n" + "pushi "+off+"\n" + "padd\n" + p[3] + p[6] + "storen\n"



#---------------------- Reads ----------------------
def p_Instrucao_read(p):
    "Instrucao : read"
    p[0] = "read\n"

def p_Instrucao_read_int(p):
    "Instrucao : read id"             
    (t,off,size)=p.parser.registers.get(p[2])
    p[0] = "read\n" + "atoi\n" + "storeg " + off +"\n"

def p_Instrucao_read_arrayInt(p):
    "Instrucao : read id '[' Exp ']'"             
    (t,off,size)=p.parser.registers.get(p[2])    
    p[0] = "pushgp\n" + "pushi "+off+"\n" + "padd\n" + p[4] + "read\n" + "atoi\n" + "storen\n"



#---------------------- Ifs ----------------------
def p_Instrucao_if(p):
    "Instrucao : if '(' Cond ')' Then Else"
    lid=p.parser.labelid
    p.parser.labelid+=1

    p[0] = p[3] + "jz else"+str(lid) + "\n" + p[5]+ "jump fimif"+str(lid) + "\n" + "else"+str(lid) + ":\n" + p[6] + "fimif"+str(lid) + ":\n"

def p_Instrucao_if_sem_else(p):
    "Instrucao : if '(' Cond ')' Then"
    p[0] = p[3] + "jz fimif1\n" + p[5] + "fimif1:\n"

def p_Then(p):
    "Then : '{' Instrucoes '}'"
    p[0] = p[2]
def p_Then_single(p):
    "Then : Instrucao"
    p[0] = p[1]

def p_Else(p):
    "Else : else '{' Instrucoes '}'"
    p[0] = p[3]
def p_Else_single(p):
    "Else : else Instrucao"
    p[0] = p[2]


def p_Cond(p):
    "Cond : Exp Oper Exp"
    p[0] = p[1] + p[3] + p[2]


def p_Oper(p):
    "Oper : '=' '=' "
    p[0] = "equal\n"




#---------------------- Repeat ----------------------


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
    (t,off,size)=p.parser.registers.get(p[1])
    p[0] = "pushg " + off +"\n"

def p_Fator_id_arr(p):
    "Fator : id '[' Exp ']'"
    (t,off,size)=p.parser.registers.get(p[1])
    p[0] = "pushgp\n" +"pushi "+off+"\n" +"padd\n" + p[3] + "loadn\n"




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
    Total+=Linha


# ToDo: read 
parser.success= True

P=parser.parse(Total)

if parser.success:
    print()

else:
    print("Frase inválida. Corrija e tente de novo...")




# maybe criar ID => id ou id[Exp]