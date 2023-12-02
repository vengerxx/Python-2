
import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)
new_data = pd.DataFrame()
unique_values = data['whoAmI'].unique()
for value in unique_values:
    new_data[value] = (data['whoAmI'] == value).astype(int)
print(new_data)
