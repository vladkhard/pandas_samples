import pandas as pd
from generate import generate_row

common = generate_row()

df1 = pd.DataFrame([generate_row(), common])
df2 = pd.DataFrame([common, generate_row()])

inner = pd.merge(df1, df2, how='inner')
outer = pd.merge(df1, df2, on=['age', 'name', 'city', 'sex'], how='outer')
right = pd.merge(df1, df2, on=['age', 'name', 'city'], how='right')
left  = pd.merge(df1, df2, how='left')

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()