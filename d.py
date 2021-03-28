import re
from graphviz import Graph

f = open("exemplo-utf8.bib", "r", encoding='utf-8')

ex_aut= "J.J. Almeida"

categoria=[]
autoresRelat=[]

#HOW TO SPLI 
l = f.read()
categoria = re.split('@',l)


#separa dentro de cada categoria a chave única e coloca em campo e os autores separa tmb
for i in categoria:

    if autor := re.search(r'\b(?i:author) *= *\{?\"?([^"}]*)',i):
        lsa=autor.group(1)
           

        lsa=re.sub(r'( |\n)+', r' ', lsa)
        autores = re.split(r' +and +',lsa)
        

        if autores.__contains__(ex_aut):

            for aut in autores:
                if aux:=re.search(r'([\w\. ]+), ([\w\. ]+)',aut): 
                    aut = aux.group(2) +' ' +aux.group(1)
                
                if not aut.__eq__(ex_aut) and aut not in autoresRelat:
                    autoresRelat.append(aut)
                         
   
g = Graph(format='png')
g.node(0, ex_aut)
k=1

for i in autoresRelat:
    g.node(k, i)
    g.edge(0, k, constraint='true')
    k+=1

g.render('test-output/doutput', view=True)
print(autoresRelat)


#nao consigo visualizar o grafico 