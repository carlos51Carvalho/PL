import re

filepath = input("Insira o filepath\n")
#print(filepath)
try:
	f = open(filepath, "r", encoding='utf-8')

	json = open("c.json","w")

	categoria=[]
	autores = []



	#HOW TO SPLI 
	l = f.read()
	categoria = re.split('@',l)
	

	json.write("{\n\t\"referencias\":[")
	for i in categoria:
		
		tipo = re.match(r'(\w+)\{([^,]+)',i)
		
		if tipo:
			g=re.split('{',tipo.group())
			
			json.write("\n\t{\n\t\t\"tipo\":\""+g[0]+"\",")
			
			
			json.write("\n\t\t\"codigo\":\""+g[1]+"\",")
			
			info = re.findall(r'\b(\w+) *= *(\d*),|\b(\w+) *= *\"([^"]*)\",?|\b(\w+) *= *\{([^\}]*(?:\{[^\}]*\})+[^\}]*)\},?|\b(\w+) *= *\{([^\}]*[^\}]*)\},?',i)

			for (c,v,c1,v1,c2,v2,c3,v3) in info:
				#print(c,": ",v, " || ",c1,": ",v1," || ",c2,": ",v2," || ",c3,": ",v3)
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
				elif c3:
					json.write("\n\t\t\"" + c3 +"\":\""+v3+"\",")
				else:
					pass

			json.write("\n\t}")


	json.write("\n\t]\n}\n")

except Exception as e:
    print(e)