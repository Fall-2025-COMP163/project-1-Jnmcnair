"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Jonathan McNair
Date: 10-31-25

AI Usage: [Document any AI assistance used]
Example: Ai helped with Unicodeencoding error in save_character function and name error in load_character function as well as fixing small syntax errors throughout
"""
# Two bonus creative elements added:1st new Dexterity, Charisma, Intellect stats for characters
#2nd Different starting gold amounts based on character class
import os

#-----------------------------
# Function 1 - Create Character
#-----------------------------
def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    """
    level = 1
    stats = calculate_stats(character_class, level)
    if character_class not in ["Warrior", "Mage", "Rogue", "Cleric"]:
        return None  # Invalid class 
    else: # if class is valid the character is created

        new_character = {
            "name": name,
            "class": character_class,
            "level": level,         
            "strength": stats[0],
            "magic": stats[1],
            "health": stats[2],
            "gold": calculate_initial_gold(character_class),
            "dexterity": stats[3],
            "charisma": stats[4],
            "intellect": stats[5]
        }
        return new_character

#-----------------------------
# Function 2 - Calculate Stats
#-----------------------------
def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    """
    strength = 10 #base stats for each class at level 1 
    magic = 10 # base stats are also medium values for all classes
    health = 100
    if character_class.lower() == "warrior":# high strength, low magic, high health
        strength = 14 + (level * 2)  
        magic = 6 + level          
        health = 140 + (level * 5)
        dexterity = 10 + level
        charisma = 6 + level
        intellect = 8 + level
    elif character_class.lower() == "mage":# low strength, high magic, medium health
        strength = 6 + level         
        magic = 14 + (level * 2)    
        health = 100 + (level * 3)
        dexterity = 8 + level
        charisma = 8 + level
        intellect = 14 + (level * 2)
    elif character_class.lower() == "rogue":# medium strength, medium magic, low health
        strength = 10 + level        
        magic = 10 + level          
        health = 60 + (level * 2)
        dexterity = 14 + (level * 2)
        charisma = 10 + level
        intellect = 8 + level
    elif character_class.lower() == "cleric":# medium strength, high magic, high health
        strength = 10 + level        
        magic = 14 + (level * 2)    
        health = 140 + (level * 4)
        dexterity = 14 + (level * 2)
        charisma = 10 + level
        intellect = 8 + level
    else: 
        return None  # Invalid class
    
    return strength, magic, health # Return tuple values of stats

#-----------------------------
# Function 2.5 - Calculate Initial Gold
#-----------------------------

def calculate_initial_gold(character_class):
    """
    Calculates starting gold based on character class.
    Returns: character gold amount.
    """
    class_gold = {
        "Warrior": 150,
        "Mage": 100,
        "Rogue": 200,
        "Cleric": 125
    }
    return class_gold.get(character_class, 100)


#-----------------------------
# Function 3 - saving character file
#-----------------------------
def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    """
    

    # checking to see if character is a dictionary and filename is valid
    if not isinstance(character, dict) or not filename:
        return False # if not valid, return false
    directory = os.path.dirname(filename) # get directory from filename
    if directory and not os.path.exists(directory):
        return False
    
    with open(filename, 'w', encoding='utf-8') as f:        
        f.write(f'Character Name: {character["name"]}\n')
        f.write(f'Character Class: {character["class"]}\n')
        f.write(f'Character Level: {character["level"]}\n')
        f.write(f'Character Strength: {character["strength"]}\n')
        f.write(f'Character Magic: {character["magic"]}\n')
        f.write(f'Character Health: {character["health"]}\n')
        f.write(f'Character Dexterity: {character["dexterity"]}\n')
        f.write(f'Character Charisma: {character["charisma"]}\n')
        f.write(f'Character Intellect: {character["intellect"]}\n')
        f.write(f'Character Gold: {character["gold"]}\n')

    return True
  
#-----------------------------
# Function 4 - Loading saved character file
#-----------------------------


def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    import os
    if not os.path.exists(filename): # checking to see if file exists if not returns none
        return None
    load = {}
    with open(filename, 'r') as f:
        for line in f:
            if ':' not in line:
                continue
            key, value = line.strip().split(':', 1)
            key = key.lower().replace('character', '').strip()
            value = value.strip()
            if value.isdigit():
                value = int(value)
            load[key] = value
    return load

        


    
#-----------------------------
# Function 4 - Displays character sheet
#-----------------------------
def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    """
    if character is None or not isinstance(character, dict):
        return None
    print("=== CHARACTER SHEET ===") #printing out each stat in the formatted way
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Dexterity: {character['dexterity']}")
    print(f"Charisma: {character['charisma']}")
    print(f"Intellect: {character['intellect']}")
    print(f"Gold: {character['gold']}")
    
#-----------------------------
# Function 5 - Level Up Character
#-----------------------------
def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    
    character['level'] += 1  # Increase level by +1
    stats = calculate_stats(character['class'], character['level'])
    character['strength'] = stats[0]
    character['magic'] = stats[1]
    character['health'] = stats[2]
    character['dexterity'] = stats[3]
    character['charisma'] = stats[4]
    character['intellect'] = stats[5]


# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    char = create_character("Rhapsody", "Warrior")
    display_character(char)
    
    print("\nSaving character...")
    save_character(char, "Rhapsody.txt")
    
    print("\nLoading character...")
    loaded = load_character("Rhapsody.txt")
    display_character(loaded)

    print("\nLeveling up character...")
    level_up(loaded)
    display_character(loaded)

