This file is a representation of how each group member individually tested their code. If you want the actual metrics check the metrics folder within this test coverage folder.

Caleb Austin:
  -
  - Created web application shell
  - Created a random name generator
  - Added a new knight character
  - Changed the start menu to be more user compatible (e.g handle invalid user input)
  
Web Application Shell:
After adding individual pages within the application, I tested them by making sure that each page was reachable. Since this was mostly html and templating there was not a whole lot to be tested other than making sure that the pages were showing up and reachable. 

Random Name Generator: 
Typically, when not putting your name into the game, the game automatically gives you the name 'Sir Lazy.' I thought it would be cool to generate random names for users who don't put a name in. The way that I tested this was by opting to not put my name in and then checking to make sure that a random name was then given to the user upon starting the game. The testing was sucessful and there seemed to be no errors when running it. Some issues at first were index out of bounds errors when searching through the csv file to pull random prefixes and suffixes for the names. 

Added Knight Character:
The addition of the knight character was created to add more dynamic layers to the game. The addition of a new character with different abilities and different strengths and weaknesses allows the game to be more fun. The addition of this character was tested by making sure that when the user selects the knight character, that the knight character is actually created and populated with the correct stats. 

Changes to the Start Menu:
Originally, the start menu was not handling error user input. Instead, the game would assign things to the user when incorrect input is put in. This becomes problematic because the user, when the game is pushed to production, should not be put in debug mode when playing the game. The way this was tested was by entering incorrect input into the console when asked if I wanted to do things like "Play in debug mode" or "Play with riddles." 

Anthony Mitchell:
  -
  - Created the Archer, Monk, and Assassin playable characters
  - Modified flow of the game within the Blacksmith and Peddler
  
Archer, Monk, and Assassin playable classes:
A rework was done to the critical system and the logic tested in a separate program to confirm correct function. Extra logic was needed and tested with the special logic for the assassin's attacks, being able to ONLY crit.

Flow of game in Blacksmith and Peddler:
Originally most actions taken at the blacksmith or peddler sent the player back to the camp where they started the interaction. This took away from the gameplay, so I modified the functions to loop until specifically requesting to go back to base. This was tested in-game and with the coverage.
  
Nour Hijazi:
  -
  - Created two mini games, Caesar cipher and word scrambler 
  - Added some input validation in game.py
  - Expanded the web functionality by adding in more templates for signing up and resetting passwords

Mini-games:
The user can play mini games while camping that can gain/lose health, depending on how well they perform. I added in the functionality for the games and modified the menu screen on game.py to allow users to play them.
I tested these games by playing them numerous time myself, with the answers printed out so I could confirm that I was correct in my guesses. I monitored my character's health while playing them to ensure that the correct amount of health was being added or subtracted. I tested multiple scenarios in winning, losing, and break even in terms of health to test edge cases. I also left the debugger on when the database in first populated to make sure my list of words were being read from the csv and populating the correct table.

Input validation:
The game would crash if the user entered in a string where an int was required. It also crashed when selecting a load file if the user typed in a number that was out of range of the indexed games. I tested these by throwing in nonsense strings and purposefully trying to load files based on numbers not in the array.

Expand the Web application:
The web application allows users to sign up for accounts in the game to save their progress. I added some functionality to it including a sign up page and a password reset page. I added some additional input validation to these pages to make sure none of the fields were left empty, that they were of appropriate length, and included a variety of characters. I tested this validation by leaving individual fields blank and typing in nonsense strings into fields without numbers or non-alphabetical characters required by the validator. I accessed these pages from the command line to make sure they rendered correctly.
  
George Brown:
  -
  - Expanded inventory/equipment management systems
  - Added autosave feature
  - Added a new barbarian character

Inventory Management System:
The inventory system holds usable items found in the game. I added changes that allowed the user to drop and see info on items in the inventory.
To test these changes, I would gather many items and ensure that the info and drop commands properly did as intended, esuring that there aren't any 
indexing exceptions.

Equipment Management System:
The equipment management system holds items such as: weapons, shields and armor. Each piece of equipment can be equipped, dropped or be shown stats.
These items are found while adventuring, the user can choose to equip, store or discard the found equipment.
I forced the game to find these items and allowed me to test the equip, store and discard options. I manually went through each type of equipment and 
ensured that each action did as intended. The same method follows for when the user is going through his/her equipment. Exceptions are placed in case of 
invalid input and incorrect indexing.

Autosave Feature:
The game will autosave when returning to camp from adventuring. All Hero data is saved into a file, the same as manually saving the game. 
This feature can be toggled on/off from the camp menu. To test this, I would allow the game to autosave then quit and reload that save to ensure that
the progress made to the Hero was actually saved.

Added Barbarian Character:
The addition of the barbarian character was created to add more dynamic layers to the game. The addition of a new character with different abilities and different strengths and weaknesses allows the game to be more fun. The addition of this character was tested by making sure that when the user selects the barbarian character, that the barbarian character is actually created and populated with the correct stats. 


Name                                                     Stmts   Miss  Cover
----------------------------------------------------------------------------
/Users/caleb/.local/lib/python3.8/site-packages/six.py     491    244    50%
Armor.py                                                    80     42    48%
Enemy.py                                                    50     17    66%
Game.py                                                   1010    739    27%
Hero.py                                                    257    123    52%
Item.py                                                     17      7    59%
Shield.py                                                   80     42    48%
Weapon.py                                                   72     36    50%
__init__.py                                                 25      6    76%
dbsetup.py                                                 167    156     7%
texttools.py                                                54      8    85%
----------------------------------------------------------------------------
TOTAL                                                     2303   1420    38%
