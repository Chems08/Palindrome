x = 4782    #nombre sélectionné
t = []      #initialisation de la liste permettant d'inverser le nombre
r = 0       #initialisation de l'itération
z = list(str(x))    #passer le nombre en liste afin de l'inverser

def check(x, t, z, r):
    for i in range(len(z)):     #boucle permettant d'inverser le nombre
        t.append(z[-i-1]) 
        
    n = int("".join(t))     #passer la liste inversée en nombre

    t = []      #initialisation de la liste permettant d'inverser le nombre
    
    print(x, " ; ", n)
    print("itération : ",r)
    
    if n != x:      #vérifier si les deux nombres ne sont pas identique
        x = n + x
        z = list(str(x))
        r = r + 1
        check(x, t, z, r)       #récursivité de la fonction afin qu'elle se répète jusqu'à atteindre la dernière itération

    

check(x, t, z, r) 
    




