import pandas as pd
df = pd.read_csv('data.csv', index_col=0)
# df.info()

for i, row in df.iterrows():
    print('## ' + row['name'])
    print(row['description'])
    print()

if __name__ == '__main__':
    pass
