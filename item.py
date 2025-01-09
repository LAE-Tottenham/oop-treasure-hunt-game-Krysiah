class Item:
    def __init__(self, name,type,desc,weight):
        self.name = name
        self.type = type
        self.desc = desc
        self.weight = weight

    def give_item_desc(self):
        print(self.name,"""
""","[",self.desc,"]")

#Battle Items
class Battle_Item(Item):
    def __init__(self, name,type,desc,health_pts,sp_pts,weight):
        super().__init__(name,type,desc,weight)
        self.health_pts = health_pts
        self.sp_pts = sp_pts
        self.weight = weight

 #Weapons   
class Weapon(Item):
    def __init__(self, name, type, hp_dmg, desc,weight):
        super().__init__(name, type, desc,weight)
        self.hp_dmg = hp_dmg

#Key Items
class Key_Item(Item):
    def __init__(self, name, type, desc,weight,can_use=False):
        super().__init__(name,type,weight,desc)
        self.can_use = can_use

sword = Weapon("Basic Sword","weapon",10,"A sturdy (and lame looking) sword. Nothing special, but good at slaying enemies.",10)
hands = Weapon("These Hands!","weapon",16,"You pray that your enemies like Pokemon, cause they're gonna Catch 'Em All!",0)
claw = Weapon("Scratch","weapon",4,"A simple scratch. Doesn't hurt much, but it's the attack that counts...",0)