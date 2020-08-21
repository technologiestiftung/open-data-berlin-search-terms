import pandas as pd

list_of_months = ['2019-02','2019-03','2019-04','2019-05','2019-06',
    '2019-07','2019-08','2019-09','2019-10','2019-11','2019-12',
    '2020-01','2020-02','2020-03','2020-04','2020-05', '2020-06','2020-07']

initial_data = pd.read_csv('data/all_months/initial_cleaning/clean_terms_2019-02.csv')
columns = initial_data.columns
merged = pd.DataFrame(columns = columns)
for month in list_of_months:
    filename = 'data/all_months/initial_cleaning/clean_terms_' + month + '.csv'                        
    data = pd.read_csv(filename) 
    data['month'] = month
    merged = pd.concat([merged, data])
print(merged)

# > 4 einbauen
merged.to_csv('data/clean_terms_all.csv', index=False)