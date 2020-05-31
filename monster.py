import pygame
import random
#from player import Player

# Créer un classe qui va gerer la notion de monstre sur notre jeu
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,300)
        self.rect.y = 340
        self.velocity = random.randint(1,3)
    
    def damage(self, amount):
        #Infliger les degats
        self.health -= amount

        # Verifier si son nouveau nombre de point de est inferieur à 0 
        if self.health  <= 0:
            # reaparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0,300)
            self.velocity = random.randint(1,3)
            self.health = self.max_health  
     

    def update_health_bar(self, surface):
        # definir une couleur pour notre jauge de vie (vert clair)
        #bar_color = (111, 240, 63)
        # définir une couleur pour l'arrière plan de la jauge (gris foncé)
        #back_bar_color = (60, 63, 60)
        # definir la position de notre jaune de vie ainsi que largeur et son épaisseur 
        #bar_position = [self.rect.x+10, self.rect.y-20, self.health, 5]
        # definir la position de l'arrière plan de notre jauge de vie
        #back_bar_position = [self.rect.x+10, self.rect.y-20, self.max_health, 5]

        # dessiner notre barre de vie
        
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x+10, self.rect.y-20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 240, 63), [self.rect.x+10, self.rect.y-20, self.health, 5])

    def forward(self):
        # le deplacement ne se fait pas que si il n'y a de collision avec les joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
            # Infliger des degats ( au joueur)
            self.game.player.damage(self.attack)