# 🐍 Python libraries and modules

This file contains Python modules and libraries I’ve used or learned in my projects, along with a brief description and example usage. It serves as a quick reference and personal cheat sheet.

---

## 📦 1. Standard Libraries
> Python Standard Library is a collection of modules that come pre-installed with Python, offering a wide range of functionalities without needing to install additional packages. 

| Module | Description | Example Usage |
|--------|-------------|---------------|
| `random` | Random numbers and selections | `random.randint(1, 10)` |
| `os` | Operating system interactions (files, directories) | `os.listdir('.')`, `os.system('cls')`  |
| `math` | Mathematical functions | `math.sqrt(16)` |
| `sys` | System-specific parameters and functions | `sys.version` |
| `datetime` | Date and time manipulation | `datetime.datetime.now()` |
| `time` | Time-related functions | `time.sleep(2)` |
| `argparse` | Command-line argument parsing | `parser = argparse.ArgumentParser()` |
| `logging` | Logging messages | `logging.info('message')` |

---

## 📦 2. Data Handling & Analysis

| Module | Description | Example Usage |
|--------|-------------|---------------|
| `pandas` | Dataframes for structured data | `pd.read_csv('file.csv')` |
| `numpy` | Numerical operations, arrays | `np.array([1,2,3])` |
| `csv` | Read/write CSV files | `csv.reader(file)` |
| `json` | JSON parsing | `json.loads(data)` |
| `prettytable` | Print tables | `` |

---

## 📦 3. Web & API

| Module | Description | Example Usage |
|--------|-------------|---------------|
| `requests` | HTTP requests for APIs | `requests.get(url)` |
| `BeautifulSoup` | Web scraping | `soup = BeautifulSoup(html, 'html.parser')` |
| `selenium` | Browser automation | `driver = webdriver.Chrome()` |

---

## 📦 4. Automation & Testing

| Module | Description | Example Usage |
|--------|-------------|---------------|
| `pytest` | Python testing framework | `pytest test_file.py` |
| `unittest` | Unit testing | `unittest.TestCase` |
| `selenium` | Web automation | `driver.get('https://example.com')` |

---

## 📦 5. Data Visualization

| Module | Description | Example Usage |
|--------|-------------|---------------|
| `matplotlib` | 2D plotting | `plt.plot(x, y)` |
| `seaborn` | Statistical visualizations | `sns.barplot(x, y)` |
| `plotly` | Interactive plots | `px.scatter(df, x='a', y='b')` |

---

## 📦 6. Other libraries

| Module | Description | Accessibility |
|--------|-------------|---------------|
| `tkinter` | GUI applications | standard library |
| `turtle` | creating graphics, used for educational purpose | standard library |
| `openpyxl` | Excel read/write | third-party library |
| `pathlib` | File paths | standard library |
| `re` | Regular expressions | standard library |

---

💡 **Tips for Using This File:**
- Keep updating as you learn new modules in projects.  
- Add short examples to remember usage quickly.  
- This file serves as a **personal cheat sheet** and can be referred to during coding or interviews.

