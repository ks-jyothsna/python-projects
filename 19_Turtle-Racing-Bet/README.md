#  🖍 Etch-a-sketch + 🐢🏁🏆 Turtle Racing Bet Game
> A fun Python project combining two interactive Turtle-based mini-applications:
🎨 Etch-A-Sketch Drawing Tool and 🏁 Turtle Racing Bet Game.  

> Both projects use Python’s built-in turtle module and are perfect for learning movement control, event listeners, loops, and user interaction.

---

## 🐢 What Is the Turtle Module?  
The **turtle** module is a simple graphics library in Python that lets you control a virtual “turtle” that moves across the screen while drawing.  
It’s commonly used for:

- Drawing shapes and patterns  
- Teaching programming visually  
- Making small games  
- Exploring event-based inputs and animations  

---

# 🎨 Etch-A-Sketch   
The **Etch-A-Sketch** is a digital version of the classic drawing toy.  
Use keyboard keys to move the turtle and draw freely on the screen.

### **Features**
- Move the turtle in four directions  
- Draw lines as you move  
- Clear the screen instantly  
- Simple keyboard controls  
- Great for practicing event listeners (`onkey`)  

### **Suggested Controls**
- `w` — Move Forward
- `s` — Move Backward  
- `a` — Move Counter-Clockwise  
- `d` — Move Clockwise  
- `c` — Clear Screen  

### **Concepts Used**
- Turtle movement  
- Key event listeners  
- Screen updates  
- Clearing and resetting graphics  

---

# 🏁 Turtle Racing Bet Game 🐢🏆  

A fun racing mini-game where the user **bets on which turtle will win**, and then watches the race unfold.

### **How It Works**
1. Player chooses a color to bet on  
2. Several turtles start lined up at the left side  
3. Each turtle moves forward in small random steps  
4. First turtle to reach the finish line wins  
5. User gets a win/lose message  

### **Features**
- Multiple colorful turtles  
- Randomized movement  
- Race animation  
- Input-based betting  
- Real-time result announcement  

### **Concepts Used**
- Screen is setup "screen.setup": width = 500, height = 400
- Taking user input on which turtle will win using "screen.textinput"
- Created multiple turtle objects from the class using "for" loop on the list of colors.
- Each object is independent of others and in different state
- Loops + randomness from random module  
- Movement updates  
- Detecting finish line : turtle is 40X40 in dimension; and x-axis is 250 from the center , the end mark of the screen is calculated as 250 - (40/2) = 230
