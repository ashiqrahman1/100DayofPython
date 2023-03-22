# list = [x*2 for x in range(1, 5)]
# print(list)


name = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
new_list = [n.upper() for n in name if len(n) > 5]
print(new_list)
