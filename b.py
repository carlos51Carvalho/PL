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
                #if c:=re.search(r'(w+), (\w+)',c):
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


#separa dentro de cada categoria a chave única e coloca em campo e os autores separa tmb
for i in categoria:
    campo = re.match(r'(\w+\{([^,]+))', i)
    
    if campo:
        print(campo[2])

        if autor := re.search(r'\b(?i:author) *= *\{?\"?([^"}]*)',i):
            lsa=autor.group(1)
           

            lsa=re.sub(r'( |\n)+', r' ', lsa)
            autores = re.split(r' +and +',lsa)
           
            
            for aut in autores:
                if aux:=re.search(r'([\w\. ]+), ([\w\. ]+)',aut): 
                    aut = aux.group(2) +' ' +aux.group(1)
                    

                if aut in autoresOcorr:
                    autoresOcorr[aut].append(campo[2])
                else:
                    autoresOcorr[aut]=[campo[2]]
                    


        print()

print("\n\n\n\n\n")
for i in sorted(autoresOcorr):
    print(i + ": ",autoresOcorr[i])
    print()