import pandas as pd
euro12 = pd.read_csv('./tsv/euro.tsv')
#队名是G开头的
team_euro = euro12[euro12.Team.str.startswith('G')]
#前7个数
team_7 = euro12.iloc[0:7]
team_last3 = euro12.iloc[-3:]
#球队在['England', 'Italy', 'Russia']中的
team_in = euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia'])]
print(team_in)