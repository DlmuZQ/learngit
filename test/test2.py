#_*_ coding:utf-8 _*_
import xlrd
def FindInList(goal,r):
    for i in range(len(r)):
        if r[i] == goal:
            return i
    return -1
data = xlrd.open_workbook('个人客户投诉工单.xls')
tabel = data.sheets()[0]
nrows = tabel.nrows
fread = open('1106.txt')
Accient = []
for line in fread.readlines():
    curLine = line.strip().split('->')
    Accient.append(curLine)
AccientCount = [0]*len(Accient)
for i in range(1,nrows):
    curLine = tabel.row_values(i)[1].split('->')
    ret = FindInList(curLine,Accient)
    if ret != -1:
        AccientCount[ret] += 1
fwrite = open('1106_count.txt','w')
for i in range(len(AccientCount)):
    line = ''
    for j in range(len(Accient[i])):
        line += Accient[i][j]
        line += '->'
    line += str(AccientCount[i])
    fwrite.writelines(line+'\n')