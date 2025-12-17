import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Situation de 1vs1
def simulationunversusun(n):
    Att = 0 # Compteur du nombre de victoires offensives
    Def=0
    for i in range(n): #n-simulations
        a=random.randint(1,6)
        d=random.randint(1,6)
        if d > a:
            Att+=1
        else:
            Def+=1
    return (Att/n, Def/n)
    # Renvoie le pourcentage de victoire de chaque côté
#Situation de 1vs2
def simulationunversusdeux(n):
    Att=0
    Def=0
    for i in range(n):
        de1=random.randint(1,6) #dé offensif
        de2=random.randint(1,6)
        de3=random.randint(1,6)
        if de1 > de2 and de1>de3:
            Att+=1
        else:
            Def +=1
        return Att/n, Def/n
#Simulation de 2v1
def simulationdeuxversusun(n):
    Att = 0
    Def = 0
    #le defenseur gagne un duel et lattaquant aussi
    for i in range(n): # n-simulations
        de1= random.randint(1,6) # De offensif 1
        de2=random.randint(1,6) #De offensif 2
        de3=random.randint(1,6)
        if de3>=de1 and de3>=de2:
            Def+=1
        if de1>de3 or de2>de3:
            Att+=1
    return Def/n, Att/n
#Situation de 2v2
def simulationdeuxversusdeux(n):
    Att = 0#Compteur du nombre de double-duels offensifs gagnés
    Def = 0
    Egalite = 0
    #le defenseur gagne un duel et lattaquant aussi
    for i in range(n):
        de1= random.randint(1,6)
        de2=random.randint(1,6)
        de3=random.randint(1,6)
        de4=random.randint(1,6)
        Attaque = [de1, de2]
        Defense = [de3,de4]
        AttaqueMax= max(de1,de2)
        DefenseMax= max(de3, de4)
        Attaque2 = deuxiememaximum(Attaque)
        Defense2=deuxiememaximum(Defense)
        if AttaqueMax>DefenseMax and Attaque2>Defense2:
            Att+=1
        if AttaqueMax>DefenseMax and Defense2>=Attaque2 or DefenseMax>=AttaqueMax and Defense2<Attaque2:
           Egalite +=1
        if DefenseMax>=AttaqueMax and Defense2>=Attaque2:
            Def+=1
    return Egalite/n, Def/n, Att/n

#Simulation de 3v1
def simulationtroisversusun(n):
    Att=0
    Def=0
    for i in range(n):
        de1= random.randint(1,6)
        de2=random.randint(1,6)
        de3=random.randint(1,6)
        de4=random.randint(1,6)
        if de4>=de1 and de4>=de2 and de4>=de3:
            Def+=1
        else:
            Att+=1
    return Def/n, Att/n
#Le code suivant permettra de simuler n fois la situation de 3vs2
def simulationtroisdeux(n):
    Att = 0
    Egalite = 0
    Def = 0
    for i in range(n):
        a=random.randint(1,6)
        b=random.randint(1,6)
        c=random.randint(1,6)
        d=random.randint(1,6)
        e=random.randint(1,6)
        Attaque=[a,b,c]
        Defense=[d,e]
        AttaqueMax = max(a,b,c)
        Attaque2 = deuxiememaximum(L)
        DefenseMax= max(d,e)
        Defense2=deuxiememaximum(L2)
        if AttaqueMax>DefenseMax and Attaque2>Defense2:
            Att+=1
        if AttaqueMax>DefenseMax and Defense2>=Attaque2 or DefenseMax>=AttaqueMax and Defense2<Attaque2:
            Egalite+=1
        if DefenseMax>=AttaqueMax and Defense2>=Attaque2:
            Def+=1
    return Egalite/n, Def/n, Att/n
##

dico={}
def gagnant(A, B):
    if (A,B) in dico:
        return dico[(A,B)]
    if A <= 0:
        dico[(A,B)] = 0
        return 0
    if B <=0:
        dico[(A,B)] = 1
        return 1
    if A == 1 and B == 1:
        dico[(A,B)] = 15/36
        return 15/36
    if A == 1 and B == 2:
        dico[(A,B)] = 55/216 * (15/36)
        return 55/216 * (15/36)
    if A == 2 and B == 1:
        dico[(A,B)] = 125/216 + 91/216 * (15/36)
        return 125/216 + 91/216 * (15/36)
    if A == 2 and B == 2:
        dico[(A,B)] = (295/1296) + (420/1296) * (15/36)
        return (295/1296) + (420/1296)*(15/36)
    if A == 3 and B == 1:
        dico[(A,B)] = 855/1296 + 441/1296 * 125/216 + 91/216*15/36* 441/1296
        return 855/1296 + 441/1296 * 125/216 + 91/216*15/36* 441/1296
    if A == 3 and B ==2:
        dico[(A,B)] = 2890/7776
        return 2890/7776
    if A == 1 and B ==3:
        dico[(A,B)]  = 0.02702
        return 0.02702
    else:
        dico[(A,B)] = 2611/7776 * gagnant(A-1,B-1) + 2278/7776 * gagnant(A-2,B) + 2890/7776 * gagnant(A,B-2)
        return dico[(A,B)]
