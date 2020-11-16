from Bio import SeqIO
import sys

filename = sys.argv[1]

for seq_parse in SeqIO.parse(filename,"fasta"):
	ids  = seq_parse.id
	name = seq_parse.description
	seq  = seq_parse.seq
	save = open(ids+".fasta","w")
	print >>save,">"+name+"\n"+seq
	save.close


