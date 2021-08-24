import pygame
class Menu:
    def __init__(self,game):
        game.setBackground("src/image/bg.png",game.screen)
        imageTitre=game.setAnImage( "src/image/Titre.png",[305,132],(game.rectBackground.center[0], game.taille[1] - game.taille[1]*0.8 ),game.screen)
        self.boucle=True
        self.actualScreen = "Menu"
        boutonCommencer=game.setBouton("src/image/BoutonCommencer.png","src/image/BoutonCommencerHover.png","src/image/BoutonCommencerOnclick.png",[302,64],( game.rectBackground.center[0], game.taille[1]- game.taille[1]*0.5 ),game.screen)
        boutonOption=game.setBouton("src/image/BoutonOption.png","src/image/BoutonOptionHover.png","src/image/BoutonOptionOnclick.png",[302,64],( game.rectBackground.center[0], game.taille[1]- game.taille[1]*0.35 ),game.screen)
        boutonQuitter=game.setBouton("src/image/BoutonQuitter.png","src/image/BoutonQuitterHover.png","src/image/BoutonQuitterOnclick.png",[302,64],( game.rectBackground.center[0], game.taille[1]- game.taille[1]*0.2 ),game.screen)
        

        # rectangledessin = game.drawRectTXT([300,100],[200,200],(247, 68, 67),"Tchatchatcha",24,(255,255,255),game.screen)
        
        pygame.display.flip()
        
        for event in  pygame.event.get(): 
                    
            if event.type == pygame.QUIT: # Si l'event est QUIT alors on quitte la boucle et on ferme la fenetre
                self.boucle=False
                pygame.quit()
                
        
            

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_focused: # Si il a été préssé dans le screen
                    if boutonQuitter["bouton"]["rect"].collidepoint(pygame.mouse.get_pos()): 
                        if pygame.mouse.get_pressed()==(True,False,False):
                            self.boucle=False
                            pygame.quit()
                    elif boutonOption["bouton"]["rect"].collidepoint(pygame.mouse.get_pos()):
                        if pygame.mouse.get_pressed()==(True,False,False):
                            self.actualScreen="Options"
                    elif boutonCommencer["bouton"]["rect"].collidepoint(pygame.mouse.get_pos()):
                        if pygame.mouse.get_pressed()==(True,False,False):
                            self.actualScreen="LevelSelection"