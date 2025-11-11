# 🎯 Guess The Number

> A simple Python console game where the player tries to guess a randomly selected number between 1 and 100.
The game provides hints and limits the number of attempts based on the chosen difficulty level.

---

## 🧩 Features
- Randomly selects a number between 1 and 100.
- Lets the player choose between Easy and Hard difficulty levels.
- Displays remaining attempts after each guess.
- Provides hints — whether the guessed number is too high or too low.
- Ends the game when the player guesses correctly or runs out of lives.

---

⚙️ Game Logic (Steps)

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
- random.randint - to generate a random number between 1 - 100
- art.py - logo created using [ASCII art](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type+Something+&x=none&v=4&h=4&w=80&we=false)

---

💡 Future Enhancements

- Add a replay option after each game.
- Implement a score tracker for multiple rounds.
- Include color-coded text for better readability in the console.
- Convert to a gaming application.
