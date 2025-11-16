# 🐍 Python libraries and modules

This file contains Python modules and libraries I’ve used or learned in my projects, along with a brief description and example usage. It serves as a quick reference and personal cheat sheet.

---

## 📦 1. Standard Libraries
> Python Standard Library is a collection of modules that come pre-installed with Python, offering a wide range of functionalities without needing to install additional packages. 

| Module | Description | Example Usage |
|--------|-------------|---------------|
| `random` | Random numbers and selections | `random.randint(1, 10)` |
| `os` | Operating system interactions (files, directories) | `os.listdir('.')`, `os.system('cls')`  |
| `sys` | System-specific parameters and functions | `sys.version` |
| `math` | Mathematical functions | `math.sqrt(16)` |
| `sys` | System-specific parameters and functions | `sys.version` |
| `datetime` | Date and time manipulation | `datetime.datetime.now()` |
| `random` | Random numbers and selections | `random.randint(1, 10)` |
| `time` | Time-related functions | `time.sleep(2)` |
| `argparse` | Command-line argument parsing | `parser = argparse.ArgumentParser()` |
| `logging` | Logging messages | `logging.info('message')` |

---

## 📦 2. Data Handling & Analysis

| Module | Description | Example Usage | Accessibility |
|--------|-------------|---------------|---------------|
| `pandas` | Dataframes for structured data | `pd.read_csv('file.csv')` | third-party library |
| `numpy` | Numerical operations, arrays | `np.array([1,2,3])` | third-party library |
| `csv` | Read/write CSV files | `csv.reader(file)` | standard library |
| `json` | JSON parsing | `json.loads(data)` | standard library |
| `prettytable` | Print tables |  | third-party library |

--- 

## 📦 3. Web & API

| Module | Description | Example Usage | Accessibility |
|--------|-------------|---------------|---------------|
| `requests` | HTTP requests for APIs | `requests.get(url)` | third-party library |
| `BeautifulSoup` | Web scraping | `soup = BeautifulSoup(html, 'html.parser')` | third-party library |
| `selenium` | Browser automation | `driver = webdriver.Chrome()` | third-party library |

---

## 📦 4. Automation & Testing

| Module | Description | Example Usage | Accessibility |
|--------|-------------|---------------|---------------|
| `pytest` | Python testing framework | `pytest test_file.py` | third-party library |
| `unittest` | Unit testing | `unittest.TestCase` | standard library |
| `selenium` | Web automation | `driver.get('https://example.com')` | third-party library |

---

## 📦 5. Data Visualization

| Module | Description | Example Usage | Accessibility |
|--------|-------------|---------------|---------------|
| `matplotlib` | 2D plotting | `plt.plot(x, y)` | third-party library |
| `seaborn` | Statistical visualizations | `sns.barplot(x, y)` | third-party library |
| `plotly` | Interactive plots | `px.scatter(df, x='a', y='b')` | third-party library |

---

## 📦 6. Other libraries

| Module | Description | Example Usage | Accessibility |
|--------|-------------|---------------|---------------|
| `tkinter` | GUI applications | `root = Tk()` | standard library |
| `turtle` | Creating graphics, used for educational purpose | `timmy = Turtle()` | standard library |
| `openpyxl` | Excel read/write | `openpyxl.load_workbook('file.xlsx')` | third-party library |
| `pathlib` | File paths | `Path('file.txt').exists()` | standard library |
| `re` | Regular expressions | `re.search(pattern, string)` | standard library |

---

💡 **Tips for Using This File:**
- Keep updating as you learn new modules in projects.  
- Add short examples to remember usage quickly.  
- This file serves as a **personal cheat sheet** and can be referred to during coding or interviews.
