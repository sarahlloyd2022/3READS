#3READS

**1. Remove Adapters with Cutadapt**

**2. Remove first four random nucleotides**
python RemoveFour.py

**3. Save first four random nucleotides in separate file**
python FourStrings.py

**4. Remove T's corresponding to PolyA tails**
python RemoveTs.py

**5. Save T's corresponding to PolyA tails (TStrings) in separate file**
python TSTrings.py

**6. Select for reads at least 23 bp long**
python SizeSelect.py

**7. Align with bowtie2 in end-to-end mode**

**8. Separate forward and reverse strands and filter by MAPQ 10**
```
#Use shell script
#Output labeled forward is actually reverse
#Output labeled reverse is actually forward
samtools view -F20 -h -q10 -o Fwd_$input $input
samtools view -f 16 -h -q 10 -o Rev_$input $input
```
**9. Convert to sam to bam with samtools view**

**10.Make bed file from bam files with bedtools bamtobed**
```
#This step is used to generate files with sequence information upstream and downstream of PASs
```
**11. Remove ChrM from bedfiles**

**12. Obtain sequence information 20bp downstream PAS**
```
#Fwd labeled strands are actually reverse, thus the reported start site is actually the stop and the stop site is actually the start. Extended bed file is from the reported start location minus 20.
#Rev labeled strands are actually forward. Their reported stop site is the actual stop site. The extended bed file is from the stop position to plus 20.

12A. Extend bed files by 20bp
python Extend_Rev.py
python Extend_Fwd.py

12B. Get fasta sequences for extended bed files with bedtools getfasta
```




