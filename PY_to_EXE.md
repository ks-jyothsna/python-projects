# 🧩 Convert Python Script to EXE

This guide explains how to convert a **Python (.py)** file into a **standalone Windows executable (.exe)** using the `auto-py-to-exe` tool.  
Once converted, the program can run **without needing Python installed**, making it easier to **share** or **deploy** your projects.  

---

## ⚙️ Step 1: Install the Required Package

Install **auto-py-to-exe** using pip:  
```bash
pip install auto-py-to-exe
```

This package provides a **graphical user interface (GUI)** for PyInstaller, making the conversion process simple and beginner-friendly.  

---

## 🚀 Step 2: Launch the Converter Tool

Run the following command in your terminal or command prompt:  
```bash
python -m auto_py_to_exe
```

This opens the **auto-py-to-exe GUI window**, where you can configure how your Python file should be converted.

---

## 🧭 Step 3: Configure Conversion Options

Inside the GUI:

1. **Select your Python script**  
   - Click **“Browse”** and choose your `.py` file.

2. **Choose the Output Type**  
   - **One File** → Packs everything into a single `.exe` file.  
   - **One Directory** → Creates a folder containing multiple files (recommended for debugging).  

3. **Console Window Option**  
   - **Console Based** → For programs that use input/output in the terminal (e.g., calculators, text-based games).  
   - **Window Based (GUI)** → For programs using Tkinter, PyQt, or other graphical interfaces.  

4. **Optional Settings**  
   - Add an **icon file (`.ico`)** to personalize your application.  
   - Choose an **output folder** for your `.exe` file.  

---

## 🔨 Step 4: Build the EXE

After configuring everything:  
- Click **“Convert .py to .exe”**.  
- Wait for the process to complete (it may take a few minutes).  
- Once finished, your `.exe` file will appear inside the **`output`** folder.  

---

## 🖥️ Step 5: Run, Pin, or Share

- Double-click your `.exe` to run your program — no Python required!  
- Move it to your **Desktop** and **pin it to the taskbar** for quick access.  
- You can **share the `.exe` file** with others — it will run directly on their Windows system.  

---

## 💡 Tips & Notes

- If you encounter issues, ensure all imports and dependencies are installed.  
- For large projects, consider using **“One Directory”** mode first, test it, then switch to **“One File”**.  
- Adding a custom icon (`.ico`) makes your app look more professional.  
- The generated `.exe` file may take a few seconds to open on the first run due to unpacking.  

---

## 📦 Result

After following the steps, you’ll have a **standalone executable application** that works on any Windows computer — no Python installation needed!

---

## Alternate method

You create an executable .exe file directly using PyInstaller from the command line, without opening the auto-py-to-exe graphical interface

You can also build directly from the command line using **PyInstaller**:  
```bash
pyinstaller --onefile your_script.py
```
