import pandas as pd
print("success")
data =  pd.Series([1,2,3,4,5,6])
print(data)

student = pd.Series({
    "Name":["Abhishek" , "Ram" , "Raju"],
    "City":["LKO","JNP","KNP"],
    "Marks":[23,45,76]
})
print(student)
df = pd.DataFrame(student)
print(df)
print(df.info())
print(df.describe())
df.to_csv("tech4B.csv")

# print(student["City"][1])
# print(student["Name"][1])
# print(student["Marks"][1])

# for i in range (0,3):
#     print(student['City'][i])
