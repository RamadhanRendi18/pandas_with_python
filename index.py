import pandas as pd
from pandas import Series

obj = pd.Series([1, 2, 3, 4])
# print(obj)
# print(obj.values)
# print(obj.index)

# SECTION Mencetak data dengan index yang diinginkan
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
# !SECTION Mencetak data dengan index yang diinginkan
