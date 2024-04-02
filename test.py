import time

class Monster:
   def __init__(self, name: str, health: int, attack_power: int, player) -> None:
      self.__name = name
      self.__health = health
      self.__attack_power = attack_power

   def attack(self, player):
      player.take_damage(self.__attack_power)

   def take_damage(self, amount):
      self.__health -= amount

   def is_alive(self):
      self.__health > 0

   @property
   def attack_power(self):
      return self.__attack_power
   
   @attack_power.setter
   def attack_power(self, value):
      self.__attack_power = value

   @property
   def health(self):
      return self.__health
   
   @property
   def name(self):
      return self.__name

class Player:
   def __init__(self, name: str, health: int, attack_power: int) -> None:
      self.__name = name
      self.__health = health 
      self.__attack_power = attack_power
    
   def attack(self, monster):
      monster.take_damage(self.__attack_power)

   def take_damage(self, amount):
      self.__health -= amount
   
   def is_alive(self):
      self.__health > 0

   @property
   def attack_power(self):
      return self.__attack_power
   
   @attack_power.setter
   def attack_power(self, value):
      self.__attack_power = value

   @property
   def health(self):
      return self.__health
   
   @property
   def name(self):
      return self.__name   

p1 = Player(name='Zhask', health=100, attack_power=50)
m1 = Monster(name='Zilong', health=200, attack_power=25, player=p1)


while True:
   print(f'\n{m1.name} is attacking...')
   time.sleep(1)

   m1.attack(p1)
   print(f"{p1.name} took damage! Current health:", p1.health)

   print(f'\n{p1.name} is attacking...')
   time.sleep(1)

   p1.attack(m1)
   print(f"{m1.name} took damage! Current health:", m1.health)

   if p1.health==0 or m1.health==0:
      print ('\nThey dead.')
      break
