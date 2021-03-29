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
       
        if autor := re.search(r'\b(?i:author) *= *\{?\"?([^"}]*)',i):
            lsa=autor.group(1)
           

            lsa=re.sub(r'( |\n)+', r' ', lsa)
            autores = re.split(r' +and +',lsa)
           
            
            for aut in autores:
                if aux:=re.search(r'([\w\. ]+), ([\w\. ]+)',aut): 
                    aut = aux.group(2) +' ' +aux.group(1)
                    

                if aut in autoresOcorr:
                    autoresOcorr[aut.strip()].append(campo[2])
                else:
                    autoresOcorr[aut.strip()]=[campo[2]]
                    


for i in sorted(autoresOcorr):
    print(i + ": ",autoresOcorr[i])
    print()