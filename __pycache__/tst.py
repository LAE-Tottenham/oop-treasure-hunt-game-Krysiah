from player import Player
from summon import Summmon
from enemy import Enemy
from fight import Fight

protag = Player("Kryssi")
opp1 = Enemy("Possessed Skull",50,6,0)

while True:
    print(Fight.player_atk(protag,opp1))
    print(Fight.enemy_hp_atk(opp1,protag))