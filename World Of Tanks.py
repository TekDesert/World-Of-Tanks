# Créé par simons, le 09/02/2018 en Python 3.2

import pygame
from math import sqrt

pygame.init() # initialisation du module "pygame"

fenetre = pygame.display.set_mode( (1600,800), pygame.RESIZABLE )

pygame.display.set_caption("World of Tanks")

fond = pygame.image.load("ecran accueil.jpg").convert()
angle = 0
vieTank1 = 8
vieTank2 = 8
imgbackground = pygame.image.load("background.jpg").convert()
imgbackground = pygame.transform.scale(imgbackground, (1600, 800))
imgmur = pygame.image.load("mur.png").convert()
boule = pygame.image.load("boule.png").convert()
imgoption = pygame.image.load("menu option.jpg").convert()
couleurtank1= 1
couleurtank2 = 2

imgtank1 = pygame.image.load("Tank 1 1.png").convert()
imgtank2 = pygame.image.load("Tank 2 2.png").convert()

imgcanon1 = pygame.image.load("Cannon 1 1.png").convert()
imgcanon2 = pygame.image.load("Cannon 2 2.png").convert()


explosion_anim = []

for i in range(9):
    filename = 'regularExplosion0'+str(i)+'.png'
##    img = pygame.image.load(filename).convert()
##    explosion_anim.append(img)

angle2 = 0
angle = 0

# On dÃ©finit les variables qui contiendront les positions des diffÃ©rents Ã©lÃ©ments (vaisseau, alien, projectile)
# Chaque position est un couple de valeur '(x,y)'
positionTank1 = (300,611)
positionTank2 = (1200,611)
positionBouleTank1 = (positionTank1[0]+192, positionTank1[1]-angle+15)
positionBouleTank2 = (positionTank2[0]+192, positionTank2[1]-angle+15)
deplaceBoule1 = 0
deplaceBoule2 = 0
trajectoireBoule1 = 0
trajectoireBoule2 = 0
cptTrajectoire1 = 0
cptTrajectoire2 = 0
ProjectileNb = 0
option = 0
score = 0
projectiledispo1 = 30
projectiledispo2 = 30
tankOneRotation = 0
tankOneRotation2 = 0

imageVie1 = pygame.image.load("8hp.png").convert()
imageVie2 = pygame.image.load("8hp.png").convert()

 #Texts
white=(255,255,255)
black = (0,0,0)
font = pygame.font.SysFont("ArcadeClassic", 27)
texteprojectiledispo1 = font.render("Obus restants  "+ str(projectiledispo1), 1, black)
texteprojectiledispo2 = font.render("Obus restants  "+ str(projectiledispo2), 1, black)



p = (0,0) #position souris


fond = pygame.transform.scale(fond , (1600, 800))

def initJeux():
    global angle, angle2, positionTank1, positionTank2, positionBouleTank1, positionBouleTank2, projectiledispo1, projectiledispo2, imageVie1, imageVie2, vieTank1, vieTank2, imgbackground
    angle = 0
    positionTank2 = (1200,611)
    positionBouleTank1 = (positionTank1[0]+192, positionTank1[1]-angle+15)
    positionBouleTank2 = (positionTank2[0]+192, positionTank2[1]-angle+15)
    projectiledispo1 = 30
    projectiledispo2 = 30
    vieTank1 = 8
    vieTank2 = 8
    imageVie1 = pygame.image.load("8hp.png").convert()
    imageVie2 = pygame.image.load("8hp.png").convert()
    imgbackground = pygame.image.load("background.jpg").convert()
    Musique = pygame.mixer.music.load('MusicEcran.mp3')
    pygame.mixer.music.play(-1)
    imgbackground = pygame.transform.scale(imgbackground, (1600, 800))



