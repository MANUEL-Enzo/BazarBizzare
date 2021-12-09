#Projet python de EL BACH Achraf et MANUEL Enzo.

from turtle import*            #Voici les modules qu'on a eu besoin d'importer 
from polygone import*           #Parmi eux se trouve le module de fonctions pratiques "polygone" permettant de se déplacer et de dessiner des formes plus aisément tout en économisant des lignes
from random import*                 #C'est assez dur de commenter du simple dessin donc ce module ne sera pas réellement commenter car on utilise uniquement des fonctions basiques de turtle

################# Personnage : Robot ##################################################################################################################################################################################################################

def jambeRobot(x,y,a):       #Fonction réprésentant le dessin des deux jambes avec comme paramètres : les coordonnées et le facteur de taille.
    bouge(x,y+50*a)     #La fonction bouge est une fonction pratique se trouvant dans le module polygone qui me permet de déplacer ma turtle.
    triangleIso(30*a,40*a,"grey")   #La fonction triangleIso est une fonction pratique qui se trouve dans le module polygone me permettant de dessiner un triangle isocèle.
    bouge(xcor(),y)
    cercle(10*a,360,"black")        #La fonction cercle est une fonction pratique du module polygone me permettant d'économiser des lignes au cours de la colorisation d'un cercle.
    bouge(x+15*a,y+50*a)            
    rectangle(50*a,-30*a,"grey",4)  #La fonction rectangle est une fonction pratique du module polygone me permettant de dessiner un rectangle.
    #Roue
    bouge(x,y+85*a)
    cercle(20*a,360,"grey")

def brasRobot(x,y,sens,couleur,a):   #Contrairement aux jambes, la fonction de dessin des bras a en paramètres le sens et la couleur en plus.
    seth(0)                     #Je reinitialise l'angle avec seth(0), la turtle se dirige vers l'Est.
    bouge(x-100*a,y+240*a)      #Le bras est une simple ligne de carré avec un cercle à la fin.
    right(155-sens)             #Le sens permet simplement de différencier le bras gauche du bras droit.
    polygone(30*a,4,"grey")     #Honnêtement je trouve peu à commenter...
    left(45)
    forward(30*sqrt(2)*a)
    right(45)
    polygone(30*a,4,"grey")
    left(45)
    forward(30*sqrt(2)*a)
    backward(10*sqrt(2)*a)
    right(90)
    cercle(20*a,360,couleur)

def robo(x,y,couleur,a):      #La fonction permettant d'assembler tous les éléments
    color("black")
    #Les jambes
    jambeRobot(x-20*a,y,a)
    jambeRobot(x+20*a,y,a)
    #La jupe
    bouge(x-20*a,y+160*a)
    trapeze(40*a,50*a,130,couleur)
    rectangle(20*a,40*a,"pink",4)
    #Les bras
    brasRobot(x+60*a,y,0,couleur,a)
    brasRobot(x+140*a,y,45,couleur,a)
    #Le haut de corps
    bouge(x-20*a,y+180*a)
    trapeze(40*a,-80*a,60,couleur)
    #Antenne
    bouge(x,y+260*a)
    triangleIso(20*a,-100*a,"grey")
    #Tête
    cercle(30*a,360,"grey")
    #Cou
    backward(20*a)
    rectangle(15*a,40*a,"grey",4)
    #Boule d'antenne
    bouge(x,y+340*a)
    cercle(10*a,360,"red")

################# Personnage : Mage ##################################################################################################################################################################################################################

def madameForte(x,y,couleur,a):     #Le premier personnage fait donc le moins optimal.
    color("black")
    bouge(x,y)
    #Jambe 1 couleur
    fillcolor(couleur)
    begin_fill()
    forward(62*a)
    circle(15*a,180)
    forward(20*a)
    right(90)
    forward(100*a)
    circle(30*a,10)
    forward(100*a)
    left(80)
    forward(60*a)
    left(90)
    circle(200*a,35)
    right(35)
    forward(118*a)
    left(90)
    end_fill()
    #Jambe 2 couleur
    bouge(x+27*a,y+235*a)
    begin_fill()
    right(65)
    forward(100*a)
    circle(-40*a,90)
    forward(100*a)
    left(65)
    forward(30*a)
    circle(-15*a,180)
    forward(62*a)
    right(60)
    forward(100*a)
    right(70)
    circle(175*a,-40)
    left(80)
    forward(72*a)
    end_fill()
    #Ventre
    rectangle(35*a,-72*a,"navajo white",4)
    left(90)
    #Sceptre
    bouge(x+120*a,y+100*a)
    rectangle(-20*a,300*a,"gold",6)
    left(90)
    forward(-10*a)
    cercle(20*a,360,"cyan")
    left(90)
    #Torse
    bouge(x+29*a,y+270*a)
    fillcolor(couleur)
    begin_fill()
    forward(30*a)
    right(90)
    circle(30*a,25)
    right(240)
    forward(40*a)
    left(180)
    forward(120*a)
    left(35)
    forward(40*a)
    left(90)
    forward(30*a)
    left(90)
    forward(40*a)
    right(45)
    forward(100*a)
    circle(60*a,45)
    forward(35*a)
    circle(15*a,90)
    forward(80*a)
    circle(30*a,45)
    left(135)
    forward(75*a)
    left(180)
    forward(65*a)
    end_fill()
    #Cou
    bouge(x-35*a,y+377*a)
    left(90)
    rectangle(a*10,a*40,"navajo white",3)
    #Cheveux
    bouge(x-45*a,y+380*a)
    fillcolor("black")
    begin_fill()
    left(180)
    forward(60*a)
    circle(-20*a,90)
    forward(30*a)
    circle(-20*a,70)
    circle(200*a,20)
    end_fill()
    left(50)
    #Chapeau (ou non)
    if random() <= 1/2:
        bouge(x-10*a,y+455*a)
        triangleIso(40*a,-80*a,couleur)
        ellipse(80*a,10*a,couleur)


