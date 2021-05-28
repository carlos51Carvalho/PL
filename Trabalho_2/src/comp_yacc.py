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


#----------------------------------------------------
#---------------------- Declaracoes -----------------------
def p_Declaracoes(p):
    "Declaracoes : VARS Decls ENDVARS"
    p[0] = p[2]

def p_Declaracoes_vazio(p):
    "Declaracoes : "
    p[0] = ""

def p_Decls(p):
    "Decls : Decls Decl"
    p[0] = p[1] + p[2]

def p_Decls_vazio(p):
    "Decls : "
    p[0] = ""

def p_Decl_int(p):
    "Decl : int DecIntList"
    p[0] = p[2]



def p_DecIntList(p):
    "DecIntList : DecIntList ',' DeclInt"
    p[0] = p[1] + p[3]

def p_DecIntList_single(p):
    "DecIntList : DeclInt"
    p[0] = p[1]



def p_DeclInt(p):
    "DeclInt : id"
    v=p.parser.registers.get(p[1])
    if v==None:
        p[0] = "pushi 0\n"
        offset=p.parser.varsoffset
        p.parser.registers.update({p[1]: ('int',str(offset),1)})
        p.parser.varsoffset+=1
    else:
        print("A variavel "+ p[1] +" foi declarada mais que uma vez")
        p[0]=""
        parser.success = False
        parser.erros+=1


def p_DeclInt_attr(p):
    "DeclInt : id '=' num"
    v=p.parser.registers.get(p[1])
    if v==None:
        p[0] = "pushi " + p[3] + "\n"
        offset=p.parser.varsoffset
        p.parser.registers.update({p[1]: ('int',str(offset),1)})
        p.parser.varsoffset+=1
    else:
        print("A variavel "+ p[1] +" foi declarada mais que uma vez")
        p[0]=""
        parser.success = False
        parser.erros+=1


def p_DeclInt_arrayInt(p):
    "DeclInt : id '[' num ']'"
    v=p.parser.registers.get(p[1])
    if v==None:
        p[0] = "pushn " + p[3] + "\n"
        offset=p.parser.varsoffset
        p.parser.registers.update({p[1]: ('arrayInt',str(offset),p[3])})
        p.parser.varsoffset+=int(p[3])
    else:
        print("A variavel "+ p[1] +" foi declarada mais que uma vez")
        p[0]=""
        parser.success = False
        parser.erros+=1


def p_DeclInt_array2Int(p):
    "DeclInt : id '[' num ']' '[' num ']'"
    v=p.parser.registers.get(p[1])
    if v==None:
        s=int(p[3]) * int(p[6])
        p[0] = "pushn " + str(s) + "\n"
        offset=p.parser.varsoffset
        p.parser.registers.update({p[1]: ('array2Int',str(offset),int(p[3]), int(p[6]))})
        p.parser.varsoffset+=s
    else:
        print("A variavel "+ p[1] +" foi declarada mais que uma vez")
        p[0]=""
        parser.success = False
        parser.erros+=1


#----------------------------------------------------
#---------------------- Corpo -----------------------
def p_Corpo(p):
    "Corpo : BEGIN Instrucoes END"
    p[0] = "start \n" + p[2] + "stop"

def p_Corpo_com_functios(p):
    "Corpo : Funcoes BEGIN Instrucoes END"
    p[0] = "start\njump INICIO\n" + p[1] + "INICIO:\n" +p[3]+ "stop"




#----------------------------------------------------
#---------------------- Funcoes -----------------------
def p_Funcoes(p):
    "Funcoes : Funcoes Funcao"
    p[0] = p[1] + p[2]

def p_Funcoes_vazio(p):
    "Funcoes : Funcao"
    p[0] = p[1]


def p_Funcao(p):
    "Funcao : FuncaoHeader FuncaoCorpo"
    p[0] = p[1] + p[2]

def p_FuncaoHeader(p):
    "FuncaoHeader : FUNCTION id"
    v=p.parser.funcoes.get(p[2])
    if v==None:
        p[0] = p[2] + ":\n"
        p.parser.funcoes[p[2]]='Funcao'
    else:
        print("A funcao "+ p[2] +" foi declarada mais que uma vez")
        p[0]=""
        parser.success = False
        parser.erros+=1


