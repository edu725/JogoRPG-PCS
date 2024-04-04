import random
from attribute import Attribute
from character import Character

attribute = Attribute()
name = input("Digite o nome do seu personagem: ")
race = random.randint(1,7)
character = Character(name, race)
strength = random.randint(1,21)
dexterity = random.randint(1,21)
constitution = random.randint(1,21)
wisdom = random.randint(1,21)
intelligence = random.randint(1,21)
charisma = random.randint(1,21)
match race:
    case 1:
        constitution +=2
        sub_race = random.randint(1,2)
        if sub_race ==  1:
            sub_race = "Anão da Colina"
            wisdom +=1
        elif sub_race == 2:
            sub_race = "Anão da Montanha"
            strength+=2
    case 2:
        dexterity+=2
        sub_race = random.randint(1,2)
        if sub_race == 1:
            sub_race = "Elfo alto"
            intelligence +=1
        elif sub_race == 2:
            sub_race = "Elfo da Floresta"
            wisdom+=1
    case 3:
        strength += 1 
        dexterity += 1
        constitution += 1
        wisdom += 1
        intelligence += 1
        charisma += 1    
    case 4:
        dexterity+=2
        sub_race = random.randint(1,2)
        if sub_race == 1:
            sub_race = "Pés leves"
            charisma +=1
        elif sub_race == 2:
            sub_race = "Parrudos"
            constitution+=1
    case 5:
        strength +=2
        charisma +=1
    case 6:
        intelligence+=2
        sub_race = random.randint(1,2)
        if sub_race == 1:
            sub_race = "Gnomo da Floresta"
            dexterity +=1
        elif sub_race == 2:
            sub_race = "Gbono da Pedra"
            constitution+=1
    case 7:
        intelligence+=1
        charisma+=2        
print("----------------")
print("Nome: ",character.definition_name(name))
print("Classe: ",character.definition_race(race))
if race == 1 or race == 2 or race == 4 or race == 6:
    print("Sub-Classe: ",character.definitios_sub_race(sub_race))
print(attribute.definition_strength(strength))
print(attribute.definition_dexterity(dexterity))
print(attribute.definition_constitution(constitution))
print(attribute.definition_wisdom(wisdom))
print(attribute.definition_intelligence(intelligence))
print(attribute.definition_charisma(charisma))