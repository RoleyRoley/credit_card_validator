# Program for testing the validity of a credit card number using the Luhn algorithm.

print("\nWelcome to the Credit Card Validator!")
print("This program will check if a credit card number is valid using the Luhn algorithm.\n")
user_number = input("Enter a credit card number: ")





class CreditCardValidator:
    def __init__(self, user_number):
        self.number = user_number
    
    # Method to validate the credit card number using the Luhn algorithm.
    def validate(self):
        print(self.number)
        # Remove leading and trailing spaces.
        self.number = self.number.strip()
        # Remove all spaces within the number.
        self.number = self.number.replace(" ", "")
        if len(self.number) == 0:
            print("Invalid input: Credit card number cannot be empty.")
            return False
        
        if not self.number.isdigit():
            print("Invalid input: Credit card number must contain only digits.")
            return False
        
        if len(self.number) < 13 or len(self.number) > 19:
            print("Invalid input: Credit card number must be between 13 and 19 digits long.")
            return False
        
        # Convert the number into a list of integers.
        digits = [int(digit) for digit in self.number]
        print(f"{digits=}")
        
        # Remove 'check digit' (last digit) from the list.
        removed_check_digit = digits.pop(-1)
        
        print(f"Removed check digit: {digits}")
        
        # Reverse the list of digits.
        reversed_digits = digits[::-1]
        print(f"Reversed digits: {reversed_digits}")
        
        # Double every second digit from the right and sum all the digits.
        for index in range(0, len(reversed_digits), 2):
            doubled_digit = reversed_digits[index] * 2
            if doubled_digit > 9:
                doubled_digit -= 9
            reversed_digits[index] = doubled_digit
                
        # Add the 'check digit' back to the list.
        reversed_digits.append(removed_check_digit)
        
        print(f"Digits after processing: {reversed_digits}")
        
        # Calculate the sum of the processed digits.       
        digit_sum = sum(reversed_digits)
        print(f"Sum of digits after processing: {digit_sum}")
        
        # Check if the sum is divisible by 10.
        if digit_sum % 10 == 0:
            print("The credit card number is valid.")
            return True
        
        print("The credit card number is invalid.")
        return False
    
        
CreditCardValidator(user_number).validate()