L=[] #Liste vide
y= [i for i in range(1,21)]
for i in range(1,21):
    Li=[] # Résultats obtenus
    for j in range(1,21):
        Li.append(gagnant(j,i))
    plt.plot(y,Li, label=f'Courbe de victoire face à {i} défenseurs' )

    L.append(Li)
plt.legend()
plt.figure()
heat_map = sns.heatmap(L, linewidth=1, annot = True)
axes=plt.gca()
axes.set_ylabel('Nombre de défenseurs',fontsize=14)
axes.set_xlabel('Nombre des attaquants',fontsize=14)
plt.title('Probabilité de victoire des attaquants ',fontsize=16)
# plt.pcolormesh(L, cmap='summer')
plt.show()

##

#Situation de 1vs1


def unversusun(n):
    NAlost = 0
    NDlost=0
    a=random.randint(1,6)
    d=random.randint(1,6)
    if d > a:
        NDlost+=1
    else:
        NAlost+=1
    return NAlost,NDlost
#Situation de 1vs2
def unversusdeux(n):
    NDlost=0
    NAlost=0
    a=random.randint(1,6)
    b= random.randint(1,6)

    d=random.randint(1,6)
    if a > b and a > d :
        NDlost=1
    else:
        NAlost=1
    return (NAlost, NDlost)

def deuxversusun(n):
    NDlost=0
    NAlost=0
    a=random.randint(1,6)
    b= random.randint(1,6)
    d=random.randint(1,6)
    if a >= b and a >= d :
        NAlost=1
    else:
        NDlost=1
    return (NAlost, NDlost)
#Situation de 2v2
def deuxversus2(n):
    NDlost = 0
    NAlost = 0
    de1= random.randint(1,6)
    de2=random.randint(1,6)
    de3=random.randint(1,6)
    de4=random.randint(1,6)
    Attaque = [de1, de2]
    Defense = [de3,de4]
    AttaqueMax= max(de1,de2)
    DefenseMax= max(de3, de4)
    Attaque2 = find_second_maximum(Attaque)
    Defense2=find_second_maximum(Defense)
    if AttaqueMax>DefenseMax and Attaque2>Defense2:
        NDlost=2
    if AttaqueMax>DefenseMax and Defense2>=Attaque2 or DefenseMax>=AttaqueMax and Defense2<Attaque2:
        NAlost = 1
        NDlost=1
    if DefenseMax>=AttaqueMax and Defense2>=Attaque2:
        NAlost=2
    return (NAlost,NDlost)
def troisversusdeux(n):
    NAlost = 0
    NDlost = 0
    a=random.randint(1,6)
    b=random.randint(1,6)
    c=random.randint(1,6)
    d=random.randint(1,6)
    e=random.randint(1,6)
    L=[a,b,c]
    L2=[d,e]
    AttaqueMax = max(a,b,c)
    Attaque2 = find_second_maximum(L)
    DefenseMax= max(d,e)
    Defense2=find_second_maximum(L2)
    if AttaqueMax>DefenseMax and Attaque2>Defense2:
        NDlost =2
    if AttaqueMax>DefenseMax and Defense2>=Attaque2 or DefenseMax>=AttaqueMax and Defense2<Attaque2:
        NAlost=1
        NDlost = 1
    if DefenseMax>=AttaqueMax and Defense2>=Attaque2:
        NAlost=2
    return (NAlost,NDlost)
def troisversusun(n):
    NAlost = 0
    NDlost = 0
    a=random.randint(1,6)
    b=random.randint(1,6)
    c=random.randint(1,6)
    d=random.randint(1,6)
    if d >= a and d>=b and d>= c:
        NAlost=1
    else:
        NDlost=1
    return NAlost,NDlost
def nbtroupesrestantes(A,D):
    while A!=0 and D!=0:
        if A >=3 and D >=2:
            A,D= A-troisversusdeux(1)[0],D - troisversusdeux(1)[1]
        if A >=3 and D == 1 :
            A,D = A- troisversusun(1)[0], D -troisversusun(1)[1]

        if D >= 2 and A == 2 :
            A,D= A-deuxversus2(1)[0],D - deuxversus2(1)[1]
        if A==1 and D >=2:
            A,D= A-unversusdeux(1)[0],D - unversusdeux(1)[1]
        if A==2 and D == 1:
            A,D = A-deuxversusun(1)[0],D- deuxversusun(1)[1]
        if A == 1 and D ==1:
            A,D = A-unversusun(1)[0],D - unversusun(1)[1]
    return (A,D)


