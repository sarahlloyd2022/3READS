###3READS+ Processing in Command Line

**1. Remove Adapters with Cutadapt**
**2. Remove first four random nucleotides**
```
python RemoveFour.py
```
**3. Save first four random nucleotides in separate file**
```
python FourStrings.py
```
**4. Remove T's corresponding to PolyA tails**
```
python RemoveTs.py
```
**5. Save T's corresponding to PolyA tails (TStrings) in separate file**
```
python TSTrings.py
```
**6. Select for reads at least 23 bp long**
```
python SizeSelect.py
```
**7. Align with bowtie2 in end-to-end mode**

**8. Separate forward and reverse strands and filter by MAPQ 10**  
Use samtools view in a shell script.  
Output labeled forward is actually reverse, and reverse is actually forward.
```
samtools view -F20 -h -q10 -o Fwd_$input $input
samtools view -f 16 -h -q 10 -o Rev_$input $input
```
**9. Convert to sam to bam with samtools view**

**10.Make bed file from aligned bam files using bedtools bamtobed**  
This step is used to generate files with sequence information upstream and downstream of PASs

**11. Remove ChrM from bed files**

**12. Convert aligned region bed file to fasta format**  
Use output from step 11 and convert to fasta format with bedtools getfasta

**13. Obtain sequence information from PAS to 20bp downstream**  
Use Output from step 11 as input  
Fwd labeled strands are actually reverse, thus the reported start site is actually the stop and the stop site is actually the start. Extended bed file is from the reported start location minus 20.  
Rev labeled strands are actually forward. Their reported stop site is the actual stop site. The extended bed file is from the stop position to plus 20.  
13A. Extend bed files by 20bp
```
python Extend_Rev.py
python Extend_Fwd.py
```
13B. Get fasta sequences for **extended region** bed files from step 12A with bedtools getfasta

**14. Convert TString file from fastq to fasta**
Use Tstring file generated in step 5 as input
```
sed -n '1~4s/^@/>/p;2~4p' $input > $input.fasta
```

**15. Move each sequencing library to its own directory to run remaining steps**  
At this point every library should have three files in **fasta** format:
1. Fasta file of aligned region (step 12)
2. Fasta file of extended(PAS + 20bp) region (step 13)
3. Fasta file of Tstring sequences

**16. Identify Last Aligned Position**  
If a nonT base is found in the TString, then it must be determined if this sequence aligns to the genome. If it aligns, it must be removed from the TString, and added to the aligned sequence. Scripts and steps slightly vary for forward and reverse strands. For both, a new fasta file is made with TSTring sequence from NonT base to the end and fasta sequences are converted to tables. A python script can then be used to search for matches in the TStrings (step 14) to the sequence in the extended region (step 13). 

**Forward Strand** (Labeled Forward, but actually reverse)  
**16FwdA.** Pull out TStrings where IDs are also in aligned region file
```
#Generate list of sequence IDs that were aligned
grep '^>' Step12Output_Fwd > RealIDs_Fwd
cut -c 2- RealIDs_Fwd > CutRealIDs_Fwd

#Make file with all TStrings that can be found in the aligned reads
#For below, TString.fasta is output from step 14 and should be a fasta file with all TStrings 
./faSomeRecords TString.fasta CutRealIDs_Fwd TString_inRealFwd
```
**16FwdB.** Make new fasta file with TString sequence from any NonT base to end
```
python TString_End_Fwd.py
```
**16FwdC.** Use fasta_formatter to make tables with Fasta ID, TString sequence (Step 14), Sequence from NonT base to end (Step 16FwdB), Extended region sequence (Step13B), Aligned region sequence (Step 12), chromosome (Step 11), start position (Step 11), and end position (Step 11).

**16FwdD.** For forward strands, if there is a NonT base in the Tstring AND the sequence from the NonT base to the END matches the END of the extended sequence, then:  
- Matching sequence is added to beginning aligned read  
- Matching sequence is removed from Tstring  
- Matching sequence is removed from extended sequence  
- The length of the matching sequence is subtracted from the listed start position for the aligned read. 
```
python Match_Fwd.py
```
**Reverse Strand** (Labeled Reverse, but actually forward)  
**16RevA.** Pull out TStrings where IDs are also in aligned region file
```
#Generate list of sequence IDs that were aligned
grep '^>' Step12Output_Rev > RealIDs_Rev
cut -c 2- RealIDs_Rev > CutRealIDs_Rev

#Make file with all TStrings that can be found in the aligned reads
#For below, TString.fasta is output from step 14 and should be a fasta file with all TStrings 
./faSomeRecords TString.fasta CutRealIDs_Rev TString_inRealRev
```
**16RevB** Convert all T strings to reverse complement.  
For reverse strands, the aligned sequence is the reverse complement of the raw read. Because of this, the reverse complement of Tstrings must be used. 
```
python RevComp.py 
```
**16RevC.** Make new fasta file with TString sequence from any NonA base to end
```
python TString_End_Fwd.py
```
**16RevD.** Use fasta_formatter to make tables with Fasta ID, TString sequence (Step 14), Sequence from start to NonA base (Step 16RevC), Extended region sequence (Step13B), Aligned region sequence (Step 12), chromosome (Step 11), start position (Step 11), and end position (Step 11).

**16RevE.** For reverse strands, if there is a NonA base in the reverse complemented Tstring AND the sequence from the START of the reverse complemented Tstring to the NonA base matches the START of the extended sequence, then:  
- Matching sequence is added to beginning end read  
- Matching sequence is removed from reverse complemented Tstring  
- Matching sequence is removed from extended sequence  
- The length of the matching sequence is added to the stop position of the aligned read.
```
python Match_Rev.py
```

