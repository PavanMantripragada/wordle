# Wordle Sieve
You can enter your wordle trials here and get the list of possible
words. 

  ## Dependencies to run the codes    
  1. Python 3.6 should be installed on your system.
  2. In case you don't want to install python on your system, you can open this [link](https://replit.com/@PavanMantriprag/wordle-sieve?v=1) on any web browers on your PC/laptop/mobile.

  ## Instructions to run the code
  1. Clone the repository by clicking [here!](https://github.com/PavanMantripragada/wordle/) 
  2. Open command prompt or terminal.
  3. Navigate to this directory using `cd wordle/scripts`
  4. To Run, type `python3 wordle_sieve.py`
  5. Enjoy!

  ### Specific instructions for wordle_sieve.py
  1. The program will ask you to enter the word that you have entered in the wordle game.
  2. Please only use lower case letters!!!
  3. Next, it will prompt you enter a response. Please follow the notation mentioned below for that input
  4. Each color is denoted with a character
  5. Green - "g", Yellow - "y", Grey - "_"
  6. Let us look at a sample run case.
  7. Let the answer be "windy" and our sequential guesses be {weary,whiny,windy}
  8. Make sure you enter the respective wordle outcome after each guess word you've entered as shown below.
    
    >>> python3 wordle_sieve.py
    >>> Enter the word : weary
    >>> Enter the outcome : g___g
    >>> The program will print all possible options here [---]
    >>> Enter the word : whiny
    >>> Enter the outcome : g_yyg
    >>> The program will print all possible options here [---]
  
  
    