#!/usr/bin/python3
#	tickerhelper: Give it a string of symbols and it returns the coingeck IDs
#   This is to address the issue that some of the coingecko IDs are not intuitice
#   
#   tickerhelp.py -s "xmr, dot"
#   will give
#   Symbol=  xmr ID=  monero
#.  Symbol=  dot ID=  polkadot



import requests
import sys, getopt

def symboltoid(code,melist):

	lowercode=code.lower()
	for i in range (len(melist)):
		target=melist[i]['symbol']
		idstring="I CANT FIND IT"
		if target==lowercode:
			theindex=i
			idstring=melist[i]['id']
			if "peg" not in idstring:
				print("Symbol= ",code,"ID= ",idstring)
	return idstring

def main():
	try:
		options, remainder = getopt.getopt(sys.argv[1:], 's:', ['symbol='])
#
	except getopt.GetoptError:
		print ('tickerhelp.py -s <symbollist>')
		sys.exit(2)
    
	for opt, arg in options:
		if opt == '-h':
			print ('tickerhelp.py -s <symbollist>')
			sys.exit()
		elif opt in ("-s", "--symbol"):
			symbollist = arg.split(",")
	coinlisturl="https://api.coingecko.com/api/v3/coins/list"
	melist=requests.get(coinlisturl).json()
	for i in range(len(symbollist)):
		symbol=symbollist[i].strip()
		symboltoid(symbol,melist)

if __name__ == '__main__':
	main()

