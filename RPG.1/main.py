import random
from attribute import Attribute

attribute = Attribute()
strength = random.randint(1,21)
dexterity = random.randint(1,21)
constitution = random.randint(1,21)
wisdom = random.randint(1,21)
intelligence = random.randint(1,21)
charisma = random.randint(1,21)



print(attribute.definition_strength(strength))
print(attribute.definition_dexterity(dexterity))
print(attribute.definition_constitution(constitution))
print(attribute.definition_wisdom(wisdom))
print(attribute.definition_intelligence(intelligence))
print(attribute.definition_charisma(charisma))
