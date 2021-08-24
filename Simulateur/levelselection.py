import pygame
import json

class LevelSelection:
    def __init__(self,game):
        doc = json.load(open("listeLVL.json", "r"))
        game.setBackground("src/image/BackgroundMenu.jpg",game.screen)
        imageTitre=game.setAnImage("src/image/LevelSelection.png",[477, 160],(game.rectBackground.center[0],game.taille[1] - game.taille[1]*0.8),game.screen)
        self.boucle=True
        self.actualScreen="LevelSelection"
        BoutonNiveau1=game.setBouton("src/image/BoutonNiveau1.png","src/image/BoutonNiveau1Hover.png","src/image/BoutonNiveau1Onclick.png",[285 , 75],( game.taille[0]- game.taille[0] * 0.75 , game.rectBackground.center[1] ),game.screen)
        if doc["Niveau1"] == 0:
            game.setAnImage("src/image/0etoile.png",[285 , 75],( game.taille[0]- game.taille[0] * 0.75 , game.rectBackground.center[0] * 0.75 ),game.screen)
        elif doc["Niveau1"] == 1:
            game.setAnImage("src/image/1etoile.png",[285 , 75],( game.taille[0]- game.taille[0] * 0.75 , game.rectBackground.center[0] * 0.75 ),game.screen)
        elif doc["Niveau1"] == 2:
            game.setAnImage("src/image/2etoile.png",[285 , 75],( game.taille[0]- game.taille[0] * 0.75 , game.rectBackground.center[0] * 0.75 ),game.screen)
        elif doc["Niveau1"] == 3:
            game.setAnImage("src/image/3etoile.png",[285 , 75],( game.taille[0]- game.taille[0] * 0.75 , game.rectBackground.center[0] * 0.75 ),game.screen)
        BoutonNiveau2=game.setBouton("src/image/BoutonNiveau2.png","src/image/BoutonNiveau2Hover.png","src/image/BoutonNiveau2Onclick.png",[285 , 75],( game.taille[0]- game.taille[0] * 0.5 , game.rectBackground.center[1] ),game.screen)
        if doc["Niveau2"] == 0:
            game.setAnImage("src/image/0etoile.png",[285 , 75],( game.taille[0]- game.taille[0] * 0.5 , game.rectBackground.center[0] * 0.75 ),game.screen)
        elif doc["Niveau2"] == 1:
            game.setAnImage("src/image/1etoile.png",[285 , 75],( game.taille[0]- game.taille[0] * 0.5 , game.rectBackground.center[0] * 0.75 ),game.screen)
        elif doc["Niveau2"] == 2:
            game.setAnImage("src/image/2etoile.png",[285 , 75],( game.taille[0]- game.taille[0] * 0.5 , game.rectBackground.center[0] * 0.75 ),game.screen)
        elif doc["Niveau2"] == 3:
            game.setAnImage("src/image/3etoile.png",[285 , 75],( game.taille[0]- game.taille[0] * 0.5 , game.rectBackground.center[0] * 0.75 ),game.screen)
        BoutonNiveau3=game.setBouton("src/image/BoutonNiveau3.png","src/image/BoutonNiveau3Hover.png","src/image/BoutonNiveau3Onclick.png",[285 , 75],( game.taille[0]- game.taille[0] * 0.25 , game.rectBackground.center[1] ),game.screen)
        if doc["Niveau3"] == 0:
            game.setAnImage("src/image/0etoile.png",[285 , 75],( game.taille[0]- game.taille[0] * 0.25 , game.rectBackground.center[0] * 0.75 ),game.screen)
        elif doc["Niveau3"] == 1:
            game.setAnImage("src/image/1etoile.png",[285 , 75],( game.taille[0]- game.taille[0] * 0.25 , game.rectBackground.center[0] * 0.75 ),game.screen)
        elif doc["Niveau3"] == 2:
            game.setAnImage("src/image/2etoile.png",[285 , 75],( game.taille[0]- game.taille[0] * 0.25 , game.rectBackground.center[0] * 0.75 ),game.screen)
        elif doc["Niveau3"] == 3:
            game.setAnImage("src/image/3etoile.png",[285 , 75],( game.taille[0]- game.taille[0] * 0.25 , game.rectBackground.center[0] * 0.75 ),game.screen)
        BoutonRetour=game.setBouton("src/image/BoutonRetour.png","src/image/BoutonRetourHover.png","src/image/BoutonRetourOnClick.png",[285 , 75],(game.rectBackground.center[0], game.taille[1]-game.taille[1] * 0.11),game.screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Si l'event est QUIT alors on quitte la boucle et on ferme la fenetre
                self.boucle=False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_focused:
                    if BoutonRetour["bouton"]["rect"].collidepoint(pygame.mouse.get_pos()):
                        if pygame.mouse.get_pressed()==(True,False,False):
                            self.actualScreen="Menu"
                    if BoutonNiveau1["bouton"]["rect"].collidepoint(pygame.mouse.get_pos()):
                        if pygame.mouse.get_pressed()==(True,False,False):
                            self.actualScreen="Niveau1"
                    if BoutonNiveau2["bouton"]["rect"].collidepoint(pygame.mouse.get_pos()):
                        if pygame.mouse.get_pressed()==(True,False,False):
                            self.actualScreen="Niveau2"
                    if BoutonNiveau3["bouton"]["rect"].collidepoint(pygame.mouse.get_pos()):
                        if pygame.mouse.get_pressed()==(True,False,False):
                            self.actualScreen="Menu"
