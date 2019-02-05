def currency_converter(amount):
    amounts = {10000:0, 5000:0, 1000:0, 500:0, 100:0, 25:0, 10:0, 5:0, 1:0}
    words = ["hundred dollar bill", "fifty dollar bill", "ten dollar bill", "five dollar bill", "one dollar bill", "quarter", "Dime", "Nickel", "Penny"]
    total_amount = amount * 100

    for item in dict.keys(amounts):
            while total_amount - item >= 0:
                amounts[item] += 1
                total_amount -= item
            else:
                pass

    totals =  list(dict.values(amounts))
    i = 0 
    while i < len(words):
        if totals[i]:
            print(f'{totals[i]}: {words[i]}')
            i += 1
        else:
            i += 1


print(currency_converter(12.33))