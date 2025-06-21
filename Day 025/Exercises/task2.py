import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250620.csv")

squirrel_colors = data["Primary Fur Color"].dropna().to_list()
non_repetitive_colors = list(set(squirrel_colors))
count = []
for color in non_repetitive_colors:
    count.append(squirrel_colors.count(color))

data_dict = {
    "Fur Color": non_repetitive_colors,
    "Count": count
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")