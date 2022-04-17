n = int(input())
small_cats = 0
big_cats = 0
huge_cats = 0
food_eaten = 0
price_for_food = 0
for n in range(n):
    food = int(input())
    if 100 <= food < 200:
        small_cats += 1
    elif 200 <= food < 300:
        big_cats += 1
    elif 300 <= food < 400:
        huge_cats += 1

    food_eaten += food
price_for_food = (food_eaten / 1000) * 12.45
print(f'Group 1: {small_cats} cats.')
print(f'Group 2: {big_cats} cats.')
print(f'Group 3: {huge_cats} cats.')
print(f'Price for food per day: {price_for_food:.2f} lv.')