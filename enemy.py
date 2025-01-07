import random
from item import Weapon
from item import Battle_Item
from healthbar import Healthbar

claw = Weapon("Scratch",True,4,"A simple scratch. Doesn't hurt much, but it's the attack that counts...")

class Enemy:
    def __init__(self,name,health,max_health,sp_drn):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.hp_dmg = claw.hp_dmg
        self.sp_drn = sp_drn
    
        self.health = Healthbar(self,self.max_health,True,"red")

    #target player
    #die + loot drop
    def enemy_death(self):
        if self.health == 0:
            print(self.name,"has fallen!")
            
