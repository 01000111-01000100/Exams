procesor = int(input())
videocard = int(input())
ram = int(input())
number_ram = int(input())
sum_discount = float(input())


price_procesor = procesor * 1.57
price_videocard = videocard * 1.57
price_ram = ram * 1.57
total_price_ram = price_ram * number_ram
total_price_procesor = price_procesor - sum_discount * price_procesor
total_price_videocard = price_videocard - sum_discount * price_videocard
total_price = total_price_procesor + total_price_videocard + total_price_ram
print(f"Money needed - {total_price:.2f} leva.")