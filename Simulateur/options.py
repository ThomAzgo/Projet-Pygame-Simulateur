import pygame
import json
class Options:
    def __init__(self,game):
        game.setBackground("src/image/bg.png",game.screen)
        imageTitre=game.setAnImage("src/image/Options.png",[278, 160],(game.rectBackground.center[0],game.taille[1] - game.taille[1]*0.77),game.screen)
        self.boucle=True
        self.actualScreen="Options"
        BoutonPleinEcran=game.setBouton("src/image/BoutonPleinEcran.png","src/image/BoutonPleinEcranHover.png","src/image/BoutonPleinEcranOnClick.png",[285 , 75],(game.rectBackground.center[0], game.taille[1]-game.taille[1]*0.55),game.screen)
        BoutonSons=game.setBouton("src/image/BoutonSons.png","src/image/BoutonSonsHover.png","src/image/BoutonSonsOnClick.png",[285 , 75],(game.rectBackground.center[0], game.taille[1]-game.taille[1]*0.4),game.screen)
        BoutonReset=game.setBouton("src/image/BoutonReset.png","src/image/BoutonResetHover.png","src/image/BoutonResetOnClick.png",[285 , 75],(game.rectBackground.center[0], game.taille[1]-game.taille[1] * 0.25),game.screen)
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
                    elif BoutonPleinEcran["bouton"]["rect"].collidepoint(pygame.mouse.get_pos()):
                        if pygame.mouse.get_pressed()==(True,False,False):
                            pygame.display.toggle_fullscreen()

                    elif BoutonReset["bouton"]["rect"].collidepoint(pygame.mouse.get_pos()):
                        if pygame.mouse.get_pressed()==(True,False,False):
                            niveau = {
                                "Niveau1" : 0,
                                "Niveau2" : 0,
                                "Niveau3" : 0
                            }
                            resetFichier = open("listeLVL.json", "w")
                            json.dump(niveau, resetFichier, indent = 4 )
                            resetFichier.close()