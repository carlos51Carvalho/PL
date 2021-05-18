#needs 	sudo apt install graphviz
#and	pip3 install graphviz

from graphviz import Graph

g = Graph(format='png')

g.node('A', 'King Arthur')
g.node('B', 'Sir Bedevere the Wise')
g.node('L', 'Sir Lancelot the Brave')

g.edges(['AB', 'AL'])
#ou
g.edge('A', 'B', constraint='true')
g.edge('A', 'L', constraint='true')


g.render('test-output/round-table.gv', view=True)