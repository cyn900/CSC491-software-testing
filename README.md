# Software Testing Exercises (Python + pytest)

![Tests](https://github.com/alicechua/CSC491-software-testing/actions/workflows/tests.yml/badge.svg)

This repository contains **hands-on labs** for practicing different kinds of software testing with Python.
You’ll write and run **unit tests, integration tests, and end-to-end (E2E) tests**, and set up **continuous testing with GitHub Actions**.

**Target environment**

* **Python:** 3.10.18
* **pytest:** 8.4.2

---

## 📂 Repository Structure

```
.
├── exercise1_unit/          # Pure function testing (math_utils.py)
├── exercise2_integration/   # Module integration (text pipeline: tokenize + sentiment)
├── exercise3_e2e_cli/       # End-to-end CLI tests (calculator app)
├── .github/workflows/       # GitHub Actions workflow for automated testing
└── README.md
```

---

## ⚙️ Quick Start

```bash
# 1) Create and activate a virtual env (recommended)
python3.10 -m venv .venv
source .venv/bin/activate        # Windows (PowerShell): .\.venv\Scripts\Activate.ps1

# 2) Install test tools
python -m pip install -U pip pytest

# 3) Run all tests
pytest -q
```

**Useful flags**

* `-v` (verbose), `-vv` (extra verbose; shows parameter sets)
* `-k "pattern"` to run tests by name pattern
* `-q` quiet mode, `-s` show print/log output
* `--maxfail=1 -x` stop at first failure

Examples:

```bash
pytest -vv
pytest -k "pipeline and pos"
pytest --maxfail=1 -x
```

---

## 🧪 Exercises

### 1) Unit Testing (tiny pure functions)

* Implement and test `add`, `div`, `clamp` in `exercise1_unit/math_utils.py`.
* Focus on:

  * Happy paths, edge cases, and error handling
  * Parameterized tests
  * Rejecting invalid inputs like `NaN`, `∞`, or non-numeric types

**Run:**

```bash
pytest exercise1_unit
```

👉 **Learning goal:** build fast, isolated, deterministic tests.

---

### 2) Integration Testing (compose tiny modules)

* Combine:

  * `tokenizer.py` → splits text into words
  * `sentiment.py` → computes sentiment score
  * `text_pipeline.py` → integrates both via `analyze(text)`
* Test the pipeline via `analyze(text)` **without mocks**.
* Cover mixed positive/negative words, punctuation, numbers, empty strings, emojis.

**Run:**

```bash
pytest exercise2_integration
```

👉 **Learning goal:** verify modules **work together** and contracts between them hold.

---

### 3) End-to-End (E2E) Testing (CLI)

* Test a CLI calculator (`exercise3_e2e_cli/calculator.py`) by running it as a subprocess.
* Feed input commands (e.g., `add 5 10`) and assert exact output.
* Cover valid commands, errors (`div by 0`, bad input), and boundary behavior.

**Run:**

```bash
pytest -vv exercise3_e2e_cli
```

👉 **Learning goal:** simulate **real user interactions** and validate the whole system.

---

### 4) End-to-End UI Testing (Streamlit + Cypress)

* This exercise replaces the CLI E2E with a real UI: a tiny Streamlit app tested in a real browser via Cypress.
* More details refer to the README.md in exercise4_e2e_streamlit

👉 **Learning goal:** simulate **user interface interactions** and validate the whole system.

## 📈 Code Coverage

### 1) Install

```bash
pip install pytest-cov
```

### 2) Run with coverage (local)

Common commands:

```bash
# Generate HTML and XML reports
pytest --cov=. --cov-report=html --cov-report=xml:coverage.xml
```

Open the HTML report in your browser:

* **macOS**

  ```bash
  open htmlcov/index.html
  ```
* **Windows (PowerShell / CMD)**

  ```bash
  start htmlcov\index.html
  ```
* **Linux**

  ```bash
  xdg-open htmlcov/index.html
  ```

---

## 🧱 Typical Layout (by exercise)

```
exercise1_unit/
  math_utils.py
  test_math_utils.py

exercise2_integration/
  tokenizer.py
  sentiment.py
  text_pipeline.py
  test_text_pipeline.py

exercise3_e2e_cli/
  calculator.py
  test_e2e_cli.py

exercise4_e2e_streamlit/
```

---

## 🎯 Learning Outcomes

By completing these exercises, you will:

* Understand the **test pyramid**: unit → integration → E2E
* Write clear, maintainable, and reliable tests
* See how testing fits into **real-world industry workflows**
* Gain confidence using **pytest** and **GitHub Actions** for automation

---
