import re 

filepath = input("Insira o filepath\n")
#print(filepath)
try:
	f = open(filepath, "r", encoding='utf-8')

	categoria={}

	for linha in f:
		#talvez nao seja preciso ser um findall
	  campos = re.findall(r'\@(\w+)',linha)
	  for c in campos:
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

	html.write('''    	</ol>
	</body>
</html>\n''')

except Exception as e:
    print(e)