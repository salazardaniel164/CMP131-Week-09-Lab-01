# CMP 131 – Python Programming


> **Required file location:** Keep every Python file directly in the repository root. Do not create a `src` folder.

## Week 8 – Lab 1: Functions and Return Values

**Total Points: 100**

* Program 1: Kinetic Energy — 30 points
* Program 2: Celsius Temperature Table — 30 points
* Program 3: Future Value — 40 points

## Learning Objectives

After completing this lab, students should be able to:

* Define and call Python functions.
* Pass values to functions as arguments.
* Use parameters to receive information inside a function.
* Perform calculations inside functions.
* Return calculated values to the calling statement.
* Store and display values returned by functions.
* Use a loop to call a function repeatedly.
* Convert user input to the appropriate numeric data type.
* Format numeric and monetary output.
* Organize a program using a `main()` function.
* Test functions using different input values.
* Use comments to explain major program sections.

## Assignment Overview

Create three separate Python programs that demonstrate the use of functions, parameters, arguments, and return values.

The programs will:

1. Calculate an object’s kinetic energy.
2. Display a Fahrenheit-to-Celsius temperature table.
3. Calculate the future value of a savings account.

Create the following Python files:

* `kinetic_energy.py`
* `celsius_temperature_table.py`
* `future_value.py`

Each program must include at least one function that performs the required calculation and returns the result.

The instructor is not providing completed Python code or an exact output design. Students must design, write, and test their own programs.

# Program 1: Kinetic Energy

**Points: 30**

## Program Description

An object that is moving has kinetic energy. The following formula calculates an object’s kinetic energy:

**KE = ½ × m × v²**

In this formula:

* `KE` represents kinetic energy.
* `m` represents the object’s mass in kilograms.
* `v` represents the object’s velocity in meters per second.

Create a program that asks the user to enter an object’s mass and velocity. Pass those values to a function that calculates and returns the object’s kinetic energy.

## Required Python File

Create a Python file named:

`kinetic_energy.py`

Include a comment header containing:

* Student name
* Course number
* Week number
* Lab number
* Assignment title
* Date

## Part 1: Create the `kineticEnergy` Function

Create a function named:

`kineticEnergy`

The function must:

* Accept the object’s mass as a parameter.
* Accept the object’s velocity as a second parameter.
* Calculate the kinetic energy.
* Return the calculated kinetic energy.

The function should perform the calculation only. It should not ask the user for input.

## Part 2: Create the Main Program

Create a `main()` function that controls the program.

The `main()` function must:

* Display a descriptive program title.
* Ask the user for the object’s mass in kilograms.
* Ask the user for the object’s velocity in meters per second.
* Convert both entries to an appropriate numeric data type.
* Call the `kineticEnergy` function.
* Pass the mass and velocity to the function as arguments.
* Store the value returned by the function.
* Display the calculated kinetic energy.

Call the `main()` function to begin the program.

## Part 3: Input Requirements

The program must accept whole-number and decimal values.

Use meaningful variable names for:

* Mass
* Velocity
* Kinetic energy

Mass and velocity must not be negative. If either value is negative, display an appropriate error message instead of calculating kinetic energy.

Zero is acceptable because an object with zero mass or zero velocity has zero kinetic energy.

## Part 4: Display the Result

Display a clearly formatted summary containing:

* The object’s mass in kilograms
* The object’s velocity in meters per second
* The calculated kinetic energy in joules

Display the kinetic energy with two digits after the decimal point.

## Required Testing for Program 1

|   Mass | Velocity | Expected Kinetic Energy |
| -----: | -------: | ----------------------: |
|  10 kg |    5 m/s |           125.00 joules |
| 2.5 kg |    4 m/s |            20.00 joules |
|  20 kg |    0 m/s |             0.00 joules |
|   0 kg |   10 m/s |             0.00 joules |

Also test a negative value and confirm that the program displays an appropriate error message.

## Program 1 Point Distribution

