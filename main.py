# Program for testing the validity of a credit card number using the Luhn algorithm

print("\nWelcome to the Credit Card Validator!")
print("This program will check if a credit card number is valid using the Luhn algorithm.\n")
user_number = input("Enter a credit card number: ")





class CreditCardValidator:
    def __init__(self, user_number):
        self.number = user_number
        
    def validate(self):
        print(self.number)
        if self.number is None or len(self.number) == 0:
            print("Invalid input: Credit card number cannot be empty.")
            return False
    
        
CreditCardValidator(user_number).validate()