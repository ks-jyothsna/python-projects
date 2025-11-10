# 🐍 Python Modules Reference

This file contains Python modules and libraries I’ve used or learned in my projects, along with a brief description and example usage. It serves as a quick reference and personal cheat sheet.

---

## 📦 1. Standard Libraries

| Module | Description | Example Usage |
|--------|-------------|---------------|
| `os` | Operating system interactions (files, directories) | `os.listdir('.')`, `os.system('cls')`  |
| `sys` | System-specific parameters and functions | `sys.version` |
| `math` | Mathematical functions | `math.sqrt(16)` |
| `datetime` | Date and time manipulation | `datetime.datetime.now()` |
| `random` | Random numbers and selections | `random.randint(1, 10)` |
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

## 📦 6. Others / Utilities

| Module | Description | Example Usage |
|--------|-------------|---------------|
| `tkinter` | GUI applications | `root = Tk()` |
| `openpyxl` | Excel read/write | `openpyxl.load_workbook('file.xlsx')` |
| `pathlib` | File paths | `Path('file.txt').exists()` |
| `re` | Regular expressions | `re.search(pattern, string)` |

---

💡 **Tips for Using This File:**
- Keep updating as you learn new modules in projects.  
- Add short examples to remember usage quickly.  
- This file serves as a **personal cheat sheet** and can be referred to during coding or interviews.

