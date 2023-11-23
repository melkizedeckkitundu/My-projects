# Melkizedeck Kitundu

# 4. Get two pieces of input from the user (Page 25)
input_1 = input("Enter the first piece of information: ")
input_2 = input("Enter the second piece of information: ")

# 5. Acknowledge the two pieces of input from the user
print("You entered:")
print("1. " + input_1)
print("2. " + input_2)

# 6. Concatenate two pieces of input from the user (Page 36)
concatenated_string = input_1 + " " + input_2
print("Concatenated string:", concatenated_string)

# 7. Ask for a number as input, use INT command, and print the input (Page 53)
number_input = int(input("Enter a number: "))
print("You entered:", number_input)

# 8. Ask for two separate numbers, print their summation
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
sum_result = number_1 + number_2
print("Sum of the two numbers:", sum_result)

# 9. Ask if the user knows the product of the two numbers
product_guess = int(input("What is the product of the two numbers? "))
product_actual = number_1 * number_2

# Check if the guess is correct
if product_guess == product_actual:
    print("Congratulations! Your guess is correct.")
else:
    print("Sorry, that's not the correct product. The actual product is:", product_actual)

# Melkizedeck Kitundu

