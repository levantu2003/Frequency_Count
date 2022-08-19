text = input("Write a line of text: ")
freq = {}
for c in text:
    c = c.lower()
    freq[c] = freq.get(c, 0) + 1
print("Here is the result!")
for key, value in freq.items():
    print(f"{key}: {value}")