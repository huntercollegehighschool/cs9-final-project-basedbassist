print("Upon a ___________ ocean sails a ______ soldier, returning from his ____ trip to a ________ island not far from his ____. The boat\'s ____ is splintered and its _____ are torn, yet he bears an incredible _____ and tries to ________ everything around him for when he _______ to ______." ) #story
# sailors code
words_lis = ["crystalline","mighty","last", "peaceful", "home", "mast", "sails", "smile", "remember", "returns", "battle"] #words in story
first_word = words_lis[0] #gets first word from list

first_wordlist = list(first_word) #makes it into list

tries = 5 #there are six but it uses up one in the beginning
guess = str(input("Time to guess the word! What letter would you like to guess? You have six tries per word. ")) #guess
empty_word = list("_" * len(first_word)) #generates the ______
emptyword_string = ' '.join(empty_word) #makes it a string
letters_guessed = [] #for when guess is formatted wrong
times_inlist = 0 #for indexing
word = 1 #while word is 1 the code runs
# continue
if word == 1:
  while tries > 0:
    if len(guess) == 1 and guess.isalpha() == True and guess.islower() == True and guess not in letters_guessed: #checks if guess is formatted right 
      if guess not in first_wordlist and tries > 0: #checks if guess is incorrect
        emptyword_string = ' '.join(empty_word)
        print("That's incorrect. Try again. You have", tries, "tries remaining. \n", emptyword_string, "\n")
        letters_guessed.append (guess)
        guess = str(input("Time to guess the word! What letter would you like to guess? "))
        tries += -1
      elif guess in first_wordlist: #checks if guess is correct
        times_inlist = first_word.count(guess) # figures out how many times the letter occurs in the word
        while times_inlist > 0: #deals with repeat letters in a word
          index_guess = first_wordlist.index(guess)  
          empty_word[index_guess] = guess
          first_wordlist[index_guess] = "*"
          times_inlist += -1
        letters_guessed.append (guess)
        until_next = empty_word.count("_")
        emptyword_string = ' '.join(empty_word)
        if until_next > 0: #checks if player needs to guess more letters
          print("That's correct! Keep guessing. \n", emptyword_string)
          guess = str(input("Time to guess the word! What letter would you like to guess? "))
        elif until_next == 0: #checks if story is done
          if len(words_lis) == 1:
            print("You finished the story! Here's the final product: \n Upon a crystalline ocean sails a mighty soldier, returning from his last trip to a peaceful island not far from his home. The boat\'s mast is splintered and its sails are torn, yet he bears an incredible smile and tries to remember everything around him for when he returns to battle.  \n If you would like to play the other story, run the game again and select 2. If not, goodbye!")
            word = 2 #stops code
          else: #continues to next word
            print("You guessed the word! It was", first_word, ". \n")
            print("Let's move on to the next word.")
            del words_lis[0] 
            first_word = words_lis[0]
            first_wordlist = list(first_word)
            tries = 6
            letters_guessed = []
            times_inlist = 0
            word = 1
            empty_word = list("_" * len(first_word))
            guess = str(input("Time to guess the word! What letter would you like to guess? You have six tries. "))     
    else: #deals with guesses that are formatted wrong
      if len(words_lis)!= 1:
        print("Your guess is formatted incorrectly. Please  enter one lowercase letter from the English alphabet that you have not guessed before. \n")
        print("The letters you have guessed so far are", letters_guessed, ". You have", tries, "tries remaining.")
        guess = str(input("Time to guess the word! What letter would you like to guess? "))
  if tries == 0: #deals with losing
    print("Whomp whomp whoooomp. You ran out of tries. Game over. Re-run the game to try again.")