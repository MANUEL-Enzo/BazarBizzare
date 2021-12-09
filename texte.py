#Projet python de EL BACH Achraf et MANUEL Enzo.

from random import*
from turtle import*
from polygone import*
from time import*

passer = Turtle()
passer.up()
passer.ht()

def scenar(boss,total,x,solution,couleurs,classes):     #La fonction permet de générer les phrases selon la situation ,elle prend en entrée le temps de réaction et la réponse du boss, notre temps de réaction, le pion choisi, la réponse correcte et les listes de classes et couleurs
    r1=random()                                     #On définit 3 variables qui vont permettre d'insérer une part d'aléatoire dans la génération de phrases
    r2=random()                                         #Dans les différentes situations il y aura différentes possibilités de phrases, seulement une choisie au hasard sera générée
    r3=random()
    if total>boss[0]:                               #Dans le cas où l'IA a répondu plus vite que le joueur :
        if r1<1/3:                                              #Ce procédé se répétera tout au long de la fonction pour les différentes situations donc je ne vais pas le répéter à chaque utilisation :
                tex1="Trop lent malheureusement..."                 #   On prend une des variables aléatoires et on fait des catégories possédant chacune la même probabilité de choix.
        elif r1>1/3 and r1<2/3:                                     #   On ne réutilise pas la même variable aléatoire pour différentes catégories consécutives, c'est pour cette raison que nous en avons 3.
                tex1="Une vraie course contre la montre..."         #   Cela permet d'obtenir un maximum de combinaisons de phrases possibles.
        else:                                                   #Ce procédé de hasard permet d'éviter cette sensation de déjà vu et le fait que le joueur peut se lasser vite, à la place il découvrira différentes phrases pour une meilleur expérience de jeu.
                tex1="Il est question de vitesse ici..."
        if r2<1/3:                                              #Ici on utilise la deuxième variable aléatoire comme dit précédemment.
            tex2="On dirait que Josephin est plus rapide."
        elif r2>1/3 and r2<2/3:                                 #On définit au fur et à mesure la combinaisons de phrases composé de 5 phrases, 5 variable "tex"+indice.
            tex2="Josephin t'as bien devancé."
        else:
            tex2="Pas au niveau de Josephin apparemment..."
        if boss[1]:                                     #Dans le sous cas où l'IA a réussi son attaque :
            score=0                                         #Le joueur n'inflige aucun dégats
            scoreboss=int(1000/boss[0])                     #Tandis que Josephin inflige des dégâts proportionnels à son temps de réaction
            if r3<1/3:                                                  #Utilisation de la troisième variable aléatoire
                tex3="Il vous attaque d'une vivacité phénoménale."
            elif r3>1/3 and r3<2/3:
                tex3="Il distrait vos compagnons avec une pierre et vous attaque."
            else:
                tex3="Ses sbires vous sautent dessus ne vous laissant pas le temps de vous défendre."
            tex4="Il vous inflige alors "+str(scoreboss)+" dégats."         #On génére une phrase permettant d'informer le joueur du nombre de dégâts causés
            tex5="On se reprend oh !"                                       #Et un petit message de motivation
        else:                                           #Dans le sous cas où l'IA a raté son attaque :
            score=150                                       #Le boss s'inflige 150 dégâts
            scoreboss=0                                     #Et il n'inflige aucun dégâts
            tex3="Heuresement pour toi il ne maîtrise pas ce qu'il fait."
            if r3<1/3:
                tex4="Dans le feu de l'action il s'inflige 150 dégats."
            elif r3>1/3 and r3<2/3:
                tex4="Il invoque un sbire insolent qui se rebelle et lui inflige 150 dégats."
            else:
                tex4="Il fonce vers vous, trébuche bêtement, et se prend 150 dégats."   #Petit message informant des dégâts qu'il s'est infligé
            tex5="C'est une chance qui n'arrive pas souvent."
    else:                                           #Dans le cas où l'on réponds plus vite que Josephin :
        if r1<1/3:
            tex1="Vous attaquez par preuve de supériorité."
        elif r1>1/3 and r1<2/3:
            tex1="Un gain de courage prend le contrôle de votre corps."
        else:
            tex1="Une soudaine envie de casser des bouches vous gagne."
        tex2="Vous décidez de l'attaquer sans détour."
        if solution==[couleurs[x-1],classes[x-1]]:      #Dans le sous cas où nous avons choisi le bon pion:
            score=int(1000/total)                           #Nous infligeons des dégâts proportionnels à notre temps de réaction à Josephin
            scoreboss=0                                     #Et nous ne recevons aucun dégats
            #Les phrases généré dans le cas où nous répondont vont dépendre du pion que nous avons choisi car c'est assez classe, il y a différentes possibilités de combinaisons de phrases pour chacune des classes
            if x==1:            #Dans le cas où le pion choisi est la robot :
                if r2<1/3:
                    tex3="Chargée d'essence, cette bête charge férocement les ennemis."                     #Une combinaison est composée d'une phrase originale
                    tex4="Le tas de boulon et de vis inflige "+str(score)+" dégats à Josephin."             #   ainsi que d'une phrase informant le joueur du nombre de dégâts infligés
                elif r2>1/3 and r2<2/3:
                    tex3="L'humanité a peur que les robots prennent le dessus... c'est le cas."
                    tex4="Son bras s'allonge jusqu'à Josephin et lui inflige "+str(score)+" dégats."
                else:
                    tex3="Du métal, un ennemi et une rage combattive, voilà la recette de la victoire."
                    tex4="Ce robot met toute sa force dans un coup et inflige "+str(score)+" dégats à Josephin."
            elif x==2:          #Dans le cas où le pion choisi est la mage :
                if r2<1/3:
                    tex3="Les meilleurs mages ne sont pas nécessairement à Poudlard."
                    tex4="Un sort explosif renverse les ennemis et inflige "+str(score)+" dégats à Josephin."
                elif r2>1/3 and r2<2/3:
                    tex3="Sabrina l'apprenti sorcière est devenu plutôt balèze apparemment..."
                    tex4="Un petit coup de baguette suffit à infliger "+str(score)+" dégats à Josephin."
                else:
                    tex3="Une aura étrange et puissante émane de cette mage, un sort violent se prépare."
                    tex4="Un torrent de feu rase tout sur son passage et inflige "+str(score)+" dégats à Josephin."
            elif x==3:          #Dans le cas où le pion choisi est le pistolero :
                if r2<1/3:
                    tex3="Il tire plus vite que son ombre et touche plus d'une cible."
                    tex4="Une balle, un travail fini en plus de "+str(score)+" dégats infligés à Josephin."
                elif r2>1/3 and r2<2/3:
                    tex3="Les ennemis s'apprêtent à découvrir qui est le meilleur tireur de l'Ouest."
                    tex4="Il tire du coin de l'oeil et inflige directement "+str(score)+" dégats à Josephin."
                else:
                    tex3="Bien des astuces cette homme cache sous sa cape, il sort un deuxième pistolet."
                    tex4="Il décime tous les ennemis en quelques coup et inflige "+str(score)+" dégats à Josephin."
            elif x==4:          #Dans le cas où le pion choisi est le guerrier :
                if r2<1/3:
                    tex3="Epée éclatante et force colossale suffisent à terrasser une équipe."
                    tex4="Les sbires décampent vite et ce berserk inflige "+str(score)+" dégats à Josephin."
                elif r2>1/3 and r2<2/3:
                    tex3="Ce personnage ressemble étrangement à un personnage de jeu vidéo..."
                    tex4="Peu importe... il attaque et inflige "+str(score)+" dégats à Josephin."
                else:
                    tex3="Fier guerrier, il ne peut accepter la défaite. Ce n'est pourtant qu'un simple jeu pour lui."
                    tex4="Il joue de son épée pour vaincre et infliger "+str(score)+" dégats à Josephin."
            elif x==5:          #Dans le cas où le pion choisi est le bonhomme de neige :
                if r2<1/3:
                    tex3="Simple, enfantin et pourtant tellement dangereux."
                    tex4="Tel une avalanche ce tas de neige inflige "+str(score)+" dégats à Josephin."
                elif r2>1/3 and r2<2/3:
                    tex3="Vive le vent, vive le vent, il est temps de montrer qui est le boss (figurativement)."
                    tex4="Il fait un bonhomme de neige, le lance sur Josephin et lui inflige "+str(score)+" dégats."
                else:
                    tex3="Nöel arrive, et votre cadeau sera une douce victoire mes amis."
                    tex4="Vous offrez un cadeau piégé et infligez "+str(score)+" dégats à Josephin."
            else:               #Dans le cas où le pion choisi est le moine combattant :
                if r2<1/3:
                    tex3="Ce jeune moine ne s'est pas durement entrainé des années pour rien."
                    tex4="Jackie Chan terrasse les sbires et inflige "+str(score)+" dégats à Josephin."
                elif r2>1/3 and r2<2/3:
                    tex3="Il possède la parfaite harmonie de tous les arts martiaux de ce monde."
                    tex4="Il dit des mots chinois et inflige à Josephin "+str(score)+" dégats avec son pied du dragon."
                else:
                    tex3="Ce moine prend son temps pour cirer son crâne afin d'aveugler les ennemis."
                    tex4="Il profite de l'occasion et inflige "+str(score)+" dégats à Josephin."
            if r3<1/3:
                tex5="Continuez ainsi si vous souhaitez sortir de ce cauchemar."
            elif r3>1/3 and r3<2/3:
                tex5="Encore quelques efforts, on y arrive progressivement."
            else:
                tex5="Si proche mais pourtant si loin, ne lâche rien."
        else:                                   #Dans le cas où nous avons choisi le mauvais pion :
            score=0                                 #Nous n'infligeons aucun dégâts
            scoreboss=150                           #Nous recevons 150 dégâts
            if x==1:            #Dans le cas où le pion choisi est la robot :
                tex3="Vous rencontrez enfin votre ennemi de tous les temps, un virus."                      #Les combinaisons de phrases sont similaires à celles présentés précedemment
                tex4="Pris par la folie ce robot attaque son propriétaire et vous inflige 150 dégats."
            elif x==2:          #Dans le cas où le pion choisi est la mage :
                tex3="La magie est parfois une épée à double tranchant, à utliser précautionneusement."
                tex4="La vie vous explose violemment au visage et vous inflige 150 dégats."
            elif x==3:          #Dans le cas où le pion choisi est le pistolero :
                tex3="En essayant d'impressionner l'ennemi celui-ci fait tourner son pistolet."
                tex4="Il vous tire dans le pied par accident et vous inflige 150 dégats."
            elif x==4:          #Dans le cas où le pion choisi est le guerrier :
                tex3="On peut le dire c'est un homme assez fort, mais une épée c'est lourd."
                tex4="Il swing l'épée et vous tombe dessus vous infligeant alors 150 dégats."
            elif x==5:          #Dans le cas où le pion choisi est le bonhomme de neige :
                tex3="La neige... bah... c'est froid... Et ce bonhomme de neige est gentil..."
                tex4="Il essaie de vous faire un calin et vous inflige 150 dégats. Assez refroidissant."
            else:               #Dans le cas où le pion choisi est le moine combattant :
                tex3="Vous donnez un ordre au moine au crâne brillant... mais il médite."
                tex4="Les sbires en profitent pour s'avancer et vous inflige 150 dégats."
            if r2<1/3:
                tex5="On dirait bien que vous êtes votre propre ennemi."
            if r2>1/3 and r2<2/3:
                tex5="Il faut savoir gérer son équipe pour gagner..."
            else:
                tex5="Ne perds pas face à tes compagnons ce serait humiliant..."
    return [score,scoreboss,tex1,tex2,tex3,tex4,tex5]                   #On renvoie en sortie les dégâts infligés, alliés ou ennemis, ainsi que le set de 5 phrases choisi aléatoirement

