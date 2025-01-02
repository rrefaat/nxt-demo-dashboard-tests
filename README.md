# nxt-demo-dashboard-tests
This repository contains automated and manual test scripts for validating the functionality, usability, and security of the NXT Demo Admin Dashboard. The project includes Selenium-based test automation using Python and pytest framework, focusing on login functionality, attendee management, and data validation.

# Get Started

## 1. Install Python
Download and install Python (version 3.8 or later) from [python.org](https://www.python.org/).

### Verify the installation:
```bash
python --version
pip --version
```

---

## 2. Create a Virtual Environment (Optional but Recommended)

### Create a virtual environment:
```bash
python -m venv venv
```

### Activate the virtual environment:
#### Windows:
```bash
.\venv\Scripts\activate
```

#### Mac/Linux:
```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

### Command to Install All Dependencies:
```bash
pip install -r requirements.txt
pip list
```

# Framework Structure

## Project Directory Structure
```
selenium_tests/
  ├── tests/
  │     ├── test_login.py
  │     ├── test_add_attendee.py
  │
  ├── utils/
  │     ├── config.py
  │     ├── base_test.py
  │
  ├── reports/
  ├── screenshots/
  ├── requirements.txt
  └── pytest.ini
```

---

## 5. Initial Setup Steps

1. Clone the repository:
```bash
git clone <repository-url>
```

2. Navigate to the project directory:
```bash
cd selenium_tests
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 6. Run Tests

### Execute tests with pytest:
```bash
pytest --html=reports/report.html
```

### Run tests in parallel:
```bash
pytest -n 4 --html=reports/report.html
```

---

## 7. Generate Reports

- HTML report files will be generated in the `reports/` folder.
- Screenshots will be stored in the `screenshots/` folder for debugging failed tests.



