class hero :
    name = "Kamisato Ayato"
    hp = 8000
    gelar = "knight"
    mana = 200
    damage = 200
    defanse = 100
    
    def __init__(self,name,hp,damage,defanse) :
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defanse = defanse
        
        
    def attack(self,target):
        target.hp = target.hp - self.damage
        print("sisa HP ", target.name, "=", target.hp)
        
#inisialisasikan class hero
hero1 = hero("Xiao", 7500, 250, 300)
hero2 = hero("Aether", 5000, 200, 400)

hero1.attack(hero2)
hero2.attack(hero1)