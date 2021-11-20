sample_list = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
l = []

for i in sample_list:
    if len(i) != 0:
        l.append(i)


print(l)