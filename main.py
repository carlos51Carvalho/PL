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
=======
f = open("exemplo-utf8.bib", "r", encoding='utf-8')

categoria=[]

#for linha in f:

  #campos = re.findall(r'\@\w+',linha)
  #if campos:
  #  categoria.append(campos)  

#print(categoria)


#HOW TO SPLI 
#l = f.read()
#categoria = re.split('\@',l,)
#print(categoria[1], categoria[2])

>>>>>>> 7f1c19524a1146907e87d4d4c784608520cf2e5d


