```
directory = 'directory'
files = os.listdir(directory)
for file in files:
    if file.startswith('NoChrM_Bed_Bam_Rev'):
        X = pd.read_csv('%s' %file, sep="\t", header=None)
        X.columns = ['Chr', 'Start', 'Stop', 'ID', 'Score', 'Strand']
        X['Start'] = pd.to_numeric(X['Start'])
        X['Stop'] = pd.to_numeric(X['Stop'])
        Stop = X['Stop']
        X['Start'] = Stop
        X['Stop'] = Stop + 20
        X = pd.DataFrame(X)
        X.to_csv('Extend_%s' %file, sep="\t", header=None, index=False)
```
