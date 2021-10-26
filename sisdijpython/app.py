#!/bin/python3

import math
import re

def main_sisdij():
	com = str(input("Masukan komplement ke brp contoh (1 - 16 atau A - F): "))
	no = str(input("Masukan nilai complement contoh ( AF12 ) : "))
	ketentuan = toHex(com)
	if(ketentuan == True):
		com = str(hex(int(com))[2:])
	com = com.upper()
	complement(no,com)

def check(no):
	ketentuan = False
	if(re.match("[0-9]+$", no)):
		ketentuan = False
	else:
		ketentuan = True 
	return ketentuan

def toHex(number):
	ketentuan = False
	if(re.match("[0-9]+$", number) and int(number) > 9):
		ketentuan = True
	return ketentuan

def complement(no,com):
	baris1s = ""
	baris2s = ""
	baris1 = []
	baris2 = []
	mysum = 0
	total1 = ""
	num = str(com) 
	jumlah = len(no)
	jumlahcom = com * len(no)
	print("-"*18)
	for i in range(jumlah):
		ketentuan = check(no[i])
		if(ketentuan == True and re.match("[A-F]+$", com)):
			baris1.append(int(no[i], 16))
			mysum = int(com, 16) - int(no[i], 16)
			baris2.append(mysum)
			print(int(com, 16)," - ", int(no[i], 16) , " = ", int(com, 16) - int(no[i], 16), " " , hex(mysum)[2:])
		if(ketentuan == True and re.match("[0-9]+$", com)):
			baris1.append(int(no[i]))
			mysum = int(com) - int(no[i], 16)
			baris2.append(mysum)
			print(int(com)," - ", int(no[i]), " = ", int(com) - int(no[i], 16), " " , hex(mysum)[2:])
		if(ketentuan == False and re.match("[A-F]+$", com)):
			baris1.append(int(no[i]))
			mysum = int(com , 16) - int(no[i])
			baris2.append(mysum)
			print(int(com, 16)," - ", int(no[i]), " = ", int(com , 16) - int(no[i])," ", hex(mysum)[2:])
		if(ketentuan == False and re.match("[0-9]+$", com)):
			baris1.append(int(no[i]))
			mysum = int(com) - int(no[i])
			baris2.append(mysum)
			print(int(com)," - ", int(no[i]), " = ", int(com) - int(no[i]), " " , hex(mysum)[2:])
	print("-"*18)
	for i in range(len(baris1)): baris1s += str(hex(baris1[i])[2:]) + " "
	for i in range(len(baris2)): baris2s += str(hex(baris2[i])[2:]) + " "
	print("\n"," ".join(jumlahcom),"\n",baris1s,"\n"," ".join("-"* (len(jumlahcom))),"\n",baris2s)

if __name__ == "__main__": 
	main_sisdij()
