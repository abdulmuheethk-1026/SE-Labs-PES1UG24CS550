https://github.com/abdulmuheethk-1026/L5_01_library_fines
# Lab 5 – Static Code Analysis

## Objective

To analyze and improve the code quality, security, readability, and maintainability of a Python program using static code analysis tools.

## Project Description

This lab uses a simple Library Management System implemented in Python. The program supports book loan registration, book returns, renewals, fine calculation, and loading and saving loan records.

Static analysis tools were used to identify potential programming errors, security vulnerabilities, and coding-style violations. The identified issues were addressed to improve the overall quality of the source code.

## Tools Used

- **Pylint:** Evaluates Python code quality, detects potential errors, and checks coding conventions and maintainability.
- **Bandit:** Identifies potential security issues in Python code.
- **Flake8:** Checks Python code for style violations and formatting issues.

## Issues Identified and Fixes

The following issues were identified and addressed during the analysis:

1. Added module and function docstrings.
2. Replaced mutable default arguments with `None` and initialized lists inside functions.
3. Replaced unsafe `eval()` usage with a restricted arithmetic-expression evaluator.
4. Replaced bare exception handling with specific exception types.
5. Used context managers for file operations and specified UTF-8 encoding.
6. Removed unused imports.
7. Improved function naming and code readability.
8. Replaced older string-formatting approaches with f-strings.
9. Corrected blank-line and line-length violations.
10. Added checks to restrict supported arithmetic expressions and limit excessively large calculations.

## Analysis Results

| Tool | Before Analysis | After Analysis |
|---|---|---|
| Pylint | 6.07/10 | 10.00/10 |
| Bandit | Security findings detected | No issues identified |
| Flake8 | Style violations detected | No violations reported |

*The results above should match the saved before-and-after reports included in this folder.*

## Files Included

| File | Description |
|---|---|
| `library_system.py` | Corrected Python source code |
| `pylint_report_before.txt` | Pylint results before modifications |
| `pylint_report_after.txt` | Pylint results after modifications |
| `bandit_report_before.txt` | Bandit security analysis before modifications |
| `bandit_report_after.txt` | Bandit security analysis after modifications |
| `flake8_report_before.txt` | Flake8 results before modifications |
| `flake8_report_after.txt` | Flake8 results after modifications |

## Verification

The final source code was checked using the following commands:

```bash
python -m py_compile library_system.py
pylint library_system.py
bandit -r library_system.py
flake8 library_system.py
```

The final verification produced a Pylint score of 10.00/10, no Bandit findings, and no Flake8 violations.

## Conclusion

This lab demonstrates how static code analysis tools can be used to improve Python code quality, identify potential security vulnerabilities, and enforce consistent coding standards. Applying the recommended fixes resulted in improved readability and maintainability, while the final analysis reports confirmed that the corrected source code met the intended checks.
