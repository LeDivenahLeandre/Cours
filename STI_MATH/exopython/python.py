from math import *

#Exo1
#x = int(input("Quelle température en C° souhaitez vous convertir ?"))
#print("Votre tempéreature vaut", x+273,"kelvin")


#Exo2
#r_ext = int(input("Rayon extérieur ?"))
#r_int = int(input("Rayon intérieur ?"))

#print("la surface de la rondelle est de", round(pi*((r_ext)**2-(r_int)**2),2), "en cm²")


#Exo 3
#def fonction(x):
    #result = 3*x**2 - 7*x + 8
    #print(result)


#x_input = int(input("Veuillez défénir x"))
#fonction(x_input)


#Exo 4
#def tarifs():
   # x = int(input("Combien de photo allez vous développer ?"))

    #if x < 75:

       # print("Cela fera", 0.16*x)

    #else:

       # print("Cela fera", 0.12*x)

#tarifs()

#Exo 5
#Ce programme refuse toute valeur de x qui est inférieur ou égale à -10, et
#aussi tout ce qui est supérieur ou égal à 10.
#def racine(x):
    #if -10<=x<=10:
        #return sqrt(100-x**2)
    #else:
        #print("non définie")


#Exo 6
#x=randint(-10,10)
#y=randint(-10,10)

#if x*y>0:
    #x=x**2
    #print(x)
#else:
    #x=x-2
    #print(x)

#Affirmation C est vraie, pour -7.
#Affirmation E est vraie.


#Exo 7
#def f(n):
    #p = 1
    #for k in range(1, n+1):
        #p = p*k
    #return p
#Ce code renvoi 24


#Exo 8

#En mettant f(2) on ne trouve rien, il faut mettre f(3)


#Exo 9

#def populas():
    #n = int(input("Combien de jour dure la simulation ?"))
    #initial = 100

    #for i in range(1, n+1):
        #initial = initial*2
    #return(initial)

    #print(initial)


#Exo 10

#def qcm1():
    #n=0
    #x=10

    #while x<=10000:
        #x=x*10
        #n=n+1
    #return n

    #print(n)

#Réponse D, le programme ressort 4.


#Exo 11

#def qcm3():
    #t=0
    #x=250

    #while x<=2000:
        #x=x*2
        #t=t+1

    #return t

    #print(t)

#Réponse C, le code ressort 4


#Exo 12

#x = 3
#y = 0
#for i in range(1, x + 1):
    #y = y + i*2
    #if y > 4:
        #y = y-1
#print(y)

#Réponse C, le code ressort 10


#Exo 13

#def qcm2():
    #a = 1
    #b = 0

    #while a < 10:
        #print("encore un tour")
        #if a > 3:
            #b = b + 2*a
        #else:
            #b = b + a
        #a = a*2
    #return b
    #print(b)

#4 Tours, sortie 27. La réponse D


#Exo 14
#u = 2
#for k in range(1, 3):
    #if k/2 == int():
        #u = (2*u)+k
    #else:
        #u = u+(3*k)-1
        
#print('u est egal à', u)

#Exo 15   
def mystere(n):
    a = 2
    b = 5
    for k in range(1, 3+1):
        a = a+3*k
        b = b*k
    print(a, b)
#reponse B
#mystere(3)