def p_FuncaoCorpo(p):
    "FuncaoCorpo : BEGIN Instrucoes END"
    p[0] = p[2] + "return\n"

#def p_FuncaoCorpoRet(p):
#    "FuncaoCorpo : BEGIN Instrucoes return id END"
#    (t,off,size)=p.parser.registers.get(p[4])
#    p[0] = p[2] + "pushg " +off +"\n" + "return\n"







#----------------------------------------------------
#---------------------- Intrucoes -----------------------

def p_Instrucoes(p):
    "Instrucoes : Instrucoes Instrucao"
    p[0] = p[1] + p[2]

def p_Instrucoes_vazio(p):
    "Instrucoes : "
    p[0] = ""


#----------------------------------------------------
#------------------Coments---------------------------
	#def p_Instrucao_comment(p):
	#    "Instrucao : IComment comment FComment"             
	#    p[0] = "//" + p[2] + "\n"
	#def p_IComment(p):
	#    "IComment : '/' '*'"             
	#    p[0] = ""
	#def p_FComment(p):
	#    "FComment : '*' '/'"             
	#    p[0] = ""


#-------------chamada da funcao------------
def p_Instrucao_call(p):
    "Instrucao : id '(' ')'"
    v=p.parser.funcoes.get(p[1])
    if v==None:        
        print("A funcao "+ p[1] +" não foi declarada antes de ser chamada")
        p[0]=""
        parser.success = False
        parser.erros+=1

    else:
        p[0] = "pusha " + p[1] + "\n" + "call\n"

#def p_Instrucao_call_retorno(p):
	#    "Instrucao : id '=' id '(' ')'"  
	#    (t,off,size)=p.parser.registers.get(p[1])
	#    p[0] = "pusha " + p[3] + "\n" + "call\n"
	#    p[0]+= "storeg " + off + "\n"           

#def p_Instrucao_call_retornoarray(p):
	#    "Instrucao : id '[' num ']' '=' id '(' ')'"  
	#    (t,off,size)=p.parser.registers.get(p[1])
	#    p[0] = "pushgp\n" + "pushi "+off+"\n" + "padd\n" + p[3] 
	#    p[0]+= "pusha " + p[6] + "\n" + "call\n"
	#    p[0]+= "storen\n"


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
    v=p.parser.registers.get(p[1])
    if v==None:
        print("A variavel "+ p[1] +" não está definida")
        p[0]=""
        parser.success = False
        parser.erros+=1
    else:
        if v[0]!='int':
            print("A variavel "+ p[1] +" é do tipo "+v[0]+", não pode ser atribuida como inteira")
            p[0]=""
            parser.success = False
            parser.erros+=1
        else: 
            (t,off,size)=v
            p[0] = p[3] +"storeg " + off + "\n"


def p_Instrucao_attr_int_exp_com_oper_antes_do_igual(p):
    "Instrucao : id Op '=' Exp"             
    #(t,off,size)=p.parser.registers.get(p[1])
    #p[0] = "pushg " + off +"\n"
    #p[0]+= p[4] + p[2] +"storeg " + off + "\n"
    
    v=p.parser.registers.get(p[1])
    if v==None:
        print("A variavel "+ p[1] +" não está definida")
        p[0]=""
        parser.success = False
        parser.erros+=1
    else:
        if v[0]!='int':
            print("A variavel "+ p[1] +" é do tipo "+v[0]+", não pode ser atribuida como inteira")
            p[0]=""
            parser.success = False
            parser.erros+=1
        else:
            (t,off,size)=v
            p[0] = "pushg " + off +"\n"
            p[0]+= p[4] + p[2] +"storeg " + off + "\n"


def p_Op_add(p):
    "Op : '+'"
    p[0] = "add\n"
def p_Op_sub(p):
    "Op : '-'"
    p[0] = "sub\n"
def p_Op_mul(p):
    "Op : '*'"
    p[0] = "mul\n"
def p_Op_div(p):
    "Op : '/'"
    p[0] = "div\n"
def p_Op_mod(p):
    "Op : '%'"
    p[0] = "mod\n"

