import pandas as pd
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
regiment = pd.DataFrame(raw_data,columns=raw_data.keys())
# print(regiment)
#小组数量
r_size = regiment.groupby(['company', 'regiment']).size()
# print(r_size)
# r1 = regiment[regiment['regiment']=='Nighthawks'].groupby('regiment').mean()
# print(regiment.groupby(['regiment', 'company']).preTestScore.mean().unstack(level=0))
# print(regiment.groupby(['regiment', 'company']).preTestScore.mean())
#遍历
for name,group in regiment.groupby('regiment'):
    print(name)
    print(group)