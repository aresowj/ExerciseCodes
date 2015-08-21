# -*- coding: utf-8 -*-
'''
A simple search program using module os.
'''

__author__ = 'aresowj'

import os

def searchInDir(keyword):
	'''The search function, will search in the working directory by default.'''
	
	filelist = os.listdir('.')	#Get a list of files under the working directory.
	result = []		#List for the files matched.
	
	for n in filelist:
		if keyword in n.lower():
			result.append(n)
	
	return result



def main():
	'''Main loop function.'''
	
	key = ''	#The keyword to be input.
	
	while True:	#Will not stop until keyboard interrupt		
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
