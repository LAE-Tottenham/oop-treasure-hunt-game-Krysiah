import time
from item import Weapon

class Fight:
    def player_atk(playr_inst,opp_inst):
        opp_inst.health = opp_inst.health - playr_inst.hp_dmg
        opp_inst.health = max(opp_inst.health, 0)
        print("[",playr_inst.name,"attacked",opp_inst.name,"!]")
        time.sleep(2)
        print("[You did",playr_inst.hp_dmg,"damage to",opp_inst.name,"!]")
        print(f"Player health: {playr_inst.health}") 
        print(f"Enemy health: {opp_inst.health}")

    def summon_atk(sum_inst,opp_inst):
        opp_inst.health = opp_inst.health - sum_inst.hp_dmg
        opp_inst.health = max(opp_inst.health, 0)
        print("[",sum_inst.name,"attacked",opp_inst.name,"!]")
        time.sleep(2)
        print("[",sum_inst.name,"did",sum_inst.hp_dmg,"damage to",opp_inst.name,"!]") 
        print(f"Enemy health: {opp_inst.health}")


    def enemy_hp_atk(opp_inst,victim_inst):
        victim_inst.health = victim_inst.health - opp_inst.hp_dmg
        victim_inst.health = max(victim_inst.health, 0)
        print("[",opp_inst.name,"attacked",victim_inst.name,"!]")
        time.sleep(2)
        print("[",opp_inst.name,"did",opp_inst.hp_dmg,"damage to",victim_inst.name,"!]")
        print(f"Player health: {victim_inst.health}") 
        print(f"Enemy health: {opp_inst.health}")

    def enemy_sp_atk(opp_inst,victim_inst):
        victim_inst.sp = victim_inst.sp - opp_inst.sp_drn
        print("[",opp_inst.name,"drained",victim_inst.name,"'s SP!]")
        time.sleep(2)
        print("[",opp_inst.name,"took",opp_inst.sp_drn,"SP points from",victim_inst.name,"!]")