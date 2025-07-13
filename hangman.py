import random

# Predefined list of 5 words
words = ['python', 'apple', 'hangman', 'code', 'alpha']
selected_word = random.choice(words)

# Variables
guessed_letters = []
tries = 6
word_display = ['_' for _ in selected_word]

print("🎯 Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

# Game loop
while tries > 0 and '_' in word_display:
    print("Word: ", ' '.join(word_display))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabetic letter.\n")
        continue

    if guess in guessed_letters:
        print("🔁 You've already guessed that letter. Try another one.\n")
        continue

    guessed_letters.append(guess)

    if guess in selected_word:
        print("✅ Good job! Letter is in the word.\n")
        for i, letter in enumerate(selected_word):
            if letter == guess:
                word_display[i] = guess
    else:
        tries -= 1
        print(f"❌ Wrong guess! You have {tries} tries left.\n")

# Game result
if '_' not in word_display:
    print("🎉 Congratulations! You guessed the word:", selected_word)
else:
    print("😢 Game over! The correct word was:", selected_word)
