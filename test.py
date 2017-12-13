# coding=utf-8
import pyltp
import codecs
import os
import HmmNERTagger
__author__ = 'adien'
def get_files(path = "2014_8_2/test/"):
    files = os.listdir(path)
    return files

def read_file(filename):
    path = "2014_8_2/test/"+filename
    f = codecs.open(path, encoding="utf-8")
    rows = f.readlines()
    # print rows
    return rows

def words2sen(row):
    words = row.split(u" ")
    sen = u""
    for term in words:
        sen += term.split(u"/")[0]
    return sen

def get_tags(row):
    row = row.replace(u"\n",u"")
    words = row.split(u" ")
    words.pop()
    # print words
    tags = []
    if len(words) != 0:
        for term in words:
            tags.append(str(term.split(u"/")[1]))
        # print tags
        return tags
    else:
        # print tags
        return tags

# nr人名456
# ns地名789
# nt机构团体123
# nz其他专名101112
"""
nt = ["1","2","3"]
nr = ["4","5","6"]
ns = ["7","8","9"]
nz = ["10","11","12"]
files = get_files()
hmm = HmmNERTagger.HMMNERTTagger()
r_sum_dict = {"nt": 0, "nr":0, "ns": 0, "nz": 0}
r_sum = 0
p_sum_dict = {"nt": 0, "nr":0, "ns": 0, "nz": 0}
p_sum = 0
right = {"nt": 0, "nr":0, "ns": 0, "nz": 0}


for file in files[:]:
    rows = read_file(file)
    for row in rows:
        real_tags = get_tags(row)
        sen = words2sen(row)
        tags = hmm.tag(sen)
        if(real_tags.__len__()==tags.__len__()):
            for i in range(real_tags.__len__()):
                if real_tags[i] in nt and tags[i] in nt:
                    right["nt"] += 1
                elif real_tags[i] in nr and tags[i] in nr:
                    right["nr"] += 1
                elif real_tags[i] in ns and tags[i] in ns:
                    right["ns"] += 1
                elif real_tags[i] in nz and tags[i] in nz:
                    right["nz"] += 1
                if tags[i] in nt:
                    p_sum_dict["nt"] += 1
                elif tags[i] in nr:
                    p_sum_dict["nr"] += 1
                elif tags[i] in ns:
                    p_sum_dict["ns"] += 1
                elif tags[i] in nz:
                    p_sum_dict["nz"] += 1
                if real_tags[i] in nt:
                    r_sum_dict["nt"] += 1
                elif real_tags[i] in nr:
                    r_sum_dict["nr"] += 1
                elif real_tags[i] in ns:
                    r_sum_dict["ns"] += 1
                elif real_tags[i] in nz:
                    r_sum_dict["nz"] += 1
                if(tags[i]!='0'):
                    p_sum += 1
                if(real_tags[i]!='0'):
                    r_sum += 1

for key in r_sum_dict.keys():
    r = right[key]/float(r_sum_dict[key])
    p = right[key]/float(p_sum_dict[key])
    print key,r,p,2*r*p/(r+p)
"""