def Simulationdeplateau(A,D): # Avec D une liste comportant L[i] ==nb de troupes au ieme territoire# Nombre de territoire
    territoiresconquis = 0
    DefensePerdu = 0
    for i in range(len(D)):
        A,B = nbtroupesrestantes(A,D[i])
        if A==0:
            return territoiresconquis,territoiresconquis, DefensePerdu
        if B == 0  and i +1== len(D):
            return A + len(D), len(D), DefensePerdu + D[i]
        if B == 0  and i < len(D):
            A = A - 1
            # On dépose une troupe sur le territoire en plus de celles perdues  car on peut plus l'utiliser
            territoiresconquis += 1
            DefensePerdu+= D[i]
    return A + territoiresconquis,territoiresconquis, DefensePerdu
Da=[2,2,2,2,2]
A=[i for i in range(25)]
L=[0 for i in range(25)]
W=[0 for i in range(25)]
for i in range(1,1000):
    for j in range(25):
            L[j] += Simulationdeplateau(j,Da)[0]
            W[j]+= Simulationdeplateau(j,Da)[1]
Resultats = [0]
TerritoireMoyenne =[0]
for j in range(1,25) :
    Resultats.append(L[j]/(1000*j))
    TerritoireMoyenne.append(W[j]/1000)
plt.figure(1)
a = plt.plot(A,Resultats,"or")
plt.tick_params(axis = 'both', labelsize = 15)
axes = plt.gca()
axes.set_xlabel('Nombres dattaquants')
axes.set_ylabel('Ratio encore en vie')
plt.show()
plt.figure(2)
plt.plot(A,TerritoireMoyenne,"ob")
axes = plt.gca()
axes.set_xlabel('Nombres dattaquants')
axes.set_ylabel('Nombre territoires conquis')


plt.show()


##Défense Pour 5 territoires et 10 troupes
#Création des configurations possibles de défenses
Dd=[2,2,2,2,2] #Territoires
Patp=[1,1,1,1,6]
TAF=[6,1,1,1,1]
Eq=[3,2,1,1,3]
Att=[i for i in range(20)]
Deuxdeux=[0 for i in range(20)]
# Initialisation des résultats selon i le nombre d'attaquants
Touspourun=[0 for i in range(20)]
Equilibre=[0 for i in range(20)]
Parisatoutprix=[0 for i in range(20)]
for i in range(1000):
    for j in range(20):
        Deuxdeux[j] += j - Simulationdeplateau(j,Da)[0]
        # Nb de Troupes offensivestuées
        Touspourun[j] += j-Simulationdeplateau(j,G)[0]
        Equilibre[j] += j-Simulationdeplateau(j,K)[0]
        Parisatoutprix[j] += j-Simulationdeplateau(j,L)[0]
for i in range(len(Deuxdeux)):
    Deuxdeux[i] = Deuxdeux[i] /1000
    Touspourun[i] = Touspourun[i] /1000
    Equilibre[i] = Equilibre[i] /1000
    Parisatoutprix[i] = Parisatoutprix[i] /1000
plt.plot(Att,Deuxdeux, label='Configuration deux-deux')
plt.plot(Att,Touspourun, label='Tous au front')
plt.plot(Att,Parisatoutprix, label='Paris à tout Prix')
plt.plot(Att,Equilibre,label='Equilibrée')
plt.legend()
axes = plt.gca()
axes.set_xlabel('Nombres dattaquants', fontsize=14)
axes.set_ylabel('Nombre de troupes adverses tuées! ',fontsize=14)
plt.show()
##Défense Pour 6 territoires et 18 troupes

Eq=[3,3,3,3,3,3]
Dd=[2,2,2,2,2,8]
Tpu=[13,1,1,1,1,1]
Upt=[1,1,1,1,1,13]
Deuxdeux=[0 for i in range(30)]
Touspourun=[0 for i in range(30)]
Equilibre=[0 for i in range(30)]
Unpourtous=[0 for i in range(30)]
W=[0 for i in range(20)]
Woippy =[0,0,0,0]
for i in range(1000):
    for j in range(30):
        Deuxdeux[j] += j - Simulationdeplateau(j,Eq)[0] # Nb de Troupes tuées
        Touspourun[j] += j-Simulationdeplateau(j,Tpu)[0]
        Equilibre[j] += j-Simulationdeplateau(j,Eq)[0]
        Unpourtous[j]+=j-Simulationdeplateau(j,Upt)[0]
for i in range(len(Deuxdeux)):
    Deuxdeux[i] = Deuxdeux[i] /1000
    Touspourun[i] = Touspourun[i] /1000
    Equilibre[i] = Equilibre[i] /1000
    Unpourtous[i] = Unpourtous[i]/1000
A=[i for i in range(30)]
plt.plot(A,Deuxdeux, label='Equilibrée')
plt.plot(A,Touspourun, label='Deux-deux')
plt.plot(A,Equilibre, label='Tous au front')
plt.plot(A,Unpourtous, label='Tous à labri')
plt.legend()
axes = plt.gca()
axes.set_xlabel('Nombres dattaquants')
axes.set_ylabel('Nombre de troupes adverses tuées! ',fontsize = 14)
plt.show()