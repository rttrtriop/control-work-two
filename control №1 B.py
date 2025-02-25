def one (num):
    num2 = num -1
    print(d.iloc[num2:num])

import pandas as pd
data = "путь к датасету"
d = pd.read_excel(data)

one(int(input("ведите номер строки")))
