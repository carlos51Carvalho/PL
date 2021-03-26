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

    autores2 = re.search(r'(\s*(?i:author)\s*=\s*[{"]+(.*)[}"]+)',i.strip())
    if autores2:
        a.append(autores2.group(2))

        for n in a:
            autores =re.split(r'((?i:and)\s+)+', n)
            if autores:
                #print(autores)
                
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

print(autoresOcorr)

#print(categoria[1], categoria.__len__(), '\n', categoria[165])


#print(categoria)
    #inserir os autores no dicionario e a sua determinada lista 
