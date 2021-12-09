#Projet python de EL BACH Achraf et MANUEL Enzo.


from random import *    #
from turtle import *    ## Voici tous les modules inclut dans python que nous utlisons pour le jeu
from time import*       ##
import winsound         #
from JosephLeBoss import *      #
from personnages import*        ## 
from decorkitu import*          ### Voici tous les modules construit par notre personne que nous avons utilisé pour construire ce jeu
from texte import*              ##
from polygone import*           #


####################### Règles ##############################################################################################################################################################################################################################

setup(width=0.99, height=0.94, startx=0, starty=0)      #On met en place la résolution de la fenêtre

regle=Turtle()
regle.hideturtle()
regle.up()

def règles(m,x,y,z,t):          #Fonction qui affiche les règles en fonction des interactions du joueur avec le clavier
    clear()
    color('white')
    bgcolor('black')
    onkey(regle_suivante,'space')
    onkey(passer_regle,'Return')
    tracer(0)
    if m==-1:                       #Cette condition est validé lorsque le joueur a finit de lire les règles et appuie sur Entrée, on affiche donc le menu
        onkey(None,'space')
        onkey(None,'Return')
        menua()
        onscreenclick(menu)
    elif m%2==0:                #Cette condition correspond à la génération de la première page (seulement de l'écriture)
        goto(x,y)
        write("Bazaris : The Bizarre Adventure",False,"center",("Fixedsys",t,'normal','bold','underline'))
        goto(x,y-z)
        write("Il s'agit d'un jeu avec 5 ou 6 combattants au",False,"center",("Fixedsys",t,'normal'))
        goto(x,y-2*z)
        write("et avec 3 niveaux de difficultés au choix.",False,"center",("Fixedsys",t,'normal'))
        goto(x,y-3*z)
        write("Les cartes contiennent 2 ou 3 éclaireurs.",False,"center",("Fixedsys",t,'normal'))
        goto(x,y-4*z)
        write("Ces éclaireurs peuvent être la réplique d'un combatant,",False,"center",("Fixedsys",t,'normal'))
        goto(x,y-5*z)
        write("par exemple un robot vert,",False,"center",("Fixedsys",t,'normal'))
        goto(x,y-6*z)
        write("dans ce cas, il faut cliquer sur le robot vert.",False,"center",("Fixedsys",t,'normal'))
        goto(x,y-7*z)
        write("Si aucun combattant n'est dessiné sur la carte,",False,"center",("Fixedsys",t,'normal'))
        goto(x,y-8*z)
        write("il faut cliquer sur le combattant qui n'a aucune",False,"center",("Fixedsys",t,'normal'))
    else:                       #Cette condition correspond à la génération de la deuxième page
        goto(x,y-z)
        write("caractéristique commune avec les éclaireurs de la carte.",False,"center",("Fixedsys",t,'normal'))
        goto(x,y-2*z)
        write("Donc par exemple, si la carte contient un robot blanc et un",False,"center",("Fixedsys",t,'normal'))
        goto(x,y-3*z)
        write("pistolero jaune, il faut cliquer sur la mage rouge foncée.",False,"center",("Fixedsys",t,'normal'))
        goto(x,y-4*z)
        write("Ce jeu se jouera contre le boss Josephin,",False,"center",("Fixedsys",t,'normal'))
        goto(x,y-5*z)
        write("une IA à l'intelligence sur-développée,",False,"center",("Fixedsys",t,'normal'))
        goto(x,y-6*z)
        write("qu'il faudra battre pour remporter la victoire.",False,"center",("Fixedsys",t,'normal'))
        goto(x,y-7*z)
        write("Mais fait bien attention plus tu lui fais mal,",False,"center",("Fixedsys",t,'normal'))
        goto(x,y-8*z)
        write("plus il devient vif et exact dans ses réponses.",False,"center",("Fixedsys",t,'normal'))
    update()
    
def passer_regle():         #Fonction qui se déclenche à l'appui de la touche entrée pour enlever les règles et commencer à jouer
    regle.goto(0,1)
    règles(-1,0,450,129,34)
    
def regle_suivante():       #Fonction qui se déclenche à l'appui de la touche espace pour changer de page
    regle.forward(1)
    règles(regle.xcor(),0,450,129,34)


