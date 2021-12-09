#Projet python de EL BACH Achraf et MANUEL Enzo.

from turtle import* #Module permettant le dessin du décor.
from polygone import*   #Module contenant différentes fonctions pratiques m'économisant beaucoup de lignes.
from JosephLeBoss import CAQUETUCE  #Module contenant les fonctions génératrices des cactus.

def fond(w,h):      #Cette fonction permet la génération du décor en fonction de la taille de la fenêtre (il se peut que les proportions ne soient pas bonnes pour les différents ordinateurs).
    tracer(0)       #La fonction tracer(0) => update() permet de tout afficher d'un coup.
    width(3)        #On définit l'épaisseur du crayon à 3 pixels pour que les traits se voient mieux.
    bouge(-w/2,-h/2)
    rectangle(h*3/4,w,"pale goldenrod",4)   #On dessine un rectangle de donnant un aspect sableux en fonction de la longueur et de la hauteur de la fenêtre.
    bouge(-w/2,1/4*h)
    rectangle(h*2/5,w,"light sky blue",4)   #Puis on dessine le ciel sur la partie restante.
    dalle(-w/2,h/4,h,w)                     #On dessine des lignes en perspecives donnant un aspect de chemin et de profondeur.
    route(-w/4,h/4,w,h)                     #On dessine une route en profondeur où se placeront les différents personnages.
    panneau(w/10,h/6,h,w)                   #Un simple panneau où est affiché le nom du jeu.
    CAQUETUCE()                             #Une génération de cactus différents dans des coordonnées aléatoire (à l'intérieur de certaines zones).
    afficheurTexte(w/10,-h/4,h/5,4*w/10)    #On dessine le cadre dans lequel sera affiché les phrases du scénario d'attaque.

    update()    #On affiche instantanément.

    
def dalle(x,y,h,w):     #Cette fonction permet de dessiner des lignes horizontales et verticales avec un aspect de profondeur, de perspective, avec un genre de point de fuite.
    seth(0)             #On réinitialise l'angle à sa valeur par défaut.
    color("black")
    l=0
    j=0
    while l>-3*h/4: #On dessine des lignes horizontales tant du bas de la fenêtre jusqu' la fin du sol.
        bouge(x,y+l)
        forward(10000)
        l=l-20*j/2  #Cette ligne permettant de déterminant l'écart entre les différentes lignes horizontales.
        j=j+1
        seth(0)
    bouge(-3000,h/4)
    forward(10000)
    bouge(-w/4,h/4)
    l=0
    i=0
    bouge(-w/4-40,h/4)
    trapeze(300,3*h/4,122,"pale goldenrod") #On dessine un trapeze qui de la couleur du sol pour effacer une partie des lignes ce qui permettra de donner un aspect de "trottoir" au bord des routes.
    while i<2:  #défaut : l<1500    #Cette partie permet de dessiner les lignes verticales en profondeur, au début il y en avait partout mais avec une on a trouvé ca plus beau. Mettez la valeur par défaut en conditions pour voir l'effet que ça fait.
        bouge(-w/4-l,h/4)       #Lignes verticales à gauche de la route
        left(240-2*i)
        forward(10000)
        seth(0)
        bouge(-w/4+220+l,h/4)   #Lignes verticales à droite de la route
        right(60-2*i)
        forward(10000)
        seth(0)
        l=l+40              #L'écart entre chaques lignes verticales.
        i=i+1
    color("black")
        

def route(x,y,w,h):     #La fonction permettant de dessiner la route sur laquelle se trouveront tous les personnages, prenant en paramètres les coordonnées et la taille de la fenêtre.
    bouge(x,y)
    trapeze(220,3*h/4,120,"grey")   #Le trapèze gris à la base la route, un trapèze et non un rectangle car ce n'est pas un mur mais une route en perspective.
    bouge(x+105,y)
    i=0
    j=10
    k=0
    l=0
    while l<3*h/4:      #On va dessiner la ligne pointillée présente sur certaines routes en dessinant une serie de trapeze pour donner un effet de profondeur.
        if k%2==0:
            down()
            color("orange") #On trapèze sur deux aura la couleur de la ligne pointillée.
            couleur="orange"
        else:
            up()
            color("grey")   #Tandis que l'autre prendra la couleur de la route afin de le rendre invisible et donc de faire une ligne pointillée.
            couleur="grey"
        i=i+5+k*2
        trapeze(j,i,95,couleur) #La petit côté du prochain trapèze est le grand côté du trapèze actuel, ce qui permet de créer une continuité avec des trapèzes, on change donc seulement la base et la hauteur.
        left(265)
        b=i/(cos((5)*3.14/180)) #regarder def trapeze dans polygone (trigonométrie)
        forward(b)              #On se déplace de la distance du côté non parallèle pour se mettre à la place du prochain trapèze
        seth(0)                #Et on réinitialise l'angle.
        c=(sin((5)*3.14/180))*b
        j=j+2*c
        k=k+1
        l=l+i
    down()


def panneau(x,y,h,w):       #Ce panneau n'est pas super utile, il affiche juste le nom du jeu pendant la partie.
    color("black")
    bouge(x,y)
    rectangle(100,10,"silver",4)        #Un simple assemblement de rectangles colorés.
    bouge(x+120,y)
    rectangle(100,10,"silver",4)
    bouge(x+240,y)
    rectangle(100,10,"silver",4)
    bouge(x+360,y)
    rectangle(100,10,"silver",4)
    seth(0)
    bouge(x-50,y+100)
    rectangle(160,480,"darkred",4)
    bouge(x-40,y+110)
    rectangle(140,460,"navajo white",4)
    color("sienna")                 #Cette couleur est celle du texte.
    bouge(x+190,y+200)
    write("Bazaris",align="center",font=("Verdana",30,"italic","bold"))     #On utlise la fonction write pour écrire avec turtle. Ici la police est "Verdana" de taille 30, en italique et en gras. Le texte est centrée.
    bouge(x+190,y+130)
    write("the bizarre adventures",align="center",font=("Arial",30,'italic','bold'))    #Ici on a juste changé la police à Arial, la différence est petite mais présente.
    color("black")


def afficheurTexte(x,y,h,w):    #Cette fonction dessine le cadre noir acceuillant le texte en fonction de la taille de la fenêtre.
    tracer()
    seth(0)
    color("black")
    bouge(x,y)
    rectangle(-h-30,w-40,"navajo white",4)
    bouge(x+5,y-5)
    rectangle(-h-20,w-50,"black",4)
    update()


