print("**************** 0 a 9 *************")

for i in range(10):  # C ->  for(int i = 0; i > 10; i++){}
    print(i) # print(i, end="\n")


print("**************** 5 a 9 *************")

for i in range(5, 10):  # C ->  for(int i = 5; i > 10; i++){}
    print(i, end=" ")

print("")
print("**************** 5 a 100 *************")

for i in range(5, 100, 5):  # C ->  for(int i = 5; i > 10; i += 5){}
    print(i, end=" ")


contador = 0
while contador < 100:
    print(f"it works: {contador}")
    contador += 1