def p_Instrucao_attr_int_sub_sub(p):
    "Instrucao : id '-' '-'"             
    #(t,off,size)=p.parser.registers.get(p[1])
    #p[0] = "pushg " + off +"\n"
    #p[0]+= "pushi 1\n" + "sub\n" +"storeg " + off + "\n"

    v=p.parser.registers.get(p[1])
    if v==None:
        print("A variavel "+ p[1] +" não está definida")
        p[0]=""
        parser.success = False
        parser.erros+=1
    else:
        if v[0]!='int':
            print("A variavel "+ p[1] +" é do tipo "+v[0]+", não pode ser atribuida como int")
            p[0]=""
            parser.success = False
            parser.erros+=1
        else:
            (t,off,size)=v
            p[0] = "pushg " + off +"\n"
            p[0]+= "pushi 1\n" + "sub\n" +"storeg " + off + "\n"



def p_Instrucao_attr_int_add_add(p):
    "Instrucao : id '+' '+'"             
    #(t,off,size)=p.parser.registers.get(p[1])
    #p[0] = "pushg " + off +"\n"
    #p[0]+= "pushi 1\n" + "add\n" +"storeg " + off + "\n"

    v=p.parser.registers.get(p[1])
    if v==None:
        print("A variavel "+ p[1] +" não está definida")
        p[0]=""
        parser.success = False
        parser.erros+=1
    else:
        if v[0]!='int':
            print("A variavel "+ p[1] +" é do tipo "+v[0]+", não pode ser atribuida como int")
            p[0]=""
            parser.success = False
            parser.erros+=1
        else:
            (t,off,size)=v
            p[0] = "pushg " + off +"\n"
            p[0]+= "pushi 1\n" + "add\n" +"storeg " + off + "\n"




def p_Instrucao_attr_arrayint_exp(p):
    "Instrucao : id '[' Exp ']' '=' Exp"             #set exp lo array
    #(t,off,size)=p.parser.registers.get(p[1])
    #p[0] = "pushgp\n" + "pushi "+off+"\n" + "padd\n" + p[3] + p[6] + "storen\n"

    v=p.parser.registers.get(p[1])
    if v==None:
        print("A variavel "+ p[1] +" não está definida")
        p[0]=""
        parser.success = False
        parser.erros+=1
    else:
        if v[0]!='arrayInt':
            print("A variavel "+ p[1] +" é do tipo "+v[0]+", não pode ser atribuida como arrayInt")
            p[0]=""
            parser.success = False
            parser.erros+=1
        else:
            (t,off,size)=v
            p[0] = "pushgp\n" + "pushi "+off+"\n" + "padd\n" + p[3] 
            p[0]+= p[6] + "storen\n"


def p_Instrucao_attr_arrayint_exp_add_add(p):
    "Instrucao : id '[' Exp ']' '+' '+'"           
    v=p.parser.registers.get(p[1])
    if v==None:
        print("A variavel "+ p[1] +" não está definida, em "+p)
        p[0]=""
    else:
        if v[0]!='arrayInt':
            print("A variavel "+ p[1] +" é do tipo "+v[0]+", não pode ser atribuida como arrayInt")
            p[0]=""
            parser.success = False
            parser.erros+=1
        else:
            (t,off,size)=v
            p[0] = "pushgp\n" + "pushi "+off+"\n" + "padd\n" + p[3]                 #1ªparte do store
            p[0]+= "pushgp\n" + "pushi "+off+"\n" + "padd\n" + p[3] + "loadn\n"     #load do valor
            p[0]+= "pushi 1\n"+ "add\n"                                             #adicao de 1
            p[0]+= "storen\n"                                                #fim do store


def p_Instrucao_attr_arrayint_exp_sub_sub(p):
    "Instrucao : id '[' Exp ']' '-' '-'"           
    v=p.parser.registers.get(p[1])
    if v==None:
        print("A variavel "+ p[1] +" não está definida, em "+p)
        p[0]=""
    else:
        if v[0]!='arrayInt':
            print("A variavel "+ p[1] +" é do tipo "+v[0]+", não pode ser atribuida como arrayInt")
            p[0]=""
            parser.success = False
            parser.erros+=1
        else:
            (t,off,size)=v
            p[0] = "pushgp\n" + "pushi "+off+"\n" + "padd\n" + p[3]                 #1ªparte do store
            p[0]+= "pushgp\n" + "pushi "+off+"\n" + "padd\n" + p[3] + "loadn\n"     #load do valor
            p[0]+= "pushi 1\n"+ "sub\n"                                             #subtracao de 1
            p[0]+= "storen\n"                                                #fim do store



