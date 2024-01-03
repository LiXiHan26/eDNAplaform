import subprocess as sp

list = []

with open('util/fish.txt', 'r', encoding='UTF-8') as f:
    data = f.readlines()
    for i in data:
        # print(i.strip('\n'))
        list.append(i.strip('\n')+ '|')
    f.close()
with open('util/mito.txt', 'w', encoding='UTF-8') as f:
    f.writelines(list)
    f.close()

with open('util/mito.txt', 'r', encoding='UTF-8') as f:
    input = f.readlines()
code = "python tools/refdb/refdb db_download --source bold --database '{}' --output bold_fish.fasta --keep_original yes".format(input[0])
print(code)
sp.run(code, shell=True, stderr=True, stdout=True)