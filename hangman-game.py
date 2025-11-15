import random  

words = ["python","data","science","machine","learning"]
secret_word = random.choice(words)
guessed_letters = []        
wrong_guesses = 0           
max_wrong = 6              
print("🎉 Welcome to Hangman!")
print("Guess the word letter by letter.")
print(f"You have {max_wrong} incorrect guesses allowed.\n")
while wrong_guesses < max_wrong:
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word)
    if "_" not in display_word:
        print("\n✅ Congratulations! You guessed the word:", secret_word)
        break
    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("❗ Please enter a single alphabet letter.\n")
        continue
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue
    if guess in secret_word:
        guessed_letters.append(guess)
        print("✓ Correct guess!\n")
    else:
        wrong_guesses += 1
        print("✗ Wrong guess!")
        print(f"Remaining attempts: {max_wrong - wrong_guesses}\n")
if wrong_guesses == max_wrong:
    print("\n❌ Game Over!")
    print("The correct word was:", secret_word)