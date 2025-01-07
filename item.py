class Item():
    def __init__(self, name, health_pts, sp_pts, weight, desc, can_use=False):
        self.name = name
        self.weight = 0
        self.health_pts = health_pts
        self.sp_pts = sp_pts
        self.weight = weight
        self.can_use = can_use
        self.desc = desc

    def give_item_desc(self):
        print(self.name,"""
""","[",self.desc,"]")

#Items
S_Heal_ptn = Item("Small Heal Potion",20,0,1,"A small healing potion. Restores 20 health",True)
L_Heal_ptn = Item("Large Heal Potion",50,0,2,"A Large healing potion. Restores 50 health",True)
S_sp_ptn = Item("Small SP Potion",0,20,1,"A small SP potion, Restores 20 SP",True)