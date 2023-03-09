import itertools
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

def sub_strings(string, K):
    res = [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1) if len(string[i:j]) == K]
    return res
    
def check_overlap(s1, s2, k):
    return s1[-k:] == s2[:k]
def flatten(l):
    return [item for sublist in l for item in sublist]
    
    
with open("rosalind_grph.txt") as f:
    string = f.readlines()
string = [line[:-1] for line in  string]

size = len(string)
idx_list = [idx for idx, val in
    enumerate(string) if "Rosalind" in val]

res = [string[i: j] for i, j in
        zip([0] + idx_list, idx_list +
        ([size] if idx_list[-1] != size else []))]
res = res[1:]
names = [sub_string[0][1:] for sub_string in res]
out = ["".join(sub_string[1:len(sub_string)]) for sub_string in res]
my_dict = dict(zip(out, names))
    
def graph_theory(my_dict, K):
    combs = []
    for u, v in itertools.combinations(list(my_dict.keys()), 2):
        data_u, data_v = u, v
        if (data_u != data_v):
            if check_overlap(data_u, data_v, K):
                combs.append([data_u, data_v])
            if check_overlap(data_v, data_u, K):
                combs.append([data_v, data_u])
            

    done = [[my_dict[key[0]], my_dict[key[1]]] for key in combs]
    return done

out = graph_theory(my_dict, 3)