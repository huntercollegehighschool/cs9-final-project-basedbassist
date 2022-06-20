#Use of this page is optional. If you use code here, make sure either import page2 or from page2 import * appear on your main.py page.
print("Here's your story: \n Once upon a time, there was a giant _______ named Barry. He wasn’t _______, but he did enjoy eating ______s and occasionally swinging on _____. Unlike most gorillas, he lived in a ________ shaped hut and enjoyed riding his pet _______ named Steven. 	Every Friday, Barry and Steven would cry to The _____ in our _____ and _______ in some buttered _______. They ended the night with a _____ jam session on the pair of ______ they shared and fell swiftly to sleep. ")
# gorilla code
words_lis = ["gorilla","typical","banana", "trees", "mushroom", "unicorn", "fault", "stars", "indulge", "popcorn", "quiet", "bongos"]
first_word = words_lis[0]

first_wordlist = list(first_word)

tries = 5
guess = str(input("Time to guess the word! What letter would you like to guess? You have six tries per word. "))
empty_word = list("_" * len(first_word))
emptyword_string = ' '.join(empty_word)
letters_guessed = []
times_inlist = 0
word = 1
# continue
if word == 1:
  while tries > 0:
    if len(guess) == 1 and guess.isalpha() == True and guess.islower() == True and guess not in letters_guessed:
      if guess not in first_wordlist and tries > 0:
        emptyword_string = ' '.join(empty_word)
        print("That's incorrect. Try again. You have", tries, "tries remaining. \n", emptyword_string, "\n")
        letters_guessed.append (guess)
        guess = str(input("Time to guess the word! What letter would you like to guess? "))
        tries += -1
      elif guess in first_wordlist:
        times_inlist = first_word.count(guess) # this letter occurs how many times in the list
        while times_inlist > 0: 
          index_guess = first_wordlist.index(guess)  
          empty_word[index_guess] = guess
          first_wordlist[index_guess] = "*"
          times_inlist += -1
        letters_guessed.append (guess)
        until_next = empty_word.count("_")
        emptyword_string = ' '.join(empty_word)
        if until_next > 0:
          print("That's correct! Keep guessing. \n", emptyword_string)
          guess = str(input("Time to guess the word! What letter would you like to guess? "))
        elif until_next == 0:
          if len(words_lis) == 1:
            print("You finished the story! Here's the final product: \n Once upon a time, there was a giant gorilla named Barry. He wasn’t typical, but he did enjoy eating bananas and occasionally swinging on trees. Unlike most gorillas, he lived in a mushroom shaped hut and enjoyed riding his pet unicorn named Steven. 	Every Friday, Barry and Steven would cry to The Fault in our Stars and indulge in some buttered popcorn. They ended the night with a quiet jam session on the pair of bongos they shared and fell swiftly to sleep. \n If you would like to play the other story, run the game again and select 2. If not, goodbye!")
            word = 2
          else:
            print("\n You guessed the word! It was", first_word, ". \n")
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
    else:
      if len(words_lis)!= 1:
        print("Your guess is formatted incorrectly. Please  enter one lowercase letter from the English alphabet that you have not guessed before. \n")
        print("The letters you have guessed so far are", letters_guessed, ". You have", tries, "tries remaining.")
        guess = str(input("Time to guess the word! What letter would you like to guess? "))
  if tries == 0:
    print("Whomp whomp whoooomp. You ran out of tries. Game over. Re-run the game to try again.")
  