#################### Menu #################################################################################################################################################################################################################################

difficulte=Turtle()
liste=Turtle()
pion=Turtle()
waiter=Turtle()

def menua():        #Fonction de dessin du menu d'options (aspect)
    setup(width=0.95, height=0.90, startx=50, starty=0)     #On change la résolution de la fenêtre afin qu'elle soit plus adaptée au menu
    clear()
    hideturtle()
    up()
    tracer(0)
    bgcolor('black')
    color('white')
    width(2)
    goto(0,300)
    write("WELCOME TO BAZARIS :",False,"center",("Verdana",65,'normal','bold','underline'))
    goto(0,200)
    write("THE BIZAR ADVENTURE",False,"center",("Verdana",65,'normal','bold','underline'))
    goto(-300,0)
    color('lime green')
    write("Facile",False,"center",("Verdana",50,'normal','bold'))
    encadrement(300,75)
    goto(-300,-100)
    color('gold')
    write("Intermédiaire",False,"center",("Verdana",50,'normal','bold'))
    encadrement(600,75)
    goto(-300,-200)
    color('dark red')
    write("Difficile",False,"center",("Verdana",50,'normal','bold'))
    encadrement(300,75)
    goto(300,-50)
    color('blue')
    write("5 Pions",False,"center",("Verdana",50,'normal','bold'))
    encadrement(300,75)
    goto(300,-150)
    color('red')
    write("6 Pions",False,"center",("Verdana",50,'normal','bold'))
    encadrement(300,75)
    goto(0,-400)
    color('white')
    write("JOUER",False,"center",("Verdana",50,'normal','bold'))
    encadrement(260,75)
    goto(0,-400)
    encadrement(1600,800)

