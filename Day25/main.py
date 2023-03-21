# with open("weather_data.csv") as csv:
#     data = csv.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as c:
#     data = csv.reader(c)
#     temp = []
#     for row in data:
#         # print(row[1])
#         if row[1] != "temp":
#             temp.append(int(row[1]))

#     print(temp)


import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
