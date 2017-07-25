#!/home/dn070017/anaconda3/bin/python

from collections import Counter

remain_fasta_file = open('/home/dn070017/temporary/dream_encode/gc_content/fasta_list.txt', 'r')
fasta_list = set()
for remain_fasta in remain_fasta_file:
    remain_fasta = remain_fasta.strip()
    # print(remain_fasta)
    fasta_list.add(remain_fasta)

fasta_file = open('/home/encode_dream/data/annotations/hg19.genome.fa', 'r')
fasta_dict = dict()
key = ''
former_fasta = ''
for fasta in fasta_file:
    fasta = fasta.strip()

    if fasta[0] == '>':
        if key != '' and key in fasta_list:
            fasta_dict[key] = former_fasta
        
        key = fasta[1:]
        former_fasta = ''
    else:
        if key not in fasta_list:
            continue
        
        former_fasta = former_fasta + fasta

fasta_file.close()
if key in fasta_dict:
    fasta_dict[key] = former_fasta

# for key, value in fasta_dict.items():
#    print('{} (length {}): {}'.format(key, len(value), value[0:99]))

sequence = ''
former_chr = ''
bed_file = open('/home/encode_dream/features/H1-hESC.dnase.train.feature', 'r')
for bed in bed_file:
    bed = bed.strip()
    bed_data = bed.split('\t')

    if former_chr == '' or bed_data[0] != former_chr:
        former_chr = bed_data[0]
        sequence = fasta_dict[bed_data[0]]

    bin_seq = sequence[int(bed_data[1]): int(bed_data[2])]
    counter = Counter(bin_seq)
    print('{}\t{}\t{}\t{:.3f}'.format(bed_data[0], bed_data[1], bed_data[2], (counter['c'] + counter['C'] + counter['g'] + counter['G'])/len(bin_seq)))

bed_file.close()
