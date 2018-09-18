import numpy as np
import pandas as pd

cars1 = pd.read_csv('./tsv/cars1.csv')
cars2 = pd.read_csv('./tsv/cars2.csv')
# print(cars1.head())
# print(cars2.head())
cars1 = cars1.loc[:, "mpg":"car"]
new_cars = cars1.append(cars2,sort=True)


raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
data1 = pd.DataFrame(raw_data_1, columns = ['subject_id', 'first_name', 'last_name'])
data2 = pd.DataFrame(raw_data_2, columns = ['subject_id', 'first_name', 'last_name'])
data3 = pd.DataFrame(raw_data_3, columns = ['subject_id','test_id'])
print(data1,data2,data3)

#只合并行
all_data  = pd.concat([data1, data2])

#合并列 axis=1连接列
all_data_col = pd.concat([data1, data2], axis = 1)

#
new_data = pd.merge(all_data,data3,on='subject_id')

#内连接
pd.merge(data1, data2, on='subject_id', how='inner')
#外连接
pd.merge(data1, data2, on='subject_id', how='outer')
print(new_data)
