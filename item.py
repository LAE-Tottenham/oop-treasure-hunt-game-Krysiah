class Item:
    def __init__(self, name,can_use,desc):
        self.name = name
        self.can_use = can_use
        self.desc = desc

    def give_item_desc(self):
        print(self.name,"""
""","[",self.desc,"]")

#Battle Items
class Battle_Item(Item):
    def __init__(self, name,can_use,desc,health_pts,sp_pts,weight):
        super().__init__(name,can_use,desc)
        self.health_pts = health_pts
        self.sp_pts = sp_pts
        self.weight = weight

 #Weapons   
class Weapon(Item):
    def __init__(self, name, can_use, hp_dmg, desc):
        super().__init__(name, can_use, desc)
        self.hp_dmg = hp_dmg




sword = Weapon("Basic Sword",True,10,"A sturdy (and lame looking) sword. Nothing special, but good at slaying enemies.")
hands = Weapon("these Hands!",True,16,"You pray that your enemies like Pokemon, cause they're gonna Catch 'Em All!")