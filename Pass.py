```
#Fwd
X = pd.read_csv('Matched_Fwd.txt', sep="\t", header=None, dtype=str)
X.columns = ['ID', 'Tstring', 'NonT2End', 'Extend', 'Real', 'Chr', 'Start', 'Stop']
X.Tstring.fillna('none', inplace=True)
X['Pass'] = ''
for index, row in X.iterrows():
    Tcount = row.Tstring.count('T')
    ExtendCount = len(str(row.Extend)) - len(str(row.Extend).rstrip('T'))
    if Tcount - ExtendCount >= 2:
        row.Pass = 'Yes'
    else:
        row.Pass = 'No'
X.to_csv('Fwd_PassInfo.txt', sep="\t", header=None, index=False)
#Rev
X = pd.read_csv('Matched_Rev.txt', sep="\t", header=None, dtype=str)
X.columns = ['ID', 'Tstring', 'NonT2End', 'Extend', 'Real', 'Chr', 'Start', 'Stop']
X.Tstring.fillna('none', inplace=True)
X['Pass'] = ''
for index, row in X.iterrows():
    Tcount = row.Tstring.count('A')
    ExtendCount = len(str(row.Extend)) - len(str(row.Extend).lstrip('A'))
    if Tcount - ExtendCount >= 2:
        row.Pass = 'Yes'
    else:
        row.Pass = 'No'
X.to_csv('Rev_PassInfo.txt', sep="\t", header=None, index=False)
```
