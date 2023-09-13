class Player:

    __health: int = 50
    __maxHealth: int = 100

    @property
    def Health(self):
        return self.__health

    @Health.setter
    def Health(self, value: int):
        # Constrains health to be within min & max
        if value > self.__maxHealth:
            value = self.__maxHealth
        if value < 0:
            value = 0
        self.__health = value

    def Heal_Max(self):
        self.Health = self.__maxHealth

    def Heal(self, value: int):
        self.Health += value

    def Damage(self, value: int):
        self.Health -= value

Instance = Player()