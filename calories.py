import pandas as pd

data = {
    'ID': list(range(1, 16)),
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male',
               'Female', 'Male', 'Female', 'Male', 'Female',
               'Male', 'Female', 'Male', 'Female', 'Male'],
    'Age': [25, 30, 22, 28, 35,
            24, 31, 29, 26, 33,
            27, 32, 23, 34, 36],
    'Height(cm)': [175, 160, 180, 165, 170,
                   158, 182, 168, 177, 162,
                   174, 161, 178, 166, 172],
    'Weight(kg)': [70, 60, 75, 55, 80,
                   58, 78, 59, 73, 62,
                   71, 61, 74, 57, 76],
    'Duration(min)': [30, 45, 60, 20, 40,
                      25, 50, 35, 55, 30,
                      45, 25, 60, 20, 50],
    'Heart_Rate': [130, 120, 150, 115, 140,
                   118, 145, 122, 148, 119,
                   135, 116, 149, 117, 142],
    'Body_Temp(C)': [36.5, 36.7, 37.2, 36.3, 37.0,
                     36.6, 37.1, 36.4, 37.3, 36.5,
                     36.8, 36.2, 37.0, 36.3, 37.2],
    'Calories': [220, 300, 450, 180, 350,
                 210, 430, 290, 470, 310,
                 360, 200, 460, 190, 420]
}

df = pd.DataFrame(data)
df.to_csv('calories_burnt.csv', index=False)
print(df)
