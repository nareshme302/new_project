given_string = "Hi am naresh"
g_s = given_string.lower()
vowels = "aeiou"
d = {}.fromkeys(vowels,0)
for char in g_s:
    if char in d:
        d[char]+= 1
print(d)
