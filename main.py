def all_variants(str):
    if len(str) == 3:
        for i in str:
            yield i
        yield str[:-1]
        yield str[1:]
        yield str[::]


a = all_variants("abc")
for i in a:
    print(i)
