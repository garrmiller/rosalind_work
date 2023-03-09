codon_dict =  {
    "UUU":   "F",
    "CUU":   "L",
    "AUU":   "I",
    "GUU":  "V",
    "UUC":  "F",
    "CUC":  "L",
    "AUC":  "I",
    "GUC":  "V",
    "UUA":  "L",
    "CUA":  "L",
    "AUA":  "I",
    "GUA":  "V",
    "UUG":  "L",
    "CUG":  "L",
    "AUG":  "M",
    "GUG":  "V",
    "UCU":  "S",
    "CCU":  "P",
    "ACU":  "T",
    "GCU":  "A",
    "UCC":  "S",
    "CCC":  "P",
    "ACC":  "T",
    "GCC":  "A",
    "UCA":  "S",
    "CCA":  "P",
    "ACA":  "T",
    "GCA":  "A",
    "UCG":  "S",
    "CCG":  "P",
    "ACG":  "T",
    "GCG":  "A",
    "UAU":  "Y",
    "CAU":  "H",
    "AAU":  "N",
    "GAU":  "D",
    "UAC":  "Y",
    "CAC":  "H",
    "AAC":  "N",
    "GAC":  "D",
    "UAA":  "Stop",
    "CAA":  "Q",
    "AAA":  "K",
    "GAA":  "E",
    "UAG":  "Stop",
    "CAG":  "Q",
    "AAG":  "K",
    "GAG":  "E",
    "UGU":  "C",
    "CGU":  "R",
    "AGU":  "S",
    "GGU":  "G",
    "UGC":  "C",
    "CGC":  "R",
    "AGC":  "S",
    "GGC":  "G",
    "UGA":  "Stop",
    "CGA":  "R",
    "AGA":  "R",
    "GGA":  "G",
    "UGG":  "W",
    "CGG":  "R",
    "AGG":  "R",
    "\n":  "", 
    "GGG":  "G"
    }
    
with open("rosalind_prot(1).txt") as f:
    string = f.read()


def flatten(l):
    return [item for sublist in l for item in sublist]
    
string_len = len(string)
num_chunks = string_len/3


print(string_len)
print(num_chunks)

out = [codon_dict[string[i:i+3]] for i in range(0, len(string), 3)]

print(out)

out = ''.join(out[0:len(out)-2])
print(out)