def p_Instrucao_attr_array2int_exp(p):
    "Instrucao : id '[' Exp ']' '[' Exp ']' '=' Exp"             #set exp lo array
    #(t,off,size)=p.parser.registers.get(p[1])
    #p[0] = "pushgp\n" + "pushi "+off+"\n" + "padd\n" + p[3] + p[6] + "storen\n"

    v=p.parser.registers.get(p[1])
    if v==None:
        print("A variavel "+ p[1] +" não está definida")
        p[0]=""
        parser.success = False
        parser.erros+=1
    else:
        if v[0]!='array2Int':
            print("A variavel "+ p[1] +" é do tipo "+v[0]+", não pode ser atribuida como array2Int")
            p[0]=""
            parser.success = False
            parser.erros+=1
        else:
            (t,off,size1,size2)=v
            p[0] = "pushgp\n" + "pushi "+off+"\n" + "padd\n" 
            p[0]+= p[3] + "pushi "+str(size2)+"\n" + "mul\n"+ p[6] + "add\n"
            p[0]+= p[9] + "storen\n"


def p_Instrucao_attr_array2int_exp_sub_sub(p):
    "Instrucao : id '[' Exp ']' '[' Exp ']' '-' '-'"           
    v=p.parser.registers.get(p[1])
    if v==None:
        print("A variavel "+ p[1] +" não está definida, em "+p)
        p[0]=""
    else:
        if v[0]!='array2Int':
            print("A variavel "+ p[1] +" é do tipo "+v[0]+", não pode ser atribuida como array2Int")
            p[0]=""
            parser.success = False
            parser.erros+=1
        else:
            (t,off,size1,size2)=v
            p[0] = "pushgp\n" + "pushi "+off+"\n" + "padd\n" 
            p[0]+= p[3] + "pushi "+str(size2)+"\n" + "mul\n"+ p[6] + "add\n"
            
            p[0]+= "pushgp\n" + "pushi "+off+"\n" + "padd\n" 
            p[0]+= p[3] + "pushi "+str(size2)+"\n" + "mul\n"+ p[6] + "add\n"
            p[0]+= "loadn\n"
            p[0]+= "pushi 1\n"+ "sub\n"     

            p[0]+= "storen\n"


def p_Instrucao_attr_array2int_exp_add_add(p):
    "Instrucao : id '[' Exp ']' '[' Exp ']' '+' '+'"           
    v=p.parser.registers.get(p[1])
    if v==None:
        print("A variavel "+ p[1] +" não está definida, em "+p)
        p[0]=""
    else:
        if v[0]!='array2Int':
            print("A variavel "+ p[1] +" é do tipo "+v[0]+", não pode ser atribuida como array2Int")
            p[0]=""
            parser.success = False
            parser.erros+=1
        else:
            (t,off,size1,size2)=v
            p[0] = "pushgp\n" + "pushi "+off+"\n" + "padd\n" 
            p[0]+= p[3] + "pushi "+str(size2)+"\n" + "mul\n"+ p[6] + "add\n"
            
            p[0]+= "pushgp\n" + "pushi "+off+"\n" + "padd\n" 
            p[0]+= p[3] + "pushi "+str(size2)+"\n" + "mul\n"+ p[6] + "add\n"
            p[0]+= "loadn\n"
            p[0]+= "pushi 1\n"+ "add\n"     

            p[0]+= "storen\n"


#---------------------- Reads ----------------------

def p_Instrucao_read_int(p):
    "Instrucao : read id"             
    #(t,off,size)=p.parser.registers.get(p[2])
    #p[0] = "read\n" + "atoi\n" + "storeg " + off +"\n"
    v=p.parser.registers.get(p[2])
    if v==None:
        print("A variavel "+ p[2] +" não está definida")
        p[0]=""
        parser.success = False
        parser.erros+=1
    else:
        if v[0]!='int':
            print("A variavel "+ p[2] +" é do tipo "+v[0]+", não pode ser lida como um int")
            p[0]=""
            parser.success = False
            parser.erros+=1
        else:
            (t,off,size)=v
            p[0] = "read\n" + "atoi\n" + "storeg " + off +"\n"



