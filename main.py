import pandas as pd

### SQUARE NUMBERS IN LIST ###
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [x ** 2 for x in numbers]

print(squared_numbers)

### EVEN NUMBER FILTER ###
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [x for x in numbers if x % 2 == 0]

print(result)

### NUMBERS APPEARING IN BOTH TXT FILES ###
with open("file1.txt") as file:
	numbers1 = [int(x) for x in file.readlines()]

with open("file2.txt") as file2:
	numbers2 = [int(x) for x in file2.readlines()]

result = [x for x in numbers1 if x in numbers2]


print(result)

### SENTENCE BY WORD WITH LENGTH OF WORD ###
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {x:len(x) for x in sentence.split()}

print(result)

### DICTIONARY INTERPRETTION ###
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = { day:round(weather * 1.8 + 32, 2) for (day,weather) in weather_c.items() }

print(weather_f)

### DATA FRAME WITH ITERROWS ###
student_dict = {
	"student": ["Angela", "James", "Lily"],
	"score": [56, 76, 98]
}

student_data_frame = pd.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
	print(index)
	print(row.score)