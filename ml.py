from knn import Data as Data
from operator import itemgetter
from random import randint
import xlrd, sys, json
from copy import deepcopy

def readFile(filename,datasetlist = [],jenis_kelas = []):
	dataset = xlrd.open_workbook(filename)
	dataset = dataset.sheet_by_name('Sheet1')
	start_row = 0

	for x in range(start_row,dataset.nrows):
		listdata = []
		index = 0
		for y in range(dataset.ncols):
			listdata.append(dataset.cell(x,y).value)
		# listdata.append(dataset.cell(x,1).value)
		# listdata.append(dataset.cell(x,2).value)
		# listdata.append(dataset.cell(x,3).value)
		# listdata.append(dataset.cell(x,4).value)
		data = Data(data = listdata)
		datasetlist.append(data)
		if data.kelas not in jenis_kelas:
			jenis_kelas.append(data.kelas)


def votingf(datasetlist, jarak, jenis_kelas, voting):
    for y in range(0, len(jarak)):
        if datasetlist[jarak[y][0]].kelas not in jenis_kelas:
            jenis_kelas.append(datasetlist[jarak[y][0]].kelas)
            voting.append([datasetlist[jarak[y][0]].kelas, 0])
    for y in range(0, len(jarak)):
        for z in range(0, len(jenis_kelas)):
            if datasetlist[jarak[y][0]].kelas == jenis_kelas[z]:
                voting[z][1] += 1


def nearestneighbour(datasetlist, datasetuntukcoba, knn):
    for x in range(0, len(datasetuntukcoba)):
        jarak = []
        for y in range(0, len(datasetlist)):
            jarak.append([y, datasetuntukcoba[x].jarak(datasetlist[y])])
        jarak.sort(key=itemgetter(1))
        print(jarak)
        jarak = jarak[:knn]
        jenis_kelas = []
        voting = []

        votingf(datasetlist=datasetlist, jarak=jarak, jenis_kelas=jenis_kelas, voting=voting)
    return str(voting[0][0])

def tes():
    datasetlist = []
    jenis_kelas = []
    data = Data(data = [0,8,0,0,0,""])
    dataarr = []
    dataarr.append(data)
    readFile(filename="data.xlsx", datasetlist=datasetlist, jenis_kelas=jenis_kelas)
    print(nearestneighbour(datasetlist = datasetlist,datasetuntukcoba = dataarr,knn=1))
    return nearestneighbour(datasetlist = datasetlist,datasetuntukcoba = dataarr,knn=1)

tes()