def p_Instrucao_read_arrayInt(p):
    "Instrucao : read id '[' Exp ']'"             
    #(t,off,size)=p.parser.registers.get(p[2])    
    #p[0] = "pushgp\n" + "pushi "+off+"\n" + "padd\n" + p[4] + "read\n" + "atoi\n" + "storen\n"

    v=p.parser.registers.get(p[2])
    if v==None:
        print("A variavel "+ p[2] +" não está definida")
        p[0]=""
        parser.success = False
        parser.erros+=1
    else:
        if v[0]!='arrayInt':
            print("A variavel "+ p[2] +" é do tipo "+v[0]+", não pode ser lida como um arrayInt")
            p[0]=""
            parser.success = False
            parser.erros+=1
        else:
            (t,off,size)=v
            p[0] = "pushgp\n" + "pushi "+off+"\n" + "padd\n" + p[4] 
            p[0]+= "read\n" + "atoi\n" + "storen\n"


def p_Instrucao_read_array2int(p):
    "Instrucao : read id '[' Exp ']' '[' Exp ']'"         
    v=p.parser.registers.get(p[2])
    if v==None:
        print("A variavel "+ p[2] +" não está definida")
        p[0]=""
        parser.success = False
        parser.erros+=1
    else:
        if v[0]!='array2Int':
            print("A variavel "+ p[2] +" é do tipo "+v[0]+", não pode ser atribuida como arrayInt")
            p[0]=""
            parser.success = False
            parser.erros+=1
        else:
            (t,off,size1,size2)=v
            p[0] = "pushgp\n" + "pushi "+off+"\n" + "padd\n" 
            p[0]+= p[4] + "pushi "+str(size2)+"\n" + "mul\n"+ p[7] + "add\n"
            p[0]+= "read\n" + "atoi\n" + "storen\n"

#---------------------- Ifs ----------------------
def p_Instrucao_if(p):
    "Instrucao : if Condicao Then Else"
    lid=p.parser.labelid
    p.parser.labelid+=1
    p[0] = p[2] + "jz else"+str(lid) + "\n" + p[3]+ "jump fimif"+str(lid) + "\n" + "else"+str(lid) + ":\n" + p[4] + "fimif"+str(lid) + ":\n"

def p_Instrucao_if_sem_else(p):
    "Instrucao : if Condicao Then"
    lid=p.parser.labelid
    p.parser.labelid+=1
    p[0] = p[2] + "jz fimif" +str(lid) + "\n" + p[3] + "fimif" + str(lid) + ":\n"

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




def p_Condicao_init(p):
    "Condicao : '(' Cond ')'"
    p[0] = p[2]

def p_Cond(p):
    "Cond : Cond '|' '|' Cond2"
    p[0] = p[1] + p[4] + "add\npushi 0\nsup\n"

def p_Cond_cond2(p):
    "Cond : Cond2"
    p[0] = p[1]

def p_Cond2(p):
    "Cond2 : Cond2 '&' '&' Cond3" 
    p[0] = p[1] + p[4] + "mul\n"

def p_Cond2_cond3(p):
    "Cond2 : Cond3" 
    p[0] = p[1]

def p_Cond3_notCond(p):
    "Cond3 : '!' Cond" 
    p[0] = p[2] + 'not\n'

def p_Cond3_parcond(p):
    "Cond3 : '(' Cond ')'" 
    p[0] = p[2]

def p_Cond3_ExpRel(p):
    "Cond3 : ExpRel" 
    p[0] = p[1]



def p_ExpRel(p):
    "ExpRel : Exp Oper Exp"
    p[0] = p[1] + p[3] + p[2]

def p_ExpRel_sem_oper(p):
    "ExpRel : Exp"
    p[0] = p[1]



def p_Oper_equal(p):
    "Oper : '=' '=' "
    p[0] = "equal\n"
def p_Oper_diff(p):
    "Oper : '<' '>' "
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




#---------------------- Repeat ----------------------
	#def p_Instrucao_repeat_num(p):
	#    "Instrucao : repeat '(' num ')' CorpoRepeat"
	#    lid=p.parser.labelid
	#    p.parser.labelid+=1

	#def p_Instrucao_repeat_id(p):
	#    "Instrucao : repeat '(' id ')' CorpoRepeat"
	#    lid=p.parser.labelid
	#    p.parser.labelid+=1

	#def p_CorpoRepeat(p):
	#    "CorpoRepeat : '{' Instrucoes '}' "
	#    p[0]=p[2]

	#def p_CorpoRepeat_single(p):
	#    "CorpoRepeat : Instrucao"
	#    p[0]=p[1]


