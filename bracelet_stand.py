p1 = float(input())
p2 = float(input())
p3 = float(input())
p4 = float(input())

spesteni_pari = 5 * p1
specheleni_pari = 5 * p2
total_spesteni_pari = spesteni_pari + specheleni_pari
razhodi = total_spesteni_pari - p3

needed_money = p4 - razhodi
if razhodi < p4:
    print(f"Insufficient money: {needed_money:.2f} BGN.")
else:
    print(f"Profit: {razhodi:.2f} BGN, the gift has been purchased.")
