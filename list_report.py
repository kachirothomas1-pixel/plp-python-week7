# List report exercise
items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")

word_count = 0
for item in items:
    if len(item) > 4:
        word_count += 1
print(f"Items with more than 4 letters: {word_count}")

longest_item = items[0]
for item in items[1:]:
    if len(item) > len(longest_item):
        longest_item = item

print(f"Longest item: {longest_item}")
