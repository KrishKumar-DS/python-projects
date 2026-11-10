# Number Analysis Tool

A Python-based command-line application that performs mathematical analysis on a user-provided number.

The project focuses on practicing Python fundamentals, particularly conditional statements, loops, functions, mathematical operations, and input validation.

## Features

- **Number Classification:** Identifies whether a number is positive, negative, or zero.
- **Even or Odd:** Determines whether the number is even or odd.
- **Square & Cube:** Calculates the square and cube of the number.
- **Factorial:** Calculates the factorial of a non-negative integer.
- **Prime Number Check:** Determines whether the number is prime.
- **Digit Count:** Counts the total number of digits.
- **Digit Sum:** Calculates the sum of the digits.
- **Input Validation:** Handles invalid numeric inputs.

## Technologies Used

- **Language:** Python 3
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
| Number Classification | Identifies positive, negative, or zero |
| Even or Odd | Determines the parity of the number |
| Square | Calculates the square of the number |
| Cube | Calculates the cube of the number |
| Factorial | Calculates the factorial of a non-negative integer |
| Prime Check | Checks whether the number is prime |
| Digit Count | Counts the number of digits |
| Digit Sum | Calculates the sum of all digits |


## Example Execution

```text
Enter a number: 7

------NUMBER ANALYSIS------

Number: 7
Type: Positive
Parity: Odd
Square: 49
Cube: 343
Factorial: 5040
Prime: Yes
Digit Count: 1
Digit Sum: 7
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

The program should handle:

- Non-numeric inputs.
- Invalid number formats.
- Negative numbers for factorial calculations.
- Non-integer values for operations that require integers.

## Learning Outcomes

Through this project, I practiced how to:

1. Break mathematical problems into smaller functions.
2. Apply conditional logic to solve programming problems.
3. Use loops to perform repetitive calculations.
4. Implement mathematical algorithms such as prime checking and factorial calculation.
5. Validate user inputs and handle exceptions.
6. Organize program logic using reusable functions.

## Future Improvements

- Add support for analyzing multiple numbers.
- Introduce additional mathematical operations.
- Improve output formatting.
- Add automated unit tests.
- Separate mathematical logic from the command-line interface.

---

**Project Status:** V1 in Progress

**Part of:** [Python Projects](https://github.com/KrishKumar-DS/python-projects)
