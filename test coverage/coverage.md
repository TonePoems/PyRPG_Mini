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
  - Created the Archer, Monk, and Assassin playable characters
  - Modified flow of the game within the Blacksmith and Peddler
  
Archer, Monk, and Assassin playable classes:
A rework was done to the critical system and the logic tested in a separate program to confirm correct function. Extra logic was needed and tested with the special logic for the assassin's attacks, being able to ONLY crit.

Flow of game in Blacksmith and Peddler:
Originally most actions taken at the blacksmith or peddler sent the player back to the camp where they started the interaction. This took away from the gameplay, so I modified the functions to loop until specifically requesting to go back to base. This was tested in-game and with the coverage.
  
Nour Hijazi:
  -
  -
  -
  
Andrew Brown:
  -
  -
  -
  
