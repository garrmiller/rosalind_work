# Protein motifs
import re

import urllib.request
with open("rosalind_mprt(1).txt") as f:
    string_2 = f.readlines()
   
uni_ids = [a[:-1] for a in string_2]
names = [re.findall("[A-Z0-9]+",uni)[0] for uni in uni_ids]
# names = [name for name in uni_ids if not "_" in name]
# with open("test_input_protein.txt") as f:
    # string = f.readlines()

def getsequence(cd):
    fastadata = urllib.request.urlopen("http://www.uniprot.org/uniprot/" + cd + ".fasta").read().decode('utf-8').splitlines()
    return ''.join(fastadata[1:])
    
out = list(map(getsequence, names))
# string = [string[0:-1] for string in string]

def flatten(l):
    return [item for sublist in l for item in sublist]
    
# size = len(string)
# idx_list = [idx for idx, val in
    # enumerate(string) if ">" in val]

# res = [string[i: j] for i, j in
        # zip([0] + idx_list, idx_list +
        # ([size] if idx_list[-1] != size else []))]
# res = res[1:]
# names = [sub_string[0] for sub_string in res]
# out = ["".join(test[1:len(test)]) for test in res]
# out = ["".join(test[1]) for test in res]
my_dict = dict(zip(out, names))
ids = flatten([re.findall(r'\|([^]]*)\|', a) for a in names])
# string_to_find = "N[^P][S|T][^P]"
string_to_find = r"(?=(N[^P][ST][^P]))"


locs = []
for i in range(0, len(out)):
    print(i)
    temp = [m.start() + 1 for m in re.finditer(string_to_find, out[i])]           
    if len(temp) > 0: locs.append([uni_ids[i], temp])

for loc in locs:
    print(loc[0])
    print(*loc[1])