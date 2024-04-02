class Character:
    def __init__(self, name, race):
        self.name = name
        self.race = race

    def definition_name(self, name_character):
        self.name = name_character
        return name_character 
    
    def definition_race(self, race_character):
        self.race = race_character 
        return race_character