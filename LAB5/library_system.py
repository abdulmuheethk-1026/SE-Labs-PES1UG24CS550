
"""Manage library loans, renewals, and overdue fines."""

import ast
import json
import operator
from datetime import datetime

# Global state
loans = {}
FINE_CONFIG = {"per_day": 2}


def add_book_loan(student_id, book_id, dates=None):
    """Record a book loan and its loan date."""
    if not student_id:
        return

    if dates is None:
        dates = []

    dates.append(str(datetime.now()))
    loans[student_id] = loans.get(student_id, []) + [book_id]

    print(
        f"{student_id} borrowed {book_id} "
        f"(loan dates on record: {len(dates)})"
    )


def return_book(student_id, book_id):
    """Return a borrowed book."""
    try:
        loans[student_id].remove(book_id)
        if not loans[student_id]:
            del loans[student_id]
    except (KeyError, ValueError):
        pass


def calculate_fine(days_overdue):
    """Calculate the fine for overdue days."""
    return days_overdue * FINE_CONFIG["per_day"]


def renew_book(student_id, book_id, extra_days):
    """Renew a book and adjust the daily fine when required."""
    if extra_days > 14:
        FINE_CONFIG["per_day"] += 1

    print(
        f"Renewed {book_id} for {student_id} "
        f"by {extra_days} days"
    )


def load_records(file="loans.json"):
    """Load loan records from a JSON file."""
    with open(file, "r", encoding="utf-8") as records_file:
        loaded_loans = json.load(records_file)

    if not isinstance(loaded_loans, dict):
        raise ValueError("Loan records must contain a JSON object.")

    loans.clear()
    loans.update(loaded_loans)


def save_records(file="loans.json"):
    """Save loan records to a JSON file."""
    with open(file, "w", encoding="utf-8") as records_file:
        json.dump(loans, records_file, indent=4)


def _evaluate_rule(node, days):
    """Evaluate only approved arithmetic expressions."""
    binary_operations = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
    }

    unary_operations = {
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

    if isinstance(node, ast.Expression):
        return _evaluate_rule(node.body, days)

    if (
        isinstance(node, ast.Constant)
        and isinstance(node.value, (int, float))
        and not isinstance(node.value, bool)
    ):
        return node.value

    if isinstance(node, ast.Name) and node.id == "days":
        return days

    if isinstance(node, ast.BinOp) and type(node.op) in binary_operations:
        left = _evaluate_rule(node.left, days)
        right = _evaluate_rule(node.right, days)

        if isinstance(node.op, ast.Pow) and abs(right) > 10:
            raise ValueError("Exponent is too large.")

        result = binary_operations[type(node.op)](left, right)

        if isinstance(result, (int, float)) and abs(result) > 1e100:
            raise ValueError("Calculated result is too large.")

        return result

    if isinstance(node, ast.UnaryOp) and type(node.op) in unary_operations:
        return unary_operations[type(node.op)](
            _evaluate_rule(node.operand, days)
        )

    raise ValueError("Unsupported expression in fine rule.")


def fine_from_rule(rule, days):
    """Calculate a fine using a restricted arithmetic rule."""
    if len(rule) > 200:
        raise ValueError("Fine rule is too long.")

    expression = ast.parse(rule, mode="eval")
    return _evaluate_rule(expression, days)


def print_report():
    """Print all recorded loans."""
    print("Loan Report")

    for student_id, book_ids in loans.items():
        print(student_id, "->", book_ids)


def main():
    """Run the library system demonstration."""
    add_book_loan("S101", "B-ALGO")
    add_book_loan("S102", "B-NETW")
    add_book_loan("", "B-DBMS")
    add_book_loan("S103", "B-4521")
    return_book("S999", "B-NONE")

    renew_book("S101", "B-ALGO", 21)

    print("Fine for 5 days:", calculate_fine(5))
    print("Fine for -3 days:", calculate_fine(-3))
    print("Fine via rule:", fine_from_rule("days * 2 + 10", 4))

    days = input("Days overdue for S102 (press Enter for 0): ") or "0"
    print("S102 owes:", calculate_fine(int(days)))

    save_records()
    load_records()
    print_report()


if __name__ == "__main__":
    main()
