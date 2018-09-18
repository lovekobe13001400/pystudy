import numpy as np
import pandas as pd

df = pd.read_csv('./tsv/student_mat.csv')
stud_alcoh  = df
#mJob fJob内容转大写
stud_alcoh['Mjob'] = stud_alcoh['Mjob'].apply(lambda x:x.upper())
# print(stud_alcoh['Mjob'])
#对所有apply
def change(x):
    if type(x) is str:
        return x.upper()
    return x
stud_alcoh = stud_alcoh.applymap(change)
print(stud_alcoh['Fjob'])