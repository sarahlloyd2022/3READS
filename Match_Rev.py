```
X = pd.read_csv('Cut_Final_table_Rev', sep="\t", header=None, dtype=str)
X.columns = ['ID', 'Tstring', 'Start2NonA', 'Extend', 'Real', 'Chr', 'Start', 'Stop']
for index, row in X.iterrows():
    if row.Extend.startswith(row.Start2NonA):
        row.Real = row.Start2NonA + row.Real
        row.Tstring = row.Tstring.replace(row.Start2NonA, '')
        row.Extend = row.Extend.replace(row.Start2NonA, '')
        row.Stop = int(row.Stop) + len(row.Start2NonA)
X.to_csv('Matched_Rev.txt', sep="\t", header=None, index=False)
```
