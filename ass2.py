s = "aabbcdeaabbceder"
count = {}

for letter in s:
    if letter in 'aeiou':
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

print(count)



d = {"don": 100, "sunny": 200, "sai": 1, "shannu": 20}
total = 0

for value in d.values():
    total += value

print(total)





d = {"don": 100, "sunny": 200, "sai": 1, "shannu": 20}
total = sum(d.values())
print(total)


d={}
n=int(input("Enter number of students u want:"))
i=1
while i<=n:
    name=input("Entera name:")
    marks=int(input("Enter marks:"))
    d[name]=marks
    i=i+1
print(d)
