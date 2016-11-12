#_*_ coding:utf-8 _*_
import xlrd
data = xlrd.open_workbook('个人客户投诉工单.xls')
tabel = data.sheets()[0]
nrows = tabel.nrows
tree = []
for i in range(1,nrows):
    curLine = tabel.row_values(i)[1].split('->')
    if len(curLine) != 5:
        print(i,len(curLine))
        continue
    if len(tree) == 0:
        tree.append(curLine)
    else:
        for j in range(len(curLine)):
            add = True
            for k in range(len(tree)):
                if curLine[j] == tree[k][j]:
                    add = False
                if k == len(tree) -1:
                    if add:
                        tree.append(curLine)
with open('1106_5.txt','w') as f:
    for i in range(len(tree)):
        line = ''
        for j in range(len(tree[i])-1):
            line += tree[i][j]
            line += '->'
        line += tree[i][len(tree[i])-1]
        f.writelines(line+'\n')