import re

class ThemesAnalyzer:

	def __init__(self, file, pattern):
		self.themes_file = file
		self.pattern = pattern

	def perform(self):
		themes_calculated = self.__themes_calculate()

		for key, value in themes_calculated.items():
			print( 'Theme "{}" was used {} times'.format( key, value ) )


	def __themes_calculate(self):
		themes = self.__themes_list()
		themes_calculated = {}

		for theme in themes:
			themes_calculated.setdefault( theme, 0 )
			themes_calculated[theme] += 1

		return themes_calculated


	def __themes_list(self):
		themes_list = []

		for line in self.themes_file:
			line = line.strip()
			theme = re.search( self.pattern, line )
			if theme:
				result = theme.group(1)
				themes_list.append( result )

		return themes_list



urls_file = open('URLs.txt')

analyzer = ThemesAnalyzer(urls_file, '\/([^/?][a-zA-Z]+)\/')

analyzer.perform()
