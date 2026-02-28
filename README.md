# Credit Card Validation (Luhn Algorithm)

A simple Python project that checks whether a credit card number is valid using the **Luhn algorithm**.

This project is useful for learning:
- input validation,
- list/digit processing,
- and checksum-based verification.

> Note: Luhn validation only checks whether a number is mathematically valid. It does **not** confirm the card is active, funded, or issued.

## Project Overview

The script:
1. Prompts the user to enter a card number.
2. Cleans the input (removes spaces and leading/trailing whitespace).
3. Verifies the input is numeric and has a realistic card length (13-19 digits).
4. Runs the Luhn checksum.
5. Prints whether the number is valid or invalid.

## How the Luhn Algorithm Works

Given a card number:

1. **Separate the check digit**
   - Remove the last digit (this is the check digit).

2. **Reverse the remaining digits**
   - This makes it easy to process every second digit from the right.

3. **Double every second digit**
   - Starting from the first digit in the reversed list (index `0`, `2`, `4`, ...).

4. **If a doubled value is greater than 9, subtract 9**
   - Example: `8 * 2 = 16`, then `16 - 9 = 7`.

5. **Add the check digit back**
   - Include it in the final sum.

6. **Sum all processed digits**
   - If the total is divisible by `10`, the number is valid.

In formula form:

`total % 10 == 0`  → valid

## Example (High-Level)

For input `7762888103111881`:
- The processed digit sum is `64`.
- `64 % 10 = 4`, not `0`.
- Therefore, the card number is **invalid**.

## Running the Project

### Requirements
- Python 3.x

### Run

From the project folder:

```bash
python main.py
```

Then enter a credit card number when prompted.


