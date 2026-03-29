# 🏓 Pong Game

A simple implementation of the classic arcade game Pong, built using Python’s **turtle** graphics module. Control paddles, bounce the ball, and try not to miss!

---

## 📌 Features

- Two-player gameplay
- Paddle controls for both players
- Ball movement with collision detection
- Score tracking
- Increasing difficulty (ball speed increases over time)

---

## 🕹️ Controls

| Player       | Key            | Action    |
| ------------ | -------------- | --------- |
| Right Paddle | ↑ (Up Arrow)   | Move Up   |
| Right Paddle | ↓ (Down Arrow) | Move Down |
| Left Paddle  | w              | Move Up   |
| Left Paddle  | s              | Move Down |

---

## 🧠 Problem-Solving Approach / Steps / Game logic

### 1️⃣ Screen Setup
- Background color: Black
- Screen size: 800 x 600

### 2️⃣ Paddle Creation
- Paddle shape: Square
- Paddle size: 20 (width) x 100 (height)
- Right paddle position: (350, 0)
- Left paddle position: (-350, 0)
- Movement step: 20 pixels per key press

### 3️⃣ Ball Movement
- Ball moves continuously across the screen
- Direction changes based on collisions

### 4️⃣ Wall Collision
- The ball bounces when it hits the top or bottom walls
- Collision condition:
   - >= 280 or y <= -280
- Calculation:
  - Screen height = 600 → half = 300
  - Ball size = 20 → adjusted boundary = 280

### 5️⃣ Paddle Collision
- Right Paddle Collision
  - ball.distance(paddle) < 50
  → Checks if the ball is close enough to the paddle
  - ball.xcor() > 320 / < -320 (for right or left paddle)
  → Ensures the ball is on the correct side of the screen
  - ball.bounce_x()
  → Reverses the ball’s horizontal direction

### 6️⃣ Miss Detection
- If the ball passes beyond a paddle:
  - Opponent scores a point
  - Ball resets to center

### 7️⃣ Scoring & Speed Increase
- Score is tracked for both players
- Ball speed increases after each successful paddle hit
- Speed control:
    - Reduce time.sleep() value
    - Multiply by 0.9 to gradually increase speed without going negative
      
---

## 📦 Project Structure

- main.py    
- paddle.py  
- ball.py
- scoreboard.py 
- README.md 
---

## 🧠 Concepts Used

- Object-Oriented Programming (OOP)
- Event handling (keyboard input)
- Collision detection
- Game loops and animation

---

## 🚀 Future Enhancements

- Add sound effects
- Add pause/resume functionality
- Single-player mode with AI
- Better UI and animations
