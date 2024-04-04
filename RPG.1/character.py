class Character:
    from attribute import Attribute
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.__sub_race = int

    @property
    def sub_race(self) -> int:
        return self.__sub_race
    
    @sub_race.setter
    def strenght(self, sub_race):
        self.__sub_race  = sub_race

    def definition_name(self, name_character):
        self.name = name_character
        return name_character 
    
    def definition_race(self, race_character):
        self.race = race_character
        match race_character:
            case 1:
                race_character = "Anão"
            case 2:
                race_character = "Elfo"
            case 3:
                race_character = "Humano"
            case 4:
                race_character = "Barbaro"
            case 5:
                race_character = "Draconato"
            case 6:
                race_character = "Gnomo"
            case 7:
                race_character = "Ladrão"
        return race_character
    
    def definitios_sub_race(self,sub_race_character):
        self.__sub_race = sub_race_character
        return sub_race_character