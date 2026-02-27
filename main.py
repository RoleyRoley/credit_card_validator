# Program for testing the validity of a credit card number using the Luhn algorithm

print("\nWelcome to the Credit Card Validator!")
print("This program will check if a credit card number is valid using the Luhn algorithm.\n")
user_number = input("Enter a credit card number: ")





class CreditCardValidator:
    def __init__(self, user_number):
        self.number = user_number
    
    # Method to validate the credit card number using the Luhn algorithm
    def validate(self):
        print(self.number)
        self.number = self.number.strip()
        if self.number is None or len(self.number) == 0:
            print("Invalid input: Credit card number cannot be empty.")
            return False
        
        if not self.number.isdigit():
            print("Invalid input: Credit card number must contain only digits.")
            return False
        
        if len(self.number) < 13 or len(self.number) > 19:
            print("Invalid input: Credit card number must be between 13 and 19 digits long.")
            return False
        
        
    
        print(self.number)
CreditCardValidator(user_number).validate()