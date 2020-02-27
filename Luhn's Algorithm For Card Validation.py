def isValidCard(card_number):
    # Checks the card validation for the initial numbers
    card_number = str(card_number)
    card_length = len(card_number)
    first_digit = int(card_number[0])
    if (card_length < 13 or card_length > 16):
        return False
    if (first_digit not in range(3, 7)):
        return False
    second_digit = int(card_number[1])
    if (first_digit == 3 and second_digit != 7):
        return False
    
    # Checks the card validation using the Luhn algorithm
    total_sum = 0
    for i in range(len(card_number) - 2, 0, -2): # Reduces the loop by half
        digit_to_double = int(card_number[i]) * 2
        total_sum += digit_to_double // 10 + digit_to_double % 10 + int(card_number[i + 1])
        if (i == 1): # Adds the first digit as this would be the last digit to be doubled
            total_sum += int(card_number[0])
    return total_sum % 10 == 0

# Executes the main function
if (__name__ == "__main__"):
    card_number = int(input("Please input the Card Number!\n"))
    isValid = isValidCard(card_number)
    print("Valid") if isValid else print("Invalid")
