import re 

<<<<<<< HEAD
def exA():
	f = open("exemplo-utf8.bib", "r", encoding='utf-8')

	categoria={}

	for linha in f:
		#talvez nao seja preciso ser um findall
	  campos = re.findall(r'\@(\w+)',linha)
	  for c in campos:
	  		#print(c)
	  		caux=c.lower()
	  		if caux in categoria:
	  			categoria[caux]+=1
	  		else:
	  			categoria[caux]=1
	  #if campos:
	  #  categoria.append(campos.group(1))  


	for i in sorted(categoria):
		print(i,categoria[i])

def exB():
	f = open("exemplo-utf8.bib", "r", encoding='utf-8')
	
	categorias=[]
	

	
	for linha in f:
		if res := re.search(r'\@.+',linha):
			print(res.group())
		elif res := re.search(r'((\w+)(.|\n)*?,?)',linha):
			print(res)
		elif res := re.search(r'(\n)',linha):
			pass
		else: print(linha)

		print()
		
	'''
	#r'\@(\w+)\{((.|\n)+)?('
	autores={}
	conteudo = f.read()
	#print(conteudo)
	#talvez nao seja preciso ser um findall
	campos = re.findall(r'(\@\w*\{\w*,)|([aA][uU][tT][hH][oO][rR]\b)',conteudo)
	for c in campos:
		print(c)
	  #if campos:
	  #  categoria.append(campos.group(1))  
	'''



if __name__ == '__main__':
	#print("Main")
	exB()
