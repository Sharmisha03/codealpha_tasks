# 🎮 Task 1: Hangman Game

## 📌 Description
This project is a simple text-based Hangman game developed using Python.  
The program randomly selects a word from a predefined list, and the user has to guess the word one letter at a time.

---

## 🚀 Features
- Random word selection from a list of 5 words
- Maximum of 6 incorrect guesses allowed
- Displays progress using underscores (_)
- Tracks already guessed letters
- Input validation for correct user input
- Win and Loss conditions

---

## 🧠 Concepts Used
- random module
- while loop
- if-else statements
- strings
- lists

---

## ▶️ How to Run
1. Open terminal or command prompt  
2. Navigate to project folder  
3. Run:
py task1_hangman.py

---

## 🎮 Sample Output

🟢 Win Case:
========================================
🎮 HANGMAN GAME
========================================
Word: _ _ _ _ _
Enter a letter: a
✅ Correct Guess!

Enter a letter: p
✅ Correct Guess!

🎉 Congratulations! You guessed the word: apple
========================================

🔴 Loss Case:
========================================
🎮 HANGMAN GAME
========================================
Enter a letter: z
❌ Wrong guess! Attempts left: 5

Enter a letter: x
❌ Wrong guess! Attempts left: 4

💀 Game Over! The word was: tiger
========================================

---

## 👨‍💻 Author
Bongoni Sharmisha
