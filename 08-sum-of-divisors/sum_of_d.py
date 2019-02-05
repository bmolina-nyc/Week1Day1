def divided_we_fall(number):
    divisors = []
    
    for num in range(1, number+1):
        if number % num == 0:
            divisors.append(num)

    sum_divisors = sum(divisors)
    total_divisors = len(divisors)
    
    return [divisors, sum_divisors, total_divisors]



print(divided_we_fall(60))