def modifierCouleurTank():
    global couleurtank1, couleurtank2, imgtank1, imgtank2, imgcanon1, imgcanon2
    #Choix de la couleur du tank en fonction du choix dans les options
    if couleurtank1 == 1:
        imgtank1 = pygame.image.load("Tank 1 1.png").convert()
    if couleurtank1 == 2:
        imgtank1 = pygame.image.load("Tank 1 2.png").convert()
    if couleurtank1 == 3:
        imgtank1 = pygame.image.load("Tank 1 3.png").convert()
    if couleurtank2 == 1:
        imgtank2 = pygame.image.load("Tank 2 1.png").convert()
    if couleurtank2 == 2:
        imgtank2 = pygame.image.load("Tank 2 2.png").convert()
    if couleurtank2 == 3:
        imgtank2 = pygame.image.load("Tank 2 3.png").convert()
    if couleurtank1 == 1:
        imgcanon1 = pygame.image.load("Cannon 1 1.png").convert()
    if couleurtank1 == 2:
        imgcanon1 = pygame.image.load("Cannon 1 2.png").convert()
    if couleurtank1 == 3:
        imgcanon1 = pygame.image.load("Cannon 1 3.png").convert()
    if couleurtank2 == 1:
        imgcanon2 = pygame.image.load("Cannon 2 1.png").convert()
    if couleurtank2 == 2:
        imgcanon2 = pygame.image.load("Cannon 2 2.png").convert()
    if couleurtank2 == 3:
        imgcanon2 = pygame.image.load("Cannon 2 3.png").convert()

#Affichage de l'écriture
def affichageMenu():
    fenetre.blit(fond, (0,0))

def gererClavierEtSouris2():
    global continuer,option,couleurtank1,couleurtank2
    for event in pygame.event.get():

        if event.type == pygame.QUIT: # Permet de gÃ©rer un clic sur le bouton de fermeture de la fenÃªtre
            continuer = 0
            touchesPressees = pygame.key.get_pressed()
            Musique = pygame.mixer.music.load('MusicEcran.mp3')
            pygame.mixer.music.play(-1)

        if pygame.mouse.get_pressed()[0]:

          p=pygame.mouse.get_pos()

          if 430>p[0]>90 and 435>p[1]>120:
                print("couleur 1")
                couleurtank1=1
                modifierCouleurTank()
                option = 0
                affichageMenu()

          if 955>p[0]>607 and 469>p[1]>120:
                print("couleur 2")
                couleurtank1=2
                modifierCouleurTank()
                option = 0
                affichageMenu()

          if 1500>p[0]>1153 and 469>p[1]>120:
                print("couleur 3")
                couleurtank1=3
                modifierCouleurTank()
                option = 0
                affichageMenu()

          if 218>p[0]>0 and 70>p[1]>0:
                option = 0
                affichageMenu()
                print("option quit")


def gererClavierEtSourisMenu():
    global continuer, fenetre, option
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Permet de gÃ©rer un clic sur le bouton de fermeture de la fenÃªtre
            continuer = 0
    # Gestion du clavier:
    touchesPressees = pygame.key.get_pressed()
    if touchesPressees[pygame.K_SPACE] == True:
        fenetre.blit(fond, (1600,800))
    if option == 1 :
        fenetre = pygame.display.set_mode( (1600,800) )
        fenetre.blit(imgoption, (0,0))
        pygame.display.update()
        font = pygame.font.SysFont("arial", 27)
        gererClavierEtSouris2()

    if pygame.mouse.get_pressed()[0]:

        p=pygame.mouse.get_pos()

        #Jouer
        if 957>p[0]>596 and 464>p[1]>370:
            gestionPartie()
            fenetre = pygame.display.set_mode( (1600,800) ) # CrÃ©ation d'une fenÃªtre graphique de taille 600x600 pixels
            pygame.display.set_caption("Marouan Laroui TO2") # DÃ©finit le titre de la fenÃªtre

        #Quit
        p=pygame.mouse.get_pos()
        if 957>p[0]>596 and 530>p[1]>469:
            continuer = 0
            pygame.quit()

        #Options
        if 957>p[0]>596 and 630>p[1]>530:
            option = 1
            fenetre = pygame.display.set_mode( (1600,800) )
            fenetre.blit(imgoption, (0,0))
            pygame.display.update()
            font = pygame.font.SysFont("arial", 27)
            gererClavierEtSouris2()
            print("options")






