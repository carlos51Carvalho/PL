import re
f = open("exemplo-utf8.bib", "r", encoding='utf-8')

json = open("c.json","w")

categoria=[]
autores = []



#HOW TO SPLI 
l = f.read()
categoria = re.split('@',l)
first=True

json.write("{\n\t\"referencias\":[")
for i in categoria:
	print(i)
	tipo = re.match(r'(\w+)\{([A-Z1-9]+)',i)
	
	if tipo:
		g=re.split('{',tipo.group())
		print("tipo: ",g[0])
		json.write("\n\t{\n\t\t\"tipo\":\""+g[0]+"\",")
		
		print("codigo: ",g[1])
		json.write("\n\t\t\"codigo\":\""+g[1]+"\",")

		info = re.findall(r'\b(\w+)[ ]*=[ ]*\{?\"?([\w ]*)',i)
		for (c,v) in info:
			print(c,": ",v)
			json.write("\n\t\t\"" + c +"\":\""+v+"\",")
	
		json.write("\n\t}")

	
	print()
	print()

json.write("\n\t]\n}\n")
