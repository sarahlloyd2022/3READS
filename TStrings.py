```
directory = '/projects/b1042/BaoLab/3READS_May2019'
files = os.listdir(directory)
for file in files:
    if file.startswith('TStrings_'):
        TString = []
        for record in SeqIO.parse("%s" %file, "fastq"):
            sequence = str(record.seq)
            letter_annotations = record.letter_annotations

            record.letter_annotations = {}

            if sequence.startswith('T'):
                pattern = re.compile('^T+[\wT]T+')
                if re.findall(pattern, sequence):
                    new_sequence = re.findall(pattern, sequence)[0]
                else:
                    new_sequence = 'none'

                record.seq = Seq.Seq(new_sequence)

                length = len(sequence) - len(new_sequence)

                new_letter_annotations = {'phred_quality': letter_annotations['phred_quality'][length:]}
                record.letter_annotations = new_letter_annotations

                TString.append(record)

            else:

                pattern = re.compile('^\wT+')
                if re.findall(pattern, sequence):
                    new_sequence = re.findall(pattern, sequence)[0]
                else:
                    new_sequence = 'none'
                record.seq = Seq.Seq(new_sequence)

                length = len(sequence) - len(new_sequence)

                new_letter_annotations = {'phred_quality': letter_annotations['phred_quality'][length:]}
                record.letter_annotations = new_letter_annotations

                TString.append(record)

        with open('TString_%s' %file, 'w') as output_handle:
            SeqIO.write(TString, output_handle, "fastq")
```
