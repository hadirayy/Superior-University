def LUHN(card_number):
    card_number=str(card_number)
    total=0
    for i, digit in enumerate(card_number[::-1]):
        digit =int(digit)
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit = digit-9
        total += digit
    return total % 10 == 0 
card_number=int(input("Enter the card number:"))
is_valid=LUHN(card_number)
print(f"The card number{card_number} is valid {is_valid}")A