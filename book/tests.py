

# Create your tests here.

import pandas as pd

# train = pd.read_csv(r'C:\Users\Administrator\LiXiHan\Library\book\train.tsv', sep='\t', index_col='seqID')
# for row in train.itertuples():
#     print(row)
#     print(getattr(row, 'Index'))
#     print(getattr(row, 'taxid'))
#     print(getattr(row, 'superkingdom'))
#     print(getattr(row, 'phylum'))
#     print(getattr(row, '_4'))
#     print(getattr(row, 'order'))
#     print(getattr(row, 'family'))
#     print(getattr(row, 'genus'))
#     print(getattr(row, 'species'))
#     print(getattr(row, 'sequence'))
#     print(type(getattr(row, 'sequence')))

sps = []
a = 'media/download/bold/bucket_temp/1.txt'
with open(a, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        sps.append(line+'|')
    print(str(''.join(sps)))
f.close()
    # with open(r'C:\Users\Administrator\LiXiHan\Library\book\temp_list.txt', 'w', encoding='utf-8') as f1:
    #     f1.write(str(''.join(sps)))
sps = ''
a = 'media/download/bold/bucket_temp/1.txt'
with open(a, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        sps += (line + '|')
    print(sps)