def menu(x,y):          #Fonction permettant de capturer le click de la souris et de définir les options de jeu en fonction des coordonnées de la souris lors du click
    if x>-450 and x<-150 and y<75 and y>0:          #Coordonnées du bouton de difficulté Facile
        winsound.PlaySound('Son/Move.wav',winsound.SND_ASYNC)       #Un petit son se joue lorsque l'on appuie sur un des boutons
        difficulte.goto(1,0)                #On viendra récupérer les coordonnées de la turtle pour savoir quelle difficulté le joueur a choisi
        goto(-300,-100)
        color('gold')
        fillcolor('black')
        begin_fill()
        encadrement(600,75)
        end_fill()
        write("Intermédiaire",False,"center",("Verdana",50,'normal','bold'))
        encadrement(600,75)
        goto(-300,-200)
        color('dark red')
        fillcolor('black')
        begin_fill()
        encadrement(300,75)
        end_fill()
        write("Difficile",False,"center",("Verdana",50,'normal','bold'))
        encadrement(300,75)
        goto(-300,0)
        color('lime green')
        begin_fill()
        encadrement(300,75)
        end_fill()
        color('black')
        write("Facile",False,"center",("Verdana",50,'normal','bold'))
        forward(10)
    if x>-600 and x<0 and y<-25 and y>-100:         #Coordonnées du bouton de difficulté Moyen
        winsound.PlaySound('Son/Move.wav',winsound.SND_ASYNC)
        difficulte.goto(2,0)
        goto(-300,0)
        color('lime green')
        fillcolor('black')
        begin_fill()
        encadrement(300,75)
        end_fill()
        write("Facile",False,"center",("Verdana",50,'normal','bold'))
        encadrement(300,75)  
        goto(-300,-200)
        color('dark red')
        fillcolor('black')
        begin_fill()
        encadrement(300,75)
        end_fill()
        write("Difficile",False,"center",("Verdana",50,'normal','bold'))
        encadrement(300,75)
        goto(-300,-100)  
        color('gold')
        fillcolor('gold')
        begin_fill()
        encadrement(600,75)
        end_fill()
        color('black')
        write("Intermédiaire",False,"center",("Verdana",50,'normal','bold'))
    if x>-450 and x<-150 and y<-125 and y>-200:     #Coordonnées du bouton de difficulté Difficile
        winsound.PlaySound('Son/Move.wav',winsound.SND_ASYNC)
        difficulte.goto(3,0)
        goto(-300,0)
        color('lime green')
        fillcolor('black')
        begin_fill()
        encadrement(300,75)
        end_fill()
        color('lime green')
        write("Facile",False,"center",("Verdana",50,'normal','bold'))
        encadrement(300,75)  
        goto(-300,-100)
        color('gold')
        fillcolor('black')
        begin_fill()
        encadrement(600,75)
        end_fill()
        write("Intermédiaire",False,"center",("Verdana",50,'normal','bold'))
        encadrement(600,75)
        goto(-300,-200)
        color('dark red')
        fillcolor('dark red')
        begin_fill()
        encadrement(300,75)
        end_fill()
        color('black')
        write("Difficile",False,"center",("Verdana",50,'normal','bold'))
    if x<450 and x>150 and y<25 and y>-50:          #Coordonnées du bouton 5 Pions
        winsound.PlaySound('Son/Move.wav',winsound.SND_ASYNC)
        liste.goto(5,0)
        goto(300,-150)
        color('red')
        fillcolor('black')
        begin_fill()
        encadrement(300,75)
        end_fill()
        write("6 Pions",False,"center",("Verdana",50,'normal','bold'))
        encadrement(300,75)
        goto(300,-50)
        color('blue')
        fillcolor('blue')
        begin_fill()
        encadrement(300,75)
        end_fill()
        color('black')
        write("5 Pions",False,"center",("Verdana",50,'normal','bold'))
    if x<450 and x>150 and y<-75 and y>-150:            #Coordonnées du bouton 6 Pions
        winsound.PlaySound('Son/Move.wav',winsound.SND_ASYNC)
        liste.goto(6,0)
        goto(300,-50)
        color('blue')
        fillcolor('black')
        begin_fill()
        encadrement(300,75)
        end_fill()
        write("5 Pions",False,"center",("Verdana",50,'normal','bold'))
        encadrement(300,75)
        goto(300,-150)
        color('red')
        fillcolor('red')
        begin_fill()
        encadrement(300,75)
        end_fill()
        color('black')
        write("6 Pions",False,"center",("Verdana",50,'normal','bold'))
    if x<130 and x>-130 and y<-325 and y>-400 and difficulte.xcor()!=0 and liste.xcor()!=0:     #Bouton Jouer
        winsound.PlaySound('Son/Start.wav',winsound.SND_ASYNC)          #Un autre son très joli se joue au click du bouton Jouer
        jeu()

#################### Menu #################################################################################################################################################################################################################################


def carteetsolution(pp,couleurs,classes):           #Fonction responsable de la génération de carte
    cf=[]
    of=[]
    for i in couleurs:                              #On crée deux listes fictives (non permanentes) qui vont servir à construire la carte en retirant les élément des listes progressivement
        cf.append(i)
        of.append(classes[couleurs.index(i)])
    solution=[cf[randint(0,len(cf)-1)]]                 #On commence par créer la solution aléatoirement
    solution.append(of[couleurs.index(solution[0])])
    cf.remove(solution[0])                              #On retire les éléments de la solution des listes fictives
    of.remove(solution[1])
    carte = []
    trash = []
    while len(cf)>0:                        #Puis on construit la carte en fonction de la solution qu'on a choisi en retirant les éléments des listes
        perso=[choice(cf)]
        if len(cf)>1:
            trash.append(of[cf.index(perso[0])])
        of.remove(of[cf.index(perso[0])])
        cf.remove(perso[0])
        if len(cf)==0:
            perso.append(choice(trash))
        else:
            perso.append(choice(of))
            cf.remove(cf[of.index(perso[1])])
            of.remove(perso[1])
        carte.append(perso)
    if randint(0,99)<pp:                #Si la condition aléatoire (probabilité d'avoir un pion) est rempli on retire un des personnages et on insère la solution dans la carte
        carte.remove(carte[len(carte)-1])
        carte.insert(randint(0,len(carte)),solution)
    return[carte,solution]          #On renvoie sous forme de liste la carte et la solution

