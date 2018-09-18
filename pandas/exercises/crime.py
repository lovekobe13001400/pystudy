import numpy as np
import pandas as pd
crime = pd.read_csv('./tsv/crime.csv')

#year转date_time
crime.Year = pd.to_datetime(crime.Year,format='%Y')

#把年设置为索引
crime = crime.set_index("Year")

#删除列
#del crime['Population']

#
#统计每年的犯罪率情况

#比较难理解：https://github.com/guipsamora/pandas_exercises/blob/master/04_Apply/US_Crime_Rates/Exercises_with_solutions.ipynb
print(crime)
crimes = crime.resample('10AS').sum()
print(crimes)
