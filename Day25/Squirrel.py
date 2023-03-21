import pandas as pd

data = pd.read_csv("squirrel_data.csv")
squirrels_count_gray = len(data[data["Primary Fur Color"] == "Gray"])
squirrels_count_black = len(data[data["Primary Fur Color"] == "Black"])
squirrels_count_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(squirrels_count_gray)
print(squirrels_count_black)
print(squirrels_count_cinnamon)
# def find_number(list, color):
#     total = 0
#     for i in list:
#         if i == color:
#             total += 1
#     return total


data_dict = {
    "color": ["Black", "Gray", "Cinnamon"],
    "count": [squirrels_count_black, squirrels_count_gray, squirrels_count_cinnamon]
}

newdata = pd.DataFrame(data_dict)
newdata.to_csv("newdata.csv")
# print(newdata)
# print(find_number(new_list, "Cinnamon"))
