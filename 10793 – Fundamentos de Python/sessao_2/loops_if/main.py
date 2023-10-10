
while True:
    print("#"*10)
    num = int(input("Digite um valor: "))

    if num < 0:
        print("sair")
        break
    else:
        print("nao sair")
        continue

    print("Fim da volta")
    print("#" * 10)

print("fora do while")





for i in range(2):
    for j in range(5):
        if j == 3:
            break

        print(f"i:{i}, j:{j}")


"""
i:0, j:0
i:0, j:1
i:0, j:2
i:1, j:0
i:1, j:1
i:1, j:2


"""