################# Personnage : Pistolero ##################################################################################################################################################################################################################

def homFor(x,y,couleur,a):  #Ce personnage n'est pas fait avec des formes élémentaires mais il est beau.
    color("black")
    up()
    goto(x,y)
    down()
    #Jambe 1
    rectangle(100*a,40*a,couleur,4)
    begin_fill()
    left(90)
    circle(200*a,30)
    right(120)
    forward(30*a)
    end_fill()
    rectangle(80*a,35*a,"midnight blue",6)
    #Jambe 2
    up()
    goto(x+100*a,y)
    down()
    fillcolor(couleur)
    begin_fill()
    forward(-30*a)
    circle(-20*a,-180)
    forward(-10*a)
    right(45)
    circle(60*a,-110)
    left(130)
    forward(-50*a)
    right(90)
    forward(100*a)
    left(60)
    forward(85*a)
    end_fill()
    forward(-85*a)
    right(60)
    forward(-100*a)
    rectangle(40*a,-60*a,"midnight blue",4)
    right(65)
    #Cheveux
    up()
    goto(x+70*a,y+510*a)
    down()
    left(180)
    cercle(40*a,360,"grey")
    left(180)
    #Echarpe
    up()
    goto(x+20*a,y+500*a)
    down()
    rectangle(-30*a,-100*a,"purple",4)
    #Chapeau
    up()
    goto(x,y+570*a)
    down()
    rectangle(-30*a,-140*a,"saddle brown",4)
    up()
    goto(x+40*a,y+585*a)
    down()
    right(90)
    rectangle(-60*a,60*a,"saddle brown",3)
    right(180)
    #Bras
    up()
    goto(x+210*a,y+390*a)
    down()
    left(50)
    rectangle(-30*a,-120*a,"burlywood",6)
    left(180)
    forward(20*a)
    rectangle(-20*a,-100*a,"black",4)
    right(50)
    #Cape qui est un enchaînement de courbe pour un aspect des plus délicieux.
    up()
    goto(x+38*a,y+180*a)
    down()
    color("black")
    left(20)
    fillcolor(couleur)
    begin_fill()
    circle(-180*a,50)
    right(130)
    circle(140*a,100)
    circle(-80*a,150)
    left(60)
    circle(-80*a,90)
    circle(-500*a,40)
    right(90)
    circle(-200*a,30)
    circle(80*a,85)
    right(25)
    end_fill()
    left(160)


################# Personnage : Guerrier ##################################################################################################################################################################################################################

def jambeGuerrier(x,y,couleur,a):
    bouge(x,y+100*a)
    triangleIso(60*a,70*a,couleur)
    bouge(x-20*a,y)
    polygone(40*a,4,"black")
    bouge(x-30*a,y+100*a)
    trapeze(60*a,-100*a,100,couleur)
    

def cloud(x,y,couleur,a):
    color("black")
    #Les jambes
    jambeGuerrier(x-30*a,y,couleur,a)
    jambeGuerrier(x+30*a,y,couleur,a)
    #Bassin
    bouge(x,y+170*a)
    fillcolor=couleur
    begin_fill()
    circle(60*a,360,steps=5)    #J'utilise la fonction circle() pour faire un pentagone avec l'argument steps=5 (pour cinq côtés)
    end_fill()
    #Cou
    bouge(x,y+420*a)
    triangleIso(30*a,-40*a,"navajo white")
    #Mèches de cheveux
    bouge(x,y+500*a)
    triangleIso(30*a,-60*a,"gold")
    for i in range(3):
        right(30)
        triangleIso(30*a,-50*a,"gold")
        forward(15*a)
    bouge(x,y+500*a)
    seth(0)
    backward(15*a)
    left(40)
    triangleIso(40*a,-60*a,"gold")
    #Tête
    seth(0)  
    bouge(x,y+430*a)
    cercle(40*a,360,"gold")
    #Bras gauche + épée
    bouge(x-110*a,y+296*a)
    seth(0)
    left(5)
    ellipse(40*a,100*a,"navajo white")
    bouge(x-124*a,y+390*a)
    left(90)
    forward(20*a)
    triangleIso(20*a,-40*a,"silver")
    right(90)
    forward(20*a)
    rectangle(40*a,240*a,"silver",4)
    forward(240*a)
    left(90)
    forward(20*a)
    triangleIso(40*a,50*a,"silver")
    right(90)
    bouge(x-124*a,y+390*a)
    cercle(20*a,360,"navajo white")
    bouge(x-50*a,y+400*a)
    seth(0)
    left(150)
    ellipse(55*a,120*a,"navajo white")
    #Bras gauche
    seth(0)
    bouge(x+50*a,y+390*a)
    right(170)
    ellipse(55*a,120*a,"navajo white")
    #Haut du corps + ceinture
    bouge(x-30*a,y+280*a)
    trapeze(60*a,-140*a,70,couleur)
    trapeze(60*a,-20*a,70,"red")


