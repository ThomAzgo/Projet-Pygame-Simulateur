import pygame
class FinNiveau:
    def __init__(self,game,point):
        game.setBackground("src/image/bg.png",game.screen)
        imageTitre=game.setAnImage( "src/image/Titre.png",[305,132],(game.rectBackground.center[0], game.taille[1] - game.taille[1]*0.8 ),game.screen)
        self.boucle=True
        self.actualScreen = "FinNiveau"
        rectangle = game.drawRectTXT([100,60],[game.rectBackground.center[0]-50,game.taille[1] - game.taille[1]*0.6],(247, 68, 67),str(point),15,(255,255,255),game.screen)
        if point>=800:
            game.setAnImage( "src/image/3etoile.png",[285 , 75],(game.rectBackground.center[0], game.taille[1] - game.taille[1]*0.45 ),game.screen)
        elif point>=600:
            game.setAnImage( "src/image/3etoile.png",[285 , 75],(game.rectBackground.center[0], game.taille[1] - game.taille[1]*0.45 ),game.screen)
        elif point>=400:
            game.setAnImage( "src/image/1etoile.png",[285 , 75],(game.rectBackground.center[0], game.taille[1] - game.taille[1]*0.45 ),game.screen)
        else :
            game.setAnImage( "src/image/0etoile.png",[285 , 75],(game.rectBackground.center[0], game.taille[1] - game.taille[1]*0.45 ),game.screen)
        boutonRetour=game.setBouton("src/image/BoutonRetour.png","src/image/BoutonRetourHover.png","src/image/BoutonRetourOnclick.png",[302,64],( game.rectBackground.center[0], game.taille[1]- game.taille[1]*0.2 ),game.screen)
        

        # rectangledessin = game.drawRectTXT([300,100],[200,200],(247, 68, 67),"Tchatchatcha",24,(255,255,255),game.screen)
        
        pygame.display.flip()
        
        for event in  pygame.event.get(): 
                    
            if event.type == pygame.QUIT: # Si l'event est QUIT alors on quitte la boucle et on ferme la fenetre
                self.boucle=False
                pygame.quit()
                
        
            

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_focused: # Si il a été préssé dans le screen
                    if boutonRetour["bouton"]["rect"].collidepoint(pygame.mouse.get_pos()): 
                        if pygame.mouse.get_pressed()==(True,False,False):
                            self.actualScreen="Menu"
                    