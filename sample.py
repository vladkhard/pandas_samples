import pandas as pd
from uuid import uuid4
from copy import deepcopy
from generate import generate_row

def read_csv(path):
    return pd.read_csv(path)

def select_limit(data):
    return data.head(3) # changes on head affects data!
    # return data[:3]

def select_by_name(data, name):
    return data[data.name == name]
    # return data.query("name == '{}'".format(name))

def select_age_range(data):
    return data[(data.age >= 18) & (data.age <= 60)]
    # return data.query('age >= 18 & age <= 60')


def select_age_max(data):
    return data.loc[data.age.idxmax()]

def select_unique(data):
    return data.drop_duplicates(keep='first')

def group_by_name(data):
    return data.groupby('name').size()

def group_by_name_and_city(data):
    return data.groupby(['name', 'city']).size()

def _filter(item):
    return (item.age > 18) & (item.sex == 'male')
def filter_with_func(data):
    return data[_filter(data)]

def filter_with_query(data):
    return data.query("age > 18 & sex == 'male'")

def filter_with_generator(data):
    return data.loc[[
        i
        for i in data.index
        if data.loc[i].age > 18 and
        data.loc[i].sex == 'male'
    ]]

def sort_by_age(data):
    return data.sort_values(by='age')

def del_age(data):
    return data.drop(columns='age')

def del_5(data):
    return data.drop(index=5)

def insert_column_id(data):
    data = deepcopy(data)
    ids = [uuid4().hex for i in range(len(data))]
    data.insert(loc=len(data.columns),
        column='id', value=ids)
    return data

def insert_row(data):
    return data.append(generate_row(), ignore_index=True)

def set_age_100(data):
    data = deepcopy(data)
    data.loc[:, 'age'] = 100
    return data
    # return data.age.map(lambda _: 100)

def set_index_to_id(data):
    return insert_column_id(data).set_index('id')
    
def reset_index(data):
    return data.reset_index().drop(columns='index')


if __name__ == '__main__':
    data = read_csv('sample.csv')
    import ipdb; ipdb.set_trace()
