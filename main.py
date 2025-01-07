from player import Player
from enemy import Enemy
from fight import Fight
from healthbar import Healthbar


protag = Player("Kryssi")
opp1 = Enemy("Skelly",50,50,0)

while True:
    Fight.player_atk(protag,opp1)
    Fight.enemy_hp_atk(opp1,protag)

    protag.health = Healthbar.draw()
    opp1.health = Healthbar.draw()

    input()
 