def calculate_discount(price, discount_percent):
    # Calculate the discount amount
    discount_amount = (discount_percent / 100) * price
    
    # Calculate the final price after applying the discount
    final_price = price - discount_amount
    
    return final_price


# Example 1

price = 1000

discount_percent = 20

final_price = calculate_discount(price, discount_percent)

print(final_price)

# Applying discount 

def apply_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = (price * discount_percentage) / 100
        return price - discount_amount
    return price

original_price = 1000
discount_percentage = 20

final_price = apply_discount(original_price, discount_percentage)
print(final_price)

def apply_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = (price * discount_percentage) / 100
        return price - discount_amount
    return price

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = apply_discount(original_price, discount_percentage)

# Display the result
if final_price == original_price:
    print(f"No discount applied. The original price is: {original_price}")
else:
    print(f"The final price after applying the discount is: {final_price}")


