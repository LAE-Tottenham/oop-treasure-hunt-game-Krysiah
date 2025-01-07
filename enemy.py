import random

class Enemy:
    def __init__(self,name,health,hp_dmg,sp_drn):
        self.name = name
        self.health = health
        self.hp_dmg = hp_dmg
        self.sp_drn = sp_drn

    #target player
    #die + loot drop
    def enemy_death(self):
        if self.health == 0:
            print(self.name,"has fallen!")
            