def dessiner():
    global imgtank1, fenetre, imageVie1, imageVie2, angle,imgcanon1,imgtank2,projectiledispo1,projectiledispo2,texteprojectiledispo1,texteprojectiledispo2
    # On remplit complÃ¨tement notre fenÃªtre avec la couleur noire: (0,0,0)
    # Ceci permet de 'nettoyer' notre fenÃªtre avant de la dessiner
    fenetre.blit(imgbackground, (0,0))
    fenetre.blit(imgtank1, positionTank1)# On dessine l'image du vaisseau Ã  sa position
    fenetre.blit(imageVie1, ( positionTank1[0] + 39, positionTank1[1] -65))
    fenetre.blit(imgtank2, positionTank2)# On dessine l'image du vaisseau Ã  sa position
    fenetre.blit(imageVie2, ( positionTank2[0] + 39, positionTank2[1] -65))
    fenetre.blit(imgmur, (750,505))
    texteprojectiledispo1 = font.render("Obus restants  "+ str(projectiledispo1), 1, black)
    texteprojectiledispo2 = font.render("Obus restants  "+ str(projectiledispo2), 1, black)
    fenetre.blit(texteprojectiledispo1, (10,10))
    fenetre.blit(texteprojectiledispo2, (1370,10))

# Fonction en charge de gÃ©rer les Ã©vÃ¨nements clavier (ou souris)
# Cette fonction sera appelÃ©e depuis notre boucle infinie
def gererClavierEtSouris():
    global imgcanon1, positionVaisseau, angle, positionTank1,positionTank2, tankOneRotation, tankOneRotation2, imgcanon2, angle2, boule, positionBouleTank1, deplaceBoule1, trajectoireBoule1
    global cptTrajectoire1,  positionBouleTank2, deplaceBoule2, trajectoireBoule2, cptTrajectoire2, explosion_anim, imageVie1, imageVie2, vieTank1, vieTank2,projectiledispo1,projectiledispo2
    press = pygame.key.get_pressed()
    #Gestion clavier deplacement tank

    #tank 1

    if positionTank1[0]<560:
        if press[pygame.K_d]:
         positionTank1 = ( positionTank1[0] + 5 , positionTank1[1] )
    if positionTank1[0] >0 :
        if press[pygame.K_a]:
         positionTank1 = ( positionTank1[0] - 5 , positionTank1[1] )


    if press[pygame.K_w]:
            if(angle > 50):
                angle = 50
            angle += 1
            imgRotation = pygame.transform.rotate(imgcanon1,angle)
            imgRotation.set_colorkey((255,255,255))
            fenetre.blit(imgRotation, (positionTank1[0]+96 , positionTank1[1]-angle+15))
            tankOneRotation = 1
    if press[pygame.K_s]:
            if(angle <= 0):
                angle = 0
            angle -= 1
            imgRotation = pygame.transform.rotate(imgcanon1,angle)
            imgRotation.set_colorkey((255,255,255))
            fenetre.blit(imgRotation, (positionTank1[0]+96 , positionTank1[1]-angle+15))
            tankOneRotation = 1



    if (tankOneRotation == 1) :
            imgRotation = pygame.transform.rotate(imgcanon1,angle)
            imgRotation.set_colorkey((255,255,255))
            fenetre.blit(imgRotation, (positionTank1[0]+96 , positionTank1[1]-angle+15))

    else :
        imgcanon1.set_colorkey((255,255,255))
        fenetre.blit(imgcanon1, (positionTank1[0]+96 , positionTank1[1]+15))


    #TANK 2
    if positionTank2[0]<1400 :
        if press[pygame.K_RIGHT]:
         positionTank2 = ( positionTank2[0] + 5 , positionTank2[1] )
    if positionTank2[0] >813:
        if press[pygame.K_LEFT]:
         positionTank2 = ( positionTank2[0] - 5 , positionTank2[1] )


    if press[pygame.K_UP]:
            if(angle2 < -50):
                angle2 = -50
            angle2 -= 1
            imgRotation2 = pygame.transform.rotate(imgcanon2,angle2)
            imgRotation2.set_colorkey((255,255,255))
            fenetre.blit(imgRotation2, (positionTank2[0]+5, positionTank2[1]+angle2+15))
            tankOneRotation2 = 1
    if press[pygame.K_DOWN]:
            if(angle2 >= 0):
                angle2 = 0
            angle2 += 1
            imgRotation2 = pygame.transform.rotate(imgcanon2,angle2)
            imgRotation2.set_colorkey((255,255,255))
            fenetre.blit(imgRotation2, (positionTank2[0]+5, positionTank2[1]+angle2+15))
            tankOneRotation2 = 1

    if (tankOneRotation2 == 1) :
            imgRotation2 = pygame.transform.rotate(imgcanon2,angle2)
            imgRotation2.set_colorkey((255,255,255))
            fenetre.blit(imgRotation2, (positionTank2[0]+5, positionTank2[1]+angle2+15))

    else :
        imgcanon2.set_colorkey((255,255,255))
        fenetre.blit(imgcanon2, (positionTank2[0]+5, positionTank2[1]+15))


    #Tank1 Projectiles
    if press[pygame.K_LSHIFT] and projectiledispo1>0 and deplaceBoule1 == 0:
        Musique = pygame.mixer.music.load('Tank shot.mp3')

        pygame.mixer.music.play(0)
        positionBouleTank1 = (positionTank1[0]+192, positionTank1[1]-angle)
        deplaceBoule1 = 1
        trajectoireBoule1 = 0
        projectiledispo1= projectiledispo1-1

    if(deplaceBoule1 == 1):

        if(trajectoireBoule1 == 0):
            fenetre.blit(boule, (positionBouleTank1[0], positionBouleTank1[1]))
            positionBouleTank1 = (positionBouleTank1[0]+7, positionBouleTank1[1]-3)

        if(positionBouleTank1[1] < 450 and trajectoireBoule1 == 0):
            trajectoireBoule1 = 1

        if(trajectoireBoule1 == 1):
            fenetre.blit(boule, (positionBouleTank1[0], positionBouleTank1[1]))
            positionBouleTank1 = (positionBouleTank1[0]+7, positionBouleTank1[1]-0.5)
            cptTrajectoire1 = cptTrajectoire1 + 1
            if(cptTrajectoire1 == 20):
                trajectoireBoule1 = 2
                cptTrajectoire1 = 0

        if(trajectoireBoule1 == 2):
            fenetre.blit(boule, (positionBouleTank1[0], positionBouleTank1[1]))
            positionBouleTank1 = (positionBouleTank1[0]+7, positionBouleTank1[1]+0.5)
            cptTrajectoire1 = cptTrajectoire1 + 1
            if(cptTrajectoire1 == 20):
                trajectoireBoule1 = 3
                cptTrajectoire1 = 0

        if(trajectoireBoule1 == 3):
            fenetre.blit(boule, (positionBouleTank1[0], positionBouleTank1[1]))
            positionBouleTank1 = (positionBouleTank1[0]+7, positionBouleTank1[1]+3)
            if positionTank2[0]<positionBouleTank1[0]<positionTank2[0]+192 :
                if positionTank2[1]<positionBouleTank1[1]<positionTank2[1]+96:
                    print("Touché!")
                    vieTank2 = vieTank2 - 1
                    imageVie2 = pygame.image.load(str(vieTank2)+"hp.png").convert()
                    for i in range (9):
                        print("image explosion" + str(i))
