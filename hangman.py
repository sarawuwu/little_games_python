import random
from replit import clear
from art import stages,hangman_logo
from list import word_list

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives=6

print(hangman_logo)

print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  clear()

  if guess in display:
    print(f"You already guess the word {guess},please try another word.")

  if guess in chosen_word:
    for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = letter
    # print(display)
    print(f"{' '.join(display)}")
  else:
    lives -=1
    if lives == 0:
      end_of_game=True
      print("you lose")
      print(stages[lives])
    else:
      print(f"You guess {guess} , that's not in the word. You lose a life, still have {lives} lives.")
      print(stages[lives])

   

    
    print(f"{' '.join(display)}")


if "_" not in display:
  end_of_game = True
  print("You win.")
