import random
from shlex import join

categories = {
      "Animals": ["Cat","Dog","Elephant", "Tiger", "Panda",      "Monkey"],
      "Colors": ["Red", "Blue", "Green", "Yellow", "Pink", "Black"],
      "Countries": ["USA", "Canada", "India", "China", "Brazil", "France"],
      "Fruits": ["Apple", "Banana", "Orange", "Grapes", "Mango", "Pineapple"],
      "Sports": ["Football", "Cricket", "Tennis", "Basketball", "Baseball", "Hockey"],
      "Vehicles": ["Car", "Bike", "Bus", "Truck", "Train", "Airplane"],
      "Movies": ["Inception", "Titanic", "Avatar", "The Godfather", "The Dark Knight", "Pulp Fiction", "Forrest Gump"],
      "Books": ["Harry Potter", "The Hobbit", "Atomic Habits", "To Kill a Mockingbird", "Pride and Prejudice"],
      "Tv Shows": ["Breaking Bad", "Game of Thrones", "Better Call Soul", "The Office", "Friends"],
}

def main():
      print("Welcome to Hangman Game!")
      print("You have to guess the word in 6 attempts.")
      print("You can choose from the following categories:")
      for i in categories.keys():
            print(i)
      category = input("Enter category: ").strip()
      print("You selected:", category)
      categoryName = {key.casefold(): key for key in categories.keys()}
      # print(categoryName)
      if category not in categoryName:
            print("Invalid category!")
            return
      # print("yep")
      # to get capatalized name of the category
      selectedCategory = categoryName[category]

      word = random.choice(categories[selectedCategory])
      #(for testing) print("word selected is: ", word)

      guessWord(word, lives = 6)
      print("Thanks for playing Hangman!! Hope you had a great time playing")

def guessWord(word, lives):
      word = list(word.lower())
      guessedWord = ["_"] * len(word)
      guessedLetters = []
      try:
            while lives > 0 and guessedWord != word:
                  print("lives remaining: ", lives)
                  print("current word: ", "".join(guessedWord))
                  print("guessed Letters: ", guessedLetters)
                  letter = input("Guess a Letter: ").strip().lower()
                  if len(letter) != 1 or not letter.isalpha():
                        print("Invalid input!! Please enter a single letter from A to Z")
                        continue
                  
                  if letter in guessedLetters:
                        print("You already guessed that letter")
                        continue
            
                  guessedLetters.append(letter)
                  if letter not in word:
                        print(f'Letter {letter} is not present in the word')
                        lives -= 1
                  
                  if letter in word:
                        for i in range(len(word)):
                              if word[i] == letter:
                                    guessedWord[i] = letter
                              if word[i] == ' ':
                                    guessedWord[i] = ' '
                  # print("guessWord: ", guessedWord)
            
            if guessedWord == word:
                  print(" ")
                  print("Word :", "".join(word))
                  print("Congratulations !! You have guessed the letter")
            else:
                  print(" ")
                  print("Word :","".join(word))
                  print("You didn't guessed the word in 6 tries")
      except:
            print("Invalid input!! try again...")
                  
main()