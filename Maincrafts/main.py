import pandas as pd

import matplotlib.pyplot as plt


df = pd.read_csv('student-mat.csv', sep=';')
print("Average Final Grade:", df['G3'].mean())

plt.hist(df['G3'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Final Grades')
plt.xlabel("Grade")
plt.ylabel("Frequency")
plt.show()