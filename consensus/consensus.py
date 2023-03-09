with open("rosalind_cons(1).txt") as f:
    string = f.readlines()
string = [line[:-1] for line in  string]
size = len(string)
idx_list = [idx for idx, val in
    enumerate(string) if "Rosalind" in val]

res = [string[i: j] for i, j in
        zip([0] + idx_list, idx_list +
        ([size] if idx_list[-1] != size else []))]


out = [sub_string[1:len(sub_string)] for sub_string in res]

out = out[1:len(out)]
mat = []

for string in out:
    mat.append("".join(string))

 
 

a_list = []
c_list = []
g_list = []
t_list = []
for index in range(0, len(mat[1])):
    hold = [item[index] for item in mat]
    a_list.append(hold.count("A"))
    c_list.append(hold.count("C"))
    g_list.append(hold.count("G"))
    t_list.append(hold.count("T"))
    

profile_list = [a_list, c_list, g_list, t_list]
vec = ["A", "C", "G", "T"]
consensus_mat = []
for index in range(0, len(mat[1])):
    four = [row[index] for row in profile_list]
    consensus_mat.append(vec[four.index(max(four))])
    

print("".join(consensus_mat))

for s in profile_list:
    print(*s)