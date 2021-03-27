import re 


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


	html = open("a.html","w")
	html.write('''<!DOCTYPE html>
<html>
    <head>
        <title>Relatório</title>
        <meta charset="UTF-8"/>
    </head>
    <body>
    	<h1>Categorias</h1>
    	<ol>
''')

	for i in sorted(categoria):
		html.write("    		<li>" +i + ": "+ str(categoria[i]) + "</li>\n")		
		print(i,categoria[i])

	html.write('''    	</ol>
	</body>
</html>\n''')

if __name__ == '__main__':
	#print("Main")
	exA()
