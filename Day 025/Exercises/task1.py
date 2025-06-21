# with open("weather_data.csv", "r") as file:
#     text = file.readlines()
# for line in text:
#     print(line)


# import csv

# with open ("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
# print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# temp_list = data["temp"].to_list()
# print(temp_list)

# avg_temperature = round(sum(temp_list)/len(temp_list),2)
# print(avg_temperature)

# print(data["temp"].mean())
# print(data["temp"].max())

# Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# def cel_to_farh(temp):
#     return (temp*9/5)+32

# print(cel_to_farh(monday.temp[0]))

# Create a DataFrame from scratch
data_dict = {
    "students":["Amy", "James", "Angela"],
    "scores":[76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("new_file.csv")