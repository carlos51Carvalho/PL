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
            autores =re.split(r'((\s+(?i:and)\s+)+|,)', n)
            if autores:
                #print(autores)
                
                for c in autores:
                    if c.strip() in autoresOcorr:
                        autoresOcorr[c.strip()]+=1
                    else:
                        autoresOcorr[c.strip()]=1

print(autoresOcorr)

#print(categoria[1], categoria.__len__(), '\n', categoria[165])


#print(categoria)
    #inserir os autores no dicionario e a sua determinada lista 
