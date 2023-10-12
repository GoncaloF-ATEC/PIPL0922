my_set = {"elm1", "elm2", "elm3", "elm4", "elm5"}

print(my_set)

"""

{'elm3', 'elm1', 'elm5', 'elm4', 'elm2'}
{'elm3', 'elm5', 'elm4', 'elm1', 'elm2'}
{'elm2', 'elm1', 'elm5', 'elm4', 'elm3'}

"""

my_set.add("teste")

print(my_set)

print(my_set.__len__())

my_set.add("teste")
print(my_set.__len__())

my_set.remove("teste")


my_set2 = {"elm1", "elm2", "elm3", "elm4", "elm5"}
my_set3 = {"elm7", "elm8", "elm3", "elm4", "elm5"}


print(my_set2.union(my_set3))
print(my_set2.intersection(my_set3))

print(my_set2.difference(my_set3))

print(my_set2.symmetric_difference(my_set3))


my_set4 = {"elm1", "elm2", "elm3"}

print(my_set4.issubset(my_set2))
print("-" * 10, "print set", "-" * 10)
for elm in my_set:
    print(elm)

