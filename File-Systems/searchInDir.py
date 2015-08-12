# -*- coding: utf-8 -*-

__author__ = aresowj

import os

def searchInDir(keyword):
    filelist = os.listdir('.')
	result = []
	
	for n in filelist:
		if keyword in n.lower():
			result.append(n)
	
	return result



def main():
	key = ''
	while True:			
		key = input('\nPlease enter the keyword you want to find: ')
		result = searchInDir(key.lower())
		
		if result == []:
			print('\nSorry, file not found.')
		else:
			print('\n File(s) or Dir(s) found: ')
			count = 1
			for f in result:
				print(str(count) + '. ' + f + '\n')
				count += 1

main()
