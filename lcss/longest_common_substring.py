# Common substring
from itertools import combinations

def sub_strings_2(string, k):
    # res = [string[x:y] for x, y in combinations(range(len(string) + 1), r = 2) if len(string[x:y]) == K ]
    unique_substrings = set(string[i: i + k] for i in range(len(string) - k + 1))
    return unique_substrings
    
with open("rosalind_lcsm.txt") as f:
    string = f.readlines()
    
string = [string[0:-1] for string in string]

size = len(string)
idx_list = [idx for idx, val in
    enumerate(string) if "Rosalind" in val]

res = [string[i: j] for i, j in
        zip([0] + idx_list, idx_list +
        ([size] if idx_list[-1] != size else []))]
res = res[1:]
names = [sub_string[0] for sub_string in res]
out = ["".join(test[1:len(test)]) for test in res]
# out = ["".join(test[1]) for test in res]
my_dict = dict(zip(out, names))

def flatten(l):
    return [item for sublist in l for item in sublist]
    
# def lcsm(my_dict):
# print(out)
out = list(my_dict.keys())
max_length = min([len(string) for string in out])

full = set()
    # print(j)
    # sub_list = list(set(get_all_substrings_2(out[j])))
    # sub = out[j]
for i in range(max_length, 2, -1):
    cands = set()
    print(i)
    for j in range(0, len(out)):
        # print(j)
        # sub_list = sub_strings_2("".join(out), i)
        
        sub_list = sub_strings_2(out[j], i)
        cands.update(sub_list)
    # cands = list(set(flatten(cands)))
    # print(i)
    # [cands.append(sub_list) for x in sub_list if not x in cands]
    # cands = list(set(cands))
    temp = [cand for cand in cands if all(cand in sub for sub in out)]
    # full.update(temp)
    if len(temp) > 0:
        print(True)
        break
        # cands.append(sub_list)
        # cands = flatten(cands)
        
        # for cand in sub_list:
            # out = list(my_dict.keys())
            # print(out)
            # test_list = [x for x in out if not x in sub]
            # test_list.pop(j)
            # hold = [all(cand in string for string in test_list)]
            # if not hold[0]: not_in_all.append(cand)
            # if hold[0]:
                # print(True)
                # cands.append(cand)
    # return cands
print(max(full))