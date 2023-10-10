a = int(input("valor A: "))
b = int(input("valor B: "))
""" 
if a == 10:
    print("a == 10")
else:
    print("outro valor")
"""

"""
if a == 10:
    print("a == 10")
else:
    if a == 15:
        print("a == 15")
    else:
        print("outro valor")

    print("fim do else")

print("fim do prog")
"""

"""
if (a > 10) or (b == 10):
    print("a > 10")
elif b > 15:
    print("a > 15")
else:
    print("outro valor")

"""
"""
if a == 0:
    print("a == 0")
elif a == 5:
    print("a == 5")
elif a == 10:
    print("a == 10")
elif a == 15:
    print("a == 15")
elif a == 20:
    print("a == 20")
else:
    print("A é outro valor")
"""


match a:
    case 5:
        print("a == 5")
    case 10:
        print("a == 10")
    case 15:
        print("a == 15")
    case 20:
        print("a == 20")
    case _:
        print("a tem outro calor")

print("fim do case")


