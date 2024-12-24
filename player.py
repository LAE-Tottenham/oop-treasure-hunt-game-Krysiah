class Player():
    def __init__(self, given_name, skill):
        self.name = given_name
        self.health = 100
        self.sp = 100
        self.inventory_max_weight = 50
        self.inventory = []
        self.skill = skill
    
    def calculate_inventory_size(self,item_instance):
        total_weight = sum(self.inventory(item_instance.weight))
        return total_weight

    def add_item(self, item_instance):
        if self.calculate_inventory_size() > self.inventory_max_weight:
            self.inventory.append(item_instance)
        else:
            print("Your inventory is full...")

    def use_item(self, item_instance):
        if item_instance.can_use == True:
            self.health = self.health + item_instance.health_pts
            self.sp = self.sp + item_instance.health_pts
        else:
            print("This item cannot be used")
        


    # add more methods as needed
