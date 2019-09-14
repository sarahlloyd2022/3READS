```
Tfasta = list(SeqIO.parse("TString_inRealFwd", "fasta"))

Tfile = []
for Tstring in Tfasta:
    Tseq = str(Tstring.seq)
    Tid = str(Tstring.id)
    pattern = re.compile('[CGA]')
    if re.search(pattern, Tseq):
        Iter = re.search(pattern, Tseq)
        Index = Iter.start()
        new_sequence = Tseq[Index:]
        Tstring.seq = Seq.Seq(new_sequence)
        Tfile.append(Tstring)
    else:
    	new_sequence = 'none'
    	Tstring.seq = Seq.Seq(new_sequence)
    	Tfile.append(Tstring)
with open('TString_End_Fwd.fasta', 'w') as output_handle:
    SeqIO.write(Tfile, output_handle, "fasta")

```
