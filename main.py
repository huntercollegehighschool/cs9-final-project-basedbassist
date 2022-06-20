"""
Name(s):
Name of Project:
"""
import page1  
story = int(input("Welcome to Mad Man: A game where you're given a prewritten story and you have to guess the words hangman style! \n You'll start with the first word of each story and you have six tries to guess it. \n After that, you'll move onto the next word until you complete the story. \n Be careful, because if you can't guess a word you'll have to start all over again... \n Would you like to play story 1 (silly) or 2 (somber) ? "))
if story == 1:
  import page2
elif story == 2:
  import page3
else: 
  print ("Oops! That's not an option!")


#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
