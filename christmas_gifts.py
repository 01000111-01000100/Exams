age = int(input())
number_kids = 0
number_adults = 0
money_for_toys = 0
money_for_seaters = 0

while age != "Christmas":
    current_number = int(age)
    if current_number <= 16:
        number_kids += 1
        money_for_toys = 5
    elif current_number >= 16:
        number_adults += 1
        money_for_seaters = 15
    age = input()
toys_price = number_kids * money_for_toys
seaters_price = number_adults * money_for_seaters
print(f"Number of adults: {number_adults}")
print(f"Number of kids: {number_kids}")
print(f"Money for toys: {toys_price}")
print(f"Money for sweaters: {seaters_price}")