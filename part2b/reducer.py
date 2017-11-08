#!/usr/bin/python

import sys

# Initialize the keys
type_dict={}

for line in sys.stdin:
	data = line.strip().split('\t')

	if len(data)!=2:
		continue

	airport_type, thisNum = data

	if airport_type not in type_dict:
		type_dict[airport_type]=0

	type_dict[airport_type]+=int(thisNum)

max_val=0
for key in type_dict:
	max_val = max(max_val,type_dict[key])

for key in type_dict:
	if max_val == type_dict[key]:
		print "{0}\t{1}".format(key,type_dict[key])