################# Personnage : Bonhomme de neige ##################################################################################################################################################################################################################

def snowy(x,y,couleur,a):
    color("black")
    seth(0)
    #Première boule de neige
    bouge(x,y)
    ellipse(240*a,180*a,couleur)
    #Bras gauche
    bouge(x-60*a,y+250*a)
    left(120)
    rectangle(20*a,80*a,"saddle brown",6)
    left(60)
    rectangle(60*a,20*a,"saddle brown",6)
    left(10)
    rectangle(-50*a,20*a,"saddle brown",4)
    left(80)
    ellipse(10*a,50*a,"saddle brown")
    left(60)
    ellipse(10*a,40*a,"saddle brown")
    left(90)
    forward(40*a)
    right(180)
    ellipse(10*a,30*a,"saddle brown")
    #Bras droit
    seth(0)
    bouge(x+60*a,y+250*a)
    left(40)
    rectangle(20*a,80*a,"saddle brown",5)
    right(60)
    rectangle(20*a,60*a,"saddle brown",6)
    rectangle(20*a,-50*a,"saddle brown",4)
    left(140)
    ellipse(10*a,40*a,"saddle brown")
    seth(0)
    #Deuxième boule de neige
    bouge(x,y+160*a)
    ellipse(160*a,120*a,couleur)
    #Tête
    bouge(x,y+270*a)
    cercle(60*a,360,couleur)
    #Chapeau
    bouge(x-60*a,y+370*a)
    rectangle(20*a,120*a,"black",4)
    bouge(x-30*a,y+380*a)
    rectangle(80*a,60*a,"black",4)
    bouge(x-30*a,y+380*a)
    rectangle(20*a,60*a,"red",6)
    seth(0)


################# Personnage : Moine combattant ##################################################################################################################################################################################################################

def avatar(x,y,couleur,a):
    color("black")
    #Jambe droite
    bouge(x+50*a,y)
    seth(0)
    parallelogramme(40*a,40*a,60,3,"black")
    forward(40*a)
    right(10)
    rectangle(-30*a,-40*a,"black",7)
    rectangle(-40*a,80*a,"navajo white",5)
    backward(40*a)
    right(130)
    ellipse(50*a,130*a,couleur)
    #Jambe gauche
    bouge(x-30*a,y)
    seth(0)
    rectangle(60*a,-40*a,"black",6)
    rectangle(-100*a,-40*a,"navajo white",4)
    bouge(x-50*a,y+130*a)
    seth(0)
    right(15)
    ellipse(50*a,120*a,couleur)
    #Tête
    seth(0)
    bouge(x-10*a,y+420*a)
    rectangle(40*a,20*a,"navajo white",4)
    bouge(x,y+440*a)
    ellipse(60*a,80*a,"navajo white")
    bouge(x-30*a,y+490*a)
    rectangle(10*a,60*a,"red",4)
    left(80)
    ellipse(10*a,40*a,"red")
    left(40)
    ellipse(10*a,40*a,"red")
    
    #Bras gauche
    bouge(x-110*a,y+296*a)
    seth(0)
    left(5)
    ellipse(35*a,100*a,"navajo white")
    bouge(x-135*a,y+390*a)
    seth(0)
    rectangle(50*a,30*a,"navajo white",5)
    rectangle(-20*a,10*a,"navajo white",4)
    bouge(x-45*a,y+400*a)
    seth(0)
    left(150)
    ellipse(45*a,120*a,"navajo white")
    seth(0)
    #Bras droit
    bouge(x+100*a,y+470*a)
    seth(0)
    ellipse(35*a,100*a,"navajo white")
    bouge(x+45*a,y+390*a)
    right(30)
    ellipse(45*a,120*a,"navajo white")
    bouge(x+85*a,y+570*a)
    seth(0)
    rectangle(50*a,30*a,"navajo white",4)
    rectangle(10*a,-20*a,"navajo white",4)
    
    #Tunique
    bouge(x-30*a,y+280*a)
    trapeze(60*a,-140*a,80,couleur)
    trapeze(60*a,-20*a,80,"red")
    trapeze(60*a,90*a,110,couleur)
    forward(60*a)
    right(120)
    ellipse(10*a,40*a,"red")
    left(40)
    ellipse(10*a,40*a,"red")

    seth(0)