* Program title and clear input prompts: 3 points
* Correct `main()` function organization organization: 4 points
* Correctly define `kineticEnergy`: 5 points
* Correct parameters and function call: 5 points
* Correct kinetic-energy calculation: 5 points
* Correct return value: 4 points
* Clear output, comments, validation, and testing: 4 points

**Program 1 Total: 30 points**

# Program 2: Celsius Temperature Table

**Points: 30**

## Program Description

The following formula converts a Fahrenheit temperature to Celsius:

**C = 5/9 × (F − 32)**

In this formula:

* `F` represents the Fahrenheit temperature.
* `C` represents the Celsius temperature.

Create a function that accepts a Fahrenheit temperature and returns its Celsius equivalent.

Use a loop to display the Fahrenheit temperatures from `0` through `20` and their Celsius equivalents.

## Required Python File

Create a Python file named:

`celsius_temperature_table.py`

Include a comment header containing:

* Student name
* Course number
* Week number
* Lab number
* Assignment title
* Date

## Part 1: Create the `celsius` Function

Create a function named:

`celsius`

The function must:

* Accept a Fahrenheit temperature as a parameter.
* Convert the Fahrenheit temperature to Celsius.
* Return the Celsius temperature.

The function should not display the entire table. Its responsibility is to perform and return one temperature conversion.

## Part 2: Create the Main Program

Create a `main()` function that controls the program.

The `main()` function must:

* Display a descriptive program title.
* Display appropriate column headings.
* Use a loop to process Fahrenheit temperatures from `0` through `20`.
* Call the `celsius` function during every loop repetition.
* Pass the current Fahrenheit temperature as an argument.
* Store or directly use the returned Celsius temperature.
* Display the Fahrenheit and Celsius values on the same row.

Call the `main()` function to begin the program.

## Part 3: Loop Requirements

The loop must:

* Begin with `0`.
* End with `20`.
* Include both `0` and `20`.
* Increase the Fahrenheit temperature by `1`.
* Repeat exactly 21 times.
* Call the `celsius` function during each repetition.

Do not manually write 21 separate conversion or output statements.

## Part 4: Display the Temperature Table

Display a table containing:

* A Fahrenheit column
* A Celsius column
* One row for every Fahrenheit temperature from `0` through `20`

Display Celsius values with two digits after the decimal point.

The output should have a structure similar to:

```text
Fahrenheit     Celsius
----------------------
0              -17.78
1              -17.22
```

Students may create their own table design, but the columns must be clearly labeled and aligned.

## Required Testing for Program 2

Verify the following values:

| Fahrenheit | Expected Celsius |
| ---------: | ---------------: |
|        0°F |         -17.78°C |
|        1°F |         -17.22°C |
|       10°F |         -12.22°C |
|       20°F |          -6.67°C |

Confirm that:

* The table begins with `0°F`.
* The table ends with `20°F`.
* Exactly 21 temperature rows are displayed.
* The `celsius` function is called during every loop repetition.
* Every Celsius value is returned by the function.
* Celsius values display two decimal places.
* The program runs without errors.

## Program 2 Point Distribution

* Program title and table headings: 3 points
* Correctly define the `celsius` function: 5 points
* Correct parameter and function call: 4 points
* Correct Fahrenheit-to-Celsius formula: 5 points
* Correct return value: 4 points
* Correct loop range from 0 through 20: 5 points
* Clear formatting, comments, and successful testing: 4 points

**Program 2 Total: 30 points**

# Program 3: Future Value

**Points: 40**

## Program Description

Suppose money is placed in a savings account that earns interest compounded monthly. The following formula calculates the account’s future value:

**F = P × (1 + i)ᵗ**

In this formula:

* `F` represents the account’s future value.
* `P` represents the account’s present value.
* `i` represents the monthly interest rate as a decimal.
* `t` represents the number of months.

Create a program that asks the user for the account’s present value, monthly interest rate, and number of months.

Pass those values to a function that calculates and returns the account’s future value.

## Required Python File

Create a Python file named:

`future_value.py`

Include a comment header containing:

