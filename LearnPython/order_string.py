some_list = ["C", "A", "K", "J"]
result_list = []

print(ord("a"))

for character in some_list:
    result_list.insert(int(ord(character.lower()) - 97), character)



print(result_list)

# new_list = [1,2,3,4]
# new_list.insert(1, 33)
# print(new_list)