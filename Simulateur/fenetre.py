import pygame
from Menu import Menu
from Niveau import Niveau
from options import Options
from levelselection import LevelSelection
from FinNiveau import FinNiveau


class Fenetre :
    def __init__(self,nomFenetre,taille):
        pygame.init()
        
        self.nomFenetre=nomFenetre
        self.taille=taille
        self.afficher=False
        pygame.display.set_caption(self.nomFenetre)
        
        self.screen = pygame.display.set_mode((self.taille[0],self.taille[1]),pygame.SCALED)
        
        # pygame.display.toggle_fullscreen()
         
    def setBackground(self,image,game):
        self.background = pygame.image.load(image).convert()
        self.background = pygame.transform.scale(self.background, (self.taille[0],self.taille[1]))
        self.rectBackground= self.background.get_rect()
        game.blit(self.background, (0,0))
    

    def setAnImage(self,image,uneTaille,position,game):
        uneImage = pygame.image.load(image)
        uneImage = pygame.transform.scale(uneImage, (uneTaille[0],uneTaille[1] ))
        rectImage=uneImage.get_rect()
        
        var ={
            "image" : uneImage,
            "rectImage" : rectImage,
            "position" : {
                "x": position[0]-uneTaille[0]/2,
                "y": position[1]-uneTaille[1]/2
            }
        }
        game.blit(var["image"], (var["position"]["x"],var["position"]["y"])) 
        return var

    def setBouton(self,image,imageHover,imageOnclick,uneTaille,position,game):
        uneImage = pygame.image.load(image)
        uneImage = pygame.transform.scale(uneImage, (uneTaille[0],uneTaille[1] ))
        rectImage = uneImage.get_rect()
        rectImage=rectImage.move(position[0]-uneTaille[0]/2,position[1]-uneTaille[1]/2)


        uneImageHover = pygame.image.load(imageHover)
        uneImageHover = pygame.transform.scale(uneImageHover, (uneTaille[0],uneTaille[1] ))
        rectImageHover = uneImageHover.get_rect()
        rectImageHover=rectImageHover.move(position[0]-uneTaille[0]/2,position[1]-uneTaille[1]/2)

        uneImageOnclick = pygame.image.load(imageOnclick)
        uneImageOnclick = pygame.transform.scale(uneImageOnclick, (uneTaille[0],uneTaille[1] ))
        rectImageOnclick = uneImageOnclick.get_rect()
        rectImageOnclick=rectImageOnclick.move(position[0]-uneTaille[0]/2,position[1]-uneTaille[1]/2)

        

        if rectImage.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()==(True,False,False):
                game.blit(uneImageOnclick, (position[0]-uneTaille[0]/2,position[1]-uneTaille[1]/2))
            else:
                game.blit(uneImageHover, (position[0]-uneTaille[0]/2,position[1]-uneTaille[1]/2))        
        else :
            game.blit(uneImage, (position[0]-uneTaille[0]/2,position[1]-uneTaille[1]/2))
        
        var ={
            "bouton" : {
                "image": uneImage,
                "rect": rectImage
            },
            "boutonHover" : {
                "image": uneImageHover,
                "rect": rectImageHover
            },
            "boutonOnclick" : {
                "image": uneImageOnclick,
                "rect": rectImageOnclick
            },

            "position" : {
                "x": position[0]-uneTaille[0]/2,
                "y": position[1]-uneTaille[1]/2
            }
        }
        return var

    def drawRectTXT(self,taille,position,couleur,texte,tailleTXT,couleurTXT,fenetre):
        rectangle=pygame.draw.rect(game.screen,couleur, (position[0],position[1], taille[0], taille[1]),border_radius = 15)
        font=pygame.font.Font("src/font/RammettoOne-Regular.ttf", tailleTXT) 
           
        text = font.render(texte,1,couleurTXT)
        size=font.size(texte)
        fenetre.blit( text, ( rectangle.center[0]-size[0]/2  , rectangle.center[1]-size[1]/2 ) )
 
        var ={
            "rectangle" :rectangle,
            "position" : {
                "x": position[0]-taille[0]/2,
                "y": position[1]-taille[1]/2
            }
        }
        return var
        
                            
    def drawRect(self,taille,position,couleur,fenetre):
        rectangle=pygame.draw.rect(game.screen,couleur, (position[0],position[1], taille[0], taille[1]),border_radius = 35)
        return rectangle
        



game=Fenetre("Game",[1320,700])
boucle=True
actualScreen="Menu"
frame_per_second = pygame.time.Clock()
firstSentence= True
phrase=""
morceau=""
point=0
humeur=""
while boucle:
    frame_per_second.tick(60)

    if actualScreen=="Menu":
        menuObject=Menu(game)
        boucle=menuObject.boucle
        actualScreen=menuObject.actualScreen
        firstSentence= True
        


    elif actualScreen=="Niveau1":
        NiveauObject=Niveau(game,firstSentence,phrase,morceau,point,humeur,"Niveau1")
        boucle=NiveauObject.boucle
        actualScreen=NiveauObject.actualScreen
        firstSentence = NiveauObject.firstSentence
        phrase = NiveauObject.phrase
        morceau= NiveauObject.morceau
        point= NiveauObject.point
        humeur= NiveauObject.humeur

    elif actualScreen=="Niveau2":
        NiveauObject=Niveau(game,firstSentence,phrase,morceau,point,humeur,"Niveau2")
        boucle=NiveauObject.boucle
        actualScreen=NiveauObject.actualScreen
        firstSentence = NiveauObject.firstSentence
        phrase = NiveauObject.phrase
        morceau= NiveauObject.morceau
        point= NiveauObject.point
        humeur= NiveauObject.humeur

    elif actualScreen=="FinNiveau":
        menuObject=FinNiveau(game,point)
        boucle=menuObject.boucle
        actualScreen=menuObject.actualScreen
        
        
    
    elif actualScreen=="Options":
        menuObject=Options(game)
        boucle=menuObject.boucle
        actualScreen=menuObject.actualScreen

    elif actualScreen=="LevelSelection":
        menuObject=LevelSelection(game)
        boucle=menuObject.boucle
        actualScreen=menuObject.actualScreen
                        

    
    
