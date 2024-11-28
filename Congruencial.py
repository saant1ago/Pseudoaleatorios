#Creamos un modelo de MCL
class mcl:
    #Le aniadimos los atributos
    def __init__(self, a, c, m):
        self.a = a
        self.c = c
        self.m = m
    
    
    #Calcular el proximo valor según un X
    def proximo(self, x,iters):
        numeros_aleatorios = []

        for i in range(iters):
            a_=self.a
            b_=self.a*x+self.c
            c_=(self.a * x + self.c)% self.m
            numeros_aleatorios.append(c_)
            
            print(f'| {x}  |  {b_}  |  {c_}  |')
            
            
            x = c_
        print(f'******//Tus números aleatorios son//*****')
        print(numeros_aleatorios)

  

#Creamos un modelo
Modelo = mcl(1, 7, 13) #mcl (a,c,b)
Modelo.proximo(7,20) #proximo(x,numero de iteraciones)
    
