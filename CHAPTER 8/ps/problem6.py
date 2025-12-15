def remove_and_strip(lst, word):
    new_list = []
    for item in lst:
        stripped_item = item.strip()      # remove extra spaces
        if stripped_item != word:         # remove given word
            new_list.append(stripped_item)
    return new_list

# Example list
words = ["  apple ", " banana", " mango ", "banana ", " grape "]

# Calling function
result = remove_and_strip(words, "banana")

print(result)