def dboss(solution,carte,phase):                    #Cette fonction va définir les temps de réaction et le taux de réussite de l'IA en fonction du nombres de pions, de la difficulté et de la phase d'améliorations de Josephin
    r=1
    i=0
    while i<len(carte):                             #Cette boucle permet simplement de réduire le temps de réaction du boss s'il y a un pion dans la carte
            if carte[i]==solution:
                r=1/difficulte.xcor()                   
            i=i+1
    if difficulte.xcor()==3:                                                                                #On définit des taux de réussite et des temps de réaction différent selon la difficulté donc on remplit tout les cas avec des valeurs adaptés
        return [randint(int((100*r)/(phase+1)),int((140*r)/(phase+1)))/10,(randint(0,99)>(9/phase))]
    if difficulte.xcor()==2:
        return [randint(int((140*r)/(phase+1)),int((200*r)/(phase+1)))/10,(randint(0,99)>(18/phase))]       #On peut aussi voir que la phase du boss influe sur le taux de réussite et le temps de réaction pendant la partie
    if difficulte.xcor()==1:
        return [randint(int((200*r)/(phase+1)),int((240*r)/(phase+1)))/10,(randint(0,99)>(27/phase))]


def generationMechant(pp,couleurs,classes,coordCarte):          #On vient chercher les paramètres nécessaires à la génération de carte ainsi que la liste des emplacements de chaque personnage
    carte = carteetsolution(pp,couleurs,classes)                #On génére la carte (qui je le rappelle est sous la forme [carte(liste),identifiant joueur] et on la stocke dans une variable
    j=0
    tracer(0)                               #On utilise toujours l'alliance tracer(0)/update() pour charger nos personnages instantanément
    for i in carte[0]:                                          #On créer une boucle qui va venir générer chaque personnage de la carte (premier élément de la variable)
        width(2)
        if i[1]=="robot":                                               #Si le personnage(deuxième élément du personnage) est un robot on va venir utiliser la fonction de dessin du robot
            robo(coordCarte[j]-j*5,coordCarte[j+1],i[0],0.45)         #On vient chercher les cordonnées du premier personnage (liste rangeant les coordonnées deux par deux)
                                                                        # ainsi que la couleur sur la carte (premier élément du personnage)
        if i[1]=="mage":                                                        #On refait la même chose pour les autres cas de personnage
            madameForte(coordCarte[j]-j*5,coordCarte[j+1],i[0],0.35)
        if i[1]=="pistolero":
            homFor(coordCarte[j]-j*2,coordCarte[j+1],i[0],0.25)
        if i[1]=="guerrier":
            cloud(coordCarte[j]-j*3,coordCarte[j+1],i[0],0.3)               #Je souligne le fait que les facteur de taille (dernière argument) change en fonction des personnages car leur taille naturelle diffère
        if i[1]=="gentil-neige":
            snowy(coordCarte[j]-j*3,coordCarte[j+1],i[0],0.3)
        if i[1]=="avatar":
            avatar(coordCarte[j]-j*3,coordCarte[j+1],i[0],0.3)
        j=j+2                                                           #On augmente l'indice qui va aller chercher les coordonnées de 2 car on en a déjà utilisé 2
    cercle(0,360,"red")                                             #Ceci ne sert à rien, il y a un bug étrange qui fait que la couleur du prochain tracé prend la couleur du boss lors d'un changement de phase donc on met un tracé inutile entre les personnages
    update()
    return carte


def nom_utilisateur(x,y,w,h):       #On prend en paramètres les coordonnées et la résolution de l'écran
    nom = ""                        #On construit une pile qui va recevoir le nom d'utilisateur
    if nom=="" or nom.length > 12:      #Les entrées vides ou trop longues ne sont pas validées (par soucis de contrôle de longueur et d'aspect)
        nom = textinput("Pseudonyme","Veuillez saisir un nom : (Maximum : 12 caractères)")      #On utilise la fonction textinput pour recevoir le nom du joueur
    bouge(x,y)                                                                                  #On se déplace au dessus du cadre d'affichage du texte
    write("Lvl "+str(randint(1,100))+" : "+str(nom),font=("Fixedsys",20,"normal"))              #Pour afficher le nom du joueur précédé d'un niveau généré aléatoirement pour garder l'aspect de jeu de rôle
        

