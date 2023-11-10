def palidrom(text):
    x = False
    a = text.lower()
    b = ''.join(reversed(a))
    if a == b:
        x = True
    return x
print(palidrom(str(input())))