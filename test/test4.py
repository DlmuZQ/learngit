#_*_ coding:utf-8 _*_
f = open('tsfl.txt')
fw = open('ts_major.txt','w')
for cur in f.readlines():
    line = cur.strip().split('\t')
    precent = int(line[-1])/6103.0
    print(precent)
    if precent > 0.01:
        linew = cur.strip() + '\t' + str(precent) + '\n'
        fw.write(linew)