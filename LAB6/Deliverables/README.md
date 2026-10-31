# Lab 6 – Code and Branch Coverage Analysis

## Water Utility Billing System

Completed Repo link: - https://github.com/abdulmuheethk-1026/L6_L7_01_water_utility_billing

### 1. Objective

The objective of this lab is to understand, measure, analyse, and improve code coverage and branch coverage using Python's `pytest` and `coverage` libraries.

The lab focuses on identifying untested statements and decision branches by writing comprehensive test cases.

### 2. Project Description

The Water Utility Billing System is a Python application that calculates water bills based on customer type, water usage, and applicable leak-waiver deductions.

It also detects possible meter tampering by analysing backward-flow sensor readings.

### 3. Technologies Used

- Python 3.13
- Pytest
- Coverage.py
- Git and GitHub

### 4. Project Structure

```text
Lab 6/
│
├── README.md
├── water_utility_billing.py
├── test_water_utility.py
│
├── CodeCoverageTest_xxxx_application.py
├── BranchCoverageTest_xxxx_application.py
│
├── code_coverage.png
└── branch_coverage.png
```

### 5. Application Modules

**water_utility_billing.py**

Contains two main functions:

1. `calculate_water_bill(accounts, base_fee)`
   - Validates account information and base fee.
   - Handles active and inactive accounts.
   - Calculates bills using residential and commercial usage tiers.
   - Handles invalid usage blocks.
   - Applies leak-waiver deductions.
   - Determines billing status.

2. `check_meter_tampering(readings_matrix)`
   - Checks meter sensor readings.
   - Identifies consecutive negative readings.
   - Returns the appropriate tampering status.

### 6. Test Cases

**Code Coverage Testing**

File: `CodeCoverageTest_xxxx_application.py`

The test suite covers:
- Invalid account inputs.
- Negative base fee.
- Active and inactive accounts.
- Residential and commercial usage calculations.
- Low, medium, and high usage tiers.
- Leak-waiver conditions.
- Excessive flagged usage.
- No-activity conditions.
- Meter tampering detection.
- Empty and normal meter readings.

**Branch Coverage Testing**

File: `BranchCoverageTest_xxxx_application.py`

The test suite focuses on both True and False outcomes of conditional statements, including:
- Input validation conditions.
- Account activation conditions.
- Usage thresholds.
- Residential and commercial billing decisions.
- Leak-waiver conditions.
- Billing status decisions.
- Meter tampering detection and counter-reset conditions.

### 7. Execution Commands

Install the required dependencies:

```bash
pip install pytest coverage
```

Run code coverage tests:

```bash
python -m coverage erase
python -m coverage run --source=water_utility_billing -m pytest -v CodeCoverageTest_xxxx_application.py
python -m coverage report -m
```

Run branch coverage tests:

```bash
python -m coverage erase
python -m coverage run --branch --source=water_utility_billing -m pytest -v BranchCoverageTest_xxxx_application.py
python -m coverage report -m
```

### 8. Coverage Results

**Code Coverage**

- Total statements: 46
- Missing statements: 0
- Line coverage achieved: 100%

**Branch Coverage**

- Total statements: 46
- Missing statements: 0
- Total branches: 34
- Partially covered branches: 0
- Overall coverage achieved: 100%

### 9. Screenshots

The following screenshots are included as evidence of the coverage analysis:

1. `code_coverage.png` – Terminal output showing 100% code coverage.
2. `branch_coverage.png` – Terminal output showing 100% branch coverage.

### 10. GitHub Commits

The lab work is maintained in a separate Git branch and merged into the personal repository's `main` branch.

Two separate commits are maintained:

1. Add tests for 100 percent code coverage.
2. Add tests for 100 percent branch coverage.

### 11. Conclusion

The lab successfully demonstrates the importance of code coverage and branch coverage in software testing.

Comprehensive test cases were developed to exercise all measured statements and decision branches in the Water Utility Billing application.

The final results achieved:

- **100% Code Coverage**
- **100% Branch Coverage**

This exercise demonstrates how systematic test design improves testing completeness and confidence in software behaviour.
