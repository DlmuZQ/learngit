#_*_ coding:utf-8 _*_

import xlrd
def getInfotsflandwtyy(tabel,nrows):
    tsfl = {}
    wtyy = {}
    for i in range(1, nrows):
        curCell1 = tabel.row_values(i)[6]
        curCell2 = tabel.row_values(i)[21]
        if curCell1 not in tsfl:
            tsfl[curCell1] = 1
        else:
            tsfl[curCell1] += 1
        if curCell2 not in wtyy:
            wtyy[curCell2] = 1
        else:
            wtyy[curCell2] += 1
    with open('tsfl_precent.txt', 'w') as f:
        for key in tsfl:
            line = key + '\t' + str(tsfl[key]) + '\t' + str(tsfl[key]//float(nrows)*100) +'\n'
            f.write(line)
    with open('wtyy_precent.txt', 'w') as f:
        for key in wtyy:
            line = key + '\t' + str(wtyy[key]) + '\t' + str(wtyy[key]//float(nrows)*100) + '\n'
            f.write(line)
def getInfoyytots(tabel,nrows):
    result = {}
    for i in range(1,nrows):
        ts = tabel.row_values(i)[6]
        yy = tabel.row_values(i)[21]
        if ts not in result:
            result[ts] = {}
        if yy not in result[ts]:
            result[ts][yy] = 1
        else:
            result[ts][yy] += 1
    f = open('yy_to_ts.txt','w')
    for ts in result:
        line = ts + '\n'
        f.write(line)
        for yy in result[ts]:
            liney = ' '*len(ts) + yy + '\t' + str(result[ts][yy]) + '\n'
            f.write(liney)
    f.close()
data = xlrd.open_workbook('个人客户投诉工单.xls')
tabel = data.sheets()[0]
nrows = tabel.nrows
if __name__ == '__main__':
    getInfotsflandwtyy(tabel,nrows)
    # getInfoyytots(tabel,nrows)

