# CLI Calculator

A command-line calculator built with Python that performs basic mathematical operations through an interactive terminal interface.

This project focuses on practicing Python fundamentals, including functions, dictionaries, function references, loops, exception handling, and input validation.

## Features

- **Addition:** Adds two numbers.
- **Subtraction:** Subtracts the second number from the first.
- **Multiplication:** Multiplies two numbers.
- **Division:** Divides the first number by the second, with division-by-zero protection.
- **Exponentiation:** Calculates the power of a number.
- **Input Validation:** Handles invalid numeric inputs and invalid menu selections.
- **Continuous Calculations:** Allows users to perform multiple calculations without restarting the program.
- **Interactive Interface:** Provides a simple menu-driven command-line experience.

## Technologies Used

- **Language:** Python
- **Libraries:** Python Standard Library
- **Interface:** Command-Line Interface (CLI)

## Project Structure

```text
01_cli_calculator/
├── calculator.py
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- A terminal or command-line application.

### Installation and Execution

1. Clone the repository:

   ```bash
   git clone https://github.com/KrishKumar-DS/python-projects.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python-projects/01_basic_programming/01_cli_calculator
   ```

3. Run the calculator:

   ```bash
   python calculator.py
   ```

   On some Linux systems, you may need to use:

   ```bash
   python3 calculator.py
   ```

## Available Operations

| Option | Operation | Description |
|:---:|---|---|
| 1 | Addition | Adds two numbers |
| 2 | Subtraction | Subtracts two numbers |
| 3 | Division | Divides two numbers |
| 4 | Multiplication | Multiplies two numbers |
| 5 | Power | Raises the first number to the power of the second |

## Example Execution

```text
Do you want to use Calculator (y/n): y

------OPERATIONS------
1. Addition
2. Subtraction
3. Division
4. Multiplication
5. Power (Exponentiation)

Which operation you want to perform: 1

Enter the first number: 25
Enter the second number: 15

40.0

Do you want to perform another calculation? (y/n): n

Exiting......
Thank you....
```

## Python Concepts Practiced

Through this project, I practiced the following Python concepts:

- **Functions:** Defining functions, passing control between functions, and returning values.
- **Dictionaries:** Using dictionaries to map user selections to corresponding functions.
- **Function References:** Storing function references in variables and dictionaries without immediately executing them.
- **Function Invocation:** Dynamically executing functions through stored references.
- **Loops:** Using `while` loops to manage repeated execution.
- **Nested Loops:** Implementing separate loops for calculation control and input validation.
- **Conditional Statements:** Using `if`, `elif`, and `else` to manage program decisions.
- **Exception Handling:** Using `try` and `except` to handle invalid numeric inputs.
- **Input Validation:** Validating user inputs and handling invalid menu selections.
- **Program Structure:** Dividing application responsibilities into separate functions.

## Error Handling

The calculator includes basic error handling for:

- Non-numeric inputs.
- Empty operation selections.
- Invalid operation selections.
- Division by zero.
- Invalid responses when continuing or exiting the calculator.

## Learning Outcomes

This project helped me understand how to:

1. Break a program into smaller, reusable functions.
2. Use dictionaries as a function-dispatch mechanism.
3. Understand the difference between function references and function calls.
4. Manage application execution using loops and conditional statements.
5. Handle invalid inputs using exception handling.
6. Organize a Python project into a maintainable directory structure.

## Future Improvements

Potential improvements for future versions:

- Add automated unit tests.
- Improve numerical input validation, including handling `NaN` and infinity.
- Add additional mathematical operations.
- Improve result formatting and user interface.
- Separate calculation logic from the command-line interface.

---

**Project Status**: V1 Completed

**Part of:** [Python Projects](https://github.com/KrishKumar-DS/python-projects)