* Student name
* Course number
* Week number
* Lab number
* Assignment title
* Date

## Part 1: Create the `futureValue` Function

Create a function named:

`futureValue`

The function must accept three parameters:

* Present value
* Monthly interest rate as a decimal
* Number of months

The function must:

* Calculate the account’s future value.
* Return the calculated future value.

The function should not ask the user for input. The required values must be received through its parameters.

## Part 2: Create the Main Program

Create a `main()` function that controls the program.

The `main()` function must:

* Display a descriptive program title.
* Ask for the account’s present value.
* Ask for the monthly interest rate.
* Ask for the number of months.
* Convert each entry to the appropriate numeric data type.
* Convert the percentage rate to decimal form.
* Call the `futureValue` function.
* Pass all three required values as arguments.
* Store the returned future value.
* Display a complete account summary.

Call the `main()` function to begin the program.

## Part 3: Present Value Input

Ask the user to enter the amount currently in the account.

The present value:

* May contain a decimal value.
* Must not be negative.
* Must be converted to an appropriate numeric type.

## Part 4: Monthly Interest Rate Input

Ask the user to enter the monthly interest rate as a percentage.

For example:

* Enter `1` for a monthly rate of 1%.
* Enter `0.5` for a monthly rate of 0.5%.
* Enter `0` if the account does not earn interest.

Before passing the rate to the function, convert it to decimal form.

Examples:

| Percentage Entered | Decimal Rate |
| -----------------: | -----------: |
|                 1% |         0.01 |
|               0.5% |        0.005 |
|              2.25% |       0.0225 |

The interest rate must not be negative.

## Part 5: Number of Months

Ask the user to enter the number of months the money will remain in the account.

The number of months must:

* Be entered as an integer.
* Be greater than zero.

## Part 6: Calculate the Future Value

Pass the following arguments to the `futureValue` function:

* Present value
* Monthly interest rate in decimal form
* Number of months

The function must apply the future-value formula and return the result.

Use Python’s exponent operator to raise `(1 + interest rate)` to the power represented by the number of months.

## Part 7: Display the Account Summary

Display a clearly formatted summary containing:

* Present value
* Monthly interest rate
* Number of months
* Future value

All monetary values must:

* Include a dollar sign.
* Display exactly two digits after the decimal point.

Display the interest rate clearly as a percentage.

## Required Testing for Program 3

### Test 1

* Present value: `$1,000`
* Monthly interest rate: `1%`
* Number of months: `12`
* Expected future value: `$1,126.83`

### Test 2

* Present value: `$2,500`
* Monthly interest rate: `0.5%`
* Number of months: `24`
* Expected future value: approximately `$2,817.90`

### Test 3

* Present value: `$5,000`
* Monthly interest rate: `0%`
* Number of months: `36`
* Expected future value: `$5,000.00`

### Invalid-Input Testing

Test each of the following:

* A negative present value
* A negative interest rate
* Zero months
* A negative number of months

Confirm that the program displays an appropriate error message instead of calculating a future value with invalid information.

## Program 3 Point Distribution

* Program title and clear prompts: 3 points
* Correct `main()` function organization: 4 points
* Correct input conversion: 4 points
* Correct percentage-to-decimal conversion: 4 points
* Correctly define `futureValue`: 5 points
* Correct parameters and function call: 5 points
* Correct future-value calculation: 6 points
* Correct return value: 4 points
* Clear monetary output, comments, validation, and testing: 5 points

**Program 3 Total: 40 points**

# Function Requirements

Every program must:

* Include a `main()` function.
* Include the required calculation function.
* Use parameters to receive values.
* Pass arguments when calling the calculation function.
* Use `return` to send the calculated result back to the calling statement.
* Call the calculation function from the main program.
* Store or appropriately use the returned value.
* Call `main()` to begin the program.

The calculation functions should not ask the user for input. Input and final output should be handled by the main program.

# Code Comments

Use comments to identify and explain the major sections of all three programs.

Include comments for:

