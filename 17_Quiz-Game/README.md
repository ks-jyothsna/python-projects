# ✔️✖️ Quiz Game - True or False

> This project is a beginner-friendly yet well-structured True/False Quiz Game that runs entirely in the console.
> The game demonstrates how Object-Oriented Programming (OOP) concepts can be applied to build a clean, modular, and easy-to-extend application.
> This project demonstrates how to structure a small application using classes, methods, and clean code practices.

---

## 🎮 Game Overview

This game presents a series of True or False questions to the player through the console.
For each question, the player must type "True" or "False".

After every answer, the game:
- Checks if the player's response is correct
- Displays the correct answer
- Updates and displays the current score
- When all questions are completed, the final score is shown.

---

## 🧩 Features

- Fully object-oriented design
- Access to change the questions
- Quiz logic separated into multiple classes
- Real-time feedback after each question
- Score tracking
- Easy to extend with additional questions

---

## 📂 Project Structure

project
- main.py
- question_model.py
- quiz_brain.py
- data.py

question_model.py
> Contains the Question class which stores:
- The question text
- The correct answer

quiz_brain.py
> Contains the QuizBrain class which
- Tracks the current question number
- Asks questions on the console
- Checks user answers
- Tracks the score

data.py
- Contains the list of question dictionaries

main.py
- Imports all classes
- Creates Question objects
- Runs the quiz loop

---

## How to change the questions list
This game can use custom questions, locally stored questions. The quiz questions can be loaded manually from the Open Trivia Database (OpenTDB).
- OpenTrivia DB provides free, high-quality trivia questions. You can use its API to fetch True/False questions dynamically.
- Steps to create data file using Trivia Database
    - Open [Open Tivia DataBase](https://opentdb.com/)
    - Click on API
    - Choose the Number of Questions, Category, Difficulty, Tye(True/False)
    - Click Generate API url
    - Copy the URL thats generated and paste it in the new window
    - A dictionary will be shown, optional, click on the Pretty-print for formatting text to make it more readable and aesthetically pleasing.
    - Copy the text to the new data file and remove  ("response_code": 0, "results":) and use the Code -> Reformat code to format it like the data.py file in the project.
    - At the end it should look like a list of dictionaries.
   
---

## 📦 Future Enhancements (Optional)
- Add difficulty levels
- Load questions from an API
- Add a GUI version
- Timer-based questions
