# 🤖 Reeborg’s World

> This project contains Python solutions for the **Reeborg’s World Hurdles Challenges 1 to 4** and **Maze Challenge** 
Reeborg is a robot that must navigate a path with obstacles (hurdles) to reach a goal.  
Each challenge introduces new logic to handle increasing difficulty.

> The final **Escape the maze** guides Reeborg through a **maze** full of twists and turns to reach the goal flag/exit 🏁.  
Reeborg must **find the correct path automatically** — without pre-programmed directions — by using logic to decide when to move, turn, or change direction.


## 🌍 About Reeborg’s World
**Reeborg’s World** is an online Python-based learning environment designed to teach programming logic through interactive challenges.

🔗 **Website:** [Reeborg’s World](https://reeborg.ca/reeborg.html)


## 🧱 Challenge Descriptions

| Challenge | World Name | Description |
|------------|-------------|-------------|
| **Hurdle 1** | `Hurdles 1` | Fixed number of hurdles; simple repetition. |
| **Hurdle 2** | `Hurdles 2` | Unknown distance to the goal; must adapt to world length. |
| **Hurdle 3** | `Hurdles 3` | The position and number of hurdles changes each time this world is reloaded.|
| **Hurdle 4** | `Hurdles 4` | Randomly placed hurdles with variable heights; must dynamically climb and descend. |
| **Escape the maze** | `Maze` | Guide the randomly placed Reeborg through a complex maze to reach the goal. |


## 💡 Key Idea to solve the **maze challenge**

The **right-hand rule** is a classic maze-solving algorithm.  
It works by imagining that Reeborg keeps **one hand (the right one)** on the wall at all times.  
By following the wall, Reeborg will eventually find the exit, as long as the maze is connected (no isolated walls).


## ⚙️ How to Run the Code

1. Go to [Reeborg’s World](https://reeborg.ca/reeborg.html).
2. Click the **World** dropdown (top-right corner).
3. Choose one of: `Hurdles 1`, `Hurdles 2`, `Hurdles 3`, `Hurdles 4`, or `Maze`
4. Open the **Editor** tab and paste the combined code below.
5. Click **Run** ▶️ to start the program.

