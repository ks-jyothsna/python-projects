# 📱 Higher Lower Game — Instagram Followers Edition

> A fun Python console game where you guess who has more Instagram followers between two randomly selected famous personalities. Your goal is to keep guessing correctly and build your streak — one wrong guess ends the game!

---
## 🎮 Game Overview
The game is similar to the [Higher Lower Online game](https://www.higherlowergame.com/) to check which subject has highest average monthly searches.

The program displays two random accounts from the provided data and asks you to guess which one has more followers.
You’ll keep playing until your guess is wrong. Your score increases with every correct answer.

---

## 🧩 Features
- 🔀 Randomized Accounts selected from a data list.
- ❓ User Input Prompt to guess between Account A and Account B.
- ✅ Follower Comparison Logic to check correctness.
- 🧮 Score Tracking — increases for each correct guess.
- 🔁 Repeatable Rounds — the previous winner becomes the next challenger.Ends the game when the player guesses correctly or runs out of lives.
- 🏁 Game Over Message when a wrong guess is made.

---

## ⚙️ Game Logic (Steps)

1. Randomly select a number between 1–100.
2. Ask the player to choose a difficulty level (Easy/Hard).
3. Display how many attempts remain.
4. Prompt the player to make a guess.
5. Compare the guessed number with the actual number:
   - If correct → 🎉 “You got it!”
   - If incorrect → Indicate whether the guess is too high or too low.
6. Reduce attempts for each wrong guess.
7. End the game when:
   - The player guesses correctly
   - Or runs out of attempts
  
---

## Additional files/modules used:
- os.sytem('cls') - a nice way to clear the screen for each round.
- random.choice - to select a random account from the data file
- art.py - logo created using [ASCII art](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type+Something+&x=none&v=4&h=4&w=80&we=false)
