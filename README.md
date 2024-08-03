# Password_Generator

This script is a simple password generator application built using the Tkinter library for the graphical user interface (GUI). It allows users to generate passwords based on various criteria such as length, inclusion of digits, uppercase letters, lowercase letters, special characters, and the word "RICK".

## Script Overview

The script consists of the following main components:

### 1. Password Generation Function
The function `gen_password` is defined to generate a password based on the specified criteria:
- `length`: Length of the password.
- `use_digits`: Boolean to include digits (0-9).
- `use_upper`: Boolean to include uppercase letters (A-Z).
- `use_lower`: Boolean to include lowercase letters (a-z).
- `use_special`: Boolean to include special characters.
- `add_rick`: Boolean to include the word "RICK".

The function constructs a character set based on the selected criteria and generates a password by randomly selecting characters from this set.

### 2. Update Password Function
The function `update_password` retrieves the user's input from the GUI, calls `gen_password` with the appropriate arguments, and updates the password field in the GUI with the newly generated password. It also handles input validation for the password length

### Script Execution
The script initializes the Tkinter main loop, which displays the GUI and waits for user interaction.

### Example of Usage
1. Run the script.
2. Enter the desired password length.
3. Select the criteria for the password (digits, uppercase, lowercase, special characters, and/or "RICK").
4. Click the "Generate Password" button.
5. The generated password will be displayed in the entry field.

This script provides a simple yet flexible way to generate passwords based on user-defined criteria through an intuitive graphical interface.
