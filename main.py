import os
from item import Item
from place import Place
from player import Player
from enemy import Enemy
from fight import Fight


class Game():
    def __init__(self):
      self.current_place = None  

    def setup(self):
        # here you will setup your Game
        # places
        castle = Place("King's Castle", 20)
        city = Place("City Gates", 5)
        plaza = Place("City Plaza", 30)
        forest = Place("Overgrown Forest", 30)
        dun_entrance = Place("Dungeon Entrance", 5,True)
        floor0 = Place("Floor 0: Abandoned Armory", 50)
        floor_1 = Place("Floor -1: Death Dungeon", 70)
        floor_2 = Place("Floor -2: Corrosive Cave", 100)
        s_floor = Place("Secret Floor: lieutenant's Secret Library", 50,True)
        floor_3 = Place("Floor -3: The Gallery", 20,True)
        
        #next locations
        castle.add_next_place(plaza)
        castle.add_next_place(city)

        city.add_next_place(plaza)
        city.add_next_place(castle)

        forest.add_next_place(dun_entrance)
        forest.add_next_place(city)

        dun_entrance.add_next_place(forest)
        dun_entrance.add_next_place(floor0)
        dun_entrance.add_next_place(city) #Quick Travel

        #f0:Armory
        floor0.add_next_place(dun_entrance)
        floor0.add_next_place(floor_1)
        floor0.add_next_place(city) #Quick Travel

    

        #f1:DD
        floor_1.add_next_place(floor0)
        floor_1.add_next_place(floor_2)
        floor_1.add_next_place(city) #Quick Travel


        #f2:CC
        floor_2.add_next_place(s_floor)
        floor_2.add_next_place(floor_1)
        floor_2.add_next_place(floor_3)
        floor_2.add_next_place(city) #Quick Travel

        #sf: Library
        s_floor.add_next_place(floor_2)

        #f3: Gallery
        floor_3.add_next_place(floor_2)
        
        # items
        hammer = Item('Hammer')
        pen = Item('Pen')
        castle.add_item(hammer)
        city.add_item(pen)
        
        # castle will be our starting place
        self.current_place = castle
        
        # finish the setup function...
    def start(self):
        print("Welcome to my game...")
        print("Storyline...")
        protag = input("Enter player name: ")
        protag = Player(protag)
        print("You are currently in " + self.current_place.name)
        self.current_place.show_next_places()
        opt = input("""
What would you like to do?
1. Go to a place
2. Pickup item
3. Check inventory
etc.      
""")
        if opt == "1":
            # add code
            pass
        elif opt == "2":
            # add code
            pass
        elif opt == "3":
            # add code
            pass

    
