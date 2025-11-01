[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/JTXl4WMa)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21255565&assignment_repo_type=AssignmentRepo)
# COMP 163 - Project 1: Character Creator & Chronicles
# 🎯 Project Overview

Build a text-based RPG character creation and story progression system that demonstrates mastery of functions and file I/O operations.

# Required Functions 
Complete these functions in project1_starter.py:

create_character(name, character_class) - Create new character

calculate_stats(character_class, level) - Calculate character stats

save_character(character, filename) - Save character to file

load_character(filename) - Load character from file

display_character(character) - Display character info

level_up(character) - Increase character level

# 🎭 Character Classes
Implement these character classes with unique stat distributions:


Warrior: High strength, low magic, high health

Mage: Low strength, high magic, medium health

Rogue: Medium strength, medium magic, low health

Cleric: Medium strength, high magic, high health

# 📁 Required File Format
Your save_character() function must create files in this exact format:

Character Name: [name]

Class: [class]

Level: [level]

Strength: [strength]

Magic: [magic]

Health: [health]

Gold: [gold]


# Run specific test file
python -m pytest tests/test_character_creation.py -v

# Test your main program
python project1_starter.py

GitHub Testing:

After pushing your code, check the Actions tab to see automated test results:

✅ Green checkmarks = tests passed
❌ Red X's = tests failed (click to see details)

# ⚠️ Important Notes
Protected Files

DO NOT MODIFY files in the tests/ directory

DO NOT MODIFY files in the .github/ directory

Modifying protected files will result in automatic academic integrity violation

# AI Usage Policy

✅ Allowed: AI assistance for implementation, debugging, learning

📝 Required: Document AI usage in code comments

🎯 Must be able to explain: Every line of code during interview

# 📝 Submission Checklist

 All required functions implemented
 
 Code passes all automated tests
 
 README updated with your documentation
 
 Interview scheduled and completed
 
 AI usage documented in code comments

# 🏆 Grading

Implementation (70%): Function correctness, file operations, error handling

Interview (30%): Code explanation and live coding challenge

What's your RPG world about?

The game is a DnD campaign in a fantasy world focused on rebuilding after a dark age. The four character classes (Warrior, Mage, Rogue, Cleric) each play a vital role in restoring the kingdom. Each class have their own expertise and unique skillset.

Why did you choose your stat formulas?

I wanted to keep the baseline around 10 for the base stat points because thats what it has been in a previous DnD campain that I have played. The calculations being in increments of 4 were just to thoroughly set each characters advantages and disadvantages while not being too under/overpowered.

Did you add anything unique?
The main creative additions were expanding the character stats to include three new core attributes being Dexterity, Charisma, and Intellect. This makes character specialization much deeper and allows for unique builds across all four classes. I also added a gold calculation system which calculated gold based on level and class of your character.

AI Usage: What AI assistance did you use and where?
Gemini AI was primarily used for debugging and error resolution. It was used to help fix the Unicodeencoding error in the load_character function and helped resolve a NameError in the save character function. It was also used for small synatx errors throughtout the entire project.

Clear instructions for testing your code

The code within the if __name__ == "__main__": block will automatically run a full test sequence:

Creates a Level 1 Warrior.

Saves the Warrior's data to a text file (Rhapsody.txt).

Loads the data back from the file.

Calls the level_up function to check that the character's level and all seven stats (including gold) are correctly recalculated.