def jeu():              #Fonction "principale" du jeu
    clear()
    screensize()
    setup(width = 0.99, height = 0.94, startx=0,starty=0)           #On définit une nouvelle résolution de fenêtre correspondant à celle du décor, presque pleine écran
    w = window_width()
    h = window_height()
    title("Bazaris : the bizarre adventures")
    fond(w,h)
    nom_utilisateur(3*w/10,-h/4+5,w,h)
    winsound.PlaySound('Son/Theme',winsound.SND_ASYNC | winsound.SND_LOOP)
    coordCarte=[-w/4,h/4-h/10,-w/4+w/8-30,h/4-h/10,-w/4+110,h/4-3*h/20]
    onscreenclick(None)
    hpJ=3000                #Points de vie du joueur (qui peuvent varier)
    hpd=3000                #Points de vie du joueur (invariable)
    hpB=1500+1500*int(difficulte.xcor())            #Points de vie du boss (qui peuvent varier
    hpbossd=1500+1500*int(difficulte.xcor())        #Points de vie du boss (invariable)
    phase=1                         #Initialisation de la phase du boss
    pp=100-30*difficulte.xcor()     #Probabilité de générer un pion dans la carte
    cyberdemon(-w/4+110,h/4+h/16,4) #Affichage du boss
    if liste.xcor()==6:                                                                 #On dessine les 6 pions si c'est le choix du joueur
        couleurs=["green","darkred","gold","blue","white","pink"]                       #Initialisation des listes d'objets et de couleurs en fonction du choix de l'utilisateur dans le menu
        classes=["robot","mage","pistolero","guerrier","gentil-neige","avatar"]
        robo(-w/4-5*w/40,-5*h/20,"green",0.9)       #coord(départ de la route - distance choisie, distance choisie)
        avatar(-w/4+220+w/10+50,-5*h/20,"pink",0.6) #coord(départ de la route + taille du haut de route + distance choisie, même distance que son opposé)
        madameForte(-w/4-3*w/40,-7*h/20,"darkred",0.6)      #même processus pour les autres
        snowy(-w/4+w/20+220+30,-7*h/20,"white",0.65)        #à savoir que les distances ont été choisis d'après la résolution de mon écran s'il y a certains problèmes
        homFor(-w/4+110-3*w/40,-9*h/20,"gold",0.48)     #ici on base les coordonnées en fonction de l'axe central de la route car les deux pions sont proches du milieu
        cloud(-w/4+110+w/20,-9*h/20,"blue",0.6)
    else:                                                                               #On dessine les 5 premiers pions si le choix du joueur est 5 pions
        couleurs=["green","darkred","gold","blue","white"]
        classes=["robot","mage","pistolero","guerrier","gentil-neige"]
        robo(-w/4-5*w/40,-5*h/20,"green",1.125)  
        snowy(-w/4+w/10+220+50,-5*h/20,"white",0.75)
        madameForte(-w/4-w/20,-7*h/20,"darkred",0.75)
        cloud(-w/4+w/20+220,-7*h/20,"blue",0.75)
        homFor(-w/4+110-50,-9*h/20,"gold",0.6)
    n=300
    seth(0)
    hpbosss(int(-w/2+20),int(h/2-100),n)        #On génére la barre de vie du boss
    hpp(int(w/10),int(-h/4+10),n)               #On génére la barre de vie du joueur
    z=0
    setundobuffer(10000)                #Cette commande permet d'autoriser un nombre d'annulation plus élevé car si le nombrem maximal est atteint trop tôt le programme bloque
    while hpJ>0 and hpB>0:      #Boucle principale : Tant que les deux joueurs ont plus de 1 point de vie le jeu continu
        pion.setx(0)        #Réinitialisation du pion choisi par le joueur
        bouge(10000,10000)          #Point de sauvegarde permettant d'effacer les personnages généré au début de chaque nouveau tour
        carteetsolutions=generationMechant(pp,couleurs,classes,coordCarte)      #Affichage des personnages et obtention de la carte
        z=1
        boss=dboss(carteetsolutions[1],carteetsolutions[0],phase)           #Génération du temps de réponse du boss et de sa réussite/échec
        '''affichage de la carte'''
        onscreenclick(pione)
        tracer(0,0.1)
        total=0         #Variable correspondant à notre temps de réaction
        while total<boss[0] and (pion.xcor()==0 or total<0.6):          #Listener munie d'une durée limitée
            listen()
            partie1=time()
            waiter.forward(1)
            update()
            partie2=time()
            total=total+partie2-partie1
        texte=scenar(boss,total,pion.xcor(),carteetsolutions[1],couleurs,classes)       #On génére le set de phrases qui vont s'afficher dans le cadre en fonction de la situation
        affichage(w,h,texte[2],texte[3],texte[4],texte[5],texte[6])         #Affichage des phrases une par une dans le cadre
        while xcor()!=10000 and ycor()!=10000 and z!=0:                 #Technique utilisée pour effacer toutes les actions depuis le point de sauvegarde (utilisé pour effacer la carte)
            undo()
        hpJ=hpJ-texte[1]
        n=int((hpJ/hpd)*300)
        if n<0:     #Cas où les dégats infligés donnent un nombre de points de vie négatif
            n=0
        hplostt(int(w/10),int(-h/4+10),n)       #Perte de points de vie du joueur
        hpB=hpB-texte[0]
        n=int((hpB/hpbossd)*300)
        if n<0:     #Cas où les dégats infligés donnent un nombre de points de vie négatif
            n=0
        hplostbosss(int(-w/2+20),int(h/2-100),n)        #Perte de points de vie du boss
        if (hpB/hpbossd)*300<200 and phase==1:              #Affichage des flammes si les points de vie du boss sont inférieurs au deux tiers des points de vie de base
            while xcor()!=10000 and ycor()!=10000 and z!=0:
                undo()
            phase=2
            flamme(-w/4+110,h/4+h/16,4)
            bouge(10000,10000)      #Point fixe permettant d'effacer les personnages généré au début de chaque nouveau tour
        if (hpB/hpbossd)*300<100 and phase==2:              #Affichage des ailes si les points de vie du boss sont inférieurs au tiers des points de vie de base
            while xcor()!=10000 and ycor()!=10000 and z!=0:
                undo()
            phase=3
            ailes(-w/4+110,h/4+h/16,4)
            bouge(10000,100000)     #Point fixe permettant d'effacer les personnages généré au début de chaque nouveau tour
        bouge(100000,100000)        #Point fixe permettant d'effacer les personnages généré au début de chaque nouveau tour
    if hpJ<1:       #Ecran de fin si le joueur a perdu
        hp.reset()
        hpboss.reset()
        winsound.PlaySound('Son/Game Over',winsound.SND_ASYNC)
        fin("GAME OVER")
    else:           #Ecran de fin si le joueur a gagné
        hp.reset()
        hpboss.reset()
        winsound.PlaySound('Son/Victory',winsound.SND_ASYNC)
        fin("YOU WIN")
    onscreenclick(endgame)

