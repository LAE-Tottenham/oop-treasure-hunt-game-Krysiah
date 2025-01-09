from item import Weapon, Battle_Item
import time

hands = Weapon("these Hands!",True,16,"You pray that your enemies like Pokemon, cause they're gonna Catch 'Em All!",10)

class Player:
    def __init__(self, given_name):
        self.name = given_name
        self.health = 100
        self.max_health = 100 
        self.sp = 70
        self.max_sp = 70
        self.inventory_max_weight = 50
        self.inventory = []
        self.weight = 0
        
        self.hp_dmg = None
    
    def check_inventory(self):
        print("Here are your current inventory items:")
        time.sleep(1)
        print(self.inventory)

    def add_item(self, item_instance):
        for item in self.inventory:
            self.weight = item_instance.weight(item) 
        if self.weight < self.inventory_max_weight:
            self.inventory.append(item_instance)
            print("[Item added to the bag]")
            time.sleep(1)
        else:
            print("Your inventory is full...")
            time.sleep(1)

    def use_item(self, item_instance):
        #battle potions
        if item_instance.type == "consume":
            self.health = self.health + item_instance.health_pts
            self.sp = self.sp + item_instance.sp_pts
            print("[Restored",item_instance.health_pts,"HP!]")
            time.sleep(2)
            print("[Restored",item_instance.sp_pts,"SP!]")
            time.sleep(2)
        #potions
        elif item_instance.type == "weapon":
            self.hp_dmg = item_instance.hp_dmg
        #key items

        #else
        else:
            print("This item cannot be used")
            time.sleep(1)
        


tst = Player("hero")

print(tst.weight)

tst.add_item(Battle_Item("S HP Potion","consume","tst potion 1",10,0,3))
#tst.add_item(Battle_Item("L HP Potion","consume","tst potion 2",20,0,5))
#tst.add_item(Battle_Item("S SP Potion","consume","tst potion 3",0,15,4))
#tst.add_item(Battle_Item("L SP Potion","consume","tst potion 4",0,15,8))
#tst.add_item(Battle_Item("Heavy item","consume","tst potion 5",0,15,10))
#tst.add_item(Battle_Item("Can't fit item in","consume","tst potion 6",0,0,1))