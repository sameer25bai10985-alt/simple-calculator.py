# Simple Calculator – Problem Statement 

## *1. Problem Statement*

The aim is to develop a *Simple Calculator Program* that allows the user to perform four basic arithmetic operations: addition, subtraction, multiplication, and division. The program displays a menu, takes two numerical inputs from the user, performs the selected operation, and shows the result. Division must handle division-by-zero cases safely.

---

## *2. Requirements*

* Display a menu of four operations: addition, subtraction, multiplication, division.
* Accept the user’s operation choice as an integer (1–4).
* Accept two integer inputs from the user.
* Perform the selected operation.
* Handle division-by-zero errors.
* Display the final result or an appropriate error message.
* Handle invalid operation choices.

---

## *3. Functional Requirements*

### *Input Functions*

* Display menu using print().
* Take input for:

  * Operation choice → operation = int(input())
  * First number → num1 = int(input())
  * Second number → num2 = int(input())

### *Processing Functions*

* If operation == 1: compute num1 + num2 (Addition)
* If operation == 2: compute num1 - num2 (Subtraction)
* If operation == 3: compute num1 * num2 (Multiplication)
* If operation == 4: check:

  * If num2 == 0: show error message.
  * Else compute num1 / num2 (Division)
* If invalid choice → display “Invalid operation!”

### *Output Functions*

* Print the result of the calculation.
* Print an error message if:

  * Operation choice is invalid.
  * Division by zero occurs.

---

## *4. Technical Requirements*

* Programming Language: *Python*
* Use only built‑in functions:

  * print() for displaying menu and results
  * input() for taking user input
  * int() to convert numbers
* Use conditional statements:

  * if, elif, else
* Program must run in any standard Python 3 environment.

---

## *5. Expected Outcome*

A sample run of the program should look like this:


calculator
1.addition
2.subtraction
3.multiplication
4.division
Enter your choice (1-4): 3
enter first number: 7
enter second number: 6
42


If division by zero occurs:


enter first number: 10
enter second number: 0
error


If invalid operation:


Enter your choice (1-4): 9
Invalid operation!


The program should work as a simple, reliable calculator for basic arithmetic operations.
