import random

word_list = ["apple", "tiger", "chair", "table", "plant"]
secret_word = random.choice(word_list)

guessed_letters = []
display_word = ["_"] * len(secret_word)
incorrect_attempts = 0
max_attempts = 6

print("="*40)
print("🎮 HANGMAN GAME")
print("="*40)
print("Guess the word letter by letter")
print(f"Maximum wrong attempts: {max_attempts}")
print("="*40)

while incorrect_attempts < max_attempts and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Guessed Letters:", ", ".join(guessed_letters))

    guess = input("Enter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Enter a valid single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good job! Correct letter.")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_attempts += 1
        print(f"❌ Wrong guess! Attempts left: {max_attempts - incorrect_attempts}")

print("\n" + "="*40)

if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game Over! The word was:", secret_word)

print("="*40)
