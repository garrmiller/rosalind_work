with open("prot_tab.txt") as f:
	string = f.readlines()
    
keys = [sub[0] for sub in string]
masses = [float(sub[1:len(sub)-1].strip()) for sub in string]

my_dict = dict(zip(keys, masses))
with open("rosalind_prtm.txt") as f:
    string = f.readlines()
string = string[0][0:(len(string)-2)]
def calc_mass(string, my_dict):
    out = [my_dict[key] for key in list(string)]
    return sum(out)