from words import words
import random
import string

def get_word():
	word = random.choice(words)

	while '-' in word or ' ' in word:
		word = random.choice(words.words)

	return word.upper()
