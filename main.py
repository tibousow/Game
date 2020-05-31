import pygame
import math
from game import Game
from player import Player
from projectile import Projectile
pygame.init()


# generer la fenetre de notre jeu
pygame.display.set_caption("commet fall Game")
screen = pygame.display.set_mode((1050, 600))

background = pygame.image.load('assets/bg.jpg')

# importer ou charger nore baninière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)

# importer ou charger nore bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/1.7) #1.5
 

# charger notre jeu
game = Game()

running = True

# boucle tant que cette condition est vrai
while running:

    # appliquer l'arriere plan de notre jeux 
    screen.blit(background, (0, -400))

    #verifier si notre jeu a commencé ou non
    if game.is_playing:
        #declencher les instruction de la partie
        game.update(screen)
    # verifier si notre jeu n'a pas commencé
    else:
        # ajouter mon ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)
        
    '''
   # on a deplacer un code ici
    '''
    #metre a jour l'ecran 
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # detecter si un joueur lache une touche  du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclanchée pour  lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancer
                game.start()