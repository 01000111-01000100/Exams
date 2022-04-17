team = input()
suveniri = input()
broi_zakupeni = int(input())

cena = 0
if team == "Argentina":
    if suveniri == "flags":
        cena = 3.25
    elif suveniri == "caps":
        cena = 7.20
    elif suveniri == "posters":
        cena = 5.10
    elif suveniri == "stickers":
        cena = 1.25

elif team == "Brazil":
    if suveniri == "flags":
        cena = 4.20
    elif suveniri == "caps":
        cena = 8.50
    elif suveniri == "posters":
        cena = 5.35
    elif suveniri == "stickers":
        cena = 1.20

elif team == "Croatia":
    if suveniri == "flags":
        cena = 2.75
    elif suveniri == "caps":
        cena = 6.90
    elif suveniri == "posters":
        cena = 4.95
    elif suveniri == "stickers":
        cena = 1.10

elif team == "Denmark":
    if suveniri == "flags":
        cena = 3.10
    elif suveniri == "caps":
        cena = 6.50
    elif suveniri == "posters":
        cena = 4.80
    elif suveniri == "stickers":
        cena = 0.90


total_sum = broi_zakupeni * cena

if not team:
    print("Invalid country!")
elif not suveniri:
    print("Invalid stock!")

print(f"Pepi bought {broi_zakupeni} {suveniri} of {team} for {total_sum:.2f} lv.")