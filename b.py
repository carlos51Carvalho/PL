'''
import re
f = open("exemplo-utf8.bib", "r", encoding='utf-8')

categoria=[]
autoresOcorr={}

#HOW TO SPLI 
l = f.read()
categoria = re.split('@',l)
a=[]

#separa dentro de cada categoria a chave única e coloca em campo e os autores separa tmb
for i in categoria:
    campo = re.match(r'(\w+\{([\w\d]+))', i)
    #if campo:
    #    print(campo[2])

    #                           \b(\w+)[ ]*=[ ]*\{?\"?([^"},]*)
    autores2 = re.search(r'(\s*(?i:author)\s*=\s*[{"]+(.*)[}"]+)',i.strip())
    if autores2:
        a.append(autores2.group(2))



        autores =re.split(r'((?i:and)\s+)+', a)
        if autores:
            print(autores)
            
            for c in autores:
                
                cs = c.strip()
                #if re.search(r'(w+), (\w+)',c):
                    #not working don't know why 
                 #   cs = (c.group(2) + c.group(1)).strip()
                 #   print(cs)

                if cs in autoresOcorr:
                    autoresOcorr[cs]+=1
                else:
                    autoresOcorr[cs]=1
'''

import re
f = open("exemplo-utf8.bib", "r", encoding='utf-8')

categoria=[]
autoresOcorr={}

#HOW TO SPLI 
l = f.read()
categoria = re.split('@',l)
a=[]

#separa dentro de cada categoria a chave única e coloca em campo e os autores separa tmb
for i in categoria:
    campo = re.match(r'(\w+\{([\w\d]+))', i)
    #print(campo)
    
    if campo:
        print(campo[2])

        if autor := re.search(r'\b(?i:author) *= *\{?\"?([^"}]*)',i):
            lsa=autor.group(1)
            #print(lsa)

            lsa=re.sub(r'( |\n)+', r' ', lsa)
            aut = re.split(r' +and +',lsa)
            print(aut)

            #perguntar ao stor o que é para fazer agr

        print()