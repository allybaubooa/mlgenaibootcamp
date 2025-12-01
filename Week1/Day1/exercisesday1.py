# price = float(input("Enter Item price): "))


# final_price = price * (1 + vat_rate)
# print(f"Original: {price} -> Final (with VAT): {final_price:.2f}")

vat_rate = 0.15

user_input = input("Enter item prices separated by commas: ")

item_prices = [float(p.strip()) for p in user_input.split(",")]

for price in item_prices:
    final_price = price * (1 + vat_rate)
    print(f"Original: {price} -> Final (with VAT): {final_price:.2f}")
    if price > 1000:
        print("You're eligible for free shipping")
    else:
        print("Shipping must be paid")




# desc = "Strings are..."
# print(desc.upper())
# print(desc.replace("are","is"))
# words = desc.split()
# print(words[0].lower())