import math
import statistics
from collections import Counter
import numpy as np 
from scipy.stats import kurtosis, skew


places = []
count = 0
gede = float('-inf')
kecil = float('inf')
jangkauan = 0

def logcallculator(jumlah):
	realnumberbanyakkelas = math.log10(jumlah) * 3.3 + 1
	return realnumberbanyakkelas

def inti():
	with open('file.txt', 'r') as filehandle:
		global places,count,gede,kecil,banyakkelas
		filecontents = filehandle.readlines()
		for lines in filecontents:
			places.append(float(lines))
			count += 1
			number	= float(lines)
			if gede < number:
				gede = number
			if kecil > number:
				kecil = number
	print("Nilai : \n",places)
	print("Nilai terbesar\t: ",gede)
	print("Nilai terkecil\t: ",kecil)
	print("banyak variable\t: ",count)

def panjangkelas():
	global realnumberbanyakkelas,jangkauan
	jangkauan = float(gede) - float(kecil)
	jangkauan = jangkauan / realnumberbanyakkelas
	jangkauan = round(jangkauan)

def table(kecil,jangkauan,banyakkelas,freqtot):
	b1 = kecil
	b2 = 0
	interval = jangkauan 
	frekuensi = 0
	count = 0
	places2 = []
	line = 0
	totalfrekuensi = 0
	print("-"*41)
	print("|\tNilai\t\t|\tFreq\t|")
	temp = b1
	for i in range(banyakkelas):
		print("-"*41)
		b2 = temp+interval - 1
		while(line <= freqtot -1):
			if places[line] >= temp and places[line] <= b2 :
				places2.append(places[line]) 
				count +=1
			line +=1
		if count == 0:
			places2 = ["Kosong"]
		print("|\t",temp,"-",b2,"\t|\t",count,"\t|"," nilai :",places2)
		totalfrekuensi += count
		temp = b2 + 1
		count = 0
		line = 0
		places2	= []
	print("-"*41)
	print("Total jumlah : ",totalfrekuensi)

def average(places):
	count = 0
	text = ""
	for i in range(len(places)):
		count += places[i]
		text += str(places[i]) + " + " 
	print("[+] Average: \n")
	print(text, " = " ,count , " / " , len(places) , " = ", count / len(places) , " \n--> " , round(count / len(places)))
	return count / len(places) 

def median(places):
	places = sorted(places)
	print("\n[+] Median: \n")
	median = len(places)
	print("Sorted : \n",places,"\n")
	if(median %2 == 0):
		median_rate = median // 2
		median = (places[median_rate - 1] + places[median_rate]) / 2
		print(places[median_rate-1] , " + " , places[median_rate] , "/ 2 = ", median )
	else:
		print("-->",places[median // 2])

def mode(places):
	mode = Counter(iter(places)).most_common(1)
	print("\n[+] Mode \n-->" , mode[0][0], "Sebanyak : ",mode[0][1], " kali")	
	
def variance(places, xbar=None):
	print("\n[+] Variance \n")
	variance = statistics.variance(places)
	print("Caranya panjang sumpah gw mager mending langsung pake module aja biar langsung bener")
	print("-->",variance)

def standard_deviation(places):
	standard_deviation = statistics.pstdev(places)
	print("\n[+] Standard Deviation\n","--> ",standard_deviation)
	return standard_deviation

def minimum(places):
	print("\n[+] Minimum\n","--> ",min(places))
	return min(places)

def maximum(places):
	print("\n[+] Maximum\n","--> ",max(places))
	return max(places)

def rangee(places):
	print("\n[+] Range\n","--> ", max(places) - min(places))

def quartil(places):
	quartil = sorted(places)
	print("\n[+] Lower Quartil\n","--> ",np.quantile(quartil, .25, interpolation='midpoint'))
	print("\n[+] High Quartil\n","--> ",np.quantile(quartil, .75, interpolation='midpoint'))
	print("\n[+] InterQuartil\n","--> ",np.quantile(quartil, .75, interpolation='midpoint') - np.quantile(quartil, .25, interpolation='midpoint'))

def scipyy(places):
	print("\n[+] Skewness\n","--> ",skew(places))
	print("\n[+] Kurtosis\n","--> ",kurtosis(places))

def CoefficientVariation(places):
	standard_deviation = statistics.pstdev(places)
	mean = statistics.mean(places)
	print("\n[+] Coefficient Variation\n","Standard Deviation = ",standard_deviation,"\n Average = ",mean,"\n--> ",standard_deviation , " / ",mean," = ",standard_deviation / mean)

inti()
realnumberbanyakkelas = logcallculator(count)
banyakkelas = round(realnumberbanyakkelas)
panjangkelas()

print("Banyak Baris \t: ",banyakkelas)
print("Panjang Baris\t: ",jangkauan)

table(kecil, jangkauan, banyakkelas,count)
average(places)
median(places)
mode(places)
variance(places)
standard_deviation(places)
minimum(places)
maximum(places)
rangee(places)
quartil(places)
scipyy(places)
CoefficientVariation(places)




print("Testing1")
