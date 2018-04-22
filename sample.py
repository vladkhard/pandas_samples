import pandas as pd
data = pd.read_csv('sample.csv')

def select(data):
    return data

def select_limit(data):
    return data.head(3)

def select_by_tender(data, tender):
    return data[data.tender == tender]

def select_value_range(data):
    return data[(data.value >= 1000) & (data.value <= 10000)]

def select_value_max(data):
    return data.loc[data.value.idxmax()]

def select_unique(data):
    return data.drop_duplicates(subset='tender', keep='first').reset_index()

def group_by_tender(data):
    return data.groupby('tender').size()

def group_by_tender_and_bid(data):
    return data.groupby(['tender', 'bid']).size()

def _filter(item):
    return (item.value > 1000) & (item.state == 1)
def filter_with_func(data):
    return data[_filter(data)]

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()