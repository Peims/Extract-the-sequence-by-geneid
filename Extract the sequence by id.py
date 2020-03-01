from sys import argv
fin=open(argv[1], "rt")
fin_file_list=fin.readlines()
fin.close()

# 将文件内容以ID号为键，索引在字典seqs_dict中
seqs_dict={}
i=0

while i<len(fin_file_list):
    if fin_file_list[i][0]==">":
        sp=fin_file_list[i].strip().split("\t")
        seq_id=sp[0][1:]
        #annotation=fin_file_list[i].strip()
        #print (annotation)
        sequence=""
        j=i+1
        while j<len(fin_file_list) and fin_file_list[j][0]!=">":
            sequence += fin_file_list[j].strip()
            j=j+1
        if not seq_id in seqs_dict:
            seqs_dict[seq_id]=[sequence]
        i=j
    else:
        i=i+1

# 计算seqs.fa中序列的数目
#print(seqs_dict.keys())

# 根据selected_id_list.txt提取序列，写入selected_sequences.fa文件
f_id_list=open(argv[2], "rt")
f_selected_seqs=open("g.fasta", "wt")
for line in f_id_list:
    #print(line)
    f_selected_seqs.write(">"+line.strip()+"\n"+seqs_dict[line.strip()][0]+"\n")
f_id_list.close()
f_selected_seqs.close()