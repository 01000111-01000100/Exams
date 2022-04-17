command = input()
player_name = ''
number_of_goals = 0
while command != "END":
    current_goals = int(input())
    if current_goals >= 10:
        number_of_goals = current_goals
        player_name = command
        break
    elif current_goals > number_of_goals:
        number_of_goals = current_goals
        player_name = command
    command = input()
print(f"{player_name} is the best player!")

if current_goals >= 3:
    print(f"He has scored {number_of_goals} "
          f"goals and made a hat-trick !!!")
else:
    print(f"He has scored {number_of_goals} goals.")