# 🐍 Snake Game

A basic Snake Game built using **Python**, designed to understand game loops, collision detection, and object movement.  
This project is beginner-friendly and helps in learning fundamental game development concepts.

---

## 📌 Features

- Classic snake movement (Up, Down, Left, Right)
- Food collision detection
- Score tracking
- Wall and self-collision detection
- Game over condition

---

## 🎮 Game Rules

- The snake moves continuously once the game starts.
- The snake cannot move backward directly.
- Eating food increases the snake’s length and score.
- The game ends if the snake hits the wall or its own body.

---

## 🧠 Problem-Solving Approach / Steps

### 1️⃣ Create the Snake Body
- Initialize the snake with **3 square segments**
- Each segment size: **20 x 20** (Default value in turtle class)

### 2️⃣ Move the Snake
- Snake moves forward automatically
- Uses a continuous game loop with a delay
- Set tracer to 0, turns turtle animation off and set delay for update drawings
- Added 0.1 sec delay after all segments move and refresh the screen

### 3️⃣ Control the Snake
- Keyboard controls:
  - ⬆️ Up
  - ⬇️ Down
  - ⬅️ Left
  - ➡️ Right
- Prevent backward movement (e.g., Left → Right not allowed)

### 4️⃣ Detect Collision with Food
- Food is a **blue circle** of size **10 x 10**
- When the distance between the snake head and food is **less than 15 pixels**:
  - Food moves to a **random location** on the screen
  - Snake grows in length
  - Score increases

### 5️⃣ Create a Scoreboard
- Display score at the top of the screen
- Uses the `write()` method to update score dynamically

### 6️⃣ Detect Collision with Wall
- Screen size: **600 x 600**
- Boundary considered: **560 x 560**
- If snake crosses boundary on all sides → Game Over

### 7️⃣ Detect Collision with Tail
- Each time food is eaten, a new segment is added
- If the snake head collides with its own body:
  - Game ends

## 🚀 Future Enhancements

- Add levels or increasing speed
- Add sound effects
- Restart button after Game Over
- High score tracking
