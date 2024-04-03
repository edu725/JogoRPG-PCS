import random
from attribute import Attribute
from character import Character

attribute = Attribute()
name = input("Digite o nome do seu personagem: ")
print("CLASSES DISPONIVEIS!")
print(" (1) Anão(+2 em constituição)")
print(" (2) Elfo(+2 em destreza)")
print(" (3) Humano(+1 em todos os atributos)")
print(" (4) Barbaro(+2 em destreza)")
print(" (5) Draconato(+2 em força e +1 em carisma)")
print(" (6) Gnomo(+2 em inteligencia)")
print(" (7) Ladrão(+1 em inteligencia e +2 em carisma)")
race = int(input("Digite o número da classe do seu persoagem: "))
sub_race = int
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
        print("ESCOLHA UMA DAS SUB-CLASSES")
        print(" (1) Anão da Colina(+1 de sabedoria)")
        print(" (2) Anão da Montanha(+2 de força)")
        sub_race = input("Digite o número da sua sub-classe: ")
        if sub_race == 1:
            wisdom +=1
        else:
            strength+=2
    case 2:
        dexterity+=2
        print("ESCOLHA UMA DAS SUB-CLASSES")
        print(" (1) Alto Elfo(+1 de inteligencia)")
        print(" (2) Elfo da floresta(+1 de sabedoria)")
        sub_race = input("Digite o número da sua sub-classe: ")
        if sub_race == 1:
            intelligence +=1
        else:
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
        print("ESCOLHA UMA DAS SUB-CLASSES")
        print(" (1) Pés leves(+1 em carisma)")
        print(" (2) Parrudos(+1 em constituição)")
        sub_race = input("Digite o número da sua sub-classe: ")
        if sub_race == 1:
            charisma +=1
        else:
            constitution+=1
    case 5:
        strength +=2
        charisma +=1
    case 6:
        intelligence+=2
        print("ESCOLHA UMA DAS SUB-CLASSES")
        print(" (1) Gnomo da Floresta(+1 em destreza)")
        print(" (2) Gnomo da Pedra(+1 em constituição)")
        sub_race = input("Digite o número da sua sub-classe: ")
        if sub_race == 1:
            dexterity +=1
        else:
            constitution+=1
    case 7:
        intelligence+=1
        charisma+=2        
print("----------------")
print("Nome: ",character.definition_name(name))
match race:
    case 1:
        race = "Anão"
        print("Classe: ",character.definition_race(race))
    case 2:
        race = "Elfo"
        print("Classe: ",character.definition_race(race))
    case 3:
        race = "Humano"
        print("Classe: ",character.definition_race(race))
    case 4:
        race = "Barbaro"
        print("Classe: ",character.definition_race(race))
    case 5:
        race = "Draconato"
        print("Classe: ",character.definition_race(race))
    case 6:
        race = "Gnomo"
        print("Classe: ",character.definition_race(race))
    case 7:
        race = "Ladrão"
        print("Classe: ",character.definition_race(race))
if race == "Anão" or race == "Elfo" or race == "Barbaro" or race =="Gnomo":
    print("Sub-Classe: ",character.definitios_sub_race(sub_race))
print(attribute.definition_strength(strength))
print(attribute.definition_dexterity(dexterity))
print(attribute.definition_constitution(constitution))
print(attribute.definition_wisdom(wisdom))
print(attribute.definition_intelligence(intelligence))
print(attribute.definition_charisma(charisma))