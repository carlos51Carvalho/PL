import re
f = open("exemplo-utf8.bib", "r", encoding='utf-8')

categoria=[]




#HOW TO SPLI 
l = f.read()
categoria = re.split('@',l)


for i in categoria:
    campo = re.match(r'(\w+\{([\w\d]+))', i)
    if campo:
        print(campo[2])
    
    #autores = re.match(r'[ \t]*(?i:author) *= *(\{|\")([\w\. ]+[^\}]|\n)+(\}|"),', i.strip())
    autores2 = re.findall(r'(\s*(?i:author)\s*=\s*[{"](.*)["}],)',i.strip())
    if autores2:
        print(autores2[0][1])

    #inserir os autores no dicionario e a sua determinada lista 
    