def quitter():      #Fonction qui permet de quitter le jeu à tout moment
    winsound.PlaySound(None,winsound.SND_FILENAME)      #On enlève la musqique lorsque l'on quitte la fenêtre turtle car elle s'arrête seulement quand on ferme l'interprète de commande
    bye()


   
def pione(x,y):      #Fonction qui prend les paramètres du joueurs pour la partie
    w=window_width()        #Il faut savoir que chaque coordonnée de la zone a été calculée sur papier en fonction de la taille de chaque personnage naturellement et du facteur de taille avec une calculatrice
    h=window_height()           #Pour être sur d'avoir le moins d'erreurs, malheureusement en fonction de la résolution de chaque ordinateur, les personnages peuvent se superposer et créer des erreurs
    if pion.xcor()==0 and liste.xcor()==6:      #Si le joueur a choisi 6 pions
        if x<-375*w/1000+55 and x>-375*w/1000-63 and y<-5*h/20+324 and y>-5*h/20:       #Robot
            onscreenclick(None)
            pion.goto(1,0)
        elif x<-325*w/1000+45 and x>-325*w/1000-45 and y<-7*h/20+275 and y>-7*h/20:     #Mage
            onscreenclick(None)
            pion.goto(2,0)
        elif x<-325*w/1000+220 and x>-325*w/1000+55 and y<-9*h/20+310 and y>-9*h/20:    #Pistolero
            onscreenclick(None)
            pion.goto(3,0)
        elif x<-2*w/10+170 and x>-2*w/10+35 and y<-9*h/20+336 and y>-9*h/20:            #Guerrier
            onscreenclick(None)
            pion.goto(4,0)
        elif x<-2*w/10+330 and x>-2*w/10+170 and y<-7*h/20+280 and y>-7*h/20:           #Bonhomme de neige
            onscreenclick(None)
            pion.goto(5,0)
        elif x<-3*w/20+320 and x>-3*w/20+190 and y<-5*h/20+342 and y>-5*h/20:           #Moine
            onscreenclick(None)
            pion.goto(6,0)
    
    if pion.xcor()==0 and liste.xcor()==5:      #Si le joueur a choisi 5 pions
        if x<-375*w/1000+79 and x>-375*w/1000-85 and y<-5*h/20+405 and y>-5*h/20:       #Robot
            onscreenclick(None)
            pion.goto(1,0)
        elif x<-3*w/10+90 and x>-3*w/10-56 and y<-7*h/20+345 and y>-7*h/20:             #Mage
            onscreenclick(None)
            pion.goto(2,0)
        elif x<-w/4+200 and x>-w/4-6 and y<-9*h/20+387 and y>-9*h/20:                   #Pistolero
            onscreenclick(None)
            pion.goto(3,0)
        elif x<-2*w/10+280 and x>-2*w/10+126 and y<-7*h/20+420 and y>-7*h/20:           #Guerrier
            onscreenclick(None)
            pion.goto(4,0)
        elif x<-3*w/20+360 and x>-3*w/20+180 and y<-5*h/20+345 and y>-5*h/20:           #Bonhomme de neige
            onscreenclick(None)
            pion.goto(5,0)