##                        fenetre.blit(explosion_anim[i], (positionBouleTank1[0], positionBouleTank1[1]))
                    Musique = pygame.mixer.music.load('impact.mp3')
                    pygame.mixer.music.play(0)
                    positionBouleTank1 = (-2,-2)



            if positionBouleTank1[1] > 700:
                positionBouleTank1 = (-2,-2)

        #Touche mur
        if positionBouleTank1 [0] > 730 and positionBouleTank1[0] < 800  and positionBouleTank1[1] > 500  :
            print("mur")
            print(positionBouleTank1)
            deplaceBoule1 = 0

         #Sort de ecran
        if positionBouleTank1[0]> 1590 or positionBouleTank1[1] > 800 or positionBouleTank1[1] < 0 :
            print("sortie ecran")
            print(positionBouleTank1)
            deplaceBoule1 = 0


    #Tank2 Projectiles
    if press[pygame.K_RSHIFT] and projectiledispo2>0  and deplaceBoule2 == 0:
        Musique = pygame.mixer.music.load('Tank shot.mp3')
        pygame.mixer.music.play(0)
        positionBouleTank2 = (positionTank2[0], positionTank2[1]+angle2)
        deplaceBoule2 = 1
        trajectoireBoule2 = 0
        projectiledispo2=projectiledispo2-1

    if(deplaceBoule2 == 1):

        if(trajectoireBoule2 == 0):
            fenetre.blit(boule, (positionBouleTank2[0], positionBouleTank2[1]))
            positionBouleTank2 = (positionBouleTank2[0]-7, positionBouleTank2[1]-3)

        if(trajectoireBoule2 == 1):
            fenetre.blit(boule, (positionBouleTank2[0], positionBouleTank2[1]))
            positionBouleTank2 = (positionBouleTank2[0]-7, positionBouleTank2[1]-0.5)
            cptTrajectoire2 = cptTrajectoire2 + 1
            if(cptTrajectoire2 == 20):
                trajectoireBoule2 = 2
                cptTrajectoire2 = 0

        if(trajectoireBoule2 == 2):
            fenetre.blit(boule, (positionBouleTank2[0], positionBouleTank2[1]))
            positionBouleTank2 = (positionBouleTank2[0]-7, positionBouleTank2[1]+0.5)
            cptTrajectoire2 = cptTrajectoire2 + 1
            if(cptTrajectoire2 == 20):
                trajectoireBoule2 = 3
                cptTrajectoire2 = 0

        if(trajectoireBoule2 == 3):
            fenetre.blit(boule, (positionBouleTank2[0], positionBouleTank2[1]))
            positionBouleTank2 = (positionBouleTank2[0]-7, positionBouleTank2[1]+3)

            if positionTank1[0]<positionBouleTank2[0]<positionTank1[0]+192 :
                if positionTank1[1]<positionBouleTank2[1]<positionTank1[1]+96:
                    print("Touché!")
                    vieTank1 = vieTank1 - 1
                    imageVie1 = pygame.image.load(str(vieTank1)+"hp.png").convert()
                    for i in range (9):
                        print("image explosion" + str(i))
