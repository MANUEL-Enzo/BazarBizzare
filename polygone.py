#Projet python de EL BACH Achraf et MANUEL Enzo.

from turtle import*
from math import*

def polygone(l,n,c):    #La simple fonction polygone faite et refaite en TD.
    fillcolor(c)
    begin_fill()
    a=360/n
    i=0
    while i<n:
        forward(l)
        left(a)
        i=i+1
    end_fill()

def triangleIso(a,h,couleur):   #Une fonction permettant la construction d'un triangle isocèle à partir de sa base, de sa hauteur et de sa couleur.
    fillcolor(couleur)
    begin_fill()
    angle1=(atan(2*h/a))*180/3.14   #L'angle à la base calculé par trigonométrie.
    angle2=360-2*angle1             #L'angle à la pointe.
    b=h/(sin(angle1*3.14/180))  #Le calcul du côté des deux côtés égaux par pure trigonométrie
    forward(a/2)                #On commence au milieu pour un meilleur aspect donc on avance d'une demie base.
    right(180-angle1)           
    forward(b)
    left(angle2)
    forward(b)
    right(180-angle1)
    forward(a/2)
    end_fill()

def rectangle(l,L,c,n):     #Une fonction permettant de dessiner un rectangle, de le remplir et en plus de repasser sur ses traits pour finir sur un meilleur angle du rectangle (pour éviter de rebouger).
    j=1
    fillcolor(c)            
    begin_fill()
    while j<=n:
        if j%2==0:          #On alterne entre longueur et largeur avec un modulo de 2.
            forward(l)
        else:
            forward(L)
        left(90)
        j=j+1
    end_fill()

def cercle(r,a,couleur):    #Cette fonction me permet simplement d'économiser des lignes (3) sur le remplissage d'un cercle dessiné avec circle().
    fillcolor(couleur)
    begin_fill()
    circle(r,a)
    end_fill()

def bouge(x,y):             #Cette fonction sauve ma santé mentale en évitant de répéter le même patterne de 3 lignes pour bouger sa turtle à une autre position ce qui m'économise 2 lignes.
    up()
    goto(x,y)
    down()

def trapeze(a,h,angle,couleur):     #Cette fonction dessine un trapèze à partir de sa base (petit côté), de sa hauteur, de son angle d'ouverture et de sa couleur de remplissage. Tout ça en calcul trigonométrique.
    seth(0)
    fillcolor(couleur)
    begin_fill()
    forward(a)                      #Ceci est le petit côté.
    right(180-angle)
    b=h/(cos((angle-90)*3.14/180))  #Côté non parallèle à son oppos
    forward(b)
    c=(sin((angle-90)*3.14/180))*b  #Fragments du côté opposé à la base représentant en quelque sorte la base des triangles rectangles voisin du rectangle central. 
    x=(acos(c/b))*180/3.14
    right(180-x)
    d=2*c+a                         #Le côté opposé à la base de la taille de la base plus l'excés de longueur à chaque extrémité.
    forward(d)
    right(180-x)
    forward(b)
    right(180-angle)
    end_fill()
    
def ellipse(l,h,couleur):       #Cette fonction dessine une ellipse à partir de sa longueur et de sa hauteur (largeur), et de sa couleur de remplissage.
    fillcolor(couleur)
    begin_fill()
    if l>h:                     #Il y a deux cas : la longueur et plus grande que la hauteur et le cas inverse.
        for i in range(2):      #Dans le cas où la longueur est plus grande que la hauteur, on commence par les milieu est on dessine un cercle applati, le même patterne se répétant par symétrie.
            forward(l/2-h/2)
            circle(h/2,180)
            forward(l/2-h/2)
    else:
        for i in range(2):      #Dans le cas où la hauteur est plus grande que la longueur, on comme par l'extremité de l'ellipse et on dessine comme un cercle allongé vers le haut, encore une fois un patterne répété deux fois.
            circle(l/2,90)
            forward(h-l)
            circle(l/2,90)          
    end_fill()                  #Ces deux cas me facilitent la construction de certaines choises car elle m'offre plus de libertés et m'économise d'éventuels surplus de lignes.

def parallelogramme(b,h,a,n,couleur):       #Cette fonction dessine un prallèlogramme à partir de la base, de l'angle, de la hauteur, de la couleur de remplissage et un paramètre me permettant de repasser sur mes traits pour mieux me positionner
    fillcolor(couleur)
    begin_fill()
    for i in range(n):  #On dessine les deux côtés différents deux fois pour dessiner un parallèlogramme, si n>2 c'est pour me placer à un angle particulier du parallèlogramme pour m'éviter un déplacement en une ligne inutile.
        forward(b)
        left(180-a)
        forward(h/(sin((a)*3.14/180)))
        left(a)
    end_fill()          #Je n'ai malheureusement utilisé cette fonction qu'une seule fois pour dessiner le moine. Mais elle est là si j'en ai besoin un jour.

