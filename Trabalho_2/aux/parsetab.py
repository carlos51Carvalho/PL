
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "BEGIN END ENDVARS FUNCTION VARS else id if int num print read repeat str until whileMain : CondicaoCondicao : '(' Condicaobase ')'Condicaobase : CondCondicaobase : LCondd OperLogico CondLCondd : CondicaobaseCond : '(' Condicaobase ')'Cond : '!' '(' Condicaobase ')'Cond : Exp Oper ExpCond : '!' ExpCond : ExpOperLogico : '&' '&' OperLogico : '|' '|' Oper : '=' '=' Oper : '!' '=' Oper : '>' Oper : '<' Oper : '>' '=' Oper : '<' '=' Exp : Exp '+' TermoExp : Exp '-' TermoExp : TermoTermo : Termo '*' FatorTermo : Termo '/' FatorTermo : Termo '%' FatorTermo : FatorFator : '(' Exp ')'Fator : numFator : idFator : id '[' Exp ']'"
    
_lr_action_items = {'(':([0,3,4,8,17,20,22,23,24,27,28,29,30,31,32,36,37,40,43,44,45,46,],[3,4,4,20,4,4,40,40,40,-15,-16,40,40,40,40,-11,-12,40,-13,-14,-17,-18,]),'$end':([1,2,16,],[0,-1,-2,]),'!':([3,4,9,10,11,12,13,15,17,20,34,36,37,41,42,47,48,49,53,],[8,8,26,-21,-25,-27,-28,26,8,8,-26,-11,-12,-19,-20,-22,-23,-24,-29,]),'num':([3,4,8,17,20,22,23,24,27,28,29,30,31,32,36,37,40,43,44,45,46,],[12,12,12,12,12,12,12,12,-15,-16,12,12,12,12,-11,-12,12,-13,-14,-17,-18,]),'id':([3,4,8,17,20,22,23,24,27,28,29,30,31,32,36,37,40,43,44,45,46,],[13,13,13,13,13,13,13,13,-15,-16,13,13,13,13,-11,-12,13,-13,-14,-17,-18,]),')':([5,6,9,10,11,12,13,14,15,21,33,34,35,38,39,41,42,47,48,49,51,52,53,],[16,-3,-10,-21,-25,-27,-28,33,34,-9,-6,-26,-4,51,-8,-19,-20,-22,-23,-24,-7,34,-29,]),'&':([5,6,7,9,10,11,12,13,14,15,18,21,33,34,35,38,39,41,42,47,48,49,51,53,],[-5,-3,18,-10,-21,-25,-27,-28,-5,-10,36,-9,-6,-26,-4,-5,-8,-19,-20,-22,-23,-24,-7,-29,]),'|':([5,6,7,9,10,11,12,13,14,15,19,21,33,34,35,38,39,41,42,47,48,49,51,53,],[-5,-3,19,-10,-21,-25,-27,-28,-5,-10,37,-9,-6,-26,-4,-5,-8,-19,-20,-22,-23,-24,-7,-29,]),'+':([9,10,11,12,13,15,21,34,39,41,42,47,48,49,50,52,53,],[23,-21,-25,-27,-28,23,23,-26,23,-19,-20,-22,-23,-24,23,23,-29,]),'-':([9,10,11,12,13,15,21,34,39,41,42,47,48,49,50,52,53,],[24,-21,-25,-27,-28,24,24,-26,24,-19,-20,-22,-23,-24,24,24,-29,]),'=':([9,10,11,12,13,15,25,26,27,28,34,41,42,47,48,49,53,],[25,-21,-25,-27,-28,25,43,44,45,46,-26,-19,-20,-22,-23,-24,-29,]),'>':([9,10,11,12,13,15,34,41,42,47,48,49,53,],[27,-21,-25,-27,-28,27,-26,-19,-20,-22,-23,-24,-29,]),'<':([9,10,11,12,13,15,34,41,42,47,48,49,53,],[28,-21,-25,-27,-28,28,-26,-19,-20,-22,-23,-24,-29,]),']':([10,11,12,13,34,41,42,47,48,49,50,53,],[-21,-25,-27,-28,-26,-19,-20,-22,-23,-24,53,-29,]),'*':([10,11,12,13,34,41,42,47,48,49,53,],[29,-25,-27,-28,-26,29,29,-22,-23,-24,-29,]),'/':([10,11,12,13,34,41,42,47,48,49,53,],[30,-25,-27,-28,-26,30,30,-22,-23,-24,-29,]),'%':([10,11,12,13,34,41,42,47,48,49,53,],[31,-25,-27,-28,-26,31,31,-22,-23,-24,-29,]),'[':([13,],[32,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Main':([0,],[1,]),'Condicao':([0,],[2,]),'Condicaobase':([3,4,20,],[5,14,38,]),'Cond':([3,4,17,20,],[6,6,35,6,]),'LCondd':([3,4,20,],[7,7,7,]),'Exp':([3,4,8,17,20,22,32,40,],[9,15,21,9,15,39,50,52,]),'Termo':([3,4,8,17,20,22,23,24,32,40,],[10,10,10,10,10,10,41,42,10,10,]),'Fator':([3,4,8,17,20,22,23,24,29,30,31,32,40,],[11,11,11,11,11,11,11,11,47,48,49,11,11,]),'OperLogico':([7,],[17,]),'Oper':([9,15,],[22,22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Main","S'",1,None,None,None),
  ('Main -> Condicao','Main',1,'p_Main','cond_yacc.py',27),
  ('Condicao -> ( Condicaobase )','Condicao',3,'p_Condicao_init','cond_yacc.py',33),
  ('Condicaobase -> Cond','Condicaobase',1,'p_Condicao_single','cond_yacc.py',37),
  ('Condicaobase -> LCondd OperLogico Cond','Condicaobase',3,'p_Condicao_list','cond_yacc.py',41),
  ('LCondd -> Condicaobase','LCondd',1,'p_LCondd','cond_yacc.py',45),
  ('Cond -> ( Condicaobase )','Cond',3,'p_Conddd','cond_yacc.py',49),
  ('Cond -> ! ( Condicaobase )','Cond',4,'p_Conddd_not','cond_yacc.py',53),
  ('Cond -> Exp Oper Exp','Cond',3,'p_Cond','cond_yacc.py',60),
  ('Cond -> ! Exp','Cond',2,'p_Cond_not','cond_yacc.py',64),
  ('Cond -> Exp','Cond',1,'p_Cond_sem_oper','cond_yacc.py',68),
  ('OperLogico -> & &','OperLogico',2,'p_OperLogico_and','cond_yacc.py',75),
  ('OperLogico -> | |','OperLogico',2,'p_OperLogico_or','cond_yacc.py',79),
  ('Oper -> = =','Oper',2,'p_Oper_equal','cond_yacc.py',84),
  ('Oper -> ! =','Oper',2,'p_Oper_diff','cond_yacc.py',87),
  ('Oper -> >','Oper',1,'p_Oper_sup','cond_yacc.py',90),
  ('Oper -> <','Oper',1,'p_Oper_inf','cond_yacc.py',93),
  ('Oper -> > =','Oper',2,'p_Oper_supeq','cond_yacc.py',96),
  ('Oper -> < =','Oper',2,'p_Oper_infeq','cond_yacc.py',99),
  ('Exp -> Exp + Termo','Exp',3,'p_Exp_add','cond_yacc.py',107),
  ('Exp -> Exp - Termo','Exp',3,'p_Exp_sub','cond_yacc.py',111),
  ('Exp -> Termo','Exp',1,'p_Exp_termo','cond_yacc.py',115),
  ('Termo -> Termo * Fator','Termo',3,'p_Termo_mul','cond_yacc.py',121),
  ('Termo -> Termo / Fator','Termo',3,'p_Termo_div','cond_yacc.py',125),
  ('Termo -> Termo % Fator','Termo',3,'p_Termo_mod','cond_yacc.py',129),
  ('Termo -> Fator','Termo',1,'p_Termo_fator','cond_yacc.py',133),
  ('Fator -> ( Exp )','Fator',3,'p_Fator_exp','cond_yacc.py',139),
  ('Fator -> num','Fator',1,'p_Fator_num','cond_yacc.py',143),
  ('Fator -> id','Fator',1,'p_Fator_id','cond_yacc.py',147),
  ('Fator -> id [ Exp ]','Fator',4,'p_Fator_id_arr','cond_yacc.py',151),
]
