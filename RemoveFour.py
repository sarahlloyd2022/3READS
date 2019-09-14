```
directory = 'directory'
files = os.listdir(directory)
for file in files:
    if file.startswith('Cut_'):
        FourRemoved = []
        for record in SeqIO.parse("%s" %file, "fastq"):
            sequence = str(record.seq)
            letter_annotations = record.letter_annotations

            record.letter_annotations = {}

            new_sequence = sequence[4:]
            record.seq = Seq.Seq(new_sequence)

            new_letter_annotations = {'phred_quality': letter_annotations['phred_quality'][4:]}
            record.letter_annotations = new_letter_annotations

            FourRemoved.append(record)

        with open('FourRemoved_%s' %file, 'w') as output_handle:
            SeqIO.write(FourRemoved, output_handle, "fastq")
```
