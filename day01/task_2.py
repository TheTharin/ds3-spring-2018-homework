from copy import copy
import re

class WordAnalyzer:

	def __init__(self, word_to_compare):
		self.word_to_compare = word_to_compare

	def perform(self, type):
		words_set = self.__compare()

		if type == 'words':
			print( words_set[0] )
		if type == 'count':
			print( words_set[1] )

	def __compare(self):
		word_to_compare = list(self.word_to_compare)
		dictionary_file = open('litf-win.txt', encoding = "Windows-1251")

		matching_words = []
		pattern = '[а-я]+'

		counter = 0

		for word in dictionary_file:
			initial_word = copy(word_to_compare)
			word = list( re.search( pattern, word ).group(0) )
			word_matches = False

			for letter in word:
				try:
					index = initial_word.index(letter)
					initial_word.pop(index)
					word_matches = True
				except ValueError:
					word_matches = False
					break

			if word_matches == True:
				counter += 1
				matching_words.append(''.join( word ))

		return [matching_words, counter]

word_to_compare = 'Ростелеком'

analyzer = WordAnalyzer(word_to_compare)

analyzer.perform('words')

print('')
print( 'Press Enter' )
input()

analyzer.perform('count')
