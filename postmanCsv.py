#!/usr/bin/python


# postmanCsv.py  
# extract API list from	postman collection json file
# $ python postmanCsv exported.json 
#
# v1.0 convert  to URL,method,   list 
#



import json
import sys


allFlag = False
argFile = 1

# check	argument
arguments = len(sys.argv) 
if( arguments < 2 ): 
	print( "Invalide argument.\n\n" )
	print( "## ------------------------------" )
	print( "## postmanCsv / API list generator from  Postman Collection json  (v1.0)" )
	print( "## written by W.Ishizuka" )
	print( "$ postmanCsv [-all] <postman-collection-json>\n\n" )
	print( "option:" )
	exit(0)

if( arguments == 3 ): 
	if sys.argv[1].find( "-all" ) == 0:
		allFlag = True
		argFile = 2

## input
try:
	f = open( sys.argv[argFile], 'r')
except OSError as e:
	print(e)
	exit(0)

try:
	json_dict = json.load(f)
except e:
	print("invalid json format")
	print(e)
	exit(0)

# print('json_dict:{}'.format(type(json_dict)))

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



