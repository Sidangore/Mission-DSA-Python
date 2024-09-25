def countVowels(self, s):
    vowels = "aeiou"
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count