import pygame
from algo import Gamelvl
import json

class Niveau:
    def __init__(self,game,firstSentence,phrase,morceau,point,humeur,lvl):
        game.setBackground("src/image/bg.png",game.screen)        
        
        with open(lvl+".json", encoding='utf-8') as fh:
            doc = json.load(fh)
        niveau=Gamelvl()
        self.boucle=True
        self.actualScreen = lvl
        self.firstSentence =  firstSentence

        #DEMANDER LES PHRASES A AFFICHER
        if self.firstSentence == True: #SI C'EST LA PREMIERE PHRASE
            self.firstSentence=False
            self.phrase="phrase1" #RECUPERER LA PREMIER PHRASE
            self.morceau="morceau1"
            self.point=0
            choix=niveau.printPhrase(self.phrase,doc,morceau)
            self.humeur="neutre"
            
        else :
            
            self.phrase=phrase
            self.morceau=morceau
            self.point=point
            choix=niveau.printPhrase(phrase,doc,morceau)
            self.humeur=humeur
        
        imagePerso=game.setAnImage( "src/image/perso/"+doc["numeroperso"]+"/"+self.humeur+".png",[275,290],(game.rectBackground.center[0]/4, game.taille[1] - game.taille[1]*0.75 ),game.screen)    
            
            
        txtPeros = game.drawRectTXT([game.rectBackground.width-15,150],[game.rectBackground.center[0]/2,game.taille[1] - game.taille[1]*0.85],(199,54,54),niveau.printPhrasePNJ(self.phrase,doc),15,(255,255,255),game.screen)

        rectangleA = game.drawRectTXT([game.rectBackground.width,60],[game.rectBackground.center[0]-game.rectBackground.width/2,game.taille[1] - game.taille[1]*0.49],(247, 68, 67),choix[0],15,(255,255,255),game.screen)
        rectangleB = game.drawRectTXT([game.rectBackground.width,60],[game.rectBackground.center[0]-game.rectBackground.width/2,game.taille[1] - game.taille[1]*0.36],(247, 68, 67),choix[1],15,(255,255,255),game.screen)

        rectangleC = game.drawRectTXT([game.rectBackground.width,60],[game.rectBackground.center[0]-game.rectBackground.width/2,game.taille[1] - game.taille[1]*0.23],(247, 68, 67),choix[2],15,(255,255,255),game.screen)
        rectangleD = game.drawRectTXT([game.rectBackground.width,60],[game.rectBackground.center[0]-game.rectBackground.width/2,game.taille[1] - game.taille[1]*0.10],(247, 68, 67),choix[3],15,(255,255,255),game.screen)

        pygame.display.flip()
        
        for event in  pygame.event.get():             
            if event.type == pygame.QUIT: # Si l'event est QUIT alors on quitte la boucle et on ferme la fenetre
                self.boucle=False
                pygame.quit()
                
        
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_focused: # Si il a été préssé dans le screen
                    if rectangleA["rectangle"].collidepoint(pygame.mouse.get_pos()): 
                        if pygame.mouse.get_pressed()==(True,False,False):
                            
                            output=niveau.Output(self.phrase,self.morceau,doc,1)
                            self.phrase = output[0]
                            self.morceau = output[1]
                            self.humeur=output[3]
                            self.point = self.point +output[2]
                            if self.phrase =="fin":
                                self.actualScreen = "FinNiveau"
                                niveau.savepoint(self.point,lvl)

                    elif rectangleB["rectangle"].collidepoint(pygame.mouse.get_pos()): 
                        if pygame.mouse.get_pressed()==(True,False,False):
                            
                            output=niveau.Output(self.phrase,self.morceau,doc,2)
                            self.phrase = output[0]
                            self.morceau = output[1]
                            self.humeur=output[3]
                            self.point = self.point +output[2]
                            if self.phrase =="fin":
                                self.actualScreen = "FinNiveau"
                                niveau.savepoint(self.point,lvl)

                    elif rectangleC["rectangle"].collidepoint(pygame.mouse.get_pos()): 
                        if pygame.mouse.get_pressed()==(True,False,False):
                            
                            output=niveau.Output(self.phrase,self.morceau,doc,3)
                            self.phrase = output[0]
                            self.morceau = output[1]
                            self.humeur=output[3]
                            self.point = self.point +output[2]
                            if self.phrase =="fin":
                                self.actualScreen = "FinNiveau"
                                niveau.savepoint(self.point,lvl)

                    elif rectangleD["rectangle"].collidepoint(pygame.mouse.get_pos()): 
                        if pygame.mouse.get_pressed()==(True,False,False):
                            
                            output=niveau.Output(self.phrase,self.morceau,doc,4)
                            self.phrase = output[0]
                            self.morceau = output[1]
                            self.humeur=output[3]
                            self.point = self.point +output[2]
                            if self.phrase =="fin":
                                self.actualScreen = "FinNiveau"
                                niveau.savepoint(self.point,lvl)
                            
                            
