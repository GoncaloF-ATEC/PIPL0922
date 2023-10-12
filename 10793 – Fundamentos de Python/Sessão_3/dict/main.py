dict = {
    "nome": "Gonçalo",
    "nota": 20,
    "Aprovado": True
}

print(dict["nome"])

dict["Escola"] = "ATEC"
print(dict)
dict.pop("Escola")

print(dict)

for elm in dict.values():
    print(elm)


for key, value in dict.items():
    print(key)
    print(value)


"""
dict = {
    "nome": "Gonçalo",
    "nota": 20,
    "Aprovado": True
}
"""
print(dict.get("name"))


print(dict.__contains__("Gonçalo")) # <- verifica se a key existe