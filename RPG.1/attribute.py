class Attribute:
    def __init__(self):
        self.__strength = int
        self.__dexterity = int
        self.__constitution = int
        self.__wisdom = int
        self.__intelligence = int
        self.__charisma = int

    @property
    def strength(self) -> int:
        return self.__strength
    
    @strength.setter
    def strenght(self):
        self.__strength  

    @property
    def dexterity(self) -> int:
        return self.__dexterity
    
    @dexterity.setter
    def dexterity(self):
        self.__dexterity

    @property
    def constitution(self) -> int:
        return self.__constitution
    
    @constitution.setter
    def constitution(self):
        self.__constitution

    @property
    def wisdom(self) -> int:
        return self.__wisdom
    
    @wisdom.setter
    def wisdom(self):
        self.__wisdom

    @property
    def intelligence(self) -> int:
        return self.__intelligence
    
    @intelligence.setter
    def intelligence(self):
        self.__intelligence

    @property
    def charisma(self) -> int:
        return self.__charisma
    
    @charisma.setter
    def charisma(self):
        self.__charisma

    def definition_strength(self,strength):
        self.__strength = strength
        
        if strength == 0:
            return print("Incorpório:",strength)
        elif strength >= 1 and strength <= 5 :
            return print("Incapaz:",strength)
        elif strength >=6 and strength <=9:
            return print("Fraco:",strength)
        elif strength >=10 and strength <=11:
            return print("Medino:",strength)
        elif strength >=12 and strength <=15:
            return print("Forte:",strength)
        elif strength >=16 and strength <=20:
            return print("Super poderoso:",strength)
        else:
            return print("Inbatível:",strength)

    def definition_dexterity(self, dexterity):
        self.__dexterity = dexterity
        
        if dexterity ==0:
            return print("Desacordado:",dexterity)
        elif dexterity >=1 and dexterity <=5:
            return print("Abatido:",dexterity)
        elif dexterity >=6 and dexterity <=9:
            return print("Desajeitado:",dexterity)
        elif dexterity >=10 and dexterity <=11:
            return print("Regular:",dexterity)
        elif dexterity >=12 and dexterity <=15:
            return print("Ágil:",dexterity)
        elif dexterity >=16 and dexterity <=20:
            return print("Ninja:",dexterity)
        else:
            return print("Inperceptível: ",dexterity) 
    
    def definition_constitution(self,constitution):
        self.__constitution == constitution
        
        if constitution ==0:
            return print("Espectro:",constitution)
        elif constitution >=1 and constitution <=5:
            return print("Enfermo:",constitution)
        elif constitution >=6 and constitution <=9:
            return print("Frági:",constitution)
        elif constitution >=10 and constitution <=11:
            return print("Saudável:",constitution)
        elif constitution >=12 and constitution <=15:
            return print("Durão:",constitution)
        elif constitution >=16 and constitution <=20:
            return print("Super resistênte:",constitution)
        else:
            return print("Imortal:",constitution)
    
    def definition_wisdom(self,wisdom):
        self.__wisdom == wisdom
        
        if wisdom ==0:
            return print("Inconscinte:",wisdom)
        elif wisdom >=1 and wisdom <=5:
            return print("Irracional:",wisdom)
        elif wisdom >=6 and wisdom <=9:
            return print("Desatento:",wisdom)
        elif wisdom >=10 and wisdom <=11:
            return print("Simples:",wisdom)
        elif wisdom >=12 and wisdom <=15:
            return print("Perspcaz:",wisdom)
        elif wisdom >=16 and wisdom <=20:
            return print("Filósofo:",wisdom)
        else:
            return print("Iluminado:",wisdom)

    def definition_intelligence(self,intelligence):
        self.__intelligence == intelligence
        
        if intelligence ==0:
            return print("Inanimado:",intelligence)
        elif intelligence >=1 and intelligence <=5:
            return print("Incivilizado:",intelligence)
        elif intelligence >=6 and intelligence <=9:
            return print("Parvo:",intelligence)
        elif intelligence >=10 and intelligence <=11:
            return print("Medíocre:",intelligence)
        elif intelligence >=12 and intelligence <=15:
            return print("Estuado:",intelligence)
        elif intelligence >=16 and intelligence <=20:
            return print("Gênio:",intelligence)
        else:
            return print("Onisciente:",intelligence)

    def definition_charisma(self,charisma):
        self.__charisma == charisma
        
        if charisma ==0:
            return print("Aberração:",charisma)
        elif charisma >=1 and charisma <=5:
            return print("Inexprecivo:",charisma)
        elif charisma >=6 and charisma <=9:
            return print("Rude:",charisma)
        elif charisma >=10 and charisma <=11:
            return print("Socíavel:",charisma)
        elif charisma >=12 and charisma <=15:
            return print("Persuasivo:",charisma)
        elif charisma >=16 and charisma <=20:
            return print("Influente:",charisma)
        else:
            return print("Ídolo:",charisma)