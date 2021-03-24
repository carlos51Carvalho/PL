import re
f = open("exemplo-utf8.bib", "r", encoding='utf-8')

categoria=[]
autores = []



#HOW TO SPLI 
l = f.read()
categoria = re.split('@',l)


for i in categoria:
    campo = re.match(r'(\w+\{([\w\d]+))', i)
    #if campo:
    #    print(campo[2])
    
    #autores = re.match(r'[ \t]*(?i:author) *= *(\{|\")([\w\. ]+[^\}]|\n)+(\}|"),', i.strip())
    autores2 = re.findall(r'(\s*(?i:author)\s*=\s*[{"](.*)["}],)',i.strip())
    a = autores2[0][1]
    if autores2:
       autores = re.split(r'(?i:and)', a)


print(autores)


#for i in autores2[0][1]:
#    autores = re.split(r'(?i:and)', i)
#   print(autores)    


    #inserir os autores no dicionario e a sua determinada lista 
