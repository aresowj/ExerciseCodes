#coding = utf-8
__author__ = 'aresowj'

'''
Analyse a file and see if it is a BMP.
Print the size and color depths if true.
'''

import re, struct

def isBMP(header):
	'''Using the header data to judge if the file is a BMP.'''
	
	result = struct.unpack('<ccIIIIIIHH', header)
	if not result[0] == b'B' and result[1] == b'M':
		print('\nThe file is not a BMP.')
	else:
		print('\nThe file is a BMP.')
		print('The size of this file is ' + str(result[6]) + 'x' + str(result[7]) + '.')
		print('The color depth of this file is ' + str(result[9]) + 'bits.')

def isValidFilename(fn):
	fn_re = re.compile(r'^([a-zA-Z0-9\!\@\#\$\%\^\&\(\)\-\_\+\=]+).([a-zA-Z0-9\!\@\#\$\%\^\&\(\)\-\_\+\=]+)')	#Use regex to judge if it is a valid filename.
	fn_match = fn_re.match(fn)
	if fn_match:
		#print(fn_match.groups())	#Showing all the matched groups
		return True
	
	return False
	
def main():
	'''Open a file and read the first 30 bytes as the header.'''
	fn = ''
	header = b''
	while True:
		fn = input('\n\nPlease input the file name.\nThe file should be in the same folder of this Py script: ')
		if not isValidFilename(fn): continue
		
		with open(fn, 'rb') as f:
			header = f.read(30)
			print(header)
		
		isBMP(header)

if __name__ == '__main__':
	main()
