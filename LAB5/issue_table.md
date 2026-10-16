# Lab 5: Static Code Analysis — Issue Table

**Repository:** `L5_01_library_fines`  
**Source file:** `library_system.py`  
**Tools used:** Pylint, Bandit, Flake8

## Issues identified and fixes applied

| No. | Tool | Issue identified | Description / risk | Fix applied | Verification |
|---:|---|---|---|---|---|
| 1 | Pylint | Mutable default argument | Using `dates=[]` as a default can cause the same list to be shared across function calls. | Changed the default to `None` and initialized a new list inside the function. | Pylint score improved. |
| 2 | Pylint | Missing docstrings | Functions and the module lacked documentation, reducing readability and maintainability. | Added module and function docstrings. | Final Pylint score: 10.00/10. |
| 3 | Pylint / Flake8 | Bare `except` | Catching every exception can hide unexpected errors and make debugging difficult. | Replaced it with `except (KeyError, ValueError)`. | Flake8 reports no issues; Bandit reports no findings. |
| 4 | Bandit / Pylint | Use of `eval()` | Evaluating a supplied string as Python code can allow unintended code execution. | Replaced `eval()` with an AST-based evaluator that permits only selected arithmetic operators and the `days` variable. | Bandit reports no issues. |
| 5 | Pylint | Global statement | Modifying a module-level variable through `global` makes state changes harder to track. | Replaced the daily fine integer with a mutable configuration dictionary; updated loaded loan records in the existing dictionary. | Final Pylint score: 10.00/10. |
| 6 | Pylint | Non-standard function naming | The original function name `renewBook` did not follow the usual Python naming convention. | Renamed it to `renew_book` and updated its call. | Final Pylint score: 10.00/10. |
| 7 | Pylint | File handling | Files were opened without explicit encoding or context managers. | Used `with open(..., encoding="utf-8")` and JSON load/dump functions. | Final Pylint score: 10.00/10. |
| 8 | Pylint | Unused import | An unnecessary `os` import was present. | Removed the unused import. | No unused-import warning in the final run. |
| 9 | Pylint | Dictionary iteration | The report function iterated over dictionary keys and accessed values separately. | Changed iteration to `loans.items()`. | Final Pylint score: 10.00/10. |
| 10 | Flake8 | Blank-line and formatting violations | Several functions had insufficient blank lines between definitions, and the file contained other style violations. | Corrected blank-line spacing and formatting to satisfy Flake8. | Flake8 produces no output. |
| 11 | Pylint / Flake8 | String formatting and long lines | Older string formatting and long lines reduced consistency and readability. | Used f-strings and split longer output statements across lines. | Final Pylint and Flake8 checks pass. |

## Final verification results

| Tool | Final result | Status |
|---|---|---|
| Pylint | 10.00/10 | Passed |
| Flake8 | No reported issues | Passed |
| Bandit | No issues identified | Passed |
| Python compilation | No syntax errors | Passed |

**Conclusion:** Static analysis helped identify code-quality, security, and formatting issues. Applying the fixes improved readability and maintainability, removed unsafe dynamic evaluation, and satisfied the lab's stated Pylint, Bandit, and Flake8 requirements.