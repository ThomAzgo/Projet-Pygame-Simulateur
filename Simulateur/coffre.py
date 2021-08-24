boutonCommencer=game.setBouton("src/image/BoutonCommencer.png","src/image/BoutonCommencerHover.png","src/image/BoutonCommencerOnclick.png",[302,64],( game.rectBackground.center[0], game.taille[1]- game.taille[1]*0.5 ))
boutonCommencer["bouton"]["rect"]=boutonCommencer["bouton"]["rect"].move(boutonCommencer["position"]["x"],boutonCommencer["position"]["y"])


boutonOption=game.setBouton("src/image/BoutonOption.png","src/image/BoutonOptionHover.png","src/image/BoutonOptionOnclick.png",[302,64],( game.rectBackground.center[0], game.taille[1]- game.taille[1]*0.35 ))
boutonOption["bouton"]["rect"]=boutonOption["bouton"]["rect"].move(boutonOption["position"]["x"],boutonOption["position"]["y"])


boutonQuitter=game.setBouton("src/image/BoutonQuitter.png","src/image/BoutonQuitterHover.png","src/image/BoutonQuitterOnclick.png",[302,64],( game.rectBackground.center[0], game.taille[1]- game.taille[1]*0.2 ))
boutonQuitter["bouton"]["rect"]=boutonQuitter["bouton"]["rect"].move(boutonQuitter["position"]["x"],boutonQuitter["position"]["y"])



if boutonCommencer["bouton"]["rect"].collidepoint(pygame.mouse.get_pos()):
        game.screen.blit(boutonCommencer["boutonHover"]["image"], (boutonCommencer["position"]["x"],boutonCommencer["position"]["y"]))
        
    else :
        game.screen.blit(boutonCommencer["bouton"]["image"], (boutonCommencer["position"]["x"],boutonCommencer["position"]["y"]))
        

    if boutonOption["bouton"]["rect"].collidepoint(pygame.mouse.get_pos()):
        game.screen.blit(boutonOption["boutonHover"]["image"], (boutonOption["position"]["x"],boutonOption["position"]["y"]))
        
    else :
         game.screen.blit(boutonOption["bouton"]["image"], (boutonOption["position"]["x"],boutonOption["position"]["y"]))

    if boutonQuitter["bouton"]["rect"].collidepoint(pygame.mouse.get_pos()):
        game.screen.blit(boutonQuitter["boutonHover"]["image"], (boutonQuitter["position"]["x"],boutonQuitter["position"]["y"]))
        
    else :
         game.screen.blit(boutonQuitter["bouton"]["image"], (boutonQuitter["position"]["x"],boutonQuitter["position"]["y"]))


    