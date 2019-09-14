```
directory = 'directory'
files = os.listdir(directory)
for file in files:
    if file.startswith('FourRemoved_'):
        TsRemoved = []
        for record in SeqIO.parse("%s" %file, "fastq"):
            sequence = str(record.seq)
            letter_annotations = record.letter_annotations

            record.letter_annotations = {}

            if sequence.startswith('T'):
                pattern = re.compile('^T+[\wT]T+')
                new_sequence = re.sub(pattern, '', sequence)
                record.seq = Seq.Seq(new_sequence)

                length = len(sequence) - len(new_sequence)

                new_letter_annotations = {'phred_quality': letter_annotations['phred_quality'][length:]}
                record.letter_annotations = new_letter_annotations

                TsRemoved.append(record)

            else:

                pattern = re.compile('^\wT+')
                new_sequence = re.sub(pattern, '', sequence)
                record.seq = Seq.Seq(new_sequence)

                length = len(sequence) - len(new_sequence)

                new_letter_annotations = {'phred_quality': letter_annotations['phred_quality'][length:]}
                record.letter_annotations = new_letter_annotations

                TsRemoved.append(record)

        with open('TsRemoved_%s' %file, 'w') as output_handle:
            SeqIO.write(TsRemoved, output_handle, "fastq")
```
