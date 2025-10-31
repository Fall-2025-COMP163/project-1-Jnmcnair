"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Jonathan McNair
Date: 10-31-25

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
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
            "gold": 100
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
    elif character_class.lower() == "mage":# low strength, high magic, medium health
        strength = 6 + level         
        magic = 14 + (level * 2)    
        health = 100 + (level * 3)
    elif character_class.lower() == "rogue":# medium strength, medium magic, low health
        strength = 10 + level        
        magic = 10 + level          
        health = 60 + (level * 2)
    elif character_class.lower() == "cleric":# medium strength, high magic, high health
        strength = 10 + level        
        magic = 14 + (level * 2)    
        health = 140 + (level * 4)
    else: 
        return None  # Invalid class
    
    return strength, magic, health # Return tuple values of stats

#-----------------------------
# Function 3 - saving character file
#-----------------------------
def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    """
    
    import os
    # checking to see if character is a dictionary and filename is valid
    if not isinstance(character, dict) or not filename:
        return False # if not valid, return false
    directory = os.path.dirname(filename) # get directory from filename
    if directory and not os.path.exists(directory):
        return False
    
    with open(filename, 'w') as file: #opens file in the write mode using with to make sure it closes afterwards
        file.write(f"Character Name: {character['name']}\n") 
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")# writing each key-value pair to the file to match the format and display stats
    return True
  



def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    pass

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
