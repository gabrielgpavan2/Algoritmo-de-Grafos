
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter



def Dijkstra(w):
	n = len(w)-1
	Vlin = [False]*(n+1); c = [None]+[float("inf")]*n; T = [None]*(n+1)
	Vlin[1] = True; c[1] = 0
	for i in range(2, n+1):
		c[i] = w[1][i]; T[i] = 1
	for vcont in range(1,n):
		cmin = float("inf")
		for z in range(1,n+1):
			if not Vlin[z] and c[z] < cmin:
				j, cmin = z, c[z]
		Vlin[j] = True
		for i in range(1, n+1):
			if not Vlin[i]:
				if c[i] > c[j]+w[j][i]:
					c[i] = c[j]+w[j][i]
					T[i] = j
	return (c, T)

def Teste():
	w = [None,
		[None,0,1,float("inf"),float("inf"),float("inf"),3,float("inf")],
		[None,float("inf"),0,float("inf"),float("inf"),float("inf"),float("inf"),2],
		[None,1,float("inf"),0,4,1,float("inf"),float("inf")],
		[None,float("inf"),1,float("inf"),0,2,float("inf"),0],
		[None,float("inf"),float("inf"),0,float("inf"),0,float("inf"),float("inf")],
		[None,float("inf"),float("inf"),float("inf"),float("inf"),5,0,float("inf")],
		[None,float("inf"),float("inf"),float("inf"),1,float("inf"),1,0],
	]

	(c,T) = Dijkstra(w)
	print ("c=",c,"\n","T=",T)


