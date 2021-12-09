#Projet python de EL BACH Achraf et MANUEL Enzo.

from turtle import*
from random import*
from polygone import*
from time import*


hpboss=Turtle()
hpboss.hideturtle()
hpboss.up()
hpboss.speed(0)
hp=Turtle()
hp.hideturtle()
hp.up()
hp.speed(0)


def affpix(x,y,l,s,m,c,v,t):    #Fonction pour les graphismes en pixels
    tracer(0)
    up() 
    hideturtle() 
    shape('square') 
    shapesize(l/21)
    goto(x,y)
    cx=x
    cy=y
    k=0
    for i in c:
        if i==" ":
            forward(l)
        elif i=="1":
            goto(cx+(m[k]*l),cy)
            cy=cy+s*l
            k=k+1 
        else:
            color(t[v.index(i)])
            stamp() 
            forward(l)
    update()

def ailes(x,y,l):   #Fonction pour dessiner les ailes du boss dans la phase 3
    tracer(0)
    x=x+24*l
    ailed='1b1brb1brdb1bbrdrb1    brrvdrb1bbbb      rvdvrb1ffff      vvdvrb1bbb       vdvvrrb1      dvvvrrb      bbb1    dvvvrrrbb  bbrdb1 bfdvvvrrrrbbrrdb1bfdvvvrrrrrrdb1bfdvvvvvvvdrb1bfdvvvvddrrb1bfdvvdvvrb1bfdddvvvrb1bfdvvvrrb1bfdvvvrrb1bfdvvrrrrb1bfdvrrrrb1bfdvvrrrb1bfdvvrrrrb1bfdvvrrrrrbb1bfdvvrrrrrrrbbbb1bfdvvvrrrrrrrrdb1bfdvvvvvvvrdddb1bfddvvvvdddrrb1bfdddddvvrrb1bfdvvvvvrrrb1bfdvvvvvrrb1bfddvvvvvrrb1bffddvvvvvrb1bbffddvvvvvb1bbffddvvvvb1bbffddvvvb1bbffddvvb1bbffddvb1bbffdvb1bbfdvb1bbfdb1bbdb1bb'
    m=[0,-1,-2,-4,-9,-14,-14,-14,-10,-8,-6,-4,-3,-2,-1,-1,0,0,0,1,1,1,1,1,2,2,2,3,3,4,4,5,6,8,10,12,14,16,18,20,22,24,26]
    v=['d','r','v','b','f']
    t=['maroon','orange','red','black','firebrick']
    s=1
    affpix(x,y,l,s,m,ailed,v,t)
    aileg='1b1brb1 rdb1   drb1       vdrb1bbbb        dvrb1fff         dvrb1bbb         vvrrb1       vvvrrb      bbb1    dvvvrrrbb  bbrdb1 bfdvvvrrrrbbrrdb1bfdvvvrrrrrrdb1bfdvvvvvvvdrb1bfdvvvvddrrb1bfdvvdvvrb1bfdddvvvrb1bfdvvvrrb1bfdvvvrrb1bfdvvrrrrb1bfdvrrrrb1bfdvvrrrb1bfdvvrrrrb1bfdvvrrrrrbb1bfdvvrrrrrrrbbbb1bfdvvvrrrrrrrrdb1bfdvvvvvvvrdddb1bfddvvvvdddrrb1bfdddddvvrrb1bfdvvvvvrrrb1bfdvvvvvrrb1bfddvvvvvrrb1bffddvvvvvrb1bbffddvvvvvb1bbffddvvvvb1bbffddvvvb1bbffddvvb1bbffddvb1bbffdvb1bbfdvb1bbfdb1bbdb1bb'
    x=x-46*l
    affpix(x,y,-l,-s,m,aileg,v,t)
    update()

