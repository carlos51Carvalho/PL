import re 

f = open("exemplo-utf8.bib", "r", encoding='utf-8')

categoria=[]

for linha in f:

  campos = re.findall(r'\@\w+',linha)
  if campos:
    categoria.append(campos)  

print(categoria)





