class Summmon:
    def __init__(self,name,health,hp_cost,sp_cost):
        self.name = name
        self.health = health
        self.hp_cost = hp_cost
        self.sp_cost = sp_cost
        

    def give_item_desc(self):
        print(self.name,"""
""","[",self.desc,"]")