import re
#f = open("exemplo-utf8.bib", "r", encoding='utf-8')
f = open("ex109.bib", "r", encoding='utf-8')

json = open("c.json","w")

categoria=[]
autores = []



#HOW TO SPLI 
l = f.read()
categoria = re.split('@',l)

json.write("{\n\t\"referencias\":[")
for i in categoria:
	#print(i)
	tipo = re.match(r'(\w+)\{([^,]+)',i)
	
	if tipo:
		g=re.split('{',tipo.group())
		#print("tipo: ",g[0])
		json.write("\n\t{\n\t\t\"tipo\":\""+g[0]+"\",")
		
		#print("codigo: ",g[1])
		json.write("\n\t\t\"codigo\":\""+g[1]+"\",")

		info = re.findall(r'\b(\w+) *= *(\d*),|\b(\w+) *= *\"([^"]*)\",?|\b(\w+) *= *\{(.*)\},?',i)
		for (c,v,c1,v1,c2,v2) in info:
			#print(c,": ",v, " || ",c1,": ",v1," || ",c2,": ",v2)
			#print()
			if c:
				json.write("\n\t\t\"" + c +"\":\""+v+"\",")
			elif c1:
				if re.search(r'^\d*$',v1):
					json.write("\n\t\t\"" + c1 +"\":"+v1+",")
				else:
					json.write("\n\t\t\"" + c1 +"\":\""+v1+"\",")
			elif c2:
					if re.search(r'^\d*$',v2):
						json.write("\n\t\t\"" + c2 +"\":"+v2+",")
					else:
						json.write("\n\t\t\"" + c2 +"\":\""+v2+"\",")
			else:
				pass
		#print()
		#print()
		json.write("\n\t}")

	
	#print()
	#print()

json.write("\n\t]\n}\n")
