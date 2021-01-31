#!/usr/bin/python

# postmanCsv.py  
# extract API list from	postman collection json file
# $ python postmanCsv exported.json 
#
# v1.0 convert  to URL,method,   list 
# v1.01 clean the code


import json
import sys


allFlag = False
argFile = 1
version = "v1.01"

# check	argument
def checkArgs():
	arguments = len(sys.argv) 
	if( arguments < 2 ): 
		print( "Invalide argument.\n\n" )
		print( "\033[32mpostmanCsv / API list generator from  Postman Collection json /"+version  )
		print( "\033[32m                written by W.Ishizuka\n" )
		print( "\033[35mUsage:\n$ postmanCsv [-all] <postman-collection-json>\n\n" )
		print( "option:" )
		print( "\033[39m\033[0m " )
		return False
	if( arguments == 3 ): 
		if sys.argv[1].find( "-all" ) == 0:
			allFlag = True
			argFile = 2
	return True

# read file by argv then convert to json 
def getJson():
	## input
	try:
		f = open( sys.argv[argFile], 'r')
	except OSError as e:
		print(e)
		return ( False, None )	
	try:
		data = json.load(f)
	except e:
		print("invalid json format")
		print(e)
		return ( False, None )	
	return ( True, data )	

# read json and print ( url, method, name ) as comma csv format
def extractPostmanText():
	( ret, json_dict ) = getJson()	
	root_items= json_dict["item"]
	def printItem( item ):
		if "name" in item and "item" in item:
			print( "# "+ item["name"]);	
			for oo in item["item"]:
				printItem( oo )
		else:
			if "request" in item:
				req = item["request"];
				print( "%s,%s,%s," % ( req["url"]["raw"] , req["method"], item["name"] ) )	;
	for item in root_items:
		# print(item);
		printItem( item )

# ---------------- main ---------------------
def main():
	if not checkArgs():
		exit(1)
	extractPostmanText()

if __name__ == "__main__":
	main()






