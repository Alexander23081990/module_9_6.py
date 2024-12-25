def all_variants(text):
    length = len(text)
    for index_1 in range(1, length + 1):
        for index_2 in range(length - index_1 + 1):
            yield text[index_2:index_2 + index_1]


a = all_variants("abc")
for i in a:
    print(i)
