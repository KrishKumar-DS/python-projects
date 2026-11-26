# Number Analysis Tool

A Python-based command-line application that performs mathematical analysis on a user-provided number.

The project focuses on practicing Python fundamentals, particularly conditional statements, loops, functions, mathematical operations, and input validation.

## Features

- **Number Classification:** Identifies whether a number is positive, negative, or zero (`Positive`, `Negative`, or `It's Zero`).
- **Even or Odd:** Determines the parity of an integer; non-integers return an explanatory message.
- **Square & Cube:** Calculates the square and cube of the number.
- **Factorial:** Calculates the factorial of a non-negative integer up to 1000; larger inputs are rejected.
- **Prime Number Check:** Determines whether an integer is prime and reports `Yes` or `No`.
- **Digit Count:** Counts the digits as written, ignoring the sign and decimal point (fractional digits are included).
- **Digit Sum:** Sums the digits as written, ignoring the sign and decimal point.
- **Input Validation:** Re-prompts until a valid number or `y`/`n` choice is entered.

## Technologies Used

- **Language:** Python 3.12+
- **Libraries:** Python Standard Library
- **Interface:** Command-Line Interface (CLI)

## Project Structure

```text
02_number_analysis/
├── number_analysis.py
└── README.md
```

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/KrishKumar-DS/python-projects.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python-projects/01_basic_programming/02_number_analysis
   ```

3. Run the program:

   ```bash
   python3 number_analysis.py
   ```

## Available Operations

| Operation | Description |
|---|---|
| Number Classification | Identifies positive, negative, or zero (`It's Zero` for 0) |
| Even or Odd | Parity of an integer; non-integers get a message |
| Square | Calculates the square of the number |
| Cube | Calculates the cube of the number |
| Factorial | Factorial of a non-negative integer up to 1000 |
| Prime Check | Reports `Yes`/`No`; integers only |
| Digit Count | Digits as written, ignoring sign and decimal point |
| Digit Sum | Sum of digits as written, ignoring sign and decimal point |


## Example Execution

```text
==============================
       NUMBER ANALYZER
==============================
Want to use Number Analyzer: y

Enter the number: 7
Type: Positive
Parity: Odd
Square: 49
Cube: 343
Prime: Yes
Factorial: 5040
Digit Count: 1
Digit Sum: 7
==============================
Want to use Number Analyzer: n
Exiting......
==============================
```

## Python Concepts Practiced

- **Functions:** Defining reusable functions for individual mathematical operations.
- **Conditional Statements:** Using `if`, `elif`, and `else` to implement logical decisions.
- **Loops:** Using `for` and `while` loops for repetitive operations and calculations.
- **Mathematical Operators:** Performing arithmetic and mathematical calculations.
- **Type Conversion:** Converting user input into appropriate numeric data types.
- **Exception Handling:** Using `try` and `except` to handle invalid inputs.
- **Input Validation:** Validating user input before performing calculations.
- **Problem Solving:** Breaking mathematical problems into smaller, manageable operations.
- **Program Structure:** Organizing program logic into separate functions.

## Error Handling

The program handles:

- Non-numeric input such as `abc` or an empty line: prints `Invalid Input! Enter numerical value` and re-prompts.
- Invalid menu choice: prints `Invalid Input! Enter y/n...` and re-prompts.
- Negative numbers for factorial return `Negative number can't have factorial`.
- Non-integer values for parity, prime, or factorial return an explanatory message instead of a result.
- Factorial inputs above 1000 return `Too Large for Factorial, MAX: 1000`.
- `float()` also accepts `nan`, `inf`, and scientific notation such as `1e3`; these are currently not validated and can produce misleading output (known limitation).

## Learning Outcomes

Through this project, I practiced how to:

1. Break mathematical problems into smaller functions.
2. Apply conditional logic to solve programming problems.
3. Use loops to perform repetitive calculations.
4. Implement mathematical algorithms such as prime checking and factorial calculation.
5. Validate user inputs and handle exceptions.
6. Organize program logic using reusable functions.

## Future Improvements

- Support batch analysis (comma-separated or file input) instead of one number at a time.
- Validate and reject special float values (`nan`, `inf`, scientific notation).
- Add automated unit tests for each operation.
- Separate the mathematical logic from the command-line interface.
- Standardise output labels and formatting.

---

**Project Status:** V1 in Progress

**Part of:** [Python Projects](https://github.com/KrishKumar-DS/python-projects)
