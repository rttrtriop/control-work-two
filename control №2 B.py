import pandas as pd
import matplotlib.pyplot as plt
data = "C:/Users/Unicum_Student/pythonProject7/dataset.xlsx"
df = pd.read_excel(data)
print(df.head())
plt.figure(figsize=(8, 6))

plt.plot(df['apple'], df['kiwi'], marker='o', label='Зависимость apple от kiwi')

plt.title('График из Excel')
plt.xlabel('apple')
plt.ylabel('kiwi')
plt.legend()
plt.grid(True)

plt.show()
