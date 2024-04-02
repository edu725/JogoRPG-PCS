class Attribute:
    def __init__(self):
        self.__strength = int
        self.__dexterity = int
        self.__constitution = int
        self.__wisdom = int
        self.__intelligence = int
        self.__charisma = int

    @property
    def strength(self):
        return self.__strength
    
    @strength.setter
    def strenght(self):
        self.__strength 

    @property
    def dexterity(self):
        return self.__dexterity
    
    @dexterity.setter
    def dexterity(self):
        self.__dexterity

    @property
    def constitution(self):
        return self.__constitution
    
    @constitution.setter
    def constitution(self):
        self.__constitution

    @property
    def wisdom(self):
        return self.__wisdom
    
    @wisdom.setter
    def wisdom(self):
        self.__wisdom

    @property
    def intelligence(self):
        return self.__intelligence
    
    @intelligence.setter
    def intelligence(self):
        self.__intelligence

    @property
    def charisma(self):
        return self.__charisma
    
    @charisma.setter
    def charisma(self):
        self.__charisma

              