#################### Ecran de fin #################################################################################################################################################################################################################################


def endgame(x,y):                                   #Cette fonction affiche l'écran de fin et nous permet de rejouer ou de fermer la fenêtre
    if x<-125 and x>-475 and y>-200 and y<-125:         #Si la zone de clique est celle du bouton "rejouer" on va tout réinitialiser et le programme va agir comme s'il s'ouvrait pour la première fois.
        restart()                                           #Cette fonction réinitialise les turtles afin de pouvoir repartir à zéro
        winsound.PlaySound(None,winsound.SND_FILENAME)
        menua()                                             #Cette fonction affiche à nouveau le menu de choix
        onscreenclick(menu)                                 #Et on vient chercher l'information du click pour démarrer la partie et définir les options de jeu
    elif x>125 and x<475 and y>-200 and y<-125:         #Si la zone de clique est celle du bouton "quitter" on va fermer la fenêtre turtle avec la commande "bye".
        winsound.PlaySound(None,winsound.SND_FILENAME)
        quitter()

def fin(a):     #Fonction qui génère l'écran de fin (aspect) et affiche un message de victoire ou de défaite
    reset()
    hideturtle()
    up()
    tracer(0)
    bgcolor('black')
    color('white')
    width(2)
    goto(0,100)
    write(a,False,"center",("Verdana",100,'normal','bold'))
    goto(-300,-200)
    write("Rejouer",False,"center",("Verdana",50,'normal','bold'))
    encadrement(350,75)
    goto(300,-200)
    write("Quitter",False,"center",("Verdana",50,'normal','bold'))
    encadrement(300,75)
    goto(0,-500)
    encadrement(1600,1000)
    update()

def restart():          #Fonction qui réinitialise toutes les tortues à leur état d'origine (au début du jeu)
    difficulte.up()
    difficulte.hideturtle()
    liste.up()
    liste.hideturtle()
    pion.up()
    pion.hideturtle()
    waiter.up()
    waiter.hideturtle()
    hp.up()
    hp.hideturtle()
    hpboss.up()
    hpboss.hideturtle()
    ht()
    up()


restart()
règles(regle.xcor(),0,450,129,34)       #On commence le jeu en affichant les règles
onkey(quitter,"Escape")             #A tout moment le joueur peut quitter le jeu en appuyant sur Echap
listen()                        #On met un listen() pour capturer l'appui sur une touche