* The program information header
* Function definitions
* Parameters and arguments
* The main function
* User input
* Input conversion
* Input validation
* Calculations
* Function calls
* Returned values
* Loops
* Final output

Comments should briefly explain the purpose of each major section. They should not repeat every Python statement word for word.

# General Requirements

* Use Python to complete all three programs.
* Create all three required Python files.
* Use the exact required function names.
* Include and call a `main()` function in every program.
* Use meaningful and consistent variable names.
* Convert user input to the appropriate data type.
* Pass values to functions using arguments.
* Return calculated values from functions.
* Do not use global variables to transfer data between functions.
* Include a complete comment header in every file.
* Include comments explaining the major program sections.
* Use clear prompts, headings, labels, and messages.
* Format numeric and monetary values as directed.
* Test every program using the required values.
* Check spelling, capitalization, grammar, and punctuation.
* Make sure all programs run without errors.
* Follow the course AI-use policy.
* Record any AI assistance in `AI-Use-Report.md`.

# Required Organization

Organize the assignment as follows:

* `Week-08`

  * `Lab-01`

    * `CMP131-Week-08-Lab-01.md`
    * `AI-Use-Report.md`
    * `src`

      * `kinetic_energy.py`
      * `celsius_temperature_table.py`
      * `future_value.py`

# Submission Requirements

Submit or push the complete `Lab-01` folder.

The submission must include:

* `kinetic_energy.py`
* `celsius_temperature_table.py`
* `future_value.py`
* `AI-Use-Report.md`

Before submitting, verify that:

* All three required Python files are included.
* All filenames are correct.
* Every file contains a complete comment header.
* Every program includes a `main()` function.
* Every program calls its `main()` function.
* The required calculation functions are correctly defined.
* Function names are spelled and capitalized correctly.
* Functions receive data through parameters.
* Programs pass the correct arguments to the functions.
* Functions return the calculated results.
* The kinetic-energy formula works correctly.
* The Celsius table displays Fahrenheit values from 0 through 20.
* The Celsius program displays exactly 21 temperature rows.
* The future-value formula works correctly.
* Interest rates are converted from percentages to decimals.
* Monetary values display two decimal places.
* All required test cases were completed.
* All programs run without errors.
* The AI-use report is complete.
* The latest work has been committed and pushed to GitHub.

# Suggested Git Commit Messages

* Create Week 8 Lab 1 Python files
* Add kinetic energy function
* Test kinetic energy calculations
* Add Celsius conversion function
* Create Fahrenheit-to-Celsius table
* Test temperature conversion loop
* Add future value function
* Add interest-rate conversion
* Test future value calculations
* Improve function comments and output
* Complete Week 8 Python lab

---

## GitHub Starter Repository

Use the following public starter repository:

[CMP131-Week-09-Lab-01](https://github.com/ahedhli12/CMP131-Week-09-Lab-01)

### Getting Started

1. Open the starter repository using the link above.
2. Select **Use this template → Create a new repository** when the template option is available.
3. Choose your personal GitHub account as the owner.
4. Name your repository `LastName-FirstName-CMP131-Week-09-Lab-01`.
5. Set your repository to **Public**.
6. Clone your own newly created repository—not the instructor’s starter repository.
7. Open the entire cloned folder in Visual Studio Code.
8. Complete and test every required Python file.
9. Commit and push your work to GitHub.
10. Verify that your latest files appear on GitHub.
11. Complete `AI-Use-Report.md`.
12. Submit the required work through Blackboard Ultra and include your public repository link when requested.

### Required Repository Files

- `CMP131-Week-09-Lab-01.md`
- `AI-Use-Policy.md`
- `AI-Use-Report.md`
- `celsius_temperature_table.py`
- `future_value.py`
- `kinetic_energy.py`

### Before You Submit

- [ ] All required Python files are in the repository root.
- [ ] Every required filename is exact.
- [ ] Each program runs successfully.
- [ ] Required tests and screenshots are complete.
- [ ] `AI-Use-Report.md` is complete and accurate.
- [ ] The latest commit is visible on GitHub.
