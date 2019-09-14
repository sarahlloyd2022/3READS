```
X = pd.read_csv('Cut_Final_table_Fwd', sep="\t", header=None, dtype=str)
X.columns = ['ID', 'Tstring', 'NonT2End', 'Extend', 'Real', 'Chr', 'Start', 'Stop']
for index, row in X.iterrows():
    if row.Extend.endswith(row.NonT2End):
        row.Real = row.NonT2End + row.Real
        row.Tstring = row.Tstring.replace(row.NonT2End, '')
        row.Extend = row.Extend.replace(row.NonT2End, '')
        row.Start = int(row.Start) - len(row.NonT2End)
X.to_csv('Matched_Fwd.txt', sep="\t", header=None, index=False)
```
