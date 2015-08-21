# -*- coding:utf-8 -*-
__author__ = 'aresowj'

'''
Using XML parser and urllib to obtain Yahoo! Weather forecast data.
'''

from xml.parsers.expat import ParserCreate
from urllib import request, parse

class WeatherSaxHandler(object):
	def __init__(self):
		self._weather=[]

	def start_element(self, name, attrs):
		if name == 'yweather:location':
			self._country = attrs['country']
			self._city = attrs['city']
		elif name == 'yweather:forecast':
			self._weather.append(attrs)

	def end_element(self, name):
		pass

	def char_data(self, text):
		pass
		
def parse_weather(xml):
	handler = WeatherSaxHandler()
	parser = ParserCreate()
	parser.StartElementHandler = handler.start_element
	parser.EndElementHandler = handler.end_element
	parser.CharacterDataHandler = handler.char_data
	parser.Parse(xml)	
    
	return{
        'city': handler._city,
        'country': handler._country,
        'today': {
            'text': handler._weather[0]['text'],
            'low': int(handler._weather[0]['low']),
            'high': int(handler._weather[0]['high'])
        },
        'tomorrow': {
            'text': handler._weather[1]['text'],
            'low': int(handler._weather[1]['low']),
            'high': int(handler._weather[1]['high'])
        }
    }

def fetch_xml(url):
	with request.urlopen(url) as f:
		return f.read()

weather = parse_weather(fetch_xml('http://weather.yahooapis.com/forecastrss?u=c&w=2151330'))

print('Weather:', str(weather))
