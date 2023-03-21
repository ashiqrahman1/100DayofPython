import pandas as pd

data = pd.read_csv("weather_data.csv")
# data_dict = data.to_dict()

# temp_list = data['temp'].to_list()

# max = data['temp'].max()
# print(max)
# print(data[data.temp == data.temp.max()]['condition'])
# Get the temp of monday and convert
newdata = data[data.day == "Monday"]["temp"] * 1.8000 + 32
print(f"{newdata},Fahrenheit")
