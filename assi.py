s = "aabbcdeaabbceder"
count = {}

for letter in s:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1

print(count)