#----------------------Repeat-until------------------------
def p_Instrucao_repeatuntil(p):
    "Instrucao : repeat CorpoCiclo until Condicao "
    lid=p.parser.labelid
    p.parser.labelid+=1
    p[0] = "ciclo" + str(lid) +":\n"
    p[0]+= p[2]
    p[0]+= p[4]
    p[0]+= "jz ciclo" + str(lid) +"\n"

def p_CorpoCiclo(p):
    "CorpoCiclo : '{' Instrucoes '}' "
    p[0]=p[2]

def p_CorpoCiclo_single(p):
    "CorpoCiclo : Instrucao"
    p[0]=p[1]


#----------------------While-do------------------------
def p_Instrucao_while(p):
    "Instrucao : while Condicao CorpoCiclo"
    lid=p.parser.labelid
    p.parser.labelid+=1
    p[0] = "ciclo" + str(lid) +":\n"
    p[0]+= p[2]
    p[0]+= "jz fimciclo" + str(lid) +"\n"
    p[0]+= p[3]
    p[0]+= "jump ciclo" + str(lid) +"\n"
    p[0]+= "fimciclo" + str(lid) +":\n"




#----------------------for-do------------------------
	#def p_Instrucao_for(p):
	#    "Instrucao : for Condicao CorpoCiclo"





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
    #(t,off,size)=p.parser.registers.get(p[1])
    #p[0] = "pushg " + off +"\n"
    
    v=p.parser.registers.get(p[1])
    if v==None:
        print("A variavel "+ p[1] +" não está definida")
        p[0]=""
        parser.success = False
        parser.erros+=1
    else:
        if v[0]!='int':
            print("A variavel "+ p[1] +" é do tipo "+v[0]+", não pode ser usada como um int")
            p[0]=""
            parser.success = False
            parser.erros+=1
        else:
            (t,off,size)=v
            p[0] = "pushg " + off +"\n"



def p_Fator_id_arr(p):
    "Fator : id '[' Exp ']'"
    #(t,off,size)=p.parser.registers.get(p[1])
    #p[0] = "pushgp\n" +"pushi "+off+"\n" +"padd\n" + p[3] + "loadn\n"
    
    v=p.parser.registers.get(p[1])
    if v==None:
        print("A variavel "+ p[1] +" não está definida")
        p[0]=""
        parser.success = False
        parser.erros+=1
    else:
        t=v[0]
        if t!='arrayInt':
            print("A variavel "+ p[1] +" é do tipo "+v[0]+", não pode ser usada como um arrayInt")
            p[0]=""
            parser.success = False
            parser.erros+=1
        else:
            (t,off,size)=v
            p[0] = "pushgp\n" +"pushi "+off+"\n" +"padd\n" + p[3] + "loadn\n"
 
def p_Fator_id_arr2(p):
    "Fator : id '[' Exp ']' '[' Exp ']'"         
    v=p.parser.registers.get(p[1])
    if v==None:
        print("A variavel "+ p[1] +" não está definida")
        p[0]=""
        parser.success = False
        parser.erros+=1
    else:
        if v[0]!='array2Int':
            print("A variavel "+ p[1] +" é do tipo "+v[0]+", não pode ser atribuida como arrayInt")
            p[0]=""
            parser.success = False
            parser.erros+=1
        else:
            (t,off,size1,size2)=v
            p[0] = "pushgp\n" + "pushi "+off+"\n" + "padd\n" 
            p[0]+= p[3] + "pushi "+str(size2)+"\n" + "mul\n"+ p[6] + "add\n"
            p[0]+= "loadn\n"




def p_error(p):         #rotina de erros para tokens
    print("Erro sintático no input: ",p)
    parser.success = False


# build the parser
parser = yacc.yacc()

# Creating the model
parser.registers={}     # Registers-> {Nome da variavel: (tipo, offset, tamanho)}
parser.varsoffset=0
parser.labelid=1
parser.funcoes={} 
parser.erros=0


# read input by line and append
import sys
Total=""
for Linha in sys.stdin:
    Total+=Linha



parser.success= True

P=parser.parse(Total)

if parser.success:
    print(P)

else:
    print()
    print("O programa tem "+str(parser.erros)+" erro(s). Corrija e tente de novo...")

