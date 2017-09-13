#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pip install requests
import requests


# 问题: 用时访问，将所有城市气温封装到对象里面

# 迭代器对象 (WeatherIterator) 抽象方法: frozenset{{'next'}}
# next方法每次返回一个城市气温
from collections import Iterable, Iterator 

class WeatherIterator(Iterator):
	"""构造器 params 城市名称列表"""
	def __init__(self, cities):
		self.cities = cities
		self.index = 0
	def getWeather(self, city):
		r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
		data = r.json()['data']['forecast'][0]
		return '%s: %s--%s' % (city,data['low'],data['high'])
		# 北京: 低温 19℃--高温 28℃
	def __next__(self):
		# 迭代完毕
		if self.index == len(self.cities):
			raise StopIteration
		city = self.cities[self.index]
		self.index += 1
		return self.getWeather(city)

# 可迭代对象WeatherIterable, __iter__ 返回一个迭代器  __iter__
class WeatherIterable(Iterable):
	"""docstring for WeatherIterable"""
	def __init__(self, cities):
		self.cities = cities
	def __iter__(self):
		# 返回实例对象
		return WeatherIterator(self.cities)

for x in WeatherIterable([u'北京',u'上海',u'广州',u'深圳',u'珠海',u'衡水']):
	print(x)