def ecriture(t,w,h):            #Cette fonction permet d'écrire une phrase progressivement et avec beauté, elle prend en entrée le texte et la résolution de la fenêtre
    seth(0)
    bouge(w/10+10,-h/4-10)      #On se déplace à l'intérieur du cadre d'affichage du texte
    color("white")              #Texte blanc sur fond noir comme on l'adore
    e=0                         #Cette variable va réprésenter la "longueur" de la ligne et va faire fluctuer la position x de lettre
    l=0                         #Cette variable va faire fluctuer la position y de la ligne lorsque on passe à la ligne
    a=0.03                      #Cette variable est la période d'attente de base entre l'écriture de chaque lettre
    bouge(5000,0)                   #Cette ligne va nous servir de point de sauvegarde pour effacer la phrase plus tard sans avoir besoin de la recouvrir
    for i in range(len(t)):         #On va décortiquer la phrase d'entrée et générer la phrase lettre par lettre pour donner l'aspect progressif d'un jeu de rôle
        if passer.xcor()==10:           #Lorsqu'on appuie sur espace, on passe la phrase et donc on casse la boucle pour arrêter l'écriture et éventuellement générer la prochaine
            break
        elif passer.xcor()==5:          #Lorsqu'on maintient appuyé la barre espace, on réduit la période d'attente entre les lettres ce qui permet d'accélérer l'affichage du texte
            a=0
        bouge(w/10+30+e,-h/4-60-l)                          #On se déplace à l'endroit de la lettre correspondante, avec x et y qui fluctuent
        write(t[i],font=("Fixedsys",20,"normal"))           #On écrit la lettre avec la fonction "write()" avec une jolie police
        sleep(a)                                            #L'attente entre chaque lettre est réalisé grace à la fonction "sleep()"
        if t[i]!="i" and t[i]!="I" and t[i]!="l" and t[i]!="1":             #Ces caractères sont plus fins donc pour un meilleur aspect visuel on réduit l'écart de la prochaine lettre pour éviter un gros vide
            e=e+20
        else:
            e=e+15
        if e>(4*w/10-300) and t[i]==" ":                    #Cette condition permet de passer la ligne si on se rapproche de la fin du cadre, on passe à la ligne après un espace pour ne pas casser les mots
            l=l+40
            e=0

def affichage(w,h,a,b,c,d,e):       #Cette fonction permet de générer les phrases du set l'une après l'autre, elle prend en entrée la résolution de la fenêtre et le set de phrases
    color("white")
    onkeypress(accelT,'space')
    onkeyrelease(finT,'space')
    bouge(w/10+10,-h/2+30)                                                              #On met au bas de l'écran les petites indication pratiques pour passer et accélérer le texte
    write("Maintenez ESPACE pour accélérer",font=("Fixedsys",10,"normal"))
    bouge(w/2-56,-h/2+30)
    write("Appuyez sur ESPACE pour passer la phrase",False,"right",font=("Fixedsys",10,"normal"))
    listen()        #Cette commande permet de capturer le moment de l'appui de touche
    tracer(0,100)       #Cette fonction va permettre de construire un sablier infini qui attendra la réponse du joueur en bougeant une turtle
    if a!="":               #Première phrase du set
        ecriture(a,w,h)         #Ecriture de la phrase
        pause()                     #Fonction qui permet d'attendre la réponse du joueur pour passer la phrase afin qu'il soit tranquille dans lecture et aussi d'effacer la phrase 
        if b!="":               #Deuxième phrase
            ecriture(b,w,h)     #On répète le même procédé sur les autres phrases
            pause()
            if c!="":               #Troisième phrase
                ecriture(c,w,h)
                pause()
                if d!="":               #Quatrième phrase
                    ecriture(d,w,h)
                    pause()
                    if e!="":               #Cinquième phrase
                        ecriture(e,w,h)
                        pause()

def pause():        #Cette fonction permet d'attendre la réponse du joueur et d'effacer la phrase
    while passer.xcor()!=10:        #Boucle agissant comme un sablier infini
        passer.forward(-1)
        update()
    while xcor()!=5000:             #On efface tous les tracés depuis le point de sauvegarde que nous avons mis en place avant d'écrire la phrase dans le cadre
        undo()
    passer.setx(0)                  #On réinitialise la turtle pour qu'elle soit utilisable pour la prochaine phrase

def accelT():           #Cette fonction s'active quand on maintient la barre espace appuyée, elle permet d'accélerer la génération de texte en positionnant une turtle à un endroit particulier
    passer.setx(5)

def finT():             #Cette fonction s'active quand on relache la barre espace, elle permet de passer à la phrase suivante
    passer.setx(10)

