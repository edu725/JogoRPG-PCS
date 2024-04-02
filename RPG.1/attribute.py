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

    def definition_strength(self,strength):
        self.__strength = strength
        if strength == 0:
            return strength, print("Incorpório")
        elif strength >= 1 and strength <= 5 :
            return strength, print("Incapaz")
        elif strength >=6 and strength <=9:
            return strength, print("Fraco")
        elif strength >=10 and strength <=11:
            return strength, print("Medino")
        elif strength >=12 and strength <=15:
            return strength, print("Forte")
        elif strength >=16 and strength <=20:
            return strength, print("Super poderoso")
        else:
            return strength, print("Inbatível")

    def definition_dexterity(self, dexterity):
        self.__dexterity = dexterity
        if dexterity ==0:
            return dexterity, print("Desacordado")
        elif dexterity >=1 and dexterity <=5:
            return dexterity, print("Abatido")
        elif dexterity >=6 and dexterity <=9:
            return dexterity, print("Desajeitado")
        elif dexterity >=10 and dexterity <=11:
            return dexterity, print("Regular")
        elif dexterity >=12 and dexterity <=15:
            return dexterity, print("Ágil")
        elif dexterity >=16 and dexterity <=20:
            return dexterity, print("Ninja")
        else:
            return dexterity, print("Inperceptível") 
    
    def definition_constitution(self,constitution):
        self.__constitution == constitution
        if constitution ==0:
            return constitution, print("Espectro")
        elif constitution >=1 and constitution <=5:
            return constitution, print("Enfermo")
        elif constitution >=6 and constitution <=9:
            return constitution, print("Frágio")
        elif constitution >=10 and constitution <=11:
            return constitution, print("Saudável")
        elif constitution >=12 and constitution <=15:
            return constitution, print("Durão")
        elif constitution >=16 and constitution <=20:
            return constitution, print("Super resistênte")
        else:
            return constitution, print("Imortal")
    
    def definition_wisdom(self,wisdom):
        self.__wisdom == wisdom
        if wisdom ==0:
            return wisdom, print("Inconscinte")
        elif wisdom >=1 and wisdom <=5:
            return wisdom, print("Irracional")
        elif wisdom >=6 and wisdom <=9:
            return wisdom, print("Desatento")
        elif wisdom >=10 and wisdom <=11:
            return wisdom, print("Simples")
        elif wisdom >=12 and wisdom <=15:
            return wisdom, print("Perspcaz")
        elif wisdom >=16 and wisdom <=20:
            return wisdom, print("Filósofo")
        else:
            return wisdom, print("Iluminado")

    def definition_intelligence(self,intelligence):
        self.__intelligence == intelligence
        if intelligence ==0:
            return intelligence, print("Inanimado")
        elif intelligence >=1 and intelligence <=5:
            return intelligence, print("Incivilizado")
        elif intelligence >=6 and intelligence <=9:
            return intelligence, print("Parvo")
        elif intelligence >=10 and intelligence <=11:
            return intelligence, print("Medíocre")
        elif intelligence >=12 and intelligence <=15:
            return intelligence, print("Estuado")
        elif intelligence >=16 and intelligence <=20:
            return intelligence, print("Gênio")
        else:
            return intelligence, print("Onisciente")

    def definition_charisma(self,charisma):
        self.__charisma == charisma
        if charisma ==0:
            return charisma, print("Aberração")
        elif charisma >=1 and charisma <=5:
            return charisma, print("Inexprecivo")
        elif charisma >=6 and charisma <=9:
            return charisma, print("Rude")
        elif charisma >=10 and charisma <=11:
            return charisma, print("Socíavel")
        elif charisma >=12 and charisma <=15:
            return charisma, print("Persuasivo")
        elif charisma >=16 and charisma <=20:
            return charisma, print("Influente")
        else:
            return charisma, print("Ídolo")