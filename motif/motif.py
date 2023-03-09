string_1 = "GCTCGATGTTTTCTCGATGCTGCGCTCGATGGCGGACTCGATGATTTCTCTCGATGCCTCGATGAACTCGATGCTCGATGATCTCGATGACTCGATGCGCTCGATGCACCCTCGATGCTCGATGAGCTCGATGAACTCGATGACCCCTCGATGCTCGATGGTAGAGCTCGATGCCTCGATGGTAGACCCAAACCGTCTCGATGGTGTATACTCGATGTGCTCGATGTCTCGATGTCTCGATGCTCGATGCTCGATGCTCTAACCTCTCGATGAATGACTTAAGTGCTCGATGGGAGCTCGATGCTCGATGTTGCCCTCGATGCCTCGATGCTCGATGGGTTGCTCGATGCTTGGCTCGATGAAAAAGCCTCGATGCTCGATGCTCGATGCCTCGATGCTCGATGCGCCTGTGCGGAGACTCGATGTAAGTCTCGATGCACACTCGATGCCTAGACTCGATGAGGCTCGATGGGACTCGATGGGACACTCGATGCTCGATGAAACTCTTTCGTGCTCGATGCCCTCGATGCTTTGGTCTCGATGCTCGATGCTGAGCGACTCGATGCTCGATGCTCGATGCTCGATGATAGGGCCTTTCTCGATGCTCGATGCTCGATGTATAGCTCGATGGCTCGATGCTCGATGAATTAAACTCGATGCTCGATGACTCGATGCGCTCGATGCTCGATGCACACCTCCTCGATGCCCCCTCGATGCTCGATGTCTCGATGTTTCTCGATGCTCGATGGTTCCTCGATGTATACTGAACCACCTCGATGACTGCTCGATGCCTCGATGCCTCGATGTCTCGATGATGATAACTCGATGCCCGGCCTCGATGCCGCTCTCGATGAAGCTCGATGCCGCTCGATGGCTCGATGCTCGATGCAGGCGCTCGATGCT"
string_2 = "CTCGATGCT"

a = string_1.find(string_2)
def find_motif(string_1, string_2):
    run = True
    start = 0
    all = []
    while run:
        start = string_1.find(string_2, start)
        all.append(start + 1)
        if start == -1: run = False 
        start += 1
    
    all = all[0:len(all)-1]
    return all
       
