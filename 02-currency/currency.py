def currency_converter(amount):
    amounts = {10: 0, 1:0, .25 : 0, .05: 0, .01: 0 }
    keys = dict.keys(amounts)

    while True:
        currency = amount 
        for key in keys:
            print(f'this is the key {key} and this is the {amount}')
            if currency - key > 1:
                amounts[key] += 1
                currency -= key
                print(currency, key)
                if currency == 0:
                    break 
            else:
                continue 
    
    return amounts

    


print(currency_converter(10))