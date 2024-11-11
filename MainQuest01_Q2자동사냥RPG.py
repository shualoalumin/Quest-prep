import random

class Character:
    def __init__(self, name, level, hp, attack, defense):
        self.name = name
        self.level = level
        self.hp = hp
        self.attack = attack
        self.defense = defense
    
    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.hp = self.hp - actual_damage
        return actual_damage
    
    def attack_target(self, target):
        damage = random.randint(1, self.attack)
        target.take_damage(damage)
        return damage

class Player(Character):
    def __init__(self, name):
        super().__init__(name, level=1, hp=100, attack=25, defense=5)
        self.experience = 0
    
    def gain_experience(self, experience):   
        self.experience += experience
        if self.experience >= 50:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.attack += 10
        self.defense += 5
        self.experience -= 50  
        print(f"{self.name}이(가) {self.level}레벨이 되었습니다!")

class Monster(Character):
    def __init__(self, name, level=1):
        hp = random.randint(10, 30) * level
        attack = random.randint(5, 20) * level
        defense = random.randint(1, 5) * level
        super().__init__(name, level, hp, attack, defense)

def battle(player, monster):
    while player.is_alive() and monster.is_alive():
        damage = player.attack_target(monster)
        print(f"{player.name}이 {monster.name}에게 {damage} 만큼 공격했다...!")
        print(f"{monster.name}의 체력: {monster.hp}")
        
        if not monster.is_alive():
            break
        
        damage = monster.attack_target(player)
        print(f"{monster.name}이 {player.name}에게 {damage} 만큼 공격했다...!")
        print(f"{player.name}의 체력: {player.hp}")
    
    if player.is_alive():
        exp = monster.level * 20
        player.gain_experience(exp)
        print("전투 승리!")
        print(f"{monster.name} 을 이겼다!")
    else:
        print("전투 패배..")

def main():
    monster_dict = {'슬라임': 1, '고블린': 2, '오크': 3}
    
    player_name = input("플레이어 이름을 입력하세요: ")
    player = Player(player_name)
    
    for monster_name, monster_level in monster_dict.items():
        monster = Monster(monster_name, monster_level)
        print(f"\n{monster_name}과의 전투를 시작합니다.")
        
        battle(player, monster)
        
        if not player.is_alive():
            print("게임오버")
            break

if __name__ == "__main__":
    main()