def cyberdemon(x,y,l):  #Fonction pour dessiner le boss
    x=x-8*l
    y=y+28*l
    boss='1dd1dd     d  d  d       d1ddd     ddddddd     ddd1vddd   ddmmdmmdd   dddd1vddddd ddmmdmmdd dddddd1vddddddddddmddddddddddd1vdddvdmvvdddddmvvdddv1vvv mmgmvddmgmm vvv1mmmgmvmgmmm1mmmmmmmmmmm     iii1d      dddkkmkkkmkkddd iisssii1dddd vddddkkrmrmrokddddmiisssi1d mvdddmvdddkkmormromokdddmiiisssi1dddmvddmvdddkkdkoookvokddmiiiiissi1vddmvdmmvdddkkkdkkkmokkddmiiiiiisi1mvdvddmmmvdddkklddmmkkdddmiiiiiisb1dmvdddddmmvddddimdmvddddddddiiiibbi1dvvdddddmvddddilidmmvddddddddibbissi1mmvvddddmvdlmliliddvdddddddd iiissi1mmmmmvvd vddddilidmddddddddd  iiissii1ddddmmmm  vdddddimdmmvddddddd  iiisssi1ddddmmmmm   mdddddlvmmvdddddm   iiiissi1dddmmmmmm   mmmdddvdmvddddmmm    iiissi1mdmmmmmm    mmmdvvdddmvdddmmm    iiiisi1mmmmmmmm     mmmddddddmvdmmm     iiiiib1dmmmmmmm       mmmmmmmmmmmmm     biiibbs1vdmmmmmm         vmmmmmmmd       ibbbissss1mvdmmmm         mvvdddddddm      iiiiiissssb1dmmvdmmm        imvvdddddddmm      iiiiiisssbb1mdddddm        iiimvvdddddmmdd      iiiiiisssbb1mmvddddd      iiiiimvvdddmmddd       iiiibbsssb1ddmvddddd      iiiissvvddmmddddd      iiiibbbssgs1mdddddddd      iiiissi   mvvdddd       iiiibgbbgi1mmmvddddd       iiiissi   mvvvddd       bbiiibggbi1dmvdddddd       iiiissi   dvvvdddd       bbiibggi1dvdmmdmdm       iiiissi    dvvvddd        bbggbi1dddmm mmm       iiiissi    dvvvdddd         iii1dddmmm mm       ibbbss      dvvvddd1dd mmm m        bissbs      dvvvddd1mm         biissib      dvvvmmd1biissib       dvmddmd1biissib       dmvdddm1biissib       mvvvddd1ibissbi       vmvvvdd1iibbbssi      vvmmmvd1iiiiissi      vvdddmv1iiiiissi      vvvdddmd1iiiiiissi     vvvvvddv1iiiiiissi     vvvddvvd1iiiiiissi     vvdddddd1iibbbissi     vvdddddd1bbiiibbsi     vvdddddd1issssiibi     vvddmmdd1iiissssib     mmmmddmm1iiiissssi     vddvdvdv1iiiiisssi    vddddvdvdv1iiiiisssi   vvddd v v v1'
    m=[0,-1,-2,-2,-2,-2,-1,0,4,4,-5,-5,-8,-8,-8,-8,-9,-9,-8,-9,-10,-11,-11,-11,-11,-12,-12,-12,-13,-13,-13,-14,-14,-15,-15,-15,-15,-15,-15,-11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    v=['g','d','m','v','k','r','o','l','i','s','b']
    t=['yellow','firebrick','crimson','maroon','orange','khaki','red','cyan','dim gray','silver','black']
    s=-1
    affpix(x, y, l, s, m, boss, v, t)

def encadrement(lo,la): #Fonction pour dessiner l'encadrement des choix dans le menu et l'écran de fin
    down()
    forward(lo/2)
    left(90)
    forward(la)
    left(90)
    forward(lo)
    left(90)
    forward(la)
    left(90)
    forward(lo/2)
    up()

def flamme(x,y,l):  #Fonction pour dessiner les flammes sur la tête du boss dans la phase 2
    x=x-1*l
    y=y+22*l
    flamme='1       1         1d         d1dr         rd1rror       orrd1rrroo rr rr orrrr1 ooooorrrrrrorrrr1rjooroorrrrrrorrr1rrjorrorrr rrorrr1rrooorrrrr  rjrr1rrjorrrrr  rrrr1rrjorrrrr   rr1rrjorrrr  rrr1rrjjrrrr  rr1rrorrrr  r1rjorrr r1rrorrr1rrjrr1rorr1rrrr1rrr1r1r'
    m=[0,-2,-3,-4,-5,-6,-6,-6,-6,-6,-5,-5,-4,-4,-3,-2,-2,-2,-1,-2,-2,-2,-3]
    v=['d','r','o','j']
    t=['crimson','red','orange','gold']
    s=1
    affpix(x,y,l,s,m,flamme,v,t)

def cactusb(x,y,l): #Fonction pour dessiner un cactus
    cactusb='1vv1fvvv1vvvv1vvvf1vvvv1vvvv1vvvv1vv vvvv     vv1vvv vfvv     vvf1vvf vvvv     vvv1vvv vvvv     vvv1vvv vvvv vv  vvv1vfv vvvv vvv vfv1vvvvvvfv vvv vvv1vvvvvvv fvv vvv1vfvvvvv vvv vvv1vv  vvvvvvv vvvvvvf1vvf  vvvvvvv vvvvvvv1vvv  vvvfvvv vvfvvvv1vvv  vvvvvvf vvvvvvv1vvvv  vvvvvv vvvvvfv1vfvv  vvvvvv vfvvvv1vvvvv fvvvvvvvvvvvv1vvvvvvvvvvvvvvvfv1vvfvvvvfvvfvvvv1vvvvvvvvvvvvv1vvvfvvvfvvvv1vvvvvvvvvv'
    m=[0,-1,-1,-1,-1,-1,-1,-4,-5,-5,-5,-5,-5,-5,-4,-4,-8,-9,-9,-9,-9,-9,-9,-8,-7,-6,-5,-4]
    v=['v','f']
    t=['lime green','green']
    s=-1
    affpix(x,y,l,s,m,cactusb,v,t)

def cactuss(x,y,l): #Fonction pour dessiner un autre cactus
    cactuss='1vff1fffff1vffff1ffffvff   ff1fvfffff  vff1fffffvf  ffff1f  fffffff  fffv1fff vffffff  ffff1ffv ffvffff  ffff1vfff fffffvf  ffff1ffvf fffffff  fvff1ffff fvfffff  ffff1ffff fffffff  fffv1ffff fffffvf  vfff1ffff ffvffff  ffff1fvfffffffffv fffvf1fffffffffffffffff1ffvffvffffffffff1ffffffffffvfff1ffffffffffff1ffffvff1vffffff1fffffff1fffffff1fffvffv1fvfffff1fffffff1fffffff1vfffvff1fffffff1vffffff1ffffffv'
    m=[0,-1,-1,-2,-2,-2,-5,-6,-6,-7,-7,-7,-7,-7,-7,-7,-7,-6,-5,-4,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2]
    v=['v','f']
    t=['lime green','green']
    s=-1
    affpix(x,y,l,s,m,cactuss,v,t)

def CAQUETUCE():    #Fonction pour dessiner 5 cactus à des emplacements aléatoires
    w=window_width()
    h=window_width()            #Les cactus se dessine à des endroits aléatoires de certaines de l'écran
    if randint(0,1)==0:
        cactuss(randint(-850,-700),randint(int(h/4-400),int(h/4-200)),4)
    else:
        cactusb(randint(-850,-700),randint(int(h/4-400),int(h/4-200)),4)
    if randint(0,1)==0:
        cactusb(randint(100,500),randint(150,250),4)
    else:
        cactuss(randint(100,500),randint(150,250),4)
    if randint(0,1)==0:
        cactusb(randint(700,850),randint(150,250),4)
    else:
        cactuss(randint(700,850),randint(150,250),4)
    if randint(0,1)==0:
        cactuss(randint(700,850),randint(-50,50),6)
    else:
        cactusb(randint(700,850),randint(-50,50),6)
    if randint(0,1)==0:
        cactusb(randint(200,500),randint(-50,50),6)
    else:
        cactuss(randint(200,500),randint(-50,50),6)
        

def hpbosss(x,y,n): #Fonction pour dessiner la barre de vie du boss
    tracer(0,100)
    hpboss.hideturtle()
    hpboss.speed('fastest')
    hpboss.color('black')
    hpboss.up()
    hpboss.goto(x-5,y-5)
    hpboss.down()
    seth(0)
    hpboss.begin_fill()
    for i in range(4):
        if int(i)%2==0:
            hpboss.forward(n+10)
            hpboss.left(90)
        else:
            hpboss.forward(40)
            hpboss.left(90)
    hpboss.end_fill()  
    hpboss.color('red')
    hpboss.up()
    hpboss.goto(x,y)
    hpboss.down()
    seth(0)
    hpboss.begin_fill()
    for i in range(4):
        if int(i)%2==0:
            hpboss.forward(n)
            hpboss.left(90)
        else:
            hpboss.forward(30)
            hpboss.left(90)
    hpboss.end_fill()
    update()

def hpp(x,y,n): #Fonction pour dessiner la barre de vie du joueur
    tracer(0,100)
    hp.hideturtle()
    hp.speed('fastest')
    hp.color('black')
    hp.up()
    hp.goto(x-5,y-5)
    hp.down()
    seth(0)
    hp.begin_fill()
    for i in range(4):
        if int(i)%2==0:
            hp.forward(n+10)
            hp.left(90)
        else:
            hp.forward(40)
            hp.left(90)
    hp.end_fill()  
    hp.color('lime green')
    hp.up()
    hp.goto(x,y)
    hp.down()
    seth(0)
    hp.begin_fill()
    for i in range(4):
        if int(i)%2==0:
            hp.forward(n)
            hp.left(90)
        else:
            hp.forward(30)
            hp.left(90)
    hp.end_fill()
    update()

def hplostbosss(x,y,n): #Fonction pour dessiner la perte de vie du boss
    tracer(0,100)
    hpboss.hideturtle()
    hpboss.speed('fastest')
    hpboss.color('maroon')
    hpboss.up()
    hpboss.goto(x+300,y)
    hpboss.down()
    seth(0)
    hpboss.begin_fill()
    for i in range(4):
        if int(i)%2==0:
            hpboss.left(90)
            hpboss.forward(30)
        else:
            hpboss.left(90)
            hpboss.forward(300-n)
    hpboss.end_fill()
    update()

def hplostt(x,y,n): #Fonction pour dessiner la perte de vie du joueur
    tracer(0,100)
    hp.hideturtle()
    hp.speed('fastest')
    hp.color('dark green')
    hp.up()
    hp.goto(x+300,y)
    hp.down()
    seth(0)
    hp.begin_fill()
    for i in range(4):
        if int(i)%2==0:
            hp.left(90)
            hp.forward(30)
        else:
            hp.left(90)
            hp.forward(300-n)
    hp.end_fill()
    update()
    

