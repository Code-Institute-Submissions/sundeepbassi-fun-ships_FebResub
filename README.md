# Fun-Ships

- Fun-Ships is a noughts and crosses game (tik tak toe in American) designed on the original paper played game.

- For more information about noughts and crosses check out [Wikipedia](https://en.wikipedia.org/wiki/Tic-tac-toe)

- Funships is coded in python and the code is outputted in the terminal the game is also deployed to Heroku.

- The game is designed to be played by a single person against the computer.

- The objective of the game is for the player to place  3 X's on the grid board in a line to win.


## How To Play

- The player has to input a number from 1 to 9.

- Then the player is prompted to enter another number.

- X represents the players symbol on the grid.

- O represents the computer symbol on the grid.

- The player must try to get three x's in a line.

- The Computer will try to block the player.



## Features

[screenshot 1](assets/screenshots/tak-1.png)

### Existing Features

- There ia a grid board for the player to play the game.

- The player is greeted with a welcome.

- The player is given an option to input a number value for the grid board from 1 - 9.

- The player is prompted again to input a numnber and this will continue until either the player or computer wins or draws.

### Future Features

- Allow player to have the opportunity to play against someone else.


###  Data Model
 
The model that I am using for this project is based on a grid board function.

The grid board function contains both the players turn and the computers turn.

The grid board functions are, define the board, who goes first, print the board, is the board full, check if there is a winner,
is a space free, place a marker on the board, who goes first, player turn, create a copy of the board, computer turn, check if player can win, if computer plays first, and run the game.

There is a choice to put in a number between 1 to 9.

###  Testing

- I did manual testing on the project by:

- Putting the code into the Pep8 linter validator testing check.  The code was passed without any problems and errors.

- I also did tests on the inputs to see what would happen if I inputted a number above 9. The function workS because 
  the player is prompted to input a number between 1 and 9.

- The code was also tested on the local terminal and in Heroku. 



###  Bugs

- There were bugs in the code that inhibited it from running properly.  I had to contact tutor support and reach out
to the slack community for support. The bugs were related to the nesting of the code in the loops.

The bugs were removed and it was the tutorial from Knowledge Mavens that helped remove the bugs.

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.




###  Remaining Bugs



###  Validator Testing

- Removed errors from code after checking in pep8 mainly indentation errors were removed. 24/10/21.

- pep8
       - No errors were returned from pep8online.com.

- [Pep 8 online passed screenshot](assets/screenshots/peppass.png)

###  Deployment
- The project was deployed using the code Instiutes mock terminal for Heroku.

  - Steps for deployment:
      - Fork or clone this repository
      - Creat a new Heroku app
      - Set the build blocks to Python and Nodejs in that order 
      - Link the Heroku app to the repository
      - Click on **Deploy**

###  Credits

- Data modelling information from Database Design 2nd Edition

- [Database Design](https://opentextbc.ca/dbdesign01/chapter/chapter-4-types-of-database-models/)

- [Database Design](https://opentextbc.ca/dbdesign01/chapter/chapter-5-data-modelling/)

- The code for adding the import random is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.

- The code for adding playerLetter and the computerLetter with values is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.


- The code for define the board is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.


- The code for the print_board function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.

- The code for the is_full function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.


- The code for the check_win function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.


- The code for the is_free function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.


- The code for the place_marker function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.

- The code for the who_goes_first function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.

- Credits to the tutor support and slack community for supporting me with bug fixes and 
  resolving errors in the code.

- The bug and errors in the code were resolved by checking with the Youtube tutorial from:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.

- The other resources to sort the bugs were:

- [Stack overflow](https://stackoverflow.com/questions/52809455/nested-loops-in-python)

- [Geeks for Geeks](https://www.geeksforgeeks.org/loops-in-python/)

- The code for the player_turn function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The code for the duplicate _board function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The code for the computer_turn function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The code for the check if the player can win function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The code for the if computer plays first function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The code for the run the game function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The code for the start the game function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- To add the # noqa: E501 at the end of line 112 is accredited to the tutors at the Code Institute 
  for helping me to rectify this warning in pep 8 online validation checker.

- To remove the white trailing spaces from the code is accredited to fellow students on Slack and 
  the tutor support team.

- In my mentoring session my mentor highlighted the need to check my code thoroughly for bugs and errors.

- 




The credits below were used for the design of previous projects,  I decided to keep them in the credits for both reference and research purposes.

- HIDDEN_BOARD and GUESS_BOARD is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- These functions code used in the project, def board():, def make_ships():, def bring_ship_place():, def count_attacked_ships():,
are all accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The code added to the print_board function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The random function import is accredited to both:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The code institute python essentials information.

- The code added to the make_ships function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The comment added at the top of the code file for the legend is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The code added to the bring_ships_place function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The code added to the count_attacked_ships function  is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The code added to the make_ships function  is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The information on constructing and checking the readme for the battleships game is accredited to the Code Institute
Battleships game readme.

- My Mentor Miguel Martinez helped me to align the grid with spaces, and the lines.  Better visibility for the player.

- Martin also helped me to insert line breaks for the input sections for the numbers and the letters.

- The code below is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.


- LENGTH_OF_SHIPS = [2, 3, 3, 4, 5]
- PLAYER_BOARD = [[" "] * 8 for i in range(8)]
- COMPUTER_BOARD = [[" "] * 8 for i in range(8)]
- PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
- COMPUTER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
- LET_TO_NUM = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

- The code added to the print_board function  is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The import random is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The code added to the place_ships function  is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.


- The code added to the check_ship_fit  function  is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

### Disclaimer

- The contents of this project are solely for the purposes of education and research.  
- All of  the information and code that has been used from outside resources has be accredited to that person or organisation.

### Acknowledgements

I would like to thank my mentor Miguel Martinez for being an excellent mentor anf guiding me with the project.  Miguel's insights, experince and knowledge have empowered me to try to do my best and not to give up.

I would like to thank Scott and Ed from the tutor support team to find good solutions whislt working with my code.

I would like to thank the whole of the tutor support for helping me with coding issues.

I would like to thank the student care team, Alex, Kieron and Aoife for listening to me and pointing me in the right direction.

I would like to thank my friends Claire and Holly for believing in me and checking on me when I was stressed with the course work and the project.

I would like thank Claire's pets, Bodhi (dog), Lass (dog), Mitzy (dog), Kiddy (cat) and Rabsie (rabbit), for sitting with me whilst I was doing my work and the endless support they gave me.  The dog walks helped me to get fresh air into my brain cells.

























    
























