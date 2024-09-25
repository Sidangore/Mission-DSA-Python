def countVowels(self, s):
    vowels = "aeiou"
    count = set()
    for i in s:
        if i in vowels:
            count.add(i)
    return len(count)