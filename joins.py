import pandas as pd

df1 = pd.DataFrame({
    'num': [1, 2, 3],
    'spam': ['spam'] * 3
})

df2 = pd.DataFrame({
    'num': [3, 4, 5],
    'ham': ['ham'] * 3
})

inner = pd.merge(df1, df2, on='num', how='inner')
outer = pd.merge(df1, df2, on=['num', 'num'], how='outer')
right = pd.merge(df1, df2, how='right')
left  = pd.merge(df1, df2, how='left')

right_inner = pd.merge(df1, df2, how='right', indicator=True)
right_inner = right_inner[right_inner['_merge'] == 'right_only']
del right_inner['_merge']

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()