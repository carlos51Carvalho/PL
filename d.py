import re
from graphviz import Graph


filepath = input("Insira o filepath\n")

try:
    f = open(filepath, "r", encoding='utf-8')
    ex_aut = input("Insira o nome do autor a gerar o gráfio\n")

    categoria=[]
    autoresRelat=[]

    #HOW TO SPLI 
    l = f.read()
    categoria = re.split('@',l)


    #separa dentro de cada categoria a chave única e coloca em campo e os autores separa tmb
    for i in categoria:

        if autor := re.search(r'\b(?i:author) *= *\"([^"]*)\",?|\b(?i:author) *= *\{(.*)\},?',i):

            lsa=autor.group(1)
            if not(lsa):
                lsa=autor.group(2)
     

            lsa=re.sub(r'( |\n)+', r' ', lsa)
            autores = re.split(r' +and +',lsa)
            

            if autores.__contains__(ex_aut):

                for aut in autores:
                    if aux:=re.search(r'([\w\. ]+), ([\w\. ]+)',aut): 
                        aut = aux.group(2) +' ' +aux.group(1)
                    
                    if not aut.__eq__(ex_aut) and aut not in autoresRelat:
                        autoresRelat.append(aut)
                             
      
    g = Graph(format='png')
    g.node(str(0), ex_aut)
    k=1

    for i in autoresRelat:
        g.node(str(k), i)
        g.edge(str(0), str(k), constraint='true')
        k+=1

    g.render('graphviz/doutput', view=True)

    print(autoresRelat)

except Exception as e:
    print(e)