class Summmon:
    def __init__(self,name,health,hp_dmg,hp_cost,sp_cost):
        self.name = name
        self.health = health
        self.hp_dmg = hp_dmg
        self.hp_cost = hp_cost
        self.sp_cost = sp_cost
        

    def give_item_desc(self):
        print(self.name,"""
""","[",self.desc,"]")
        

#Summons
sum1 = Summmon("Yin",20,4,0,2)
sum2 = Summmon("Yang",20,6,8,0)