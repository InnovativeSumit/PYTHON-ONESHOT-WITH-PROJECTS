letter = '''Dear <|NAME|>,'''
print(letter.replace("<|NAME|>", "Sumit"))

letter = '''Dear <|NAME|>,
you are seleceted DATE'''
print(letter.replace("<|NAME|>", "Sumit").replace("DATE", "20th Jan 2024"))