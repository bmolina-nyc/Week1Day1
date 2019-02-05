def palindromes(string):
    return string == string[::-1]


print(palindromes("racecar"))