```
Tfasta = list(SeqIO.parse("TString_inRealRev", "fasta"))

Tfile = []
for Tstring in Tfasta:
    seq = str(Tstring.seq)
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    revcomp = "".join(complement.get(base, base) for base in reversed(seq))
    Tstring.seq = Seq.Seq(revcomp)
    Tfile.append(Tstring)
with open('TString_RevComp_Rev.fasta', 'w') as output_handle:
    SeqIO.write(Tfile, output_handle, "fasta")
```