##                        fenetre.blit(explosion_anim[i], (positionBouleTank2[0], positionBouleTank2[1]))
                    Musique = pygame.mixer.music.load('impact.mp3')
                    pygame.mixer.music.play(0)
                    positionBouleTank2 = (-2,-2)

        if(positionBouleTank2[1] < 450 and trajectoireBoule2 == 0):
            trajectoireBoule2 = 1

        #Touche mur
        if positionBouleTank2 [0] > 730 and positionBouleTank2[0] < 800  and positionBouleTank2[1] > 500  :
            print("mur")
            print(positionBouleTank2)
            deplaceBoule2 = 0

         #Sort de ecran
        if positionBouleTank2[0]> 1590 or positionBouleTank2[1] > 800 or positionBouleTank2[1] < 0 :
            print("sortie ecran")
            print(positionBouleTank2)
            deplaceBoule2 = 0

def gestionMenu():
    global continuer
    continuer = 1
    while continuer == 1:
        pygame.display.update()
        affichageMenu()
        gererClavierEtSourisMenu()

def gestionPartie():
    global continuer, clock, vieTank1, vieTank2, positionTank1, positionTank2, imgbackground
    continuer = 1
    while continuer==1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = 0
        clock.tick(60)
        dessiner()
        gererClavierEtSouris()
        white = (255,255,255)
        black =(0,0,0)

        if vieTank1==0:
                positionTank1=(0,1200)
                imgbackground = pygame.image.load("background win 2 " + str(couleurtank2) +".jpg").convert()
                pygame.display.update()
                if pygame.mouse.get_pressed()[0]:

                     p=pygame.mouse.get_pos()

                     #Rejouer
                     if 957>p[0]>638 and 360>p[1]>324:
                        initJeux()
                        gestionPartie()

                     #Quit
                     if 957>p[0]>638 and 424>p[1]>376:
                        initJeux()
                        affichageMenu()
                        gestionMenu()

        if vieTank2==0:
                positionTank2=(0,1200)
                imgbackground = pygame.image.load("background win 1 " + str(couleurtank1) +".jpg").convert()
                pygame.display.update()
                if pygame.mouse.get_pressed()[0]:
                     p=pygame.mouse.get_pos()

                     #Rejouer
                     if 957>p[0]>638 and 360>p[1]>324:
                        initJeux()
                        gestionPartie()

                     #Quit
                     if 957>p[0]>638 and 424>p[1]>376:
                        initJeux()
                        affichageMenu()
                        gestionMenu()

        pygame.display.update()

#Ecran fin du jeux


clock = pygame.time.Clock()

font = pygame.font.SysFont("ArcadeClassic", 27)

#Le son

Musique = pygame.mixer.music.load('MusicEcran.mp3')
pygame.mixer.music.play(-1)

gestionMenu()

pygame.display.flip()

gestionPartie()

print("quit")
pygame.quit()



