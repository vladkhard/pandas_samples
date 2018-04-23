import random
import pandas as pd

def generate_row():
    result = {
        'name': random.choice(('Alice', 'Bob', 'Joe', 'John', 'Annie')),
        'age': random.randint(0, 99),
        'city': random.choice(('New York', 'Los Angeles', 'San Francisco', 'Seattle', 'Chicago'))
    }
    if result['name'] in ('Alice', 'Annie'):
        result['sex'] = 'female'
    else:
        result['sex'] = 'male'
    return result

if __name__ == '__main__':
    df = pd.DataFrame([generate_row() for i in range(2000000)])
    df.to_csv('sample.csv', index=False)
