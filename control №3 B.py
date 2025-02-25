import pandas as pd
import matplotlib.pyplot as plt


file_path = 'путь к датасету'
df = pd.read_excel(file_path)

print(df.head())

plt.figure(figsize=(8, 6))

plt.scatter(df['apple'], df['kiwi'], label='Зависимость яблока от киви')

plt.title('График из Excel')
plt.xlabel('apple')
plt.ylabel('kiwi')
plt.legend()
plt.grid(True)
plt.show()
