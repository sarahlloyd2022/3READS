directory = 'directory'
files = os.listdir(directory)
for file in files:
    SizeSelect = []
    if file.startswith('TsRemoved_'):
        SizeSelect = []
        for record in SeqIO.parse("%s" %file, "fastq"):
            sequence = str(record.seq)
            if len(sequence) > 22:
                sequence = str(record.seq)
                SizeSelect.append(record)
        with open('Sized_%s' %file, 'w') as output_handle:
            SeqIO.write(SizeSelect, output_